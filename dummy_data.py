import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from products.models import Product,Brand
from faker import Faker

def seed_brand(n):
    
    for _ in range(n):
        fake=Faker()
        images=['0.jpg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','45.jpg']

        Brand.objects.create(
            name=fake.name(),
            image=f'photo_product/{images[random.randint(0,10)]}'

        )

def seed_product(n):
    fake=Faker()
    flag_type=['New','Sale','Feature']
    images=['0.jpg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','45.jpg']
    brands=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            price=round(random.uniform(5.55,99.99),2),
            sku=random.randint(1000,10000000000),
            flag=flag_type[random.randint(0,2)],
            quantity=random.randint(20,100),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brands[random.randint(0,len(brands)-1)],
            image=f'photo_brand/{images[random.randint(0,10)]}',






        )

#seed_brand(200)
seed_product(1500)