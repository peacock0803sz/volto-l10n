import polib

VOLTO_FILE = 'volto.po'
ID_PREFIX = 'msgid "'


def initialize():
    # po = polib.POFile
    # entries = []
    # for i in range(len(volto_ids)):
    #     entries[i] = polib.POEntry(msgid=volto_ids[i], msgstr='')
    with open(VOLTO_FILE, mode='r') as r:
        lines = r.readlines()
    for i in range(20, len(lines)):
        if lines[i].startswith(ID_PREFIX):
            lines[i + 1] = 'msgstr ""\n'
    with open(VOLTO_FILE, mode='w') as w:
        for l in lines:
            w.writelines(l)
