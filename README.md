
# Punisher

<p align="center">
  <img src="img/lPunisher-Logo.png" alt="Punisher Logo" width="300">
</p>

**Punisher** is an advanced, AI-powered network defense tool designed to monitor, detect, and neutralize wireless threats within your internal network. Leveraging real-time packet analysis and reinforcement learning, Punisher adapts to evolving threats and optimizes its responses to secure your environment.

> **Note**: This is a private project and remains strictly for personal use or testing in authorized environments.

## 🛡️ Purpose

Punisher aims to:
- Detect and log malicious activity on your internal Wi-Fi network.
- Automate defensive actions, such as blocking rogue devices or sending deauth packets to disrupt attackers.
- Use AI-driven reinforcement learning to improve detection accuracy and response strategies over time.
- Provide real-time visibility into network threats through logs and potential dashboard features.

## ⚙️ Features

- **AI-Driven Threat Detection**:
  - Incorporates reinforcement learning to identify patterns associated with deauth packets, rogue devices, and abnormal traffic.
  - Learns from previous responses to optimize future actions.
- **Real-Time Monitoring**:
  - Continuously analyzes Wi-Fi traffic for suspicious activity.
- **Automated Response**:
  - Dynamically blocks or isolates malicious devices.
  - Sends deauth packets to disrupt attackers within authorized environments.
- **Logging and Alerting**:
  - Maintains detailed logs of threats and actions.
  - Optional integration for email/SMS notifications for detected attacks.
- **Customizable and Extensible**:
  - Whitelist/blacklist management for trusted and untrusted devices.
  - Modular design to add features like Bluetooth monitoring or advanced anomaly detection.

## 🛠️ Technology Stack

Punisher is primarily developed in **Python** for its flexibility and extensive library ecosystem. 

- **Python**:
  - Libraries: `scapy`, `stable-baselines3`, `torch`, `flask` (for future dashboard), `logging`.
- **Reinforcement Learning**:
  - Powered by `stable-baselines3` and `PyTorch`.
- **Hardware**:
  - Optimized for lightweight deployment on devices like Raspberry Pi with a Wi-Fi adapter capable of monitor mode.
- **Containerization**:
  - Optionally developed and deployed using Podman for consistency and ease of use across devices.

## 🔧 Setup
### Prerequisites
1. **Hardware**:
   - A Raspberry Pi (or similar device) with a Wi-Fi adapter capable of monitor mode.
2. **Software**:
   - Python 3.8+ installed on the system.
   - Required Python libraries:
     - `scapy`
     - `stable-baselines3`
     - `torch`
     - `flask`
     - `logging`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/punisher.git
   cd punisher
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the tool:
   - Set up your whitelist of trusted MAC addresses in `config.py`.
   - Update alert preferences (e.g., email or SMS) in `alerts.py`.
4. Run the tool:
   - Start monitoring with:
     ```bash
     python main.py
     ```

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
2. **Advanced Machine Learning**:
   - Reinforcement learning models to enhance anomaly detection and response strategies.
3. **Bluetooth Threat Detection**:
   - Expand support to detect and respond to malicious Bluetooth activity.
4. **Automated Updates**:
   - Add mechanisms to fetch and deploy updates seamlessly.

## 📝 Disclaimer
Punisher is intended strictly for **personal or authorized use** within controlled environments. Misuse of this tool for unauthorized or malicious purposes is strictly prohibited and may violate laws in your jurisdiction.
