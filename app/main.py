from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_list = []

    for customer in customers:
        CinemaBar.sell_product(customer["name"], customer["food"])
        customers_list.append(Customer(customer["name"], customer["food"]))

    init_hall = CinemaHall(hall_number)
    init_hall.movie_session(movie, customers_list, Cleaner(cleaner))
