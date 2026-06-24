import logging

from sic_framework.devices.desktop import Desktop
from sic_framework.devices.common_desktop.desktop_speakers import SpeakersConf

from nardial.conversation_agent import ConversationAgent
from nardial.session_manager import SessionManager

from nardial.providers.device.desktop import DesktopAdapter
from nardial.providers.nlu.written_keyword import WrittenKeywordNLUProvider

from nardial.providers.tts.elevenlabs import (
    ElevenLabsTTSProvider,
    ElevenLabsTTSConf,
)

# =========================
# DEVICE
# =========================

desktop = Desktop(
    speakers_conf=SpeakersConf(
        sample_rate=22050
    )
)

device = DesktopAdapter(desktop)
device.setup(logger=logging.getLogger())

# =========================
# ELEVENLABS TTS
# =========================

# =========================
# ELEVENLABS TTS
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

# =========================
# NLU
# =========================

nlu = WrittenKeywordNLUProvider()

agent = ConversationAgent(
    device=device,
    tts_provider=tts,
    nlu_provider=nlu,
)

# =========================
# SESSION
# =========================

session_manager = SessionManager(
    session_agenda=["test_voice"],
    agent=agent,
    dialog_json_path="dialog_configs/test_elevenlabs.json",
    participant_id="test",
)

session_manager.run()