class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):
        last_command = self.history.pop()
        return last_command.backup
# TODO: write test case
# a = CommandHistory()
# a.push(1)
# a.push(2)
# print( a.pop())

