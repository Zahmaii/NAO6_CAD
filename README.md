# NAO Health Assistant
📖 Overview
- This is an intelligent health assistant powered by NAO Robot that provides cardiovascular health support through voice interaction.
- The system uses speech recognition to detect user queries and responds with appropriate medical guidance, treatment information, and lifestyle recommendations.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🔖 Features
- Real-time Speech Recognition and Natural Language Processing
- Intent-based conversation handling for health queries
- Cardiovascular health information and guidance
- Treatment and medication dosage assistance
- Preventive care recommendations and safety tips
- Motivational quotes and light humor for patient engagement
- Voice synthesis for natural robot-human interaction
🧰 Technologies Used
- Python Programming
- NAOqi SDK for Robot Control
- Speech Recognition (ALSpeechRecognition)
- Text-to-Speech (ALTextToSpeech)
- JSON-based Intent Management
- Natural Language Processing for Intent Detection
📂 APP Explanation
- main.py: Core application that handles speech detection, intent matching, and robot responses
- intents.json: Configuration file containing all supported intents, example phrases, and corresponding responses
- speechdetectmod.py: Speech detection module for handling voice input (referenced but not included)
- loadjsonintents.py: Utility module for loading and parsing intent configurations (referenced but not included)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🏥 Supported Health Intents
- **Diagnosis**: Symptom reporting and cardiovascular health monitoring
- **Treatment**: Medication guidance and lifestyle recommendations  
- **Precaution**: Safety tips and warning signs to watch for
- **Dosage**: Medication scheduling and dosage information
- **CAD_Info**: Educational content about Coronary Artery Disease
- **Greetings**: Natural conversation starters
- **Quotes**: Motivational health quotes
- **Jokes**: Light humor for patient comfort
- **Farewell**: Conversation endings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📱 How to Implement it
1. **Setup NAO Robot Connection**
   - Update the robot IP address in main.py (currently set to "172.20.10.2")
   - Ensure NAO robot is connected to the same network

2. **Install Dependencies**
   - Install NAOqi SDK for Python
   - Ensure all required modules are available:
     ```bash
     pip install naoqi-python
     ```

3. **Prepare Configuration Files**
   - Ensure intents.json is in the same directory as main.py
   - Implement missing modules: speechdetectmod.py and loadjsonintents.py

4. **Run the Application**
   - Execute the main script:
     ```bash
     python main.py
     ```
   - The NAO robot will greet you and start listening for voice commands

5. **Interact with NAO**
   - Speak naturally about health concerns
   - Ask questions about symptoms, treatments, or medications
   - Request motivational quotes or jokes for comfort
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
⚕️ Health Disclaimer
This NAO Health Assistant is designed for educational and supportive purposes only. It does not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📜 License
This project is open-source and available under the MIT License.
💯 Acknowledgements
- SoftBank Robotics for NAO Robot platform and NAOqi SDK
- Healthcare professionals who provided guidance on cardiovascular health information
- Speech recognition and natural language processing communities
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🌟 If you found this project interesting, please consider giving it a star on GitHub! 🌟
