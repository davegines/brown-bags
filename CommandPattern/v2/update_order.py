from CommandPattern.v2.command_abc import CommandAbc


class UpdateOrder(CommandAbc):
    name = 'UpdateQuantity'

    def __init__(self, args):
        self.new_quantity = args[1]

    def execute(self):
        print('Updating quantity to {}'.format(self.new_quantity))
