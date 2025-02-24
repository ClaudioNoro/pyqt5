#!/bin/bash

# Atualize o pip para garantir que está na versão mais recente
python -m pip install --upgrade pip

# Instalar pacotes de dependência listados no arquivo requirements
pip install click==8.1.7
pip install colorama==0.4.6
pip install distlib==0.3.8
pip install filelock==3.13.1
pip install flake8==7.0.0
pip install mccabe==0.7.0
pip install pep8==1.7.1
pip install platformdirs==4.1.0
pip install pycodestyle==2.11.1
pip install pyflakes==3.2.0
pip install PyQt5==5.15.9
pip install python-dotenv==1.0.0
pip install qt5-applications==5.15.2.2.3
pip install qt5-tools==5.15.2.1.3
pip install setuptools==69.0.3
pip install virtualenv==20.25.0
pip install wheel==0.36.0
pip install requests==2.31.0
pip install pandas==2.0.3
pip install matplotlib==3.8.3
pip install auto-py-to-exe==2.44.1
pip install pyinstaller==6.10.0
pip install pyinstaller_versionfile==3.0.0

# Instalar pacotes a partir dos arquivos .whl
pip install JsonModule-0.8.2-py3-none-any.whl
pip install glaciation-1.9b1-py3-none-any.whl
pip install AtriaWrapper-4.0.1-py3-none-any.whl
