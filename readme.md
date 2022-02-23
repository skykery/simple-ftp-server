Command to build
```commandline
pyinstaller -w -F  --osx-bundle-identifier 'SIMPLEFTPSERVER' --hidden-import PyQt6.sip --noconfirm  app.py
```

Command to translate .ui to py class
```commandline
pyside6-uic test-design.ui > ui_mainwindow.py 
```