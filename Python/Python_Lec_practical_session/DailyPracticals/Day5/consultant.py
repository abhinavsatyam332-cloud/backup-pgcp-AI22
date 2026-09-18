from typing import override

from TaxPayer import TaxPayer

class consultant(TaxPayer):
    def __init__(self,pan):
        super().__init__(pan)

    @override
    def calculate_tax(self):
        print("In consultant")
