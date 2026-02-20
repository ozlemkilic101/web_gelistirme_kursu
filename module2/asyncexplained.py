import asyncio

async def birinci_fonksiyon():
    print("1. fonksiyon başladı")
    await asyncio.sleep(5)
    print("1. fonksiyon bitti")
    return 5

async def ikinci_fonksiyon():
    print("2. fonksiyon başladı")
    await asyncio.sleep(5)
    print("2. fonksiyon bitti")
    return 10

if __name__ == '__main__':
    x=birinci_fonksiyon()
    y=ikinci_fonksiyon()
    #bu böyle çalışmaz çünkü asenkron fonksiyonlar çalıştırıyoruz.

async def main():
    #aşağıdaki gibi çalıştırmalıyız.
    task1=asyncio.create_task(birinci_fonksiyon())
    task2=asyncio.create_task(ikinci_fonksiyon())

    x= await task1
    y= await task2

    print(x)
    print(y)
    # şimdi gidip main içinde bu maini çalıştırmalıyız.

if __name__ == '__main__':
    asyncio.run(main())
