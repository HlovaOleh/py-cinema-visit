from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: dict,
        hall_number: int,
        cleaning_staff: str,
        movie: str
) -> None:
    customer_instances = []
    for customer_value in customers:
        name = customer_value.get("name")
        food = customer_value.get("food")
        customer = Customer(name, food)
        customer_instances.append(customer)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    for value in customer_instances:
        CinemaBar.sell_product(product=value.food, customer=value)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
