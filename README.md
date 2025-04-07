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

# Executar os testes pela classe

```bash
pytest tests/specs/test_login.py::TestLogin
```

# Executar testes pelo métodos da classe

```bash
pytest tests/specs/test_login.py::TestLogin::test_login_with_invalid_credentials
```

# Executar teste com a saída e captura de prints

```bash
pytest -s tests/
```

# Executar testes que contenha o nome

```bash
pytest -k invalid
```