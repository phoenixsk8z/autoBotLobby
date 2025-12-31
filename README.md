# autoBotLobby
Screen-State UI Automation (Python)
Overview

This project is a Python-based UI automation and screen-state detection demo designed to showcase how automation logic can be driven entirely by visual cues on the screen.

The script observes predefined screen regions, detects specific visual states using image-based recognition, and automatically performs actions when those states are detected. The project focuses on event-driven automation, computer vision concepts, and structured automation workflows.

This repository is intended strictly for educational and experimental purposes.

Key Concepts Demonstrated

Screen-based automation (no memory or network access)

Visual state detection using image comparison

Event-driven logic triggered by screen changes

Automated session entry and exit handling

Continuous state monitoring with fail-safe loops

Features

📸 Real-time screen capture of defined regions

🧠 Detection of specific UI states using reference images

⚙️ Automated input actions based on detected states

🔁 Loop-based state monitoring system

🧩 Modular structure for easy expansion

How It Works (High-Level)

The script captures specific regions of the screen at regular intervals.

Captured frames are compared against predefined reference images.

When a target visual state is detected, an associated automated action is triggered.

The script continues monitoring until an exit or end-state condition is reached.

All automation is performed purely through screen analysis and simulated input.

Technologies Used

Python 3

Screen capture utilities

Image comparison / basic computer vision techniques

Input automation libraries

Example Use Cases

Learning UI automation fundamentals

Practicing computer vision–based state detection

Prototyping automation workflows

Demonstrating event-driven scripting logic

Building automation demos for a portfolio
