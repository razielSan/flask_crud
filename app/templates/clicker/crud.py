from dataclasses import dataclass


@dataclass
class Clicker:
    count_form: int = 0
    count: int = 0

    def inc_count(self):
        self.count += 1
        return  self.count

    def inc_count_form(self):
        self.count_form += 1
        return  self.count
            