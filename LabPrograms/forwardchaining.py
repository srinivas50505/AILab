class Rule:
    def _init_(self, conditions, result):
        self.conditions = conditions 
        self.result = result

    def evaluate(self, facts):

        if all(condition in facts for condition in self.conditions):
            return self.result
        return None

class ForwardChainingEngine:
    def _init_(self, rules):
        self.rules = rules

    def infer(self, initial_facts):
        facts = initial_facts.copy()
        while True:
            new_facts_added = False
            for rule in self.rules:
                result = rule.evaluate(facts)
                if result and result not in facts:
                    facts.append(result)
                    new_facts_added = True
            if not new_facts_added:
                break
        return facts

# Example usage
rules = [
    Rule(["fever", "cough"], "flu"),
    Rule(["fever", "sore throat"], "flu"),
    Rule(["headache", "fatigue"], "migraine"),
    Rule(["runny nose"], "common cold"),
    Rule(["sneezing"], "allergies")
]

engine = ForwardChainingEngine(rules)
initial_facts = ["fever", "cough", "sore throat"]
conclusion = engine.infer(initial_facts)
print("Initial facts:", initial_facts)
print("Conclusion:", conclusion[-1])
