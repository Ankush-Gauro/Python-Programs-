blockchain = []

#get last blockchain value
def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('your transaction amount please: '))

name = 'chica'
def x():
    global name 
    name = 'joao'

print(name)
x()
print(name)

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(transaction_amount=tx_amount,
          last_transaction=get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)