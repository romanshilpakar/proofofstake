from inspect import signature
from signal import siginterrupt
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'


    wallet = Wallet()
    fradulantWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount ,type)

    # signatureValid = Wallet.signatureValid(
    #     transaction.payload(), transaction.signature, fradulantWallet.publicKeyString())

    

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    print(pool.transactions)



