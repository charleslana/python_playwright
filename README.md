# Install on linux

```bash
sudo apt install python3.12-venv
```

# Install venv

```bash
python3 -m venv venv
```

# Ativar source

```bash
source venv/bin/activate
```

# Install requirements

```bash
pip install -r requirements.txt
```

# Install browsers

```bash
playwright install --with-deps
```

# Executar os testes

```bash
pytest
```

# Com relatório

```bash
pytest --html=report.html --self-contained-html
```

# Executar modo headless ou head

### [sem cabeça = true, com cabeça = false]

```bash
HEADLESS=false pytest
```

# Uninstall package

```bash
python -m pip uninstall package-aqui
```

# Configurar o play tests do vscode

Ctrl+Shift+P -> Python: Configurar Testes -> pytest -> tests

# Selecionar ambiente virtual do venv

Ctrl+Shift+P -> Python: Selecionar Interpretador -> venv

# Executar os testes pela classe

```bash
pytest tests/specs/test_login.py::TestLogin
```

# Executar testes pelo métodos da classe

```bash
pytest tests/specs/test_login.py::TestLogin::test_login_with_invalid_credentials
```

# Executar teste com a saída de logs

```bash
pytest -s tests/
```

# Executar testes que contenha o nome

```bash
pytest -k invalid
```

# Extensões para o VSCode

- Black
- Python
- Pylint
- Python Debugger
- Pylance
- Robot Framework Language Server
- String Manipulation
- Select Line Status Bar
- Material Icon Theme
- Git Blame
- Dracula Theme Official
- Brazilian Portuguese - Code Spell Checker
- Code Spell Checker

User json

```bash
{
  "cSpell.language": "en,pt,pt_BR",
  "editor.formatOnSave": true,
  "explorer.compactFolders": false,
  "files.autoSave": "afterDelay",
  "workbench.colorTheme": "Dracula Theme",
  "workbench.iconTheme": "material-icon-theme"
}
```

User keyboard json

```bash
// Coloque as suas associações de teclas neste arquivo para substituir os padrõesauto[]
[
    {
        "key": "ctrl+d ctrl+d",
        "command": "editor.action.addSelectionToNextFindMatch",
        "when": "editorFocus"
    },
    {
        "key": "ctrl+d",
        "command": "-editor.action.addSelectionToNextFindMatch",
        "when": "editorFocus"
    },
    {
        "key": "ctrl+d",
        "command": "editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+alt+down",
        "command": "-editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    }
]
```