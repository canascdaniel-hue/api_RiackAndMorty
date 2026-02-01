# 🛸 Rick and Morty API

## 📋 Descripción

API épica de Rick and Morty construida con **FastAPI** que proporciona información de personajes del universo de Rick and Morty en tiempo real.

### 🚀 Características

- **🧪 Personajes Épicos**: Más de 800 personajes de Rick and Morty
- **🎯 Búsqueda**: Busca personajes por nombre
- **📂 Estados**: Personajes organizados por estado (alive, dead, unknown)
- **⚡ Súper Rápida**: Solo las dependencias esenciales
- **📚 Documentada**: Documentación automática con Swagger UI
- **🆓 Completamente Gratuita**: Sin API keys, sin límites, sin registro

---

## 🏗️ Estructura del Proyecto

```
api_clima-main2.0/
├── 📄 main.py                     # Aplicación principal FastAPI
├── 📄 appsettings.py             # Configuración de variables de entorno
├── 📁 controllers/               # Controladores
│   └── rickMortyController.py    # Controlador de Rick and Morty
├── 📁 services/                  # Lógica de negocio
│   └── rickMortyServices.py      # Servicios de Rick and Morty
├── 📁 clients/                   # Clientes para APIs externas
│   └── rickMortyClient.py        # Cliente rickandmortyapi.com
├── 📁 DTOs/                      # Modelos de datos
│   └── rickMortyDtos.py          # DTOs de Rick and Morty
├── 📄 requirements.txt           # Dependencias mínimas
├── 📄 .env.example              # Configuración de ejemplo
└── 📄 README.md                 # Esta documentación
```

---

## 🌐 Endpoints de la API

### 📍 Endpoints Principales

#### 1. **Personaje Aleatorio**
```http
GET /api/character/random
```
**Ejemplo:**
```bash
curl "http://localhost:8000/api/character/random"
```

#### 2. **Estados Disponibles**
```http
GET /api/character/statuses
```
**Ejemplo:**
```bash
curl "http://localhost:8000/api/character/statuses"
```

#### 3. **Personaje por Estado**
```http
GET /api/character/status/{status}
```
**Ejemplo:**
```bash
curl "http://localhost:8000/api/character/status/alive"
```

#### 4. **Buscar Personajes**
```http
GET /api/character/search?q={query}
```
**Ejemplo:**
```bash
curl "http://localhost:8000/api/character/search?q=rick"
```

---

## 📊 Ejemplos de Respuestas

### ✅ Personaje Aleatorio

```json
{
  "id": 1,
  "name": "Rick Sanchez",
  "status": "Alive",
  "species": "Human",
  "type": "",
  "gender": "Male",
  "origin": "Earth (C-137)",
  "location": "Citadel of Ricks",
  "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
  "episode_count": 51,
  "created": "2017-11-04T18:48:46.250Z"
}
```

### ✅ Estados

```json
{
  "statuses": ["alive", "dead", "unknown"]
}
```

### ✅ Resultados de Búsqueda

```json
{
  "total": 2,
  "result": [
    {
      "id": 1,
      "name": "Rick Sanchez",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Male",
      "origin": "Earth (C-137)",
      "location": "Citadel of Ricks",
      "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
      "episode_count": 51,
      "created": "2017-11-04T18:48:46.250Z"
    }
  ]
}
```

---

## ⚙️ Instalación

### 📋 Requisitos

- **Python 3.8+**
- **¡Eso es todo!** (No requiere API keys ni configuración adicional)

### 🚀 Instalación Súper Rápida

1. **Clonar y configurar**
```bash
git clone <repository-url>
cd api_clima-main2.0
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación**
```bash
uvicorn main:app --reload
```

4. **¡Listo! Acceder a la API**
- Swagger UI: http://localhost:8000/docs
- API: http://localhost:8000

---

## 🧪 Probar la API

### 1. **Personaje Aleatorio**
```bash
curl http://localhost:8000/api/character/random
```

### 2. **Ver Estados**
```bash
curl http://localhost:8000/api/character/statuses
```

### 3. **Personajes Vivos**
```bash
curl http://localhost:8000/api/character/status/alive
```

### 4. **Buscar Rick**
```bash
curl "http://localhost:8000/api/character/search?q=rick"
```

### 5. **Documentación Interactiva**
Visita http://localhost:8000/docs para probar todos los endpoints

---

## 📦 Dependencias

Solo las dependencias esenciales:

```txt
fastapi==0.104.1              # Framework web
uvicorn[standard]==0.24.0     # Servidor ASGI
httpx==0.25.2                 # Cliente HTTP
python-dotenv==1.0.0          # Variables de entorno
```

---

## 🌐 API Externa Utilizada

**rickandmortyapi.com**
- ✅ **Completamente gratuita**
- ✅ **Sin API key requerida**
- ✅ **Sin límites de peticiones**
- ✅ **Sin registro necesario**
- ✅ **Funciona inmediatamente**
- ✅ **Más de 800 personajes**

---

## 🚀 Despliegue

### Producción Simple
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Con Gunicorn
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 🎯 Estados Disponibles

- **alive** - Personajes vivos
- **dead** - Personajes muertos
- **unknown** - Estado desconocido

---

## 🧪 Personajes Populares

Algunos personajes que puedes buscar:
- **Rick** - El científico loco
- **Morty** - El nieto nervioso
- **Summer** - La hermana adolescente
- **Beth** - La madre veterinaria
- **Jerry** - El padre inseguro
- **Pickle** - Rick convertido en pepinillo

---

## 👨‍💻 Desarrollador

- **Nombre**: Ing. Daniel Issac Cañas
- **Fecha**: Enero 2026
- **Versión**: 1.0.0

---

## 🛸 Dato Curioso

"Wubba Lubba Dub Dub!" significa "Estoy sufriendo mucho, por favor ayúdame" en el idioma de Bird Person.

¡La API está lista para explorar el multiverso! 🚀 Visita `/docs` para la documentación interactiva completa.# rickAndMorty_api
