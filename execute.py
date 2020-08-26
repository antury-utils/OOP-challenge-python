from account import Account

class Execute(Account):

    def __init__(self, owner, quantity = 0) -> None:
        super().__init__(owner, quantity)
    

if __name__ == "__main__":
    execute = Execute('Fernando')
    print(execute.to_string())
    execute.add(34.6)
    execute.add(3.4)
    execute.add(-4003.4)
    print(execute.to_string())
    execute.remove(3.6)
    execute.remove(2.4)
    execute.remove(3.6)
    print(execute.to_string())
    execute.remove(100.4)
    print(execute.to_string())