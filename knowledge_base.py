# List of all possible symptoms (Facts) the user can input
AVAILABLE_SYMPTOMS = [
    "lights_dim", "engine_cranks_slowly", "rapid_clicking",
    "lights_bright", "engine_cranks_normally", "engine_wont_start",
    "fuel_gauge_empty", "smells_like_gas", "no_fuel_pump_whine",
    "engine_runs_rough", "check_engine_light", "high_mileage"
]

# Rule Base: If all 'conditions' are met, the 'result' is deduced.
RULES = [
    # Multi-step Battery Reasoning
    {"id": "R1", "conditions": ["lights_dim", "engine_cranks_slowly"], "result": "battery_low"},
    {"id": "R2", "conditions": ["battery_low", "rapid_clicking"], "result": "battery_dead"},
    {"id": "R3", "conditions": ["battery_dead"], "result": "CONCLUSION: Replace Battery"},
    
    # Starter Motor Reasoning
    {"id": "R4", "conditions": ["lights_bright", "rapid_clicking"], "result": "starter_faulty"},
    {"id": "R5", "conditions": ["starter_faulty"], "result": "CONCLUSION: Replace Starter Motor"},
    
    # General Fuel/Spark Reasoning (Multi-step)
    {"id": "R6", "conditions": ["engine_cranks_normally", "engine_wont_start"], "result": "check_fuel_spark"},
    
    # Specific Fuel/Spark Issues
    {"id": "R7", "conditions": ["check_fuel_spark", "fuel_gauge_empty"], "result": "out_of_gas"},
    {"id": "R8", "conditions": ["out_of_gas"], "result": "CONCLUSION: Add Fuel"},
    
    {"id": "R9", "conditions": ["check_fuel_spark", "smells_like_gas"], "result": "flooded_engine"},
    {"id": "R10", "conditions": ["flooded_engine"], "result": "CONCLUSION: Wait 15 mins and try starting with pedal to the floor"},
    
    {"id": "R11", "conditions": ["check_fuel_spark", "no_fuel_pump_whine"], "result": "bad_fuel_pump"},
    {"id": "R12", "conditions": ["bad_fuel_pump"], "result": "CONCLUSION: Replace Fuel Pump"},
    
    # Engine Running Issues
    {"id": "R13", "conditions": ["engine_runs_rough", "check_engine_light"], "result": "misfire"},
    {"id": "R14", "conditions": ["misfire", "high_mileage"], "result": "worn_spark_plugs"},
    {"id": "R15", "conditions": ["worn_spark_plugs"], "result": "CONCLUSION: Replace Spark Plugs"}
]