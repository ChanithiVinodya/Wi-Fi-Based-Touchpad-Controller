# 📱 Touchpad Controller – Control Your Laptop with Your Phone

A web-based touchpad that lets you control your laptop’s mouse using your smartphone.
Built using **WebSockets** for real-time communication and **Python + PyAutoGUI** for system-level mouse control, with a futuristic neon UI for a modern experience.

---

## 🚀 Features

* 🖱️ Move mouse cursor using phone touch gestures
* 👆 Single tap → Left click
* 👉 Dedicated Left & Right click buttons
* 🔄 Two-finger scrolling
* 🎨 Futuristic neon glowing UI
* 🌐 Works over Wi-Fi (no cables needed)
* ⚡ Real-time low-latency communication via WebSockets

---

## 🛠️ Technologies Used

**Frontend (Client – Mobile Browser):**

* HTML
* CSS (Flexbox, animations, neon theme)
* JavaScript (Touch events, WebSocket API)

**Backend (Server – Laptop/Desktop):**

* Python
* `websockets` (for real-time communication)
* `pyautogui` (for controlling mouse input)
* `asyncio` (for asynchronous handling)

**Networking:**

* WebSockets over local Wi-Fi network

---

## 🔄 How It Works (Process)

1. The Python server runs on the laptop and listens for WebSocket connections.
2. The phone opens a web page (`touchpad_client.html`) in the browser.
3. Touch gestures on the phone are captured using JavaScript.
4. These gestures are sent as JSON messages via WebSocket.
5. The Python server receives the messages and translates them into mouse actions using PyAutoGUI.

---

## 📚 What I Learned

* How **WebSockets** enable real-time, bidirectional communication
* Handling **touch events** in mobile browsers
* Using **asyncio** for non-blocking server operations
* Integrating **Python automation tools** with web technologies
* Designing a responsive **mobile UI using Flexbox**
* Debugging network issues (IP, ports, firewalls, local hosting)

This project helped me understand how frontend and backend systems communicate in real time and how software can interact directly with operating system input.

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

### 2️⃣ Create and Activate Virtual Environment

### 3️⃣ Install Dependencies

### 4️⃣ Run the Server (on Laptop)

```bash
python touchpad_server.py
```

You should see:

```
WebSocket server listening on ws://0.0.0.0:9000
```

---

### 5️⃣ Find Your Laptop IP Address

### 6️⃣ Open the Client on Your Phone

On your phone browser, go to:

```
http://YOUR_IP:8000/touchpad_client.html
```

⚠️ Make sure:

* Both devices are on the **same Wi-Fi network**
* Your firewall allows Python access

---

## 🔧 How It Can Be Improved

* ✨ Double-tap for double click
* 🎛️ Sensitivity slider in the UI
* ⌨️ Virtual keyboard support
* 📱 Haptic feedback on tap (vibration)
* 🔒 Authentication / pairing system
* 🌍 Remote control over the internet (not just LAN)
* 📦 Convert into a Progressive Web App (PWA)

---

## 🧠 Project Motivation

This project was built to explore:

* Real-time web communication
* Device interaction through software
* Practical applications of WebSockets and automation tools

It also demonstrates full-stack thinking: **UI → Network → Backend → OS interaction**.

## Video
https://github.com/user-attachments/assets/b2931826-c5c8-4015-bda6-c8fb8c8711cd
