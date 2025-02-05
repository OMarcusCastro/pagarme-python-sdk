# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_google_pay_request import CreateGooglePayRequest


class CreateCardPayloadRequest(object):

    """Implementation of the 'CreateCardPayloadRequest' model.

    TODO: type model description here.

    Attributes:
        mtype (str): TODO: type description here.
        google_pay (CreateGooglePayRequest): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "google_pay": 'google_pay'
    }

    _optionals = [
        'mtype',
        'google_pay',
    ]

    _nullables = [
        'mtype',
        'google_pay',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 google_pay=APIHelper.SKIP):
        """Constructor for the CreateCardPayloadRequest class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if google_pay is not APIHelper.SKIP:
            self.google_pay = google_pay 

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
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        if 'google_pay' in dictionary.keys():
            google_pay = CreateGooglePayRequest.from_dictionary(dictionary.get('google_pay')) if dictionary.get('google_pay') else None
        else:
            google_pay = APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   google_pay)
