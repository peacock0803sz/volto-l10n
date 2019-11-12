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


def fetch(pofile):
    plone = polib.pofile('plone/' + pofile)
    plone_ids = [entry.msgid for entry in plone]
    plone_strs = [entry.msgstr for entry in plone]
    volto = polib.pofile(VOLTO_FILE)
    volto_ids = [entry.msgid for entry in volto]
    plone_fetched_indexes = []
    for id_ in volto_ids:
        if id_ in plone_ids:
            plone_fetched_indexes.append(plone_ids.index(id_))
        else:
            plone_fetched_indexes.append(None)
    fetched_strs, fetched_ids = [], []
    for i in plone_fetched_indexes:
        if i is not None:
            fetched_strs.append(plone_strs[i])
        else:
            fetched_strs.append(None)
    # fetched_strs = [plone_strs[i[0]][i[1]] for i in plone_fetched_indexes]
    return volto_ids, fetched_strs
