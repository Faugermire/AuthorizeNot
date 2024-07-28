
class deleteCustomerPaymentProfileController(apicontrollersbase.APIOperationBase):
    
    def __init__(self, apirequest):
        super(deleteCustomerPaymentProfileController, self).__init__(apirequest)
        return 
    
    def validaterequest(self):
        anetLogger.debug('performing custom validation..') 
        #validate required fields
        #if (self._request.xyz == "null"):
        #    raise ValueError('xyz is required')         
        return
    
    def getrequesttype(self):
        '''Returns request type''' 
        return 'deleteCustomerPaymentProfileRequest'

    def getresponseclass(self):
        ''' Returns the response class '''
        return apicontractsv1.deleteCustomerPaymentProfileResponse() 