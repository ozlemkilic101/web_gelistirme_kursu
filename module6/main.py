from fastapi import FastAPI, Depends
from typing import Annotated


app=FastAPI()

def hello_world():
    return "Hello , welcome to FastAPI!"


def get_hello_world(hello:str= Depends(hello_world)):
    return f"Hello world service : {hello_world()}"


@app.get("/hello")
def hello(message:str=Depends(get_hello_world)):
    return {"message":message}



#Bu işlem ileride daha karmaşık ve okunamaz olacağı için şöyle bir kısayolu var diyebiliriz.

HelloDependency=Annotated[str, Depends(hello_world)] # ilk fonksiyondan bu şekilde bir tanımlama yaptık 

# ardından get_hello_world () fonksiyonu şu hale büründü.

'''
def get_hello_world(hello:HelloDependency):
    return f"Hello world service : {hello}"
'''

