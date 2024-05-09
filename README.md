CS 510 project - Context Aware AI Bookmark extension (CABT)

Team Members
- Aayush Agarwal (aayush8@illinois.edu)
- Suvodeep Saibal Sinha (sssinha2@illinois.edu)


# Bookmark.ai - AI-Powered Bookmarking Tool

## Introduction
Bookmark.ai is an AI-powered bookmarking tool designed to enhance how users manage and categorize their web content. By leveraging advanced LLMs, Bookmark.ai automates the process of bookmark categorization, offering a dynamic and intuitive user experience. This tool simplifies content management by providing smart, AI-generated suggestions for bookmark categories, which users can customize as needed.

## Installation and Usage

### Step 1: Clone the Repository
Clone the repository to your local machine to get started with Bookmark.ai.
```
git clone https://github.com/your-repository/CS510-Final-Project.git
cd CS510-Final-Project
```

### Step 2: Install Requirements
Install the necessary requirements using pip:
```
pip install -r requirements.txt
```

### Step 3: Set Up Chrome Extension
Navigate to `chrome://extensions` in your Google Chrome browser, ensure that the Developer Mode is enabled at the top right corner, then click on "Load unpacked" and select the folder of the cloned repository to upload.

### Step 4: Configure API Key
Open the `server.py` file in a text editor and enter your API key for the Cohere model at the designated line:
```
api_key = "YOUR_COHERE_API_KEY"
```

### Step 5: Run the Server
Save the changes to `server.py` and run the server using the following command:
```
python server.py
```

### Step 6: Using the Extension
With the server running, open Google Chrome, navigate to any website of your choice, and click on the Coherence extension icon. The extension will display the suggested label for the webpage based on its content.

### Step 7: Edit and Customize Labels
If the suggested label isn't quite right or if you want to customize it, simply edit the label directly in the textbox provided within the extension's popup.

## Conclusion
Enjoy a more organized and efficient web browsing experience with Bookmark.ai, your AI-powered assistant for managing and categorizing bookmarks in real-time!
