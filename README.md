# AudioToAction

# Introduction

This project analyzes and builds a Web-based information extraction platform. It uses a front-end and back-end separation architecture to design the information extraction platform, and accesses the OpenAI API to process user input.
The platform can handle content in a variety of text formats, including text, doc, pdf, etc., and provides enhanced support for audio type files such as mp3 and mp4. Simultaneously, various types of information extraction tasks are built-in.
Users can extract information through simple operations, while using the database for data persistence, making information management easier.

## GDPR Statement

```
In today's digital age, privacy is a paramount concern.  As you navigate our website, we want you to feel confident that your personal information is safeguarded.  Hence, we've developed a GDPR Privacy Policy to outline how we collect, use, and protect your data.

  When you interact with our website, we may gather certain information, such as your name, email address, and technical details like IP addresses.  Rest assured, this data is collected with your explicit consent and solely for legitimate purposes.

  Your privacy is our priority, and we take stringent measures to ensure the security of your personal data.  While we implement robust security protocols, including encryption and firewalls, it's important to note that no system is entirely immune to potential risks.

  We are committed to transparency in our data practices.  We do not sell or trade your personal information to third parties without your explicit consent.  However, there may be instances where we need to share data with service providers or comply with legal obligations.

  Your rights regarding your personal data are paramount.  You have the right to access, rectify, or delete your information.  Additionally, you can object to or restrict the processing of your data as necessary.

  Our use of cookies enhances your browsing experience by customizing content and improving functionality.  You have the option to manage cookie settings in your browser according to your preferences.

  As part of our commitment to transparency, this Privacy Policy may undergo updates periodically.  We encourage you to review it regularly for any changes.

  Should you have any questions or concerns about our GDPR Privacy Policy, please don't hesitate to reach out to us.  Your trust is essential to us, and we're dedicated to ensuring the protection of your privacy every step of the way.

  Thank you for entrusting us with your information.

```

## Run the Project

### Front-end

To start the front-end part of the project, you will need to navigate to the client directory, install the necessary dependencies, and then run the development server. Use the following commands in your terminal:

```
cd frontend
npm install
npm run serve

```

### Backend

To get the back-end running, which includes setting up the server and database connections, navigate to the server directory and start the Flask server with debug mode enabled:

```
cd backend
flask run --debug

```
