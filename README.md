# Gaze Guard 👁️

> Make AI respond only when the user is truly paying attention.

---

## 🚀 Overview

Gaze Guard is a lightweight Python library designed to make AI systems more human-aware.

It enables AI applications to respond **only when the user is actively looking at the system**, preventing interruptions during real-world conversations and improving overall user experience.

---

## 🔥 Key Features

* 👁️ **Attention Detection** – Detects whether the user is facing the system using a camera
* 🤖 **Smart AI Control** – AI responds only when the user is attentive
* 👥 **Multi-Person Awareness** – Automatically pauses when multiple people are detected
* ⚡ **Background Processing** – Runs silently without any UI or screen display
* 🔔 **Event-Based Callbacks** – Trigger custom actions on attention gain/loss

---

## 📦 Installation

```bash
pip install gaze-guard
```

---

## 🧪 Example Usage

```python
from gaze_guard import AttentionController

def on_start():
    print("AI STARTED 🔊")

def on_stop():
    print("AI STOPPED 🔇")

controller = AttentionController()

controller.on_attention_gain = on_start
controller.on_attention_loss = on_stop

while True:
    pass
```

---

## 🎯 Use Cases

Gaze Guard can be integrated into:

* 🎤 Voice assistants
* 🧠 Conversational AI systems
* 🕶️ AR/VR applications
* 🤖 Robotics and automation
* 💬 Smart chat interfaces

---

## 🌍 Project Links

* PyPI: https://pypi.org/project/gaze-guard/
* GitHub: https://github.com/Ramarathinam0/gaze-guard

---

## 🧠 Concept

Modern AI systems often respond regardless of user context.

Gaze Guard introduces a simple but powerful idea:

> **AI should respond only when the user is engaged.**

This helps create more natural, non-intrusive human-AI interactions.

---

## 👨‍💻 Author

**Ramarathinam**
B.E. Artificial Intelligence & Machine Learning | Data analyst

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.
