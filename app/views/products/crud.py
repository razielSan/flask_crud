from dataclasses import dataclass, field
from typing import Dict
import random
from string import ascii_letters


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductStorage:
    products: Dict[int, Product] = field(default_factory=dict)
    id: int = 0

    @property
    def get_next_id(self):
        self.id += 1
        return self.id

    def add(self, name: str, price: int):
        product = Product(
            name=name,
            price=price,
            id=self.get_next_id,
        )
        self.products[product.id] = product
        return product

    @property
    def get_set_names(self):
        return {product.name for product in self.products.values()}

    @property
    def get_list(self):
        return [product for product in self.products.values()]

    def get_check_name_is_exists(self, name: str):
        return name in self.get_set_names

    def delete_product_by_id(self, id: int):
        self.products.pop(id)

    def update_product_by_id(self, id: int, name: str, price: int):
        product = Product(
            id=id,
            name=name,
            price=price,
        )
        self.products[id] = product
        return product

    def get_product_by_id(self, id: int):
        product = self.products.get(id)
        return product


product_storage = ProductStorage()

name = "Laptop"
for i in range(1, 100):
    random_suffix = "".join(random.choices(ascii_letters, k=4))
    product_storage.add(
        name=f"product_{i:03d} {random_suffix}",
        price=random.randint(1, 9) * random.choice([10, 50 , 100, 200, 400, 600])
    )
