import os
import shutil

def hello_world():
    print('hello world')

def hello_to_you(name_of_person):
    response = 'hello to you, ' + name_of_person
    print(response)

def test():
    hello_world()
    hello_to_you(name_of_person='Test Person 1')

if __name__ == "__main__":
    hello_world()
    hello_to_you(name_of_person='Hassan i Sabbah')
    hello_to_you(name_of_person='Sophie Germain')
    hello_to_you(name_of_person='Ludwig Wittgenstein')

    test()