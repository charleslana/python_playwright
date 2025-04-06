from faker import Faker

faker = Faker()

def get_fake_user():
    return {
        "username": faker.user_name(),
        "password": faker.password(),
        "email": faker.email()
    }
