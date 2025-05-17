
import traci
import numpy as np

def get_state():
    lanes = ["lane1", "lane2", "lane3", "lane4"]
    state = []
    for lane in lanes:
        state.append(traci.lane.getLastStepVehicleNumber(lane))
    state += [traci.trafficlight.getPhase("junction")]  # "junction" is the traffic light ID
    return np.array(state, dtype=np.float32)

def compute_reward():
    lanes = ["lane1", "lane2", "lane3", "lane4"]
    total_wait = 0
    for lane in lanes:
        total_wait += traci.lane.getWaitingTime(lane)
    return -total_wait

def apply_action(action):
    if action == 0:
        traci.trafficlight.setPhase("junction", 0)
    elif action == 1:
        traci.trafficlight.setPhase("junction", 2)
    elif action == 2:
        traci.trafficlight.setPhase("junction", 4)
    else:
        traci.trafficlight.setPhase("junction", 6)
