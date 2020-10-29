# clean up the generated documentation files

import os.path
import shutil


def main():
    docdir = os.path.dirname(__file__) + '/../docs/'
    shutil.move(docdir + 'olcarpc/index.md', docdir + 'index.md')
    shutil.rmtree(docdir + 'olcarpc', ignore_errors=True)


if __name__ == '__main__':
    main()
