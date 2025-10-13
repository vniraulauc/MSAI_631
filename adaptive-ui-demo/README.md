Adaptive UI Demo (AI-Based Adaptive HCI Project)
===============================================

This is a minimal demo of an adaptive user interface that adjusts layout (compact vs spacious) and font size based on simple user interaction heuristics. It is intentionally lightweight to demonstrate the idea of adaptation and local learning without external services.

Files:
- index.html — main page
- styles.css — styling including layout classes
- app.js — adaptive logic; uses localStorage to persist scores and layout decisions
- README.md — this file

How it adapts:
- The script keeps 'compactScore' and 'spaciousScore' and updates them when the user toggles layout or adjusts font size.
- A simple decision rule maps the score difference to a chosen layout.
- This demonstrates AI-like adaptation (learning from interaction) without requiring external AI tooling.

How to run:
1. Unzip the project.
2. Open index.html in a modern browser.
3. Interact with the buttons — your choices persist locally.

This project was generated with assistance from an AI tool (ChatGPT). See the project report for full details.
