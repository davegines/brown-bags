from v2.command_abc import CommandAbc


class CreateOrder(CommandAbc):
    name = 'CreateOrder'

    def __init__(self, args):
        pass

    def execute(self):
        print('creating order')
