# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class DebitReversal(
    CreateableAPIResource["DebitReversal"],
    ListableAPIResource["DebitReversal"],
):
    """
    You can reverse some [ReceivedDebits](https://stripe.com/docs/api#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.debit_reversal"]
    ] = "treasury.debit_reversal"

    class LinkedFlows(StripeObject):
        issuing_dispute: Optional[str]
        """
        Set if there is an Issuing dispute associated with the DebitReversal.
        """

    class StatusTransitions(StripeObject):
        completed_at: Optional[int]
        """
        Timestamp describing when the DebitReversal changed status to `completed`.
        """

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            received_debit: str
            """
            The ReceivedDebit to reverse.
            """

        class ListParams(RequestOptions):
            ending_before: NotRequired["str"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_account: str
            """
            Returns objects associated with this FinancialAccount.
            """
            limit: NotRequired["int"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            received_debit: NotRequired["str"]
            """
            Only return DebitReversals for the ReceivedDebit ID.
            """
            resolution: NotRequired["Literal['lost', 'won']"]
            """
            Only return DebitReversals for a given resolution.
            """
            starting_after: NotRequired["str"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['canceled', 'completed', 'processing']"
            ]
            """
            Only return DebitReversals for a given status.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: int
    """
    Amount (in cents) transferred.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    financial_account: Optional[str]
    """
    The FinancialAccount to reverse funds from.
    """
    hosted_regulatory_receipt_url: Optional[str]
    """
    A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    id: str
    """
    Unique identifier for the object.
    """
    linked_flows: Optional[LinkedFlows]
    """
    Other flows linked to a DebitReversal.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network: Literal["ach", "card"]
    """
    The rails used to reverse the funds.
    """
    object: Literal["treasury.debit_reversal"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    received_debit: str
    """
    The ReceivedDebit being reversed.
    """
    status: Literal["failed", "processing", "succeeded"]
    """
    Status of the DebitReversal
    """
    status_transitions: StatusTransitions
    transaction: Optional[ExpandableField["Transaction"]]
    """
    The Transaction associated with this object.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "DebitReversal.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "DebitReversal":
        """
        Reverses a ReceivedDebit and creates a DebitReversal object.
        """
        return cast(
            "DebitReversal",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "DebitReversal.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["DebitReversal"]:
        """
        Returns a list of DebitReversals.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["DebitReversal.RetrieveParams"]
    ) -> "DebitReversal":
        """
        Retrieves a DebitReversal object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "linked_flows": LinkedFlows,
        "status_transitions": StatusTransitions,
    }
