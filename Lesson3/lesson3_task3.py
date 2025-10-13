from mailing import Mailing
from addresses import Address

to_address = Address("630005", "Новосибирск", "Красный проспект", "12", "1")

from_address = Address("300007", "Тула", "Ленина", "33", "11")

my_track = Mailing("Новосибирск-1234", from_address, to_address, 1050.30)


print(f"Отправление: {my_track}")
