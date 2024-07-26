def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello!, {username.title()}")


greet_user('Rahidul')


def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
