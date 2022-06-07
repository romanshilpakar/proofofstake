from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint

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

    block = wallet.createBlock(pool.transactions, 'lasthash', 1)
    signatureValid = Wallet.signatureValid(block.payload(), block.signature, fradulantWallet.publicKeyString())
    print(signatureValid)
    # pprint.pprint(block.toJson())

    



