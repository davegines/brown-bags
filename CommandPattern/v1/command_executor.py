class CommandExecutor(object):
    def execute_command(self, args):
        if args[0] == 'CreateOrder':
            self.create_order()
        elif args[0] == 'UpdateQuantity':
            self.update_order(args[1])
        else:
            print('Unrecognized command: ' + args[0])

    def create_order(self):
        print('create order')

    def update_order(self, amount):
        print('update quantity to {}'.format(amount))
