#!/usr/bin/env python

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

ignore = ['duplex', 'alias', 'Current configuration']


def convert_config_to_dict(config_filename):
    with open('config_sw1.txt') as cfg:
        cfg = cfg.readlines()
        cfg_new = [line for line in cfg if not ignore_command(line, ignore)]
        l = []
        for line in ''.join(cfg_new).split('\n!'):
            line = line.lstrip()
            l.append(line)
        d = {}
        for intf in l:
            if intf.startswith('int'):
                intf = intf.split('\n')
                d.update({intf[0]: intf[0:]})
    return d



rslt = convert_config_to_dict('config_sw1.txt')

print(rslt)
