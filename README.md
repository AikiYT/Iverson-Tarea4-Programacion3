# 🧪 Automatización de Pruebas con Selenium - Contact List App

Este proyecto consiste en la automatización de pruebas funcionales sobre la aplicación web [Contact List App](https://thinking-tester-contact-list.herokuapp.com/), utilizando **pytest** y **Python**. Las pruebas cubren operaciones básicas como inicio de sesión, creación de contactos y validaciones de campos.

---

## 🌐 Página probada

- [https://thinking-tester-contact-list.herokuapp.com/](https://thinking-tester-contact-list.herokuapp.com/)

<img width="900" alt="App Web" src="https://github.com/user-attachments/assets/113aa919-bf4e-4e7e-8bac-ac0bf17d06f8" />

---

## ⚙️ Tecnologías utilizadas

- Python 3.12  
- Selenium  
- Pytest  
- Pytest-html  
- ChromeDriver  
- Visual Studio Code (opcional)

---

## ✅ Casos de prueba automatizados

Se implementó **un caso de prueba por cada historia de usuario** (mínimo 5):

| Archivo                          | Descripción del caso de prueba                                         |
|----------------------------------|------------------------------------------------------------------------|
| `test_contact_crud.py`          | Agregar un nuevo contacto correctamente.                              |
| `test_login_failed.py`          | Fallar al iniciar sesión con credenciales inválidas.                  |
| `test_contact_phone_limit.py`   | Validación del límite de caracteres en el número telefónico.          |
| `test_phone_too_short.py`       | Validación de número de teléfono demasiado corto.                     |
| `test_phone_with_letters.py`    | Validación de letras en el campo de teléfono.                         |

---

## 📸 Capturas de pruebas (HTML Report)

Capturas de pantalla tomadas automáticamente durante la ejecución de los tests:

- `result/assets/contact_added.png`  
  <img width="800" alt="Contacto agregado" src="https://github.com/user-attachments/assets/25a9cc52-861a-4dd5-a090-2926f815e97c" />

- `result/assets/short_phone_attempt.png`  
  <img width="800" alt="Teléfono corto" src="https://github.com/user-attachments/assets/3a344e8b-93bd-4adb-b1dd-ca8fce122d1e" />

- `result/assets/letters_phone_attempt.png`  
  <img width="800" alt="Teléfono con letras" src="https://github.com/user-attachments/assets/e4d9f9b1-90a2-4ab4-a5a0-16fa7b87ade3" />

🔍 Puedes encontrar más imágenes adjuntas en las historias dentro del tablero Jira.

---

## 🗂️ Tablero en Jira

Aquí puedes ver las historias de usuario, los casos de uso, adjuntos y planificación general del proyecto:

🔗 [Ir al tablero Jira](https://itla-equipo3-bxfkc83r.atlassian.net/jira/software/projects/TI/boards/36)

---

## ▶️ Cómo ejecutar los tests (uno por uno)

> ⚠️ **Se recomienda ejecutar los tests individualmente** para evitar errores de concurrencia o conflictos con el navegador.

```bash
python -m pytest tests/test_contact_crud.py --html=result/report.html
python -m pytest tests/test_login_failed.py --html=result/report.html
python -m pytest tests/test_contact_phone_limit.py --html=result/report.html
python -m pytest tests/test_phone_too_short.py --html=result/report.html
python -m pytest tests/test_phone_with_letters.py --html=result/report.html





