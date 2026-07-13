# Interactive Storytelling with Pepper for English Vocabulary Learning

This project contains an interactive storytelling system developed for a Bachelor's thesis in Artificial Intelligence at Vrije Universiteit Amsterdam.

The system uses the Pepper social robot to support English vocabulary learning through an interactive story. The interaction is designed for children aged 5–8 and focuses on English words related to body parts.

The system was implemented using the Social Interaction Cloud (SIC) framework and NarDial. It combines spoken dialogue, character voices, images, sound effects, tablet activities, physical activities, personalization, and rule-based dialogue branching.

## Interaction Overview

During the interaction, the child:

1. Enters their name.
2. Meets the story characters.
3. Follows an interactive story.
4. Encounters English body-part words during the story.
5. Completes guided vocabulary practice.
6. Selects a helper character.
7. Completes a Learning Round with hints and second attempts.
8. Selects a champion character.
9. Completes a more difficult Challenge Round.
10. Participates in a physical vocabulary activity.

The vocabulary is repeated across different activities, while the difficulty gradually increases.

## Main Features

* Interactive storytelling
* English body-part vocabulary
* Rule-based dialogue flow
* Personalized use of the child's name
* Choice of a helper and champion character
* Different ElevenLabs voices for the story characters
* Images and sound effects
* Tablet-based multiple-choice activities
* Guided learning with hints and second attempts
* Challenge questions with one attempt
* Physical vocabulary activities
* Reward feedback using hearts

## Project Structure

The project is located in:

```text
sic_applications/
└── demos/
    └── nardial/
        └── thesis_robot/
```

The main files and folders are:

```text
thesis_robot/
├── demo_thesis_robot.py
├── demo_thesis_robot_pepper.py
├── dialog_configs/
│   ├── thesis_dialogs.json
│   └── thesis_dialogs_pepper.json
├── assets/
│   ├── audio/
│   ├── html/
│   └── images/
└── participants/
```

* `demo_thesis_robot.py` runs the interaction on a desktop computer.
* `demo_thesis_robot_pepper.py` runs the interaction using the Pepper robot.
* `dialog_configs/` contains the JSON dialogue configurations.
* `assets/audio/` contains the sound effects used during the story.
* `assets/html/` contains the HTML content used for interactive activities.
* `assets/images/` contains character images, vocabulary images, feedback images, and other visual content.
* `participants/` stores participant interaction data and conversation states.

## Requirements

The project requires:

* Python
* Social Interaction Cloud (SIC) framework
* NarDial
* Redis
* ElevenLabs text-to-speech
* A configured Python virtual environment
* Pepper robot for the Pepper version

For the Pepper version, the computer and Pepper must be connected to the same Wi-Fi network.

## Running the Application

The application requires several services to run at the same time. Open a separate terminal window for each service.

In every terminal, first go to the SIC applications folder and activate the virtual environment:

```bash
cd ~/Desktop/sic_applications
source venv_sic/bin/activate
```

Then run one of the following commands in each terminal:

```text
Terminal 1: redis-server conf/redis/redis.conf

Terminal 2: run-gpt

Terminal 3: run-elevenlabs-tts

Terminal 4: run-dialogflow

Terminal 5: run-webserver
```

Keep all five terminals open while running the interaction.

### Running the Desktop Version

Open one more terminal, activate the virtual environment, and go to the project folder:

```bash
cd ~/Desktop/sic_applications
source venv_sic/bin/activate
cd demos/nardial/thesis_robot
```

Run the desktop application:

```bash
python -u demo_thesis_robot.py
```
After the application starts, open the following address in a web browser:

http://localhost:5000/

The desktop version uses the computer's speakers and displays the visual content on the computer.

### Running the Pepper Version

Before starting the Pepper version:

* Connect Pepper and the computer to the same Wi-Fi network.
* Check that the correct Pepper IP address is set in `demo_thesis_robot_pepper.py`.
* Check that the correct host computer IP address is configured.

Open one more terminal, activate the virtual environment, and go to the project folder:

```bash
cd ~/Desktop/sic_applications
source venv_sic/bin/activate
cd demos/nardial/thesis_robot
```

Run the Pepper application:

```bash
python -u demo_thesis_robot_pepper.py
```

The Pepper version uses the robot for speech and movement. Images and interactive activities are displayed on Pepper's tablet.

## Dialogue Configuration

The interaction flow is defined in JSON dialogue files.

The desktop version uses:

```text
dialog_configs/thesis_dialogs.json
```

The Pepper version uses:

```text
dialog_configs/thesis_dialogs_pepper.json
```

The dialogue files contain:

* Story narration
* Character dialogue
* Images
* Sound effects
* Tablet activities
* User choices
* Feedback
* Dialogue branching
* Learning activities
* Challenge activities

## Participant Data

Interaction data are stored in:

```text
participants/
```

Each participant is assigned a participant ID. The conversation state is stored in a JSON file associated with this ID.

Before starting a new evaluation session, check that the intended participant ID is set correctly in the application file.

## Known Limitations

* The computer and Pepper must be connected to the same Wi-Fi network.
* Network IP addresses may change and may need to be updated in the application.
* Pepper's tablet may occasionally require the application to be restarted.
* The interaction follows predefined rule-based dialogue paths.
* User responses are provided through predefined input options rather than unrestricted speech recognition.
* Some services may need to be restarted if the application does not connect correctly.
* Redis may fail to start if port `6379` is already in use.
