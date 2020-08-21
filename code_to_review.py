def remove_spaces(s):
    if not isinstance(s, str):
        return None
    if not s:
        raise Exception('Empty string is not expected.')
    return s.replace(' ', '')


def write_slots(slots):
    try:
        with open('results.txt', mode='wt') as f:
            for s in slots:
                try:
                    f.writelines([s.result])
                except OSError:
                    print('Ошибка записи в файл')
            return True
    except PermissionError:
        print('Нет прав на создание файла! Переместите скрипт в домашнюю директорию.')
        return False


def main():
    slots = []
    for slot in slots:
        if slot.should_modify:
            slot.result = '<{}:{}>'.format(slot.beginning, slot.ending)
    slots = [slot.result for slot in slots if slot.result is not None]
    if write_slots(slots):
        print('Done')
    else:
        print('Error')
    return None
