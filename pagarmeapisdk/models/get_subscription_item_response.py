# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_discount_response import *
from pagarmeapisdk.models.get_increment_response import *
from pagarmeapisdk.models.get_pricing_scheme_response import GetPricingSchemeResponse
from pagarmeapisdk.models.get_subscription_response import *


class GetSubscriptionItemResponse(object):

    """Implementation of the 'GetSubscriptionItemResponse' model.

    TODO: type model description here.

    Attributes:
        id (str): TODO: type description here.
        description (str): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        pricing_scheme (GetPricingSchemeResponse): TODO: type description
            here.
        discounts (List[GetDiscountResponse]): TODO: type description here.
        increments (List[GetIncrementResponse]): TODO: type description here.
        subscription (GetSubscriptionResponse): TODO: type description here.
        name (str): Item name
        quantity (int): TODO: type description here.
        cycles (int): TODO: type description here.
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "description": 'description',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "pricing_scheme": 'pricing_scheme',
        "discounts": 'discounts',
        "increments": 'increments',
        "subscription": 'subscription',
        "name": 'name',
        "quantity": 'quantity',
        "cycles": 'cycles',
        "deleted_at": 'deleted_at'
    }

    _optionals = [
        'id',
        'description',
        'status',
        'created_at',
        'updated_at',
        'pricing_scheme',
        'discounts',
        'increments',
        'subscription',
        'name',
        'quantity',
        'cycles',
        'deleted_at',
    ]

    _nullables = [
        'id',
        'description',
        'status',
        'created_at',
        'updated_at',
        'pricing_scheme',
        'discounts',
        'increments',
        'subscription',
        'name',
        'quantity',
        'cycles',
        'deleted_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 increments=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 cycles=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP):
        """Constructor for the GetSubscriptionItemResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if description is not APIHelper.SKIP:
            self.description = description 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if increments is not APIHelper.SKIP:
            self.increments = increments 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 
        if name is not APIHelper.SKIP:
            self.name = name 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'pricing_scheme' in dictionary.keys():
            pricing_scheme = GetPricingSchemeResponse.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        else:
            pricing_scheme = APIHelper.SKIP
        if 'discounts' in dictionary.keys():
            discounts = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('discounts')] if dictionary.get('discounts') else None
        else:
            discounts = APIHelper.SKIP
        if 'increments' in dictionary.keys():
            increments = [GetIncrementResponse.from_dictionary(x) for x in dictionary.get('increments')] if dictionary.get('increments') else None
        else:
            increments = APIHelper.SKIP
        if 'subscription' in dictionary.keys():
            subscription = GetSubscriptionResponse.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        else:
            subscription = APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("quantity") if "quantity" in dictionary.keys() else APIHelper.SKIP
        cycles = dictionary.get("cycles") if "cycles" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   description,
                   status,
                   created_at,
                   updated_at,
                   pricing_scheme,
                   discounts,
                   increments,
                   subscription,
                   name,
                   quantity,
                   cycles,
                   deleted_at)
