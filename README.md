# KAF

KAF is an example multi-platform project demonstrating how a single codebase can be organized for mobile and backend services.

## Project Goal

The aim of this repository is to provide a basic skeleton for applications that include a backend API, a mobile client, and related documentation.

## Features

- Separate `mobile` and `backend` subprojects
- Basic authentication flow (placeholder)
- Data synchronization between clients and server
- Documentation in the `docs` directory

## Setup

### Prerequisites

- [Node.js](https://nodejs.org/) and `npm` installed for running the backend and development tools
- A recent Android or iOS development environment for the mobile client (e.g. Android Studio)

### Installing dependencies

```bash
# Install backend dependencies
cd backend
npm install

# Install mobile dependencies (example using npm as well)
cd ../mobile
npm install
```

### Running the project

```bash
# Start the backend API
cd backend
npm start

# In another terminal, start the mobile app (details depend on chosen framework)
cd ../mobile
npm start
```

These commands assume a Node.js based workflow. Adapt as necessary if you use different tooling.


## Voice Module Setup

This repository contains various utilities including a simple voice module that interacts with external speech services.

The voice module uses Google Speech-to-Text for transcription and Amazon Polly for speech synthesis. Both services require credentials which are **not** provided in this repository.

1. Copy `backend/voice/config_example.yaml` to `backend/voice/config.yaml` and fill in your credential values.
2. Install the optional dependencies:

   ```bash
   pip install google-cloud-speech boto3
   ```

3. Run the example functions:

   ```python
   from backend.voice.examples import demo_transcription, demo_synthesis

   demo_transcription()
   demo_synthesis()
   ```

The example functions expect an `example.wav` audio file for transcription and will write an `output.mp3` file for synthesized speech.
