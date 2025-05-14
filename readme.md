Crea tu entorno virtual

```sh
python -m venv .venv
```

Activar tu entorno virtual

```sh
.venv\Scripts\Activate.ps1

# En Linux
source .venv/bin/activate
```

Actualizar `pip`

```sh
python -m pip install --upgrade pip
```

Instalar fastapi

```sh
pip install "fastapi[standard]"

# Sin dependencias opcionales
pip install "fastapi"
```

Correr el codigo

```sh
fastapi dev main.py
```