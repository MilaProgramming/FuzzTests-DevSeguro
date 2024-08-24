# Proyecto de Microservicios con Pruebas de Fuzz

## Descripción del Proyecto

Este repositorio contiene una arquitectura de microservicios utilizando Docker, que incluye varios servicios que interactúan a través de una red. El proyecto incluye:

- Base de Datos PostgreSQL: Utilizada por el microservicio msvc-cursos.
- Base de Datos MySQL: Utilizada por el microservicio msvc-usuarios.
- Microservicios:
- - msvc-usuarios: Un microservicio para gestionar los datos de los usuarios.
- - msvc-cursos: Un microservicio para gestionar los datos de los cursos.
- Pruebas de Fuzz: Un servicio dedicado a realizar pruebas de fuzz en los microservicios.
- Front-end Angular: Una aplicación frontend para interactuar con los microservicios.

## Instalación y Configuración

1. Clonar el Repositorio

- Copiar código

```sh
git clone https://github.com/MilaProgramming/FuzzTests-DevSeguro.git
cd FuzzTests-DevSeguro
```

- Construir e Iniciar los Contenedores Docker

- Copiar código

```sh
docker-compose up --build
```

## Pruebas de Fuzz

El servicio fuzz está diseñado para realizar pruebas de fuzz en los microservicios msvc-cursos y msvc-usuarios. Utiliza un script en Python para enviar datos aleatorios y malformados a los endpoints de los microservicios para identificar posibles vulnerabilidades.

### Flujo de Trabajo de las Pruebas de Fuzz

El servicio de pruebas de fuzz ejecuta el script fuzz_test.py, que realiza las siguientes acciones:

- Envía solicitudes POST con cargas útiles aleatorias al microservicio msvc-usuarios en `http://localhost:8001/api/usuarios/crear`.
- Envía solicitudes POST con cargas útiles aleatorias al microservicio msvc-cursos en `http://localhost:8002/cursos`.
- Elimina los datos después de la prueba utilizando los endpoints DELETE proporcionados.
- Los resultados de las pruebas de fuzz, incluidos el número de actualizaciones, las acciones realizadas y los registros, se guardan en un archivo llamado `fuzz_test_logs.txt` ubicado en el directorio FuzzTest.

**Para ver los registros, puedes consultar el archivo fuzz_test_logs.txt que está montado como un volumen.**

### Ejecución de Pruebas de Fuzz

Inicia los contenedores Docker utilizando docker-compose up --build.

El servicio de pruebas de fuzz ejecutará automáticamente las pruebas de fuzz contra los microservicios.

Una vez completadas las pruebas, puedes revisar el archivo `fuzz_test_logs.txt` para obtener los resultados detallados.
