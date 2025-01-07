
import requests
def my_function():
       r = requests.get('https://dummyjson.com/users').json()
       return r