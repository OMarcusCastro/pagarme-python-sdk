# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_charge_response import *
from pagarmeapisdk.models.get_checkout_payment_response import GetCheckoutPaymentResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
from pagarmeapisdk.models.get_device_response import GetDeviceResponse
from pagarmeapisdk.models.get_location_response import GetLocationResponse
from pagarmeapisdk.models.get_order_item_response import GetOrderItemResponse
from pagarmeapisdk.models.get_shipping_response import GetShippingResponse


class GetOrderResponse(object):

    """Implementation of the 'GetOrderResponse' model.

    Response object for getting an Order

    Attributes:
        id (str): TODO: type description here.
        code (str): TODO: type description here.
        amount (int): TODO: type description here.
        currency (str): TODO: type description here.
        closed (bool): Indicates whether the order is closed
        items (List[GetOrderItemResponse]): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        closed_at (datetime): TODO: type description here.
        charges (List[GetChargeResponse]): TODO: type description here.
        invoice_url (str): TODO: type description here.
        shipping (GetShippingResponse): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        checkouts (List[GetCheckoutPaymentResponse]): Checkout Payment
            Settings Response
        ip (str): Ip address
        session_id (str): Session id
        location (GetLocationResponse): Location
        device (GetDeviceResponse): Device's informations

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "code": 'code',
        "amount": 'amount',
        "currency": 'currency',
        "closed": 'closed',
        "items": 'items',
        "customer": 'customer',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "closed_at": 'closed_at',
        "charges": 'charges',
        "invoice_url": 'invoice_url',
        "shipping": 'shipping',
        "metadata": 'metadata',
        "checkouts": 'checkouts',
        "ip": 'ip',
        "session_id": 'session_id',
        "location": 'location',
        "device": 'device'
    }

    _optionals = [
        'id',
        'code',
        'amount',
        'currency',
        'closed',
        'items',
        'customer',
        'status',
        'created_at',
        'updated_at',
        'closed_at',
        'charges',
        'invoice_url',
        'shipping',
        'metadata',
        'checkouts',
        'ip',
        'session_id',
        'location',
        'device',
    ]

    _nullables = [
        'id',
        'code',
        'amount',
        'currency',
        'closed',
        'items',
        'customer',
        'status',
        'created_at',
        'updated_at',
        'closed_at',
        'charges',
        'invoice_url',
        'shipping',
        'metadata',
        'checkouts',
        'ip',
        'session_id',
        'location',
        'device',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 closed=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 closed_at=APIHelper.SKIP,
                 charges=APIHelper.SKIP,
                 invoice_url=APIHelper.SKIP,
                 shipping=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 checkouts=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 session_id=APIHelper.SKIP,
                 location=APIHelper.SKIP,
                 device=APIHelper.SKIP):
        """Constructor for the GetOrderResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if closed is not APIHelper.SKIP:
            self.closed = closed 
        if items is not APIHelper.SKIP:
            self.items = items 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if closed_at is not APIHelper.SKIP:
            self.closed_at = APIHelper.apply_datetime_converter(closed_at, APIHelper.RFC3339DateTime) if closed_at else None 
        if charges is not APIHelper.SKIP:
            self.charges = charges 
        if invoice_url is not APIHelper.SKIP:
            self.invoice_url = invoice_url 
        if shipping is not APIHelper.SKIP:
            self.shipping = shipping 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if checkouts is not APIHelper.SKIP:
            self.checkouts = checkouts 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if session_id is not APIHelper.SKIP:
            self.session_id = session_id 
        if location is not APIHelper.SKIP:
            self.location = location 
        if device is not APIHelper.SKIP:
            self.device = device 

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
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if "currency" in dictionary.keys() else APIHelper.SKIP
        closed = dictionary.get("closed") if "closed" in dictionary.keys() else APIHelper.SKIP
        if 'items' in dictionary.keys():
            items = [GetOrderItemResponse.from_dictionary(x) for x in dictionary.get('items')] if dictionary.get('items') else None
        else:
            items = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'closed_at' in dictionary.keys():
            closed_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("closed_at")).datetime if dictionary.get("closed_at") else None
        else:
            closed_at = APIHelper.SKIP
        if 'charges' in dictionary.keys():
            charges = [GetChargeResponse.from_dictionary(x) for x in dictionary.get('charges')] if dictionary.get('charges') else None
        else:
            charges = APIHelper.SKIP
        invoice_url = dictionary.get("invoice_url") if "invoice_url" in dictionary.keys() else APIHelper.SKIP
        if 'shipping' in dictionary.keys():
            shipping = GetShippingResponse.from_dictionary(dictionary.get('shipping')) if dictionary.get('shipping') else None
        else:
            shipping = APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        if 'checkouts' in dictionary.keys():
            checkouts = [GetCheckoutPaymentResponse.from_dictionary(x) for x in dictionary.get('checkouts')] if dictionary.get('checkouts') else None
        else:
            checkouts = APIHelper.SKIP
        ip = dictionary.get("ip") if "ip" in dictionary.keys() else APIHelper.SKIP
        session_id = dictionary.get("session_id") if "session_id" in dictionary.keys() else APIHelper.SKIP
        if 'location' in dictionary.keys():
            location = GetLocationResponse.from_dictionary(dictionary.get('location')) if dictionary.get('location') else None
        else:
            location = APIHelper.SKIP
        if 'device' in dictionary.keys():
            device = GetDeviceResponse.from_dictionary(dictionary.get('device')) if dictionary.get('device') else None
        else:
            device = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   amount,
                   currency,
                   closed,
                   items,
                   customer,
                   status,
                   created_at,
                   updated_at,
                   closed_at,
                   charges,
                   invoice_url,
                   shipping,
                   metadata,
                   checkouts,
                   ip,
                   session_id,
                   location,
                   device)
