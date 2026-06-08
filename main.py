from knowledge_base import RULES, AVAILABLE_SYMPTOMS

class ExpertSystem:
    def __init__(self):
        self.facts = set()
        self.explanation_log = []
        self.conclusions = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def infer(self):
        new_knowledge_added = True
        
        while new_knowledge_added:
            new_knowledge_added = False
            for rule in RULES:
                # Check if all conditions of the rule are in our current facts
                if all(condition in self.facts for condition in rule["conditions"]):
                    if rule["result"] not in self.facts:
                        self.facts.add(rule["result"])
                        new_knowledge_added = True
                        
                        # Part C: Explanation Facility - Record the reasoning
                        explanation = f"Applied {rule['id']}: Because {', '.join(rule['conditions'])}, inferred -> {rule['result']}."
                        self.explanation_log.append(explanation)
                        
                        # Check if it's a final recommendation
                        if rule["result"].startswith("CONCLUSION:"):
                            self.conclusions.append(rule["result"].replace("CONCLUSION: ", ""))

    def explain_reasoning(self):
        print("\n--- Explanation Facility ---")
        if not self.explanation_log:
            print("No rules were triggered based on the provided symptoms.")
        for step, log in enumerate(self.explanation_log, 1):
            print(f"Step {step}: {log}")

    def report_findings(self):
        print("\n--- Final Diagnosis ---")
        if self.conclusions:
            for conclusion in self.conclusions:
                print(f"Recommendation: {conclusion}")
        else:
            print("System could not reach a definitive conclusion based on current facts.")

def main():
    print("Welcome to the Car Fault Diagnosis Expert System")
    print("Available symptoms to report:")
    for i, symptom in enumerate(AVAILABLE_SYMPTOMS, 1):
        print(f"{i}. {symptom}")
    
    print("\nEnter the numbers of the symptoms your car is experiencing (comma-separated, e.g., 1,2,3):")
    user_input = input("> ")
    
    system = ExpertSystem()
    
    # Process user input
    try:
        selections = [int(x.strip()) for x in user_input.split(',')]
        for sel in selections:
            if 1 <= sel <= len(AVAILABLE_SYMPTOMS):
                system.add_fact(AVAILABLE_SYMPTOMS[sel-1])
    except ValueError:
        print("Invalid input. Please run again and enter numbers.")
        return

    # Run Inference
    system.infer()
    
    # Output Results
    system.report_findings()
    system.explain_reasoning()

if __name__ == "__main__":
    main()