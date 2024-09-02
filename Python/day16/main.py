from menu import Menu, MenuItem
from lam_ca_phe import CoffeeMaker
from money_machine import MoneyMachine

menuJun = Menu()
cacmon = menuJun.get_items()

maytien = MoneyMachine()
thanhtoanThanhCong = maytien.make_payment(menuJun.menu.cost)
print()