from .rules import DEFAULT_RULES

def evaluate(sample):
    actions = []

    if sample["soil_moisture"] < DEFAULT_RULES["soil_moisture_low"]:
        actions.append("Irrigation ON")

    if sample["temperature_c"] > DEFAULT_RULES["temperature_high"]:
        actions.append("Cooling fans ON")

    return actions
