from fastapi import FastAPI

app = FastAPI()

courses_db =[
    {'id':1,'instructor':'Ozlem','course':'Python','category':'Programming'},
    {'id':2,'instructor':'Ahmet','course':'JavaScript','category':'Programming'},
    {'id':3,'instructor':'Ozlem','course':'Data Science','category':'Data'},
    {'id':4,'instructor':'Ayse','course':'Machine Learning','category':'Data'},
    {'id':5,'instructor':'Ozlem','course':'Docker','category':'Devops'},
]

@app.get("/courses")
async def get_all_courses():
    return courses_db
