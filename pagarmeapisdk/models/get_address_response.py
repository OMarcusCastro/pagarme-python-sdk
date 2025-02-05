# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_customer_response import *


class GetAddressResponse(object):

    """Implementation of the 'GetAddressResponse' model.

    Response object for getting an Address

    Attributes:
        id (str): TODO: type description here.
        street (str): TODO: type description here.
        number (str): TODO: type description here.
        complement (str): TODO: type description here.
        zip_code (str): TODO: type description here.
        neighborhood (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        country (str): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        line_1 (str): Line 1 for address
        line_2 (str): Line 2 for address
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "street": 'street',
        "number": 'number',
        "complement": 'complement',
        "zip_code": 'zip_code',
        "neighborhood": 'neighborhood',
        "city": 'city',
        "state": 'state',
        "country": 'country',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "customer": 'customer',
        "metadata": 'metadata',
        "line_1": 'line_1',
        "line_2": 'line_2',
        "deleted_at": 'deleted_at'
    }

    _optionals = [
        'id',
        'street',
        'number',
        'complement',
        'zip_code',
        'neighborhood',
        'city',
        'state',
        'country',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'metadata',
        'line_1',
        'line_2',
        'deleted_at',
    ]

    _nullables = [
        'id',
        'street',
        'number',
        'complement',
        'zip_code',
        'neighborhood',
        'city',
        'state',
        'country',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'metadata',
        'line_1',
        'line_2',
        'deleted_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 street=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 complement=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 neighborhood=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 line_1=APIHelper.SKIP,
                 line_2=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP):
        """Constructor for the GetAddressResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if street is not APIHelper.SKIP:
            self.street = street
        if number is not APIHelper.SKIP:
            self.number = number
        if complement is not APIHelper.SKIP:
            self.complement = complement
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code
        if neighborhood is not APIHelper.SKIP:
            self.neighborhood = neighborhood
        if city is not APIHelper.SKIP:
            self.city = city
        if state is not APIHelper.SKIP:
            self.state = state
        if country is not APIHelper.SKIP:
            self.country = country
        if status is not APIHelper.SKIP:
            self.status = status
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime) if created_at else None
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(
                updated_at, APIHelper.RFC3339DateTime) if updated_at else None
        if customer is not APIHelper.SKIP:
            self.customer = customer
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata
        if line_1 is not APIHelper.SKIP:
            self.line_1 = line_1
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(
                deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None

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
        from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
        # Extract variables from the dictionary
        id = dictionary.get(
            "id") if "id" in dictionary.keys() else APIHelper.SKIP
        street = dictionary.get(
            "street") if "street" in dictionary.keys() else APIHelper.SKIP
        number = dictionary.get(
            "number") if "number" in dictionary.keys() else APIHelper.SKIP
        complement = dictionary.get(
            "complement") if "complement" in dictionary.keys() else APIHelper.SKIP
        zip_code = dictionary.get(
            "zip_code") if "zip_code" in dictionary.keys() else APIHelper.SKIP
        neighborhood = dictionary.get(
            "neighborhood") if "neighborhood" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get(
            "city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get(
            "state") if "state" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get(
            "country") if "country" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get(
            "status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get(
                "created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get(
                "updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(
                dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        metadata = dictionary.get(
            "metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        line_1 = dictionary.get(
            "line_1") if "line_1" in dictionary.keys() else APIHelper.SKIP
        line_2 = dictionary.get(
            "line_2") if "line_2" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get(
                "deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   street,
                   number,
                   complement,
                   zip_code,
                   neighborhood,
                   city,
                   state,
                   country,
                   status,
                   created_at,
                   updated_at,
                   customer,
                   metadata,
                   line_1,
                   line_2,
                   deleted_at)
