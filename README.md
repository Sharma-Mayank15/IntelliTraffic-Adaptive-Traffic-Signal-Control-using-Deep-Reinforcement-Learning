
# Deep Q-Learning Based Traffic Signal Control System

This project implements a Deep Q-Learning (DQN) agent to control traffic lights in a simulated environment using **SUMO** (Simulation of Urban MObility). The goal is to optimize traffic flow by learning efficient traffic light control policies.

---

## 🧠 Project Overview

Using a reinforcement learning approach, the DQN agent observes traffic conditions and decides which phase (green/red) to activate at an intersection. The agent is trained using the SUMO simulator and Python.

---

## 📁 Project Structure

```
dqn_traffic_signal_control/
├── main.py                    # Main script to run training loop and interact with SUMO
├── dqn_agent.py               # Contains DQNAgent class with training and prediction logic
├── utils.py                   # Helper functions for state construction, rewards, actions
├── cross3itl.sumocfg          # SUMO configuration file
├── input_routes.rou.xml       # Route file defining vehicle flows
├── net.net.xml                # Network file for the traffic intersection
├── traffic_light_control.add.xml  # Additional file for traffic light logic definition
├── log/                       # Directory for logs and trained models
│   └── training_log.txt       # Example log file storing training metrics
└── README.md                  # Documentation and setup instructions
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- SUMO (installed and added to your system path)
- Required Python packages (install with pip):

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

### Run the Training

```bash
python main.py
```

This script will start a SUMO simulation and train the DQN agent to optimize traffic light control.

---

## 📊 Outputs

- Logs are saved in the `log/` directory.
- Trained model weights are saved periodically.
- Visualizations of the training progress (reward, wait time, etc.) can be added.

---

## 🤖 How It Works

1. **State Representation**: The current traffic state is encoded from SUMO.
2. **Action Selection**: DQN selects an action (e.g., change light phase).
3. **Reward Function**: Designed to minimize vehicle wait time.
4. **Learning**: Experience replay and Q-learning updates the agent.

---

## 🛠️ Customization

- Modify `utils.py` to change the state or reward definition.
- Edit `cross3itl.sumocfg` or `input_routes.rou.xml` to simulate different traffic conditions.
- Extend `main.py` to test multiple intersections or change hyperparameters.

---

## 🧾 License

MIT License. Feel free to use, modify, and distribute.

---

## 👤 Author

**Mayank Sharma**  
linkedin.com/in/mayank-sharma-359807230/
📧 MAYANKARYAN309@GMAIL.COM



