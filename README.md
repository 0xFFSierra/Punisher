# Punisher

**Punisher** is an advanced network defense tool designed to monitor, detect, and neutralize wireless threats within your internal network. It focuses on identifying malicious activities like deauthentication (deauth) attacks, rogue devices, and unusual traffic patterns, and provides automated countermeasures to protect your environment.

> **Note**: This is a private project and remains strictly for personal use or testing in authorized environments.

## 🛡️ Purpose

Punisher aims to:
- Detect and log malicious activity on your internal Wi-Fi network.
- Automate defensive actions, such as blocking rogue devices or sending deauth packets to disrupt attackers.
- Provide real-time visibility into network threats through logs and potential dashboard features.

## ⚙️ Features

- **Real-Time Threat Detection**:
  - Monitors Wi-Fi traffic to identify deauth packets, rogue devices, and abnormal patterns.
- **Automated Response**:
  - Blocks or isolates malicious devices dynamically.
  - Sends deauth packets to disrupt detected attackers (only within your authorized network).
- **Logging and Alerting**:
  - Maintains detailed logs of threats.
  - Supports optional email/SMS notifications for detected attacks.
- **Customizable and Extensible**:
  - Whitelist/blacklist management for trusted and untrusted devices.
  - Modular design to add features like Bluetooth monitoring or anomaly detection.

## 🛠️ Technology Stack

Punisher is primarily developed in **Python** for its flexibility and vast library support in networking and security. However, additional technologies may be considered for specific components:

- **Python**:
  - Libraries: `scapy`, `os`, `logging`, `flask` (for future dashboard).
- **Optional Alternatives**:
  - **Go**: For high-performance packet processing.
  - **C/C++**: For low-level networking tasks.
  - **JavaScript/Node.js**: For a real-time web interface if needed.
- **Hardware**:
  - Designed for lightweight deployment on devices like Raspberry Pi with a Wi-Fi adapter in monitor mode.

## 🔧 Setup
### Prerequisites
1. **Hardware**:
   - A Raspberry Pi (or any lightweight system) with a Wi-Fi adapter capable of monitor mode.
2. **Software**:
   - Python 3.8+ installed on the system.
   - Required Python libraries:
     - `scapy`
     - `flask`
     - `logging`

### Installation
1. Ensure you have the repository on your system.
2. Configure the tool:
   - Set up your whitelist of trusted MAC addresses in `config.py` (to be created).
   - Update alert preferences (e.g., email or SMS) in `alerts.py`.
3. Run the tool:
   - Execute the Python script to start monitoring.

## 🚀 Usage

- **Start Monitoring**:
  - Punisher continuously monitors traffic and logs any detected threats.
- **Automated Actions**:
  - When a threat is detected, Punisher will:
    - Log the incident.
    - Take predefined actions (e.g., block device or send deauth packets).
- **Access Logs**:
  - Logs are stored in a local `logs/` directory for review.

## 📈 Roadmap

Planned features include:
1. **Real-Time Dashboard**:
   - A web-based interface built with Flask to visualize active threats and responses.
2. **Bluetooth Threat Detection**:
   - Expand support to detect and respond to malicious Bluetooth activity.
3. **Machine Learning Anomaly Detection**:
   - Use machine learning to identify unusual traffic patterns and enhance threat detection.
