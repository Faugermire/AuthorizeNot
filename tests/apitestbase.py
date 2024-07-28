'''
Created on Jul 15, 2015

@author: egodolja
'''

import unittest
import datetime
from decimal import *
import random

from authorizenet import apicontractsv1
from authorizenet.utility import Helper


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.helper = Helper('anet_python_sdk_properties.ini')
        self.amount = str(round(random.random()*100, 2))
        self.merchantAuthentication = apicontractsv1.merchantAuthenticationType()
        self.merchantAuthentication.name = self.helper.get_property('api.login.id')

        if self.merchantAuthentication.name is None:
            self.merchantAuthentication.name = self.helper.get_property('api_login_id')
        self.merchantAuthentication.transactionKey = self.helper.get_property('transaction.key')
        if self.merchantAuthentication.transactionKey is None:
            self.merchantAuthentication.transactionKey = self.helper.get_property('transaction_key')
        
        self.ref_id = 'Sample'
        self.dateOne = datetime.date(2020, 8, 30)

        self.paymentScheduleOne = apicontractsv1.paymentScheduleType()
        self.paymentScheduleOne.interval = apicontractsv1.paymentScheduleTypeInterval()
        
        self.paymentScheduleOne.interval.length = 1
        self.paymentScheduleOne.interval.unit = 'months'
        
        self.paymentScheduleOne.startDate = self.dateOne
        self.paymentScheduleOne.totalOccurrences = 12
        self.paymentScheduleOne.trialOccurrences = 1
        
        self.creditCardOne = apicontractsv1.creditCardType()
        self.creditCardOne.cardNumber = "4111111111111111"
        self.creditCardOne.expirationDate = "2040-12"
        
        self.payment = apicontractsv1.paymentType()
        self.payment.creditCard = self.creditCardOne
        
        self.customerOne = apicontractsv1.nameAndAddressType()
        self.customerOne.firstName = "John" + str(random.randint(0, 10000))
        self.customerOne.lastName = "Smith"
        
        self.customerData = apicontractsv1.customerDataType()
        self.customerData.id = "99999456654"
        
        self.subscriptionOne = apicontractsv1.ARBSubscriptionType()
        self.subscriptionOne.paymentSchedule = self.paymentScheduleOne
        self.subscriptionOne.amount = Decimal(str(round(random.random()*100, 2)))
        self.subscriptionOne.trialAmount = Decimal(str(round(random.random()*100, 2)))
        self.subscriptionOne.payment = self.payment
        self.subscriptionOne.billTo = self.customerOne

        self.order = apicontractsv1.orderType()
        self.order.invoiceNumber = "INV-21345"
        self.order.description = "Product description"
        
        self.billTo = apicontractsv1.customerAddressType()
        self.billTo.firstName = "Ellen"
        self.billTo.lastName = "Johnson"
        self.billTo.company = "Souveniropolis"
        self.billTo.address = "14 Main St"
        self.billTo.city = "Seattle"
        self.billTo.state = "WA"
        self.billTo.zip = "98122"
        self.billTo.country = "USA"
       
    
        
