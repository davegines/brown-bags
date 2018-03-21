import sys
from CommandPattern.v1.command_executor import CommandExecutor

if len(sys.argv) < 2:
    print('Commands:')
    print(' CreateOrder')
    print(' UpdateQuantity')
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])
