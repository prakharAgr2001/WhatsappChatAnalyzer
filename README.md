# WhatsappChatAnalyzer
![Demo](./images/ezgif.com-video-to-gif.gif)

This is a WhatsApp chat analyzer tool that allows you to analyze the overall group chat as well as individual participants within the group. The analyzer is built using Python, numpy, pandas, and streamlit. It provides insights on a daily and monthly basis, highlights the most frequently used emojis, and displays a word cloud.

## Features

- Overall group analysis
- Individual participant analysis
- Daily and monthly analysis
- Most used emoji identification
- Word cloud generation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/whatsapp-chat-analyzer.git
   ```

2. Change into the project directory:

   ```bash
   cd whatsapp-chat-analyzer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Export WhatsApp chat: Export the WhatsApp chat you want to analyze as a text file. Open the chat, go to "Settings" > "More" > "Export chat" and choose the "Without Media" option. Save the exported file to the project directory.

2. Run the analyzer:

   ```bash
   streamlit run analyzer.py
   ```

3. Upload the chat file: In the Streamlit app, click on the "Choose File" button and select the exported chat file.

4. Explore the analysis: Once the chat file is uploaded, the analyzer will process the data and display various analysis sections. Use the interactive widgets provided to navigate through different analysis options.

## Analysis Results

### Overall Group Analysis

- Total messages sent
- Messages per participant
- Most active participants
- Busiest day and time of the week
- Most used emojis

### Individual Participant Analysis

- Messages per day and month
- Most active days and months
- Most used emojis
- Word cloud of frequently used words

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.



## Contact

For any questions or inquiries, feel free to reach out to [prakharagrawal2001@gmail.com](mailto:prakharagrawal2001@gmail.com).
