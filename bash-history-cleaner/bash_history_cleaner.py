import os

HOME_DIRECTORY = os.path.expanduser('~')
command_repetition = {}

with open('{home_directory}/.bash_history'.format(home_directory=HOME_DIRECTORY)) as bash_history:
    history = bash_history.readlines()

    for command in history:
        if command in command_repetition:
            command_repetition[command] += 1
        else:
            command_repetition[command] = 1

with open('{home_directory}/.bash_history'.format(home_directory=HOME_DIRECTORY), 'w') as bash_history:
    bash_history.writelines(list(command_repetition.keys()))
