# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_price_bracket_request import CreatePriceBracketRequest


class CreatePricingSchemeRequest(object):

    """Implementation of the 'CreatePricingSchemeRequest' model.

    Request for creating a pricing scheme

    Attributes:
        scheme_type (str): Scheme type
        price_brackets (List[CreatePriceBracketRequest]): Price brackets
        price (int): Price
        minimum_price (int): Minimum price
        percentage (float): percentual value used in pricing_scheme Percent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_type": 'scheme_type',
        "price_brackets": 'price_brackets',
        "price": 'price',
        "minimum_price": 'minimum_price',
        "percentage": 'percentage'
    }

    _optionals = [
        'price_brackets',
        'price',
        'minimum_price',
        'percentage',
    ]

    def __init__(self,
                 scheme_type=None,
                 price_brackets=APIHelper.SKIP,
                 price=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 percentage=APIHelper.SKIP):
        """Constructor for the CreatePricingSchemeRequest class"""

        # Initialize members of the class
        self.scheme_type = scheme_type 
        if price_brackets is not APIHelper.SKIP:
            self.price_brackets = price_brackets 
        if price is not APIHelper.SKIP:
            self.price = price 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 

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
        scheme_type = dictionary.get("scheme_type") if dictionary.get("scheme_type") else None
        price_brackets = None
        if dictionary.get('price_brackets') is not None:
            price_brackets = [CreatePriceBracketRequest.from_dictionary(x) for x in dictionary.get('price_brackets')]
        else:
            price_brackets = APIHelper.SKIP
        price = dictionary.get("price") if dictionary.get("price") else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if dictionary.get("minimum_price") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_type,
                   price_brackets,
                   price,
                   minimum_price,
                   percentage)
