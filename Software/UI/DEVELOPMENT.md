# Kancil UI development

## Requirements
- Python 3.12+
- Git
- pip
- A Nerd Font (required for icons)

## Setting up a development environment
1. Clone the repository
    ```
    git clone https://github.com/muhammadelfatir5
    ```

2. Set up a virtual environment and install dependencies
2.1 Create a virtual environment
    ```
    python -m venv .venv
    ```
    2.2 Activate the environment
    Note: depends on what OS/shell you use.
    Linux/MacOS (Bash/Zsh)
    ```
    source .venv/bin/activate.txt
    ```
    Windows (CMD)
    ```
    .venv/bin/activate.bat
    ```
    Windows (Powershell)
    ```
    .venv/bin/activate.ps1
    ```
    2.2 Install dependencies.Install dependencies
    ```
    pip install -r requirements.txt
    ```
3. Run the UI
    ```
    python main.py
    ```
4. When you're done, deactivate the virtual environment
    ```
    deactivate
    ```