#### Sistema de ranking de postos de Oeiras

###### Instalação:
* Clone o repositório. 
* Crie um virtualenv com Python 3.10
* Ative o virtualenv. 
* Instale as dependências

```
git clone https://github.com/fabiorolim/postos_oeiras.git
cd postos_oeiras 
python3 -m venv .postos_oeiras
source .postos_oeiras/bin/activate
pip install -r requirements-dev.txt
```

* Crie o arquivo .env
```
SECRET_KEY=
DEBUG=
```

###### Rodando localmente:
```
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
