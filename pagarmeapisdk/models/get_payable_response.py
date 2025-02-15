# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetPayableResponse(object):

    """Implementation of the 'GetPayableResponse' model.

    Response object for getting an payable

    Attributes:
        id (long|int): TODO: type description here.
        status (str): TODO: type description here.
        amount (int): TODO: type description here.
        fee (int): TODO: type description here.
        anticipation_fee (int): TODO: type description here.
        fraud_coverage_fee (int): TODO: type description here.
        installment (int): TODO: type description here.
        gateway_id (int): TODO: type description here.
        charge_id (str): TODO: type description here.
        split_id (str): TODO: type description here.
        bulk_anticipation_id (str): TODO: type description here.
        anticipation_id (str): TODO: type description here.
        recipient_id (str): TODO: type description here.
        originator_model (str): TODO: type description here.
        originator_model_id (str): TODO: type description here.
        payment_date (datetime): TODO: type description here.
        original_payment_date (datetime): TODO: type description here.
        mtype (str): TODO: type description here.
        payment_method (str): TODO: type description here.
        accrual_at (datetime): TODO: type description here.
        created_at (datetime): TODO: type description here.
        liquidation_arrangement_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "fee": 'fee',
        "anticipation_fee": 'anticipation_fee',
        "fraud_coverage_fee": 'fraud_coverage_fee',
        "installment": 'installment',
        "gateway_id": 'gateway_id',
        "charge_id": 'charge_id',
        "split_id": 'split_id',
        "bulk_anticipation_id": 'bulk_anticipation_id',
        "anticipation_id": 'anticipation_id',
        "recipient_id": 'recipient_id',
        "originator_model": 'originator_model',
        "originator_model_id": 'originator_model_id',
        "payment_date": 'payment_date',
        "original_payment_date": 'original_payment_date',
        "mtype": 'type',
        "payment_method": 'payment_method',
        "accrual_at": 'accrual_at',
        "created_at": 'created_at',
        "liquidation_arrangement_id": 'liquidation_arrangement_id'
    }

    _optionals = [
        'id',
        'status',
        'amount',
        'fee',
        'anticipation_fee',
        'fraud_coverage_fee',
        'installment',
        'gateway_id',
        'charge_id',
        'split_id',
        'bulk_anticipation_id',
        'anticipation_id',
        'recipient_id',
        'originator_model',
        'originator_model_id',
        'payment_date',
        'original_payment_date',
        'mtype',
        'payment_method',
        'accrual_at',
        'created_at',
        'liquidation_arrangement_id',
    ]

    _nullables = [
        'id',
        'status',
        'amount',
        'fee',
        'anticipation_fee',
        'fraud_coverage_fee',
        'installment',
        'gateway_id',
        'charge_id',
        'split_id',
        'bulk_anticipation_id',
        'anticipation_id',
        'recipient_id',
        'originator_model',
        'originator_model_id',
        'payment_date',
        'original_payment_date',
        'mtype',
        'payment_method',
        'accrual_at',
        'created_at',
        'liquidation_arrangement_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 fee=APIHelper.SKIP,
                 anticipation_fee=APIHelper.SKIP,
                 fraud_coverage_fee=APIHelper.SKIP,
                 installment=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 split_id=APIHelper.SKIP,
                 bulk_anticipation_id=APIHelper.SKIP,
                 anticipation_id=APIHelper.SKIP,
                 recipient_id=APIHelper.SKIP,
                 originator_model=APIHelper.SKIP,
                 originator_model_id=APIHelper.SKIP,
                 payment_date=APIHelper.SKIP,
                 original_payment_date=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 accrual_at=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 liquidation_arrangement_id=APIHelper.SKIP):
        """Constructor for the GetPayableResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if fee is not APIHelper.SKIP:
            self.fee = fee 
        if anticipation_fee is not APIHelper.SKIP:
            self.anticipation_fee = anticipation_fee 
        if fraud_coverage_fee is not APIHelper.SKIP:
            self.fraud_coverage_fee = fraud_coverage_fee 
        if installment is not APIHelper.SKIP:
            self.installment = installment 
        if gateway_id is not APIHelper.SKIP:
            self.gateway_id = gateway_id 
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 
        if split_id is not APIHelper.SKIP:
            self.split_id = split_id 
        if bulk_anticipation_id is not APIHelper.SKIP:
            self.bulk_anticipation_id = bulk_anticipation_id 
        if anticipation_id is not APIHelper.SKIP:
            self.anticipation_id = anticipation_id 
        if recipient_id is not APIHelper.SKIP:
            self.recipient_id = recipient_id 
        if originator_model is not APIHelper.SKIP:
            self.originator_model = originator_model 
        if originator_model_id is not APIHelper.SKIP:
            self.originator_model_id = originator_model_id 
        if payment_date is not APIHelper.SKIP:
            self.payment_date = APIHelper.apply_datetime_converter(payment_date, APIHelper.RFC3339DateTime) if payment_date else None 
        if original_payment_date is not APIHelper.SKIP:
            self.original_payment_date = APIHelper.apply_datetime_converter(original_payment_date, APIHelper.RFC3339DateTime) if original_payment_date else None 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if accrual_at is not APIHelper.SKIP:
            self.accrual_at = APIHelper.apply_datetime_converter(accrual_at, APIHelper.RFC3339DateTime) if accrual_at else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if liquidation_arrangement_id is not APIHelper.SKIP:
            self.liquidation_arrangement_id = liquidation_arrangement_id 

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
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        fee = dictionary.get("fee") if "fee" in dictionary.keys() else APIHelper.SKIP
        anticipation_fee = dictionary.get("anticipation_fee") if "anticipation_fee" in dictionary.keys() else APIHelper.SKIP
        fraud_coverage_fee = dictionary.get("fraud_coverage_fee") if "fraud_coverage_fee" in dictionary.keys() else APIHelper.SKIP
        installment = dictionary.get("installment") if "installment" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        split_id = dictionary.get("split_id") if "split_id" in dictionary.keys() else APIHelper.SKIP
        bulk_anticipation_id = dictionary.get("bulk_anticipation_id") if "bulk_anticipation_id" in dictionary.keys() else APIHelper.SKIP
        anticipation_id = dictionary.get("anticipation_id") if "anticipation_id" in dictionary.keys() else APIHelper.SKIP
        recipient_id = dictionary.get("recipient_id") if "recipient_id" in dictionary.keys() else APIHelper.SKIP
        originator_model = dictionary.get("originator_model") if "originator_model" in dictionary.keys() else APIHelper.SKIP
        originator_model_id = dictionary.get("originator_model_id") if "originator_model_id" in dictionary.keys() else APIHelper.SKIP
        if 'payment_date' in dictionary.keys():
            payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("payment_date")).datetime if dictionary.get("payment_date") else None
        else:
            payment_date = APIHelper.SKIP
        if 'original_payment_date' in dictionary.keys():
            original_payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("original_payment_date")).datetime if dictionary.get("original_payment_date") else None
        else:
            original_payment_date = APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        payment_method = dictionary.get("payment_method") if "payment_method" in dictionary.keys() else APIHelper.SKIP
        if 'accrual_at' in dictionary.keys():
            accrual_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("accrual_at")).datetime if dictionary.get("accrual_at") else None
        else:
            accrual_at = APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        liquidation_arrangement_id = dictionary.get("liquidation_arrangement_id") if "liquidation_arrangement_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   status,
                   amount,
                   fee,
                   anticipation_fee,
                   fraud_coverage_fee,
                   installment,
                   gateway_id,
                   charge_id,
                   split_id,
                   bulk_anticipation_id,
                   anticipation_id,
                   recipient_id,
                   originator_model,
                   originator_model_id,
                   payment_date,
                   original_payment_date,
                   mtype,
                   payment_method,
                   accrual_at,
                   created_at,
                   liquidation_arrangement_id)
