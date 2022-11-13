import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
from customer_table import Customer
from config import USER, PASSWORD, DB_NAME


class Database():
    """this class manage customer table
    """
    # create the connection with the DB connection link
    engine = db.create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}')

    def __init__(self) -> None:
        """
        When instantiated, connect to database.
        """
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query) -> None:
        """a method that receives an argument that will be part of
        query and make a request to the database with the information
        What are we looking for

        :param query: argument that will be part of
        query
        :type query: string
        """
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")        
        for data in fetchQuery.fetchall():
            print(data)

    def fetchUserByName(self) -> None:
        # get all names from customer table
        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchAllUsers(self) -> None:
        # get all customers data from dtabase
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)

    def saveData(self, customer) -> None:
        """save a new customer into the database

        :param customer: customer data you want to add to the database
        :type customer: object
        """
        session = Session(bind=self.connection)
        session.add(customer)
        session.commit()

    def updateCustomer(self, customerName, address) -> None:
        """update customer's addres

        :param customerName: the customer name
        :type customerName: string
        :param address: the new adderss
        :type address: string
        """
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        customerData = session.query(Customer).filter(Customer.name == customerName)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self, customerName) -> None:
        """delete customers by name

        :param customerName: the customer name
        :type customerName: string
        """
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.name == customerName).first()
        session.delete(customerData)
        session.commit()


def main():
    database = Database()
    new_customer = Customer('pepito troquel', 25, 'something@gmail.com', 'something 123', '2450')
    database.saveData(new_customer)
    # database.fetchAllUsers()
    database.updateCustomer('pepito troquel', 'primera junta 123')


main()
