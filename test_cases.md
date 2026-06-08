# Test Cases and Evaluation

| Test Case | User Input (Symptoms) | Expected Inferred Facts (Middle Steps) | Expected Conclusion | Result |
| :--- | :--- | :--- | :--- | :--- |
| **TC1: Dead Battery** | `lights_dim`, `engine_cranks_slowly`, `rapid_clicking` | `battery_low`, `battery_dead` | Replace Battery | Pass |
| **TC2: Bad Starter** | `lights_bright`, `rapid_clicking` | `starter_faulty` | Replace Starter Motor | Pass |
| **TC3: Unknown Issue** | `engine_cranks_slowly`, `engine_wont_start`, `fuel_gauge_empty` |  None | System could not reach a definitive conclusion | Pass |
| **TC4: Out of Gas** | `engine_cranks_normally`, `engine_wont_start`, `fuel_gauge_empty` | `check_fuel_spark`, `out_of_gas` | Add Fuel | Pass |
| **TC5: Bad Fuel Pump** | `engine_cranks_normally`, `engine_wont_start`, `no_fuel_pump_whine` | `check_fuel_spark`, `bad_fuel_pump` | Replace Fuel Pump | Pass |
| **TC6: Unknown Issue** | `smells_like_gas` (only) | None | System could not reach a definitive conclusion | Pass |

**Evaluation:** The forward-chaining engine successfully handles multi-step reasoning. In TC1, the system first deduces `battery_low` from two symptoms, then combines that new fact with `rapid_clicking` to deduce `battery_dead`, proving inference depth.