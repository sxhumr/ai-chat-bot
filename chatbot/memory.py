class ConversationMemory:
    def __init__(self, system_prompt: str, max_turns: int = 20):
        self.max_turns = max_turns
        self.messages = [{"role": "system", "content": system_prompt}]

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_turns * 2 + 1:
            self.messages = [self.messages[0]] + self.messages[-(self.max_turns * 2):]

    def get(self) -> list:
        return self.messages

    def clear(self):
        system = self.messages[0]
        self.messages = [system]