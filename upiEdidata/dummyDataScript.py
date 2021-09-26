import random
import csv
import datetime
from _datetime import timedelta

file_name = f'upiEdidata\\upi_data.csv'
with open(file_name, 'a+') as csvfile:
    fieldnames = ['purpose', 'product', 'service', 'detail', 'date','price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer1 = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    writer.writeheader()

    purposeList = [{'Food': 0, 'price-range': [10, 300]}, {'Entertainment': 1, 'price-range': [500, 3000]}, {'Grocery': 0, 'price-range': [10, 400]
                                                                                                           },
                   {'Apparel': 0, 'price-range': [500, 3000]}, {'Bill Payments': 1, 'price-range': [100, 2000]}, {'Fitness': 1, 'price-range': [1500, 2000]}, {'Makeover': 1, 'price-range': [50, 1000]}]
    # print(random.choices(purposeList, k=1))

    itemDict = {
        'Food':
        # list of food item
        ['Chicken', 'Beef', 'Momos', 'dosa', 'Eggs', 'Pao Bhaji',
            'Samosa', 'Masala Paneer', 'Tandoori Chicken'],

        'Grocery':
            ['Bread', 'Milk', 'Eggs', 'Cheese', 'Butter', 'Yogurt', 'Cereal', 'Pasta',
                'Noodles', 'Rice', 'Flour', 'Sugar', 'Salt', 'Pepper', 'Other'],

        'Apparel':
            ['Shirts', 'Pants', 'Shoes', 'Bags',
                'Jewelry', 'Hats', 'Socks', 'Other'],



    }

    serviceDict = {
        'Entertainment':
            ['Movies', 'Music', 'Books', 'Video Games', 'TV', 'Online',
                'Sports', 'Outdoor', 'Travel', 'Events', 'Art', 'Crafts', 'Other'],



        'Bill Payments':
            ['Utilities', 'Rent', 'Mortgage', 'Credit Card', 'Other'],


        'Fitness':
            ['Exercise', 'Diet', 'Stress', 'Other'],


        'Makeover':
            ['Hair', 'Makeup', 'Nail', 'Skin', 'Other'],

    }
    noOfTransactions = 1500
    for i in range(noOfTransactions):
        print(random.choices(purposeList, k=1)[0])
        purposeName = " "
        prodDetail = " "
        price=0
        date = datetime.date.today()
        i = 0
        purposeDict = random.choices(purposeList, k=1)[0]
        for key, value in purposeDict.items():
            
            if i == 0:
                purposeName = key
                
                print(key, value)
                if value == 0:
                    print(random.choice(itemDict[key]))
                    prodDetail = random.choice(itemDict[key])
                else:
                    print(random.choice(serviceDict[key]))
                    prodDetail = random.choice(serviceDict[key])
            else:
                priceRangeList = purposeDict[key]
                price=random.randint(priceRangeList[0], priceRangeList[1])

            i=i+1
        itemStatus = 1 if key == 0 else 1
        serviceStatus = 1 if key == 1 else 0
        # date += timedelta(days=i)

        start_date = date
        end_date = datetime.date(2020, 12, 25)
        
        time_between_dates = end_date - start_date
        days_between_dates = abs(time_between_dates.days)
        # print(days_between_dates)
        random_number_of_days = random.randrange(0, days_between_dates, 1)
        # print(random_number_of_days)

        random_date =start_date + datetime.timedelta(days=random_number_of_days)

        writer1.writerow(
            [purposeName, itemStatus, serviceStatus, prodDetail, random_date,price])

    # dataDict = [{'Merchant Name': 'City Pride', 'Transaction Category': 'Entertainment', 'Item/Service Name': 'Shershah movie'},
    #             {'Merchant Name': 'Yevle Chai',
    #                 'Transaction Category': 'Food', 'Item/Service Name': 'Chai'},
    #             {'Merchant Name': 'DMart', 'Transaction Category': 'Shopping',
    #                 'Item/Service Name': 'Protein powder'},
    #             {'Merchant Name': 'Club Factory', 'Transaction Category': 'Shopping', 'Item/Service Name': 'Formal Shoes red chief'}]

    # csv_writer.writeheader()
    # csv_writer.writerows(dataDict)
