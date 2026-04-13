import os
import time
import json
import subprocess
import shutil

# ArmstrongLogic: Unified Sovereign Controller v4.1
# Core: M4 Apple Silicon | Location: Ottawa, IL Node
# Features: Thermal Logic, Priority Gating, Storage Guard (10GB)
# Security Clearance: LEVEL-OMEGA

class SovereignStateMachine:
    def __init__(self):
        self.state = "NOMINAL"
        self.hysteresis = 5
        self.paths = {
            "prophet": os.path.expanduser("~/prophet_module/state/prophet_sync.json"),
            "tiktok": os.path.expanduser("~/popular_picks/api_status.json"),
            "thermal": "/usr/bin/powermetrics",
            "audit_logs": os.path.expanduser("~/prophet_module/logs/"),
            "ecommerce_logs": os.path.expanduser("~/popular_picks/logs/")
        }
        self.thresholds = {"NOMINAL": 70, "CAUTION": 75, "ALERT": 80, "STRIKE": 70}
        self.storage_limit_gb = 10

    def check_storage_health(self):
        """Ensures the Prophet has a runway. Purges if disk < 10GB."""
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)
        
        if free_gb < self.storage_limit_gb:
            print(f"[CRITICAL] Storage at {free_gb}GB. Initiating Log-Purge Protocol.")
            for log_path in [self.paths["audit_logs"], self.paths["ecommerce_logs"]]:
                if os.path.exists(log_path):
                    files = [os.path.join(log_path, f) for f in os.listdir(log_path)]
                    # Sort by modification time, delete oldest
                    files.sort(key=os.path.getmtime)
                    for f in files[:-10]: # Keep only the 10 most recent logs
                        try:
                            os.remove(f)
                            print(f"[PURGE] Deleted legacy log: {f}")
                        except: pass

    def get_telemetry(self):
        try:
            cmd = f"sudo {self.paths['thermal']} -n 1 --samplers thermal | grep 'CPU die temperature'"
            temp_out = subprocess.check_output(cmd, shell=True).decode('utf-8')
            temp = float(temp_out.split(":")[1].strip().replace(" C", ""))
            
            prophet = False
            if os.path.exists(self.paths["prophet"]):
                with open(self.paths["prophet"], 'r') as f:
                    prophet = json.load(f).get("status") == "active_strike"
            
            tiktok = False
            if os.path.exists(self.paths["tiktok"]):
                with open(self.paths["tiktok"], 'r') as f:
                    tiktok = json.load(f).get("high_traffic") is True
            return temp, prophet, tiktok
        except: return 55.0, False, False

    def engage_omega_protocol(self, mode):
        if mode == "PROPHET_PROTECTION":
            print("[OMEGA
if mode == "PROPHET_PROTECTION":
            print("[OMEGA] Prophet Shield Active. E-Core Handoff.")
            subprocess.run(["sysctl", "-w", "debug.lowpri_throttle=1"], capture_output=True)
            self.set_fans(70)
        elif mode == "ECOMMERCE_PRIORITY":
            print("[ALERT] E-commerce Spike. Balanced Throttling.")
            subprocess.run(["sysctl", "-w", "debug.lowpri_throttle=1"], capture_output=True)
            self.set_fans(55)
        elif mode == "RESTORE_PERFORMANCE":
            print("[OPTIMAL] Nominal 7-Logic. Performance mode active.")
            subprocess.run(["sysctl", "-w", "debug.lowpri_throttle=0"], capture_output=True)
            self.set_fans(40)

    def set_fans(self, speed):
        # SMC Interface Simulation
        print(f"[ACTION] M4 Mesh Fan Duty: {speed}%")

    def run(self):
        print("[ArmstrongLogic Online] Sovereign State-Machine v4.1 Engaged.")
        while True:
            self.check_storage_health()
            temp, prophet, tiktok = self.get_telemetry()
            
            target = self.thresholds["STRIKE"] if prophet else self.thresholds["NOMINAL"]
            if temp > target + self.hysteresis:
                mode = "PROPHET_PROTECTION" if prophet else "ECOMMERCE_PRIORITY"
                self.engage_omega_protocol(mode)
            elif temp < target - self.hysteresis:
                self.engage_omega_protocol("RESTORE_PERFORMANCE")
            
            time.sleep(60)

if __name__ == "__main__":
    try:
        SovereignStateMachine().run()
    except KeyboardInterrupt:
        subprocess.run(["sysctl", "-w", "debug.lowpri_throttle=0"], capture_output=True)
        print("\n[ALERT] Resetting to Performance Mode.")
