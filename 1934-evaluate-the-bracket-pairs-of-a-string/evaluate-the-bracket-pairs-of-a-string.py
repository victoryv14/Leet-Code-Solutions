class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        
        result = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
                current_key = []
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                result.append(lookup.get(key_str, "?"))
            elif in_bracket:
                current_key.append(char)
            else:
                result.append(char)
                
        return "".join(result)