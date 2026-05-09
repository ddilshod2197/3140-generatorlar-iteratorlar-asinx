import asyncio
import concurrent.futures

# Generatorlar
def generator_sonlar(n):
    for i in range(n):
        yield i

# Iteratorlar
class IteratorSoni:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            son = self.i
            self.i += 1
            return son
        else:
            raise StopIteration

# Asinxron ishlaydigan funksiya
async def asinxron_funksiya(n):
    await asyncio.sleep(1)
    return n * n

# Generatorlar va Iteratorlar orasidagi farqni ko'rsatish
def generator_iterator_fark():
    generator = generator_sonlar(5)
    iterator = IteratorSoni(5)

    print("Generator:")
    for son in generator:
        print(son)

    print("\nIterator:")
    for son in iterator:
        print(son)

# Asinxron ishlaydigan funksiya ni chaqirish
async def main():
    n = 5
    task = asyncio.create_task(asinxron_funksiya(n))
    result = await task
    print(f"Asinxron funksiya natijasi: {result}")

# Generatorlar, Iteratorlar va Asinxron ishlaydigan funksiya ni chaqirish
if __name__ == "__main__":
    generator_iterator_fark()
    asyncio.run(main())
```

Kodda quyidagi funksiyalar mavjud:

- `generator_sonlar(n)`: Generator funksiyasi, n sonni keltirib chiqaradi.
- `IteratorSoni(n)`: Iterator klassi, n sonni keltirib chiqaradi.
- `asinxron_funksiya(n)`: Asinxron ishlaydigan funksiya, n sonini keltirib chiqaradi.
- `generator_iterator_fark()`: Generatorlar va Iteratorlar orasidagi farqni ko'rsatish uchun funksiya.
- `main()`: Asinxron ishlaydigan funksiya ni chaqirish uchun funksiya.
