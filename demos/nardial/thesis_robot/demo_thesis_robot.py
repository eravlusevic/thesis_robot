from nardial.conversation_agent import ConversationAgent
from nardial.session_manager import SessionManager
from nardial.providers.tts.elevenlabs import (
    ElevenLabsTTSProvider,
    ElevenLabsTTSConf,
)
from nardial.providers.nlu.written_keyword import WrittenKeywordNLUProvider
from nardial.providers.device.desktop import DesktopAdapter
from nardial.providers.screen.sic_adapter import SICScreenAdapter
import nardial.providers.screen as _screen_pkg

from sic_framework.services.webserver.webserver_service import Webserver, WebserverConf
from sic_framework.devices.desktop import Desktop
from sic_framework.devices.common_desktop.desktop_speakers import SpeakersConf

import sys
import json
from pathlib import Path
from os.path import join
import logging
import os


_WEB_DIR = Path(_screen_pkg.__file__).parent / "web"

google_keyfile_path = join("..", "..", "..", "conf", "google", "google-key.json")
env_file_path = join("..", "..", "..", "conf", ".env")


# =======================
# -------- MAIN --------
# =======================

if __name__ == "__main__":

    # =========================
    # 1. SELECT DEVICE
    # =========================

    desktop = Desktop(
        speakers_conf=SpeakersConf(
            sample_rate=22050
        )
    )

    device = DesktopAdapter(desktop)
    device.setup(logger=logging.getLogger())

    # =========================
    # 2. SET UP SCREEN / IMAGES
    # =========================

    webserver = Webserver(
        conf=WebserverConf(
            templates_dir=str(_WEB_DIR / "templates"),
            static_dir=str(_WEB_DIR / "static"),
            port=5000,
        )
    )

    assets_root = (Path(__file__).parent / "assets").resolve()
    screen = SICScreenAdapter(webserver=webserver, assets_root=assets_root)

    # =========================
    # 3. CONFIGURE ELEVENLABS TTS
    # =========================

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "YOUR_API_KEY_HERE")

    tts = ElevenLabsTTSProvider(
        conf=ElevenLabsTTSConf(
            api_key=ELEVENLABS_API_KEY,
            voice_id="bD9maNcCuQQS75DGuteM",
            model_id="eleven_flash_v2_5",
            sample_rate=22050,
            default_mode="ws",
        ),
        device=device,
    )

    nlu = WrittenKeywordNLUProvider()

    agent = ConversationAgent(
        device=device,
        tts_provider=tts,
        nlu_provider=nlu,
        screen_provider=screen,
    )

    # =========================
    # 4. SESSION AGENDA
    # =========================
    #"session1_story_intro",

    session_agenda = [
        "welcome_and_name",
        "session1_story_intro",
        "session1_qna_practice",
        "session1_meet_remaining_friends",
        "session1_kahoot",
        "session2_kahoot",
        "session1_do_it_fast"
        #"session1_goodbye",
        #"session2_memory_intro"
    ]

    participant_id = "999"

    session_manager = SessionManager(
        session_agenda=session_agenda,
        agent=agent,
        dialog_json_path="dialog_configs/thesis_dialogs.json",
        participant_id=participant_id,
    )

    session_manager.run()

    intro_buttons = {
        "START", "LET'S GO", "GO",
        "TOROB", "JOJO", "SHILA",
        "GINGER", "KOKO", "SIMO",
        "Alex", "Sam", "Mia", "Lina", "Noah"
    }

    sys.exit()