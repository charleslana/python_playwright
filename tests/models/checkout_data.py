from dataclasses import dataclass
from faker import Faker

fake = Faker()


@dataclass
class CheckoutData:
    first_name: str
    last_name: str
    zip_code: str

    @classmethod
    def random(cls):
        return cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            zip_code=fake.postcode(),
        )
