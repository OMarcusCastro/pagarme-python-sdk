# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_bank_account_response import GetBankAccountResponse


class GetTransferResponse(object):

    """Implementation of the 'GetTransferResponse' model.

    Transfer response

    Attributes:
        id (string): Id
        amount (int): Transfer amount
        status (string): Transfer status
        created_at (datetime): Transfer creation date
        updated_at (datetime): Transfer last update date
        bank_account (GetBankAccountResponse): Bank account
        metadata (dict): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount": 'amount',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "bank_account": 'bank_account',
        "metadata": 'metadata'
    }

    _nullables = [
        'id',
        'amount',
        'status',
        'created_at',
        'updated_at',
        'bank_account',
        'metadata',
    ]

    def __init__(self,
                 id=None,
                 amount=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 bank_account=None,
                 metadata=None):
        """Constructor for the GetTransferResponse class"""

        # Initialize members of the class
        self.id = id 
        self.amount = amount 
        self.status = status 
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None 
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None 
        self.bank_account = bank_account 
        self.metadata = metadata 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        bank_account = GetBankAccountResponse.from_dictionary(dictionary.get('bank_account')) if dictionary.get('bank_account') else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        # Return an object of this model
        return cls(id,
                   amount,
                   status,
                   created_at,
                   updated_at,
                   bank_account,
                   metadata)
