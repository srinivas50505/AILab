class Rule:
    def _init_(self, result, conditions):
        self.result = result
        self.conditions = conditions

    def evaluate(self, facts):
        if self.result in facts:
            return all(condition in facts for condition in self.conditions)
        return False

class BackwardChainingEngine:
    def _init_(self, rules):
        self.rules = rules

    def infer(self, goal, known_facts):
        if goal in known_facts:
            return True
        for rule in self.rules:
            if rule.result == goal:
                if all(self.infer(condition, known_facts) for condition in rule.conditions):
                    return True
        return False

# Example usage
rules = [
    Rule("flu", ["fever", "cough"]),
    Rule("flu", ["fever", "sore throat"]),
    Rule("migraine", ["headache", "fatigue"]),
    Rule("common cold", ["runny nose"]),
    Rule("allergies", ["sneezing"])
]

engine = BackwardChainingEngine(rules)
goal = "flu"

# Goal 'flu' can be inferred from known facts.
known_facts = ["fever", "cough", "sore throat"]
if engine.infer(goal, known_facts):
    print("Goal '{}' can be inferred from known facts.".format(goal))
else:
    print("Goal '{}' cannot be inferred from known facts.".format(goal))
