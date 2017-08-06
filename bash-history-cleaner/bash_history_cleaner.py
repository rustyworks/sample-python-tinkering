import os
import sqlite3


HOME_DIRECTORY = os.path.expanduser('~')


def read_bash_history():
    with open('{home_directory}/.bash_history'.format(home_directory=HOME_DIRECTORY)) as bash_history:
        history = bash_history.readlines()
    return history

def bash_history_to_dictionary(history):
    command_repetition = {}

    for command in history:
        if command in command_repetition:
            command_repetition[command] += 1
        else:
            command_repetition[command] = 1
    return command_repetition

def compact_history(command_repetition):
    with open('{home_directory}/.bash_history'.format(home_directory=HOME_DIRECTORY), 'w') as bash_history:
        bash_history.writelines(list(command_repetition.keys()))

def save_to_db(command_repetition):
    connection = sqlite3.connect('bash_history.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS command_repetitions (command TEXT, repetition INT)')
    connection.commit()

    for command in command_repetition:
        total_repetition = command_repetition[command]
        cursor.execute('SELECT * FROM command_repetitions WHERE command=?', (command, ))
        result = cursor.fetchone()
        if result is None:
            cursor.execute('INSERT INTO command_repetitions VALUES (?, ?)', (command, total_repetition))
            connection.commit()
        elif total_repetition > 1:
            new_repetition_value = (total_repetition - 1) + result[1]
            cursor.execute('UPDATE command_repetitions SET repetition=? WHERE command=?', (new_repetition_value, command))
        connection.commit()

    cursor.execute('SELECT * fROM command_repetitions')


if __name__ == '__main__':
    bash_history = read_bash_history()
    command_repetition = bash_history_to_dictionary(bash_history)
    save_to_db(command_repetition)
    compact_history(command_repetition)
