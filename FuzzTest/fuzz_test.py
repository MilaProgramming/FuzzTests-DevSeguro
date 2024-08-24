import requests
import random
import string
import logging

# Base URLs of your APIs
COURSES_URL = 'http://msvc-cursos:8002/cursos'
USERS_URL = 'http://msvc-usuarios:8001/api/usuarios'

# Setup logging
logging.basicConfig(filename='/logs/fuzz_test_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fuzz_post_courses():
    for _ in range(10):  # Number of iterations
        payload = {
            'nombre': generate_random_string(15)
        }
        response = requests.post(COURSES_URL, json=payload)
        logging.info(f'POST {COURSES_URL} with {payload} -> Status Code: {response.status_code}, Response: {response.text}')

def fuzz_delete_courses():
    for course_id in range(1, 6):  # Example course IDs to delete
        url = f'{COURSES_URL}/{course_id}'
        response = requests.delete(url)
        logging.info(f'DELETE {url} -> Status Code: {response.status_code}, Response: {response.text}')

def fuzz_post_users():
    for _ in range(10):  # Number of iterations
        payload = {
            'nombre': generate_random_string(15)
        }
        response = requests.post(f'{USERS_URL}/crear', json=payload)
        logging.info(f'POST {USERS_URL}/crear with {payload} -> Status Code: {response.status_code}, Response: {response.text}')

def fuzz_delete_users():
    for user_id in range(1, 6):  # Example user IDs to delete
        url = f'{USERS_URL}/eliminar/{user_id}'
        response = requests.delete(url)
        logging.info(f'DELETE {url} -> Status Code: {response.status_code}, Response: {response.text}')

def fuzz_get_courses():
    response = requests.get(COURSES_URL)
    logging.info(f'GET {COURSES_URL} -> Status Code: {response.status_code}, Response: {response.text}')

def fuzz_get_users():
    response = requests.get(f'{USERS_URL}/listar')
    logging.info(f'GET {USERS_URL}/listar -> Status Code: {response.status_code}, Response: {response.text}')

if __name__ == "__main__":
    logging.info("Starting fuzz tests...")
    fuzz_post_courses()
    fuzz_delete_courses()
    fuzz_post_users()
    fuzz_delete_users()
    fuzz_get_courses()
    fuzz_get_users()
    logging.info("Fuzz tests completed.")
