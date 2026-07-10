from nardial.conversation_agent import ConversationAgent
from nardial.session_manager import SessionManager
from nardial.providers.tts.elevenlabs import (
    ElevenLabsTTSProvider,
    ElevenLabsTTSConf,
)
from nardial.providers.nlu.written_keyword import WrittenKeywordNLUProvider
from nardial.providers.device.pepper import PepperAdapter
from nardial.providers.screen.pepper_tablet import PepperTabletScreenAdapter
import nardial.providers.screen as _screen_pkg

from sic_framework.services.webserver.webserver_service import Webserver, WebserverConf
from sic_framework.devices.pepper import Pepper

import sys
import json
from pathlib import Path
from os.path import join
import logging
import os


_WEB_DIR = Path(_screen_pkg.__file__).parent / "web"

google_keyfile_path = join("..", "..", "..", "conf", "google", "google-key.json")


if __name__ == "__main__":

    # =========================
    # 1. SELECT PEPPER
    # =========================

    pepper = Pepper("10.0.0.148")
    device = PepperAdapter(pepper)
    device.setup(logger=logging.getLogger())

    # =========================
    # 2. SET UP PEPPER TABLET / SCREEN
    # =========================

    host_ip = "10.0.0.218"
    port = 5000

    assets_root = (Path(__file__).parent / "assets").resolve()
    allowed_origin = f"http://{host_ip}:{port}"

    webserver = Webserver(
        conf=WebserverConf(
            templates_dir=str(_WEB_DIR / "templates"),
            static_dir=str(_WEB_DIR / "static"),
            port=port,
            cors_allowed_origins=[allowed_origin],
        )
    )

    screen = PepperTabletScreenAdapter(
        webserver=webserver,
        host_ip=host_ip,
        tablet=pepper.tablet,
        port=port,
        assets_root=assets_root,
    )

    # =========================
    # 3. CONFIGURE GOOGLE TTS
    # =========================

    ELEVENLABS_API_KEY="sk_43c8ad64889c9b155004c6cab07ca23e999bd8cda6f0a491"

    tts = ElevenLabsTTSProvider(
        conf=ElevenLabsTTSConf(
            api_key=ELEVENLABS_API_KEY,
            voice_id="bD9maNcCuQQS75DGuteM",
            model_id="eleven_flash_v2_5",
            sample_rate=22050,
            default_mode="batch",
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

    session_agenda = [
        "welcome_and_name",
        "session1_story_intro",
        "session1_qna_practice",
        "session1_meet_remaining_friends",
        "session1_kahoot",
        "session2_kahoot",
        "session1_do_it_fast"
    ]

    participant_id = "2"

    session_manager = SessionManager(
        session_agenda=session_agenda,
        agent=agent,
        dialog_json_path="dialog_configs/thesis_dialogs_pepper.json",
        participant_id=participant_id,
    )

    session_manager.run()

    intro_buttons = [
        "START",
        "LET'S GO",
        "GO",
        "TOROB",
        "JOJO",
        "SHILA",
        "GINGER",
        "KOKO",
        "SIMO"
    ]

    sys.exit()