# Car-Fault-Diagnosis-Expert-System

## Problem Being Solved
This project implements an Expert System to diagnose common car faults. Non-expert drivers often struggle to identify the root cause of vehicular breakdowns. This system allows users to input observable symptoms and utilizes a rule-based inference engine to diagnose the issue and recommend a fix.

## Facts Used
The system relies on observable symptoms as base facts, including:
`lights_dim`, `engine_cranks_slowly`, `rapid_clicking`, `lights_bright`, `engine_cranks_normally`, `engine_wont_start`, `fuel_gauge_empty`, `smells_like_gas`, `no_fuel_pump_whine`, `engine_runs_rough`, `check_engine_light`, `high_mileage`.

## Rules Used
The system uses 15 forward-chaining rules. Examples include:
* **Rule 1:** IF `lights_dim` AND `engine_cranks_slowly` THEN `battery_low`.
* **Rule 2:** IF `battery_low` AND `rapid_clicking` THEN `battery_dead`.
* **Rule 11:** IF `check_fuel_spark` AND `no_fuel_pump_whine` THEN `bad_fuel_pump`.

## How Inference Works
This system uses **Forward Chaining**. 
1. The user inputs initial facts into the "working memory".
2. The engine iterates through the rule base. If all conditions of a rule are met in the working memory, the rule's result is appended as a new fact.
3. This process repeats (multi-step reasoning) until no new facts can be generated.
4. If a fact tagged as a `CONCLUSION:` is generated, it is presented as the final diagnosis.

## How to Run the System
1. Ensure you have Python 3.x installed.
2. Clone this repository.
3. Run the main script via terminal:
   ```bash
   python main.py


graph TD
    Car -- has_part --> Electrical_System
    Car -- has_part --> Fuel_System
    Electrical_System -- has_part --> Battery
    Electrical_System -- has_part --> Starter_Motor
    Fuel_System -- has_part --> Fuel_Pump
    
    Lights_Dim -- indicates --> Battery_Low
    Engine_Cranks_Slowly -- indicates --> Battery_Low
    Battery_Low -- causes --> Rapid_Clicking
    Rapid_Clicking -- indicates --> Battery_Dead
    Battery_Dead -- requires --> Replace_Battery
    
    No_Fuel_Pump_Whine -- indicates --> Bad_Fuel_Pump
    Bad_Fuel_Pump -- requires --> Replace_Fuel_Pump