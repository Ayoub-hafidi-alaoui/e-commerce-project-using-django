import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
import random
from products.models import Product, Brand, Category


def seed_brand(n):
    fake = Faker()
    images = ["1.png", "2.png", "3.jpeg"]
    
    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0, 2)]}"
        Brand.objects.create(
            name = name,
            image = image
        )
    print(f"succefully seeded {n} brand")
        

def seed_category(n):
    fake = Faker()
    images = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg"]
    
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0, 3)]}"
        Category.objects.create(
            name = name,
            image = image
        )
    print(f"succefully seeded {n} category")
    

def seed_products(n):
    fake = Faker()
    images = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg", "6.jpeg" ]
    flag_type = ['New', 'Feature', 'Sale']
    
    for _ in range(n):
        name = fake.name()  
        image = f"products/{images[random.randint(0, 5)]}"
        sku = random.randint(1, 100000)
        subtitle = fake.text(max_nb_chars=250)
        desc = fake.text(max_nb_chars=10000)
        flag = flag_type[random.randint(0, 2)]
        price = round(random.uniform(20.99, 98.99), 2)
        category = Category.objects.get(pk=random.randint(1, 60))
        brand = Brand.objects.get(pk = random.randint(1, 90))
        Product.objects.create(
            name = name,
            sku = sku,
            subtitle = subtitle,
            desc = desc,
            image = image,
            price = price,
            category = category,
            brand = brand,
            flag = flag,
            video_url = "https://www.youtube.com/watch?v=PZIqV7wNyyU"
        )
    print(f"succefully seeded {n} product")
    
    



seed_brand(5)
seed_category(10)
seed_products(100)