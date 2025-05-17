
import os
import traci
import numpy as np
from dqn_agent import DQNAgent
from utils import get_state, compute_reward, apply_action
import sumolib

EPISODES = 100
MAX_STEPS = 1000

sumo_binary = "sumo"  # Or "sumo-gui" for visualization
sumo_config = "your_sumo_config.sumocfg"  # Replace with your .sumocfg path
sumo_cmd = [sumo_binary, "-c", sumo_config]

agent = DQNAgent(state_size=147, action_size=4)  # Adjust state size

for episode in range(EPISODES):
    traci.start(sumo_cmd)
    state = get_state()
    total_reward = 0

    for step in range(MAX_STEPS):
        action = agent.act(state)
        apply_action(action)
        traci.simulationStep()
        next_state = get_state()
        reward = compute_reward()
        total_reward += reward

        agent.remember(state, action, reward, next_state)
        state = next_state

        if step % 10 == 0:
            agent.replay()

    agent.update_target_model()
    traci.close()
    print(f"Episode {episode+1}/{EPISODES}, Total Reward: {total_reward}")

agent.save("dqn_model.h5")
