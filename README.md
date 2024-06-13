
# OpenAI Chatbot with Voice Recognition




## Overview
This project is a Python-based chatbot that leverages the OpenAI API for generating responses and Google's Speech Recognition library for voice input. The user can interact with the chatbot by either typing text or speaking. The chatbot runs in a Tkinter GUI, and threading is used to ensure smooth performance.

## Features
Text and voice input support.

Uses OpenAI API to generate intelligent responses.

Tkinter GUI for a user-friendly interface.

Threading to handle voice recognition and GUI simultaneously.
## Installation
Clone the repository


```bash
  git clone https://github.com/VaibhavRajpoot/Talkbot_Raspberry_PI.git
  cd Talkbot_Raspberry_PI
```
    
## Setup OpenAI API Key
Obtain your OpenAI API key from the OpenAI website.
## Usage
Run the main script to start the 
## Usage 

To run this project run

```bash
  python mainfile(1).py
```


## How it works
Tkinter GUI: The graphical user interface is built using Tkinter.

Text Input: Users can type their queries directly into the text box.

Voice Input: Users can click the "Speak" button to speak their queries.

OpenAI API: The input is sent to the OpenAI API, and the response is displayed in the GUI.

Threading: Threading ensures that the GUI remains responsive during voice recognition and API calls.