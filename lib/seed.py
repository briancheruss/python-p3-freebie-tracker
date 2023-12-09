#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

def seed_data(session):
    print("Adding seed data...")


    dev_instance = Dev(name='John Doe')
    session.add(dev_instance)


    company_instance = Company(name='Example Corp', founding_year=2000)
    session.add(company_instance)


    freebie1 = Freebie(item_name='Laptop', value=100, dev=dev_instance, company=company_instance)
    freebie2 = Freebie(item_name='T-shirt', value=20, dev=dev_instance, company=company_instance)
    session.add_all([freebie1, freebie2])

    session.commit()

    print("Seed data added successfully.")

if __name__ == '__main__':

    engine = create_engine('sqlite:///freebies.db')

   
    Session = sessionmaker(bind=engine)
    session = Session()

    
    seed_data(session)
