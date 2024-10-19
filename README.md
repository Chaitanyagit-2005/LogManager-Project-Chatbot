# Rasa Chatbot Project

This is a Rasa-based chatbot project. The following guide provides instructions for setting up, using, and modifying the chatbot.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup Process](#setup-process)
   - [1. Clone or Download the Project](#1-clone-or-download-the-project)
   - [2. Install Dependencies](#2-install-dependencies)
   - [3. Set Up Rasa](#3-set-up-rasa)
   - [4. Run the Chatbot](#4-run-the-chatbot)
4. [Using the Chatbot](#using-the-chatbot)
5. [Making Changes to the Chatbot](#making-changes-to-the-chatbot)
   - [1. Updating NLU Training Data](#1-updating-nlu-training-data)
   - [2. Adding New Intents and Responses](#2-adding-new-intents-and-responses)
   - [3. Modifying Stories](#3-modifying-stories)
   - [4. Custom Actions](#4-custom-actions)
6. [Testing the Chatbot](#testing-the-chatbot)
7. [Deployment](#deployment)
8. [Troubleshooting](#troubleshooting)
9. [Conclusion](#conclusion)

## Introduction

This manual provides detailed instructions for setting up and using the chatbot developed with Rasa. The chatbot is designed to handle conversations and can be integrated into a web application.

## Prerequisites

Before starting, ensure that you have the following installed on your system:

- Python (version 3.6 or higher)
- Pip (Python package installer)
- Rasa (version matching your project)
- A code editor (e.g., Visual Studio Code, PyCharm)

## Setup Process

### 1. Clone or Download the Project

- Download the ZIP file of the project folder shared with you.
- Extract the contents of the ZIP file to your preferred location.

### 2. Install Dependencies

Open a terminal/command prompt and navigate to the project directory. Install the required Python packages by running:

```bash
pip install -r requirements.txt
3. Set Up Rasa

To set up Rasa, you will need to initialize the model:

    Navigate to the project directory in your terminal.
    Run the following command to train the Rasa model:

bash

rasa train

This command will process the training data and create a model.
4. Run the Chatbot

To run the chatbot, use the following command:

bash

rasa run

This will start the Rasa server. You can also run a separate command for the action server if you have custom actions:

bash

rasa run actions

The chatbot will be accessible through the specified socket URL.
Using the Chatbot

Once the chatbot is running, you can interact with it using a web interface. You can integrate it into your website using the provided JavaScript code snippet.
Example Integration Code:

html

<script>
!(function () {
  let e = document.createElement("script"),
    t = document.head || document.getElementsByTagName("head")[0];
  (e.src =
    "https://cdn.jsdelivr.net/npm/rasa-webchat@1.x.x/lib/index.js"), // Replace 1.x.x with the version that you want
    (e.async = !0),
    (e.onload = () => {
      window.WebChat.default(
        {
          customData: { language: "en" },
          socketUrl: "http://localhost:5005", // Update with your Rasa server URL
        },
        null
      );
    }),
    t.insertBefore(e, t.firstChild);
})();
</script>

Making Changes to the Chatbot
1. Updating NLU Training Data

To update the NLU training data, edit the data/nlu.yml file. Add new examples for intents and entities.
2. Adding New Intents and Responses

    Update domain.yml to include new intents and responses.
    Define the new intents in the data/nlu.yml file.
    Specify the corresponding responses in domain.yml.

3. Modifying Stories

To modify the conversation flow, update the data/stories.yml file. Add new stories to define how the chatbot should respond to different user inputs.
4. Custom Actions

If your chatbot requires custom logic, update actions.py. Define new action classes and ensure to register them in domain.yml.
Testing the Chatbot

To test the chatbot, you can use the Rasa shell:

bash

rasa shell

This allows you to interact with the chatbot in the command line to ensure it's working as expected.
Deployment

For deploying the chatbot:

    Choose a cloud provider (e.g., AWS, Heroku, etc.).
    Follow the provider's documentation to deploy the Rasa server.
    Ensure that the socket URL is updated in your web integration code.

Troubleshooting

If you encounter issues:

    Check Dependencies: Ensure all required packages are installed.
    Logs: Check Rasa server logs for error messages.
    Configurations: Ensure that endpoints.yml and domain.yml are correctly configured.
