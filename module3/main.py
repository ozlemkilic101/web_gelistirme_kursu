from fastapi import FastAPI, Body

app = FastAPI()

courses_db =[
    {'id':1,'instructor':'Ozlem','title':'Python','category':'Programming'},
    {'id':2,'instructor':'Ahmet','title':'JavaScript','category':'Programming'},
    {'id':3,'instructor':'Ozlem','title':'Data Science','category':'Data'},
    {'id':4,'instructor':'Ayse','title':'Machine Learning','category':'Data'},
    {'id':5,'instructor':'Ozlem','title':'Docker','category':'Devops'},
]

@app.get("/courses")
async def get_all_courses():
    return courses_db

#Filtrelenmiş kursları döndürmek için Path , Query gibi parametreler kullanabiliriz.

#Path kullanımı: 
@app.get("/courses/{course_title}") #course_title yerine ne gelirse onu bir değişken olarak kabul eder.
async def get_course(course_title:str):
   for course in courses_db:
    if course.get("title").lower() == course_title.lower():
        return course


#Path 2. örnek (bu örnekte path'in problemini ele alacağız.
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id:str):
    for course in courses_db:
        if course.get("id").casefold() == course_id.casefold(): #casefold ile lower aynı şey sayılır
            return course

'''
bu metodu fast api tarafında deneyince null geldiğini gördük.çünkü biz bi üst metotta fast api'ye 
course'dan sonrabir şey gelirse bu geleni course_title olarak al dedik ,
 bu yüzden de biz 3 ,4 ,5 gibi id'leri gönderdiğimizde fast api onları course_title olarak algılıyor 
 ve o yüzden de null dönüyor.
'''

#Query kullanımı:
@app.get("/courses/")
async def get_category_by_query(category:str):
    courses_to_return = []
    for course in courses_db:
        if course.get("category").lower() == category.lower():
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor:str, category:str):
    courses_to_return = []
    for course in courses_db:
        if course.get("instructor").lower() == course_instructor.lower() and course.get("category").lower() == category.lower():
            courses_to_return.append(course)
    return courses_to_return


#buraya kadar hep get kullandık ama post da kullanabiliriz.
#post ile yeni bir kayıt ekleyelim.

@app.post("/courses/create_course")
async def create_course(new_course=Body()):  #bu satırda en üste gidip body'yi import etmemiz gerekiyor.
    courses_db.append(new_course)


#update ve delete işlemlerine geçiyoruz.

#update işlemi :
@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == updated_course.get("id"):
            courses_db[index] = updated_course
            return {"message":"Course updated successfully"}

#delete işlemi:
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id:int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id")==course_id:
            courses_db.pop(index)
            return {"message":"Course deleted successfully"}