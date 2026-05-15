# Instrucciones para Estudiantes

## Objetivo de la practica

En esta práctica vas a crear un ejemplo sencillo de Python con objetos que se comunican entre sí. La idea es aprender cómo una parte del programa puede avisar a otras cuando ocurre algo importante.

También vas a practicar cómo trabajar con un entorno virtual, cómo ejecutar la aplicación y cómo correr las pruebas automáticas.

## Antes de empezar

La actividad se organiza con issues en GitHub. Cuando termines una parte, el sistema revisará tu avance y creará la siguiente misión.

No cierres los issues manualmente. Ese cierre lo hace el flujo automático cuando todo está correcto.

## Iniciar la práctica en GitHub

Después de tener tu copia del repositorio, haz esto una sola vez:

1. Entra a la pestaña **Actions**.
2. Elige **Iniciar práctica**.
3. Haz clic en **Run workflow**.
4. Revisa la pestaña **Issues** para ver la primera misión.

## Crear el entorno virtual

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Si PowerShell no te deja activar el entorno, ejecuta primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después vuelve a ejecutar la línea de activación.

## Estructura esperada

Durante la práctica vas a trabajar con esta organización:

```text
src/
  main.py
  observer_practice/
    __init__.py
    observer.py
    suscriptores.py
    canal.py
tests/
  test_observer.py
```

## Crear clases en Python

### `CanalNoticias`

Esta clase representa el canal de noticias. Su trabajo es guardar el nombre del canal, permitir que otras personas se suscriban, eliminar suscripciones y avisar cuando hay un nuevo mensaje.

En palabras simples: es el que publica la noticia y se la envía a todos los que están atentos.

### `SuscriptorEmail`

Esta clase representa a una persona que recibe noticias por correo electrónico.

En palabras simples:

- guarda el nombre del suscriptor;
- indica que su medio de recepción es el correo electrónico;
- almacena en una lista todos los mensajes que recibe;
- responde al aviso del canal agregando el mensaje a esa lista.

Es útil porque permite ver qué mensajes recibió cada persona sin mezclar esa información con la del canal.

### `SuscriptorSMS`

Esta clase representa a una persona que recibe noticias por mensaje de texto. Su funcionamiento es muy parecido al del suscriptor por correo, pero identifica su canal como SMS.

## Implementar Observer paso a paso

El patrón Observer se puede entender así: hay un canal que avisa y varias personas que escuchan.

En este proyecto:

- `CanalNoticias` es el sujeto. Es quien cambia y quien avisa.
- `SuscriptorEmail` y `SuscriptorSMS` son los observadores. Son quienes reciben el aviso.

Cada parte cumple una función simple:

- `suscribir` agrega un observador al canal.
- `desuscribir` quita un observador del canal.
- `notificar` envía el mensaje a todos los observadores.
- `publicar` guarda el último mensaje y luego lo comparte.

La idea es que, cuando el canal publique algo nuevo, todos los suscriptores que siguen conectados reciban ese mensaje en su lista.

## Ejecutar la demo

Cuando se necesite probar la aplicacion, se ejecuta desde la raiz del proyecto:

```bash
python src/main.py
```

Ese comando muestra una demostracion donde se crea un canal, se agregan suscriptores y se imprime lo que recibió cada uno.

## Ejecutar pruebas

Para comprobar que todo funciona como debe, ejecuta:

```bash
python -m pytest
```

Si una prueba falla, lee el mensaje que aparece en la terminal. Ese mensaje te dice qué comportamiento no se está cumpliendo y en qué parte debes corregirlo.

## Qué debe pasar al final

Al terminar, deberías poder ver que:

- los suscriptores guardan los mensajes que reciben,
- el canal avisa a todos los suscriptores activos,
- si alguien se desuscribe, deja de recibir mensajes nuevos,
- no se repiten suscriptores iguales,
- las pruebas automáticas pasan sin errores.

## Ver la calificación

Cuando completes las misiones, se creará un issue final de calificación. Si quieres actualizar la revisión, puedes ejecutar manualmente el workflow **Validar progreso de misiones**.

## Autores

Matthew Habib Corzo Torres.
