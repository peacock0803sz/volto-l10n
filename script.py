import polib

VOLTO_FILE = 'volto.po'
ID_PREFIX = 'msgid "'


def initialize():
    with open(VOLTO_FILE, mode='r') as r:
        lines = r.readlines()
    for i in range(20, len(lines)):
        if lines[i].startswith(ID_PREFIX):
            lines[i + 1] = 'msgstr ""\n'
    with open(VOLTO_FILE, mode='w') as w:
        for l in lines:
            w.writelines(l)


def match(pofile):
    plone = polib.pofile('plone/' + pofile)
    plone_ids = [entry.msgid for entry in plone]
    plone_strs = [entry.msgstr for entry in plone]
    volto = polib.pofile(VOLTO_FILE)
    volto_ids = [entry.msgid for entry in volto]
    plone_matched_indexes = []
    for id_ in volto_ids:
        if id_ in plone_ids:
            plone_matched_indexes.append(plone_ids.index(id_))
        else:
            plone_matched_indexes.append(None)
    matched = []
    for i in plone_matched_indexes:
        if i is not None:
            matched.append((plone_ids[i], plone_strs[i]))
        else:
            matched.append((None, None))
    return matched


def write(matched):
    with open(VOLTO_FILE, mode='r') as r:
        lines = r.readlines()
        for j in range(10, len(lines)):
            if lines[j].startswith(ID_PREFIX):
                for i in range(len(matched)):
                    if lines[j].startswith(f'msgid "{matched[i][0]}'):
                        print(matched[i])
                        lines[j + 1] = f'msgstr "{matched[i][1]}"\n'
                        break
    with open(VOLTO_FILE, mode='w') as w:
        w.writelines(lines)


def main():
    initialize()
    pofiles = ['atcontenttypes.po', 'cmfeditions.po', 'plone.po', 'plonelocales.po',
               'atreferencebrowserwidget.po', 'cmfplacefulworkflow.po', 'plonefrontpage.po', 'widgets.po']
    for po in pofiles:
        write(match(po))
        # print(fetch(po))


if __name__ == '__main__':
    main()
