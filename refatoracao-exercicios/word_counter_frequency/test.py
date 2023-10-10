import sys

from app import main

def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['app.py', mode, 'file.txt'])
    main()
    out, _ = capsys.readouterr()
    return out

