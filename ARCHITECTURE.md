# System Architecture

## Overview

This project is designed around a modular architecture that automates end-to-end quality assurance testing for a healthcare AI phone agent. The workflow begins when the Python application initiates an outbound phone call through the Twilio Voice API. Twilio routes the call to the healthcare AI while also communicating with a local Flask server, which is exposed to the internet using Ngrok during development. The Flask server acts as the webhook endpoint responsible for managing the voice interaction and coordinating communication between the patient simulator and the healthcare AI.

The patient simulator is powered by the OpenAI API and uses carefully designed system prompts to roleplay realistic patients across multiple healthcare scenarios. During each conversation, the application records the dialogue, generates a timestamped transcript, and automatically produces a structured bug report summarizing the interaction and any observed issues. This modular approach separates conversation handling, transcript logging, and bug reporting into independent components, making the system easier to maintain, extend, and test.

---

## Design Decisions

Several design decisions were made to keep the project simple, modular, and easy to expand.

- **Twilio** was selected because it provides reliable outbound voice calling and recording capabilities through a straightforward API.

- **Flask** serves as a lightweight webhook server that integrates cleanly with Twilio and keeps the application architecture simple.

- **OpenAI** was used to generate realistic patient conversations while allowing new scenarios to be created by modifying only the system prompt rather than changing application logic.

- **Ngrok** enables secure HTTPS access to the local Flask server during development without requiring cloud deployment.

- Separating the project into dedicated modules for conversation handling, transcript generation, and bug reporting improves readability and allows each component to evolve independently as additional testing capabilities are added.

---

## System Workflow

```text
                OpenAI Patient Simulator
                         │
                         ▼
                Python Application
                         │
                         ▼
                 Twilio Voice API
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
 Flask Webhook Server             Healthcare AI Phone Agent
        │                                 ▲
        └────────── Voice Conversation ───┘
                         │
                         ▼
                Transcript Logger
                         │
                         ▼
               Bug Report Generator
```