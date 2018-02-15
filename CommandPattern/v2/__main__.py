import sys
from v2.create_order import CreateOrder
from v2.update_order import UpdateOrder

if len(sys.argv) < 2:
    print('Commands:')
    print(' CreateOrder')
    print(' UpdateQuantity')
    exit()


def get_commands():
    cmds = (CreateOrder, UpdateOrder)
    return dict([cls.name, cls] for cls in cmds)


def parse_command(cmds, args):
    cmd = cmds.setdefault(args[0])
    return cmd(args)


commands = get_commands()

command = parse_command(commands, sys.argv[1:])
command.execute()
