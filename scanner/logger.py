from datetime import datetime
import os

def save_results(results, target):
    target_clean = target.replace(".", "_").replace(":", "_")
    filename = f"scan_{target_clean}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    os.makedirs("logs", exist_ok=True)
    filepath = os.path.join("logs", filename)

    with open(filepath, "w") as f:
        f.write(f"Scan Results for {target} - {datetime.now()}\n")
        f.write("-" * 50 + "\n")
        for port, banner in results:
            f.write(f"Port {port}: {banner}\n")

    print(f"\n[✓] Results saved to {filepath}")
