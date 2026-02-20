#Ders 2 - Pydantic Ne İçin Kullanılır?
class Product:

    def __init__(self, name : str, price : float , in_stock : bool):
        self.name=name
        self.price=price
        self.in_stock=in_stock

if __name__=='__main__':
    ornek_product=Product("Ornek",100,20)
    print(ornek_product.in_stock)
    print(ornek_product.name)
    print(ornek_product.price)

    print(type(ornek_product.in_stock))
    print(type(ornek_product.name))
    print(type(ornek_product.price))

    #dikkat edersek price için float , in_stock için bool dememize rağmen herhangi bir hata olmaksızın çalıştı.
    #Yalnızca ide bize minik bir uyarı verdi. Bazen kodun devamlılığı için bu konuda daha katı olmamız gerekebilir.
    # typeları kontrol ettiğimizde de farklı typelarda olduğunu gördük. 
    # bir sonraki derste aynı kodu pydantic kullanarak yazacağız
