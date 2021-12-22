import click
import random


@click.group()
def cli():
    pass


@cli.command()
@click.option('--size', default='L', type=str)
@click.option('--pickup', default=False, is_flag=True)
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, pickup: bool, size: str):
    """готовит пиццу, отправляет курьера"""
    if delivery and pickup:
        click.echo('Самовывоз и доставка одновременно невозможны')
        return

    if pizza.lower() == 'margherita':
        ordered_pizza = Margherita(size)
    elif pizza.lower() == 'pepperoni':
        ordered_pizza = Pepperoni(size)
    elif pizza.lower() == 'hawaiian':
        ordered_pizza = Hawaiian(size)
    else:
        click.echo('Такой пиццы нет в меню')
        return

    click.echo(bake(ordered_pizza))
    if delivery:
        click.echo(deliver(ordered_pizza))
    if pickup:
        click.echo(pick_up(ordered_pizza))


@cli.command()
def menu():
    """выводит меню"""
    list_pizza = [Margherita, Pepperoni, Hawaiian]

    for pizza in list_pizza:
        click.echo(f"- {pizza.name} {pizza.symbol} : {', '.join(pizza.ingredients)}")


def log(message: str = None):
    """
    Декоратор, который выводит имя функции и время выполнения, если не заданн параметр massage. Если указать параметр
    massage в формате '...{}...', то выведет время выполнения на месте {} выполнения и текст вокруг.
    """
    def decorator(func):
        def inner_wrapper(*args, **kwargs):
            timer = random.randint(10, 20)
            if message is None:
                return f"{func(*args, **kwargs).__name__} — {timer} мин"
            else:
                return message.format(timer)

        return inner_wrapper

    return decorator


@log('✔ Приготовили за {} мин!')
def bake(pizza):
    """Готовит пиццу"""
    return


@log('🛵 Доставили за {} мин!')
def deliver(pizza):
    """Доставляет пиццу"""
    return


@log('🏠 Забрали за {} мин!')
def pick_up(pizza):
    """Забирает пиццу"""
    return


class BasePizza:
    """Базовый класс, от которого будут наследоваться все пиццы"""
    base_size = ['L', 'XL']
    ingredients = []
    name = ''

    def __init__(self, size: str):
        if size.upper() in self.base_size:
            self.size = size.upper()
        else:
            raise ValueError('Invalid size')

    def dict(self):
        return self.ingredients

    def __eq__(self, other):
        return isinstance(other, BasePizza) and self.size == other.size and self.name == other.name


class Margherita(BasePizza):
    """Пицца Маргарита"""
    name = 'Margherita'
    symbol = '🧀'
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str = 'L'):
        super().__init__(size)


class Pepperoni(BasePizza):
    """Пицца пепперони"""
    name = 'Pepperoni'
    symbol = '🍕'
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str = 'L'):
        super().__init__(size)


class Hawaiian(BasePizza):
    """Пицца гавайская"""
    name = 'Hawaiian'
    symbol = '🍍'
    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str = 'L'):
        super().__init__(size)


if __name__ == '__main__':
    cli()
