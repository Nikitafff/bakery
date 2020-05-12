import click


class Pizza:
    sauce: str = 'tomato sauce'
    cheese: str = 'mozzarella'
    size: str = 'L'

    def __init__(self, size: str = None):
        if size:
            self.size = size.upper()

    def __eq__(self, other):
        print(f'{self.__class__.__name__} = {self.size} size and '
              f'{other.__class__.__name__} = {other.size} size')
        return self.size == other.size


class Margarita(Pizza):
    topping: list = ['tomatoes']


class Pepperoni(Pizza):
    topping: list = ['pepperoni']


class Hawaiian(Pizza):
    topping: list = ['chicken', 'pineapples']


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def bake(pizza: str, delivery: bool, size: str):
    print(pizza, delivery)


@cli.command()
def menu():
    print('Наши пиццы:\n')
    for _class in Pizza.__subclasses__():
        x = _class
        attributes = [attr for attr in dir(x)
                      if not attr.startswith('__')]
        print(f'\n{x.__name__}')
        for a in attributes:
            if isinstance(getattr(x, a), list):
                print(f'{a} : {", ".join(getattr(x, a))}')
            else:
                print(f'{a} : {getattr(x, a)}')


if __name__ == '__main__':
    cli()



