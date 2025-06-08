from dataclasses import dataclass, field
from typing import Dict


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
 

product_storage = ProductStorage()
product_storage.add("Laptop", price=123)
product_storage.add("Desctop", price=43)
product_storage.add("Smartphone", price=443)
