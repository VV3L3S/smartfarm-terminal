import random
from datetime import datetime

def sample():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "soil_moisture": round(random.uniform(10, 80), 1),
        "temperature_c": round(random.uniform(5, 35), 1),
        "humidity": round(random.uniform(20, 95), 1),
        "light_lux": int(random.uniform(0, 20000))
    }
