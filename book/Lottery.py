from random import sample


class Lottery:
    """Лотерея"""

    def __init__(self):
        """Инициализация атрибутов лотерейного билета"""
        self.lottery_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
        self.my_ticket = [sample(self.lottery_ticket, 4)]
        self.win_ticket = []
        self.num_iterations = 0

    def iterations_for_win(self):
        """Выводит информацию о кол-ве попыток генерации выигрышного билета"""
        while self.my_ticket != self.win_ticket:
            self.win_ticket = [sample(self.lottery_ticket, 4)]
            self.num_iterations += 1
        print(f"Yeah, your # {''.join(map(str, self.win_ticket))} wins.", f"\nIt took {self.num_iterations} iterations.")


ticket = Lottery()
ticket.iterations_for_win()
