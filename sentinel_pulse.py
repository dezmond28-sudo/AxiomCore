import os
import socket
import time
import json
import datetime
import sys

# Sentinel Heartbeat v1.1 - Hardened
NODE_NAME = socket.gethostname()
LOG_FILE = os.path.expanduser("~/prophet/heartbeat.log")

def pulse():
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "node": NODE_NAME,
        "status": "ONLINE",
        "mesh_integrity": 1.0,
        "security_clearance": "LEVEL-OMEGA"
    }
    
    # Write to local JSON buffer
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    
    # Force flush stdout for launchd visibility
    print(f"[ArmstrongLogic] Pulse emitted from {NODE_NAME} at {data['timestamp']}")
    sys.stdout.flush()

if __name__ == "__main__":
    while True:
        pulse()
        time.sleep(60)
