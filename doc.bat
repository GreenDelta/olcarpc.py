@echo off
rem we use pdoc3 to generate our documentation
rem see https://github.com/pdoc3/pdoc

del /s /q doc\*.html

pdoc --html --force --config latex_math=True --output-dir docs olcarpc
