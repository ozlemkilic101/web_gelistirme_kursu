# senkron : işlerin sıra sıra halledilmesidir. Bir iş bitmeden diğerine geçilmez.

import time 

def my_func():
    print("1. fonksiyon başladı")
    time.sleep(5)
    print("1. fonksiyon bitti")
    return

def my_func2():
    print("2. fonksiyon başladı")
    time.sleep(5)
    print("2. fonksiyon bitti")
    return

if __name__ == '__main__':
    x=my_func1()
    y=my_func2()

"""
bu noktaya kadar senkron bir işlem yaptık . ilk fonksiyon çağırıldı ve bitmeden 
ikinci fonksiyon çağrılmadı. Bu yüzden toplamda 10 saniye sürdü.Bu web programlama tarafında çok 
istediğimiz bir durum değildir. Çünkü kullanıcıya hızlı bir şekilde geri dönüş yapmamız gerekir.

"""
