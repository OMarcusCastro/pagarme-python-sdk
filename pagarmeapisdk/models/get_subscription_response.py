# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_card_response import GetCardResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
from pagarmeapisdk.models.get_discount_response import *
from pagarmeapisdk.models.get_increment_response import *
from pagarmeapisdk.models.get_period_response import *
from pagarmeapisdk.models.get_setup_response import GetSetupResponse
from pagarmeapisdk.models.get_subscription_boleto_response import GetSubscriptionBoletoResponse
from pagarmeapisdk.models.get_subscription_item_response import *
from pagarmeapisdk.models.get_subscription_split_response import GetSubscriptionSplitResponse


class GetSubscriptionResponse(object):

    """Implementation of the 'GetSubscriptionResponse' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        start_at (datetime): TODO: type description here.
        interval (string): TODO: type description here.
        interval_count (int): TODO: type description here.
        billing_type (string): TODO: type description here.
        current_cycle (GetPeriodResponse): TODO: type description here.
        payment_method (string): TODO: type description here.
        currency (string): TODO: type description here.
        installments (int): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        card (GetCardResponse): TODO: type description here.
        items (list of GetSubscriptionItemResponse): TODO: type description
            here.
        statement_descriptor (string): TODO: type description here.
        metadata (dict): TODO: type description here.
        setup (GetSetupResponse): TODO: type description here.
        gateway_affiliation_id (string): Affiliation Code
        next_billing_at (datetime): TODO: type description here.
        billing_day (int): TODO: type description here.
        minimum_price (int): TODO: type description here.
        canceled_at (datetime): TODO: type description here.
        discounts (list of GetDiscountResponse): Subscription discounts
        increments (list of GetIncrementResponse): Subscription increments
        boleto_due_days (int): Days until boleto expires
        split (GetSubscriptionSplitResponse): Subscription's split response
        boleto (GetSubscriptionBoletoResponse): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "code": 'code',
        "start_at": 'start_at',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_type": 'billing_type',
        "payment_method": 'payment_method',
        "currency": 'currency',
        "installments": 'installments',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "card": 'card',
        "items": 'items',
        "statement_descriptor": 'statement_descriptor',
        "metadata": 'metadata',
        "setup": 'setup',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "increments": 'increments',
        "split": 'split',
        "current_cycle": 'current_cycle',
        "customer": 'customer',
        "next_billing_at": 'next_billing_at',
        "billing_day": 'billing_day',
        "minimum_price": 'minimum_price',
        "canceled_at": 'canceled_at',
        "discounts": 'discounts',
        "boleto_due_days": 'boleto_due_days',
        "boleto": 'boleto'
    }

    _optionals = [
        'current_cycle',
        'customer',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'boleto_due_days',
        'boleto',
    ]

    _nullables = [
        'id',
        'code',
        'start_at',
        'interval',
        'interval_count',
        'billing_type',
        'current_cycle',
        'payment_method',
        'currency',
        'installments',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'card',
        'items',
        'statement_descriptor',
        'metadata',
        'setup',
        'gateway_affiliation_id',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'increments',
        'boleto_due_days',
        'split',
        'boleto',
    ]

    def __init__(self,
                 id=None,
                 code=None,
                 start_at=None,
                 interval=None,
                 interval_count=None,
                 billing_type=None,
                 payment_method=None,
                 currency=None,
                 installments=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 card=None,
                 items=None,
                 statement_descriptor=None,
                 metadata=None,
                 setup=None,
                 gateway_affiliation_id=None,
                 increments=None,
                 split=None,
                 current_cycle=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 billing_day=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 boleto_due_days=APIHelper.SKIP,
                 boleto=APIHelper.SKIP):
        """Constructor for the GetSubscriptionResponse class"""

        # Initialize members of the class
        self.id = id 
        self.code = code 
        self.start_at = APIHelper.RFC3339DateTime(start_at) if start_at else None 
        self.interval = interval 
        self.interval_count = interval_count 
        self.billing_type = billing_type 
        if current_cycle is not APIHelper.SKIP:
            self.current_cycle = current_cycle 
        self.payment_method = payment_method 
        self.currency = currency 
        self.installments = installments 
        self.status = status 
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None 
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        self.card = card 
        self.items = items 
        self.statement_descriptor = statement_descriptor 
        self.metadata = metadata 
        self.setup = setup 
        self.gateway_affiliation_id = gateway_affiliation_id 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = APIHelper.RFC3339DateTime(next_billing_at) if next_billing_at else None 
        if billing_day is not APIHelper.SKIP:
            self.billing_day = billing_day 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.RFC3339DateTime(canceled_at) if canceled_at else None 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        self.increments = increments 
        if boleto_due_days is not APIHelper.SKIP:
            self.boleto_due_days = boleto_due_days 
        self.split = split 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 

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
        code = dictionary.get("code") if dictionary.get("code") else None
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_count = dictionary.get("interval_count") if dictionary.get("interval_count") else None
        billing_type = dictionary.get("billing_type") if dictionary.get("billing_type") else None
        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        currency = dictionary.get("currency") if dictionary.get("currency") else None
        installments = dictionary.get("installments") if dictionary.get("installments") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        card = GetCardResponse.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        items = None
        if dictionary.get('items') is not None:
            items = [GetSubscriptionItemResponse.from_dictionary(x) for x in dictionary.get('items')]
        statement_descriptor = dictionary.get("statement_descriptor") if dictionary.get("statement_descriptor") else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        setup = GetSetupResponse.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id") if dictionary.get("gateway_affiliation_id") else None
        increments = None
        if dictionary.get('increments') is not None:
            increments = [GetIncrementResponse.from_dictionary(x) for x in dictionary.get('increments')]
        split = GetSubscriptionSplitResponse.from_dictionary(dictionary.get('split')) if dictionary.get('split') else None
        if 'current_cycle' in dictionary.keys():
            current_cycle = GetPeriodResponse.from_dictionary(dictionary.get('current_cycle')) if dictionary.get('current_cycle') else None
        else:
            current_cycle = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        if 'next_billing_at' in dictionary.keys():
            next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else None
        else:
            next_billing_at = APIHelper.SKIP
        billing_day = dictionary.get("billing_day") if "billing_day" in dictionary.keys() else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if "minimum_price" in dictionary.keys() else APIHelper.SKIP
        if 'canceled_at' in dictionary.keys():
            canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        else:
            canceled_at = APIHelper.SKIP
        if 'discounts' in dictionary.keys():
            discounts = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('discounts')] if dictionary.get('discounts') else None
        else:
            discounts = APIHelper.SKIP
        boleto_due_days = dictionary.get("boleto_due_days") if "boleto_due_days" in dictionary.keys() else APIHelper.SKIP
        if 'boleto' in dictionary.keys():
            boleto = GetSubscriptionBoletoResponse.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        else:
            boleto = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   start_at,
                   interval,
                   interval_count,
                   billing_type,
                   payment_method,
                   currency,
                   installments,
                   status,
                   created_at,
                   updated_at,
                   card,
                   items,
                   statement_descriptor,
                   metadata,
                   setup,
                   gateway_affiliation_id,
                   increments,
                   split,
                   current_cycle,
                   customer,
                   next_billing_at,
                   billing_day,
                   minimum_price,
                   canceled_at,
                   discounts,
                   boleto_due_days,
                   boleto)
