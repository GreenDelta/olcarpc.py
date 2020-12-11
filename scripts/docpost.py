# clean up the generated documentation files

import os.path
import shutil


def main():
    docdir = os.path.dirname(__file__) + '/../docs/'

    # move files to doc folder
    if os.path.exists(docdir + '/olcarpc'):
        for f in os.listdir(docdir + '/olcarpc'):
            shutil.move(docdir + 'olcarpc/' + f, docdir + f)
        shutil.rmtree(docdir + 'olcarpc', ignore_errors=True)

    for f in os.listdir(docdir):
        if f.endswith('.html'):
            strip_html(docdir + f)


def strip_html(path: str):
    print('clean up %s' % path)

    skip_blocks = [
        '<h3>Class variables</h3>',
        '<h3>Static methods</h3>'
    ]

    stripped = ''
    with open(path, 'r', encoding='utf-8', newline='\n') as stream:
        skip = False
        for line in stream:
            line = line.strip()

            # check for blocks that should be skipped
            if not skip:
                if line in skip_blocks:
                    skip = True
                    continue
            else:
                if line == '</dl>':
                    skip = False
                continue

            # remove uppercase identifiers from outline (these are Protocol
            # Buffers internal things)
            if line.startswith('<li><code><a title="'):
                if line[20:].split('"')[0].split('.')[-1][0].isupper():
                    continue

            # skip useless 'Getter for ...'  messages
            if line.startswith('<div class="desc"><p>Getter for '):
                continue

            stripped += line + '\n'

    with open(path, 'w', encoding='utf-8', newline='\n') as stream:
        stream.write(stripped)


if __name__ == '__main__':
    main()
