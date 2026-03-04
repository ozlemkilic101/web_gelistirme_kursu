from fastapi import FastAPI

#bir uygulama oluşturuyoruz ve işte bu bizim sitemiz oluyor.
app = FastAPI()

#çalışıyor mu denemesi
@app.get("/")
async def hello_world():
    return {"message":"Hello World"}

#CRUD İşlemleri : Create, Read, Update, Delete adımlarını kapsar.

# get ve post nedir? 
# get: verileri okumak için kullanılır. örneğin bir ürünün bilgilerini almak istediğimizde get isteği yaparız.
# post: verileri oluşturmak için kullanılır. örneğin yeni bir ürün eklemek istediğimizde post isteği yaparız.
#get ile sadece veri alırız postla veri oluşştururuz kesin gibi kalmasın ama bu şekilde özelleştirilmiştir.

#get ile yolladığımız veriler url üzerinden gönderilir. Dolayısıyla url'de görünürler. Bu nedenle hassas veriler get ile gönderilmemelidir.
#post ile yolladığımız veriler ise body üzerinden gönderilir. Bu nedenle url'de görünmezler. Bu nedenle hassas veriler post ile gönderilmelidir.

#put ile yapılan işlem get ve post ile de yapılabilir. güncelleme yapmayı sağlar. kod bize bağlı istesek put kullanmayız ama araçları yerinde uygun kullanmak gereklidir.
