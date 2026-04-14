import mlx_lm
from mlx_lm.sample_utils import make_sampler
import os
import json

# [ArmstrongLogic Online] - LEVEL-OMEGA
# Optimized for MLX-LM v0.31.2 API Standards
MODEL_PATH = os.path.expanduser("~/.armstrong_models/gemma-4-e4b-4bit")
ADAPTER_PATH = os.path.expanduser("~/adapters")

class SyntropicMesh:
    def __init__(self):
        print("[ArmstrongLogic] Calibrating Syntropic Core (v0.31.2)...")
        self.model, self.tokenizer = mlx_lm.load(MODEL_PATH, adapter_path=ADAPTER_PATH)
        # Construct the sampler separately to avoid TypeError
        self.sampler = make_sampler(temp=0.7, repetition_penalty=1.2)

    def dream_recovery(self, corridor_data):
        prompt = (
            f"SYNTROPIC_DATA: {corridor_data}. "
            "Using 7/8 logic, analyze the I-80 pharma desync. "
            "Provide a clinical, non-repetitive recovery strategy."
        )
        
        # Pass the sampler object explicitly
        recovery_path = mlx_lm.generate(
            self.model, 
            self.tokenizer, 
            prompt=prompt, 
            max_tokens=300,
            sampler=self.sampler
        )
        return recovery_path

if __name__ == "__main__":
    telemetry = {
        "node": "ORD-SOUTH-CARGO",
        "load": "Biologics-V-08",
        "threat": "Imminent 45m Desync at I-294 interchange"
    }
    
    mesh = SyntropicMesh()
    result = mesh.dream_recovery(json.dumps(telemetry))
    
    print("\n" + "="*60)
    print("SYNTROPIC RECOVERY PATH (STABILIZED):")
    print("="*60)
    print(result)
    print("="*60)
