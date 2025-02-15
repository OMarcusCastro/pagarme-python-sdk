# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_fine_response import GetFineResponse
from pagarmeapisdk.models.get_interest_response import GetInterestResponse


class GetSubscriptionBoletoResponse(object):

    """Implementation of the 'GetSubscriptionBoletoResponse' model.

    Response object for getting a boleto

    Attributes:
        interest (GetInterestResponse): Interest
        fine (GetFineResponse): Fine
        max_days_to_pay_past_due (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interest": 'interest',
        "fine": 'fine',
        "max_days_to_pay_past_due": 'max_days_to_pay_past_due'
    }

    _optionals = [
        'interest',
        'fine',
        'max_days_to_pay_past_due',
    ]

    _nullables = [
        'interest',
        'fine',
        'max_days_to_pay_past_due',
    ]

    def __init__(self,
                 interest=APIHelper.SKIP,
                 fine=APIHelper.SKIP,
                 max_days_to_pay_past_due=APIHelper.SKIP):
        """Constructor for the GetSubscriptionBoletoResponse class"""

        # Initialize members of the class
        if interest is not APIHelper.SKIP:
            self.interest = interest 
        if fine is not APIHelper.SKIP:
            self.fine = fine 
        if max_days_to_pay_past_due is not APIHelper.SKIP:
            self.max_days_to_pay_past_due = max_days_to_pay_past_due 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        if 'interest' in dictionary.keys():
            interest = GetInterestResponse.from_dictionary(dictionary.get('interest')) if dictionary.get('interest') else None
        else:
            interest = APIHelper.SKIP
        if 'fine' in dictionary.keys():
            fine = GetFineResponse.from_dictionary(dictionary.get('fine')) if dictionary.get('fine') else None
        else:
            fine = APIHelper.SKIP
        max_days_to_pay_past_due = dictionary.get("max_days_to_pay_past_due") if "max_days_to_pay_past_due" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(interest,
                   fine,
                   max_days_to_pay_past_due)
