class Account:

    _quantity = float
    _owner = str
    
    def __init__(self, owner, quantity = 0 ) -> None:
        self._owner = owner
        self._quantity = quantity
    
    def add(self, quantity:float):
        if quantity < 0:
            return
        self._quantity += quantity

    def remove(self, quantity:float):
        if quantity < 0:
            return
        new_qty = self._quantity - quantity
        if new_qty < 0:
            self._quantity = 0
        else:
            self._quantity = new_qty
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
    
    def __str__(self) -> str:
        return f'Owner: {self._owner} - Quantity: {self._quantity}'

    def to_string(self) -> str:
        return f'Owner: {self._owner} - Quantity: {self._quantity}'    
    