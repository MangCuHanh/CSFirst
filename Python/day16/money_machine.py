class MoneyMachine:

    CURRENCY = "vnđ"

    COIN_VALUES = {
        "năm trăm": 500.000,
        "hai trăm": 200.000,
        "một trăm": 100.000,
        "năm muơi": 50.000,
        "hai muơi": 20.000,
        "muời": 10.000,
        "năm": 5.000,
        "hai": 2.000,
        "một": 1.000,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.profit}{self.CURRENCY}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Vui lòng nhập tiền vào.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"bao nhiêu tờ {coin} vnđ?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, giá_tiền):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= giá_tiền:
            change = round(self.money_received - giá_tiền, 2)
            print(f"thối lại: {change}{self.CURRENCY}")
            self.profit += giá_tiền
            self.money_received = 0
            return True
        else:
            print("xin lỗi bạn không đủ tiền, số tiền sẽ được trả lại.")
            self.money_received = 0
            return False
        