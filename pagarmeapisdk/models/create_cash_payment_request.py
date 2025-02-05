# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateCashPaymentRequest(object):

    """Implementation of the 'CreateCashPaymentRequest' model.

    TODO: type model description here.

    Attributes:
        description (str): Description
        confirm (bool): Indicates whether cash collection will be confirmed in
            the act of creation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "confirm": 'confirm'
    }

    def __init__(self,
                 description=None,
                 confirm=None):
        """Constructor for the CreateCashPaymentRequest class"""

        # Initialize members of the class
        self.description = description 
        self.confirm = confirm 

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
        description = dictionary.get("description") if dictionary.get("description") else None
        confirm = dictionary.get("confirm") if "confirm" in dictionary.keys() else None
        # Return an object of this model
        return cls(description,
                   confirm)
