# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.terminal.location import Location


class Reader(
    CreateableAPIResource["Reader"],
    DeletableAPIResource["Reader"],
    ListableAPIResource["Reader"],
    UpdateableAPIResource["Reader"],
):
    """
    A Reader represents a physical device for accepting payment details.

    Related guide: [Connecting to a reader](https://stripe.com/docs/terminal/payments/connect-reader)
    """

    OBJECT_NAME: ClassVar[Literal["terminal.reader"]] = "terminal.reader"

    class Action(StripeObject):
        class ProcessPaymentIntent(StripeObject):
            class ProcessConfig(StripeObject):
                class Tipping(StripeObject):
                    amount_eligible: Optional[int]
                    """
                    Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
                    """

                skip_tipping: Optional[bool]
                """
                Override showing a tipping selection screen on this transaction.
                """
                tipping: Optional[Tipping]
                """
                Represents a per-transaction tipping configuration
                """
                _inner_class_types = {"tipping": Tipping}

            payment_intent: ExpandableField["PaymentIntent"]
            """
            Most recent PaymentIntent processed by the reader.
            """
            process_config: Optional[ProcessConfig]
            """
            Represents a per-transaction override of a reader configuration
            """
            _inner_class_types = {"process_config": ProcessConfig}

        class ProcessSetupIntent(StripeObject):
            class ProcessConfig(StripeObject):
                pass

            generated_card: Optional[str]
            """
            ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.
            """
            process_config: Optional[ProcessConfig]
            """
            Represents a per-setup override of a reader configuration
            """
            setup_intent: ExpandableField["SetupIntent"]
            """
            Most recent SetupIntent processed by the reader.
            """
            _inner_class_types = {"process_config": ProcessConfig}

        class RefundPayment(StripeObject):
            amount: Optional[int]
            """
            The amount being refunded.
            """
            charge: Optional[ExpandableField["Charge"]]
            """
            Charge that is being refunded.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            payment_intent: Optional[ExpandableField["PaymentIntent"]]
            """
            Payment intent that is being refunded.
            """
            reason: Optional[
                Literal["duplicate", "fraudulent", "requested_by_customer"]
            ]
            """
            The reason for the refund.
            """
            refund: Optional[ExpandableField["Refund"]]
            """
            Unique identifier for the refund object.
            """
            refund_application_fee: Optional[bool]
            """
            Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
            """
            reverse_transfer: Optional[bool]
            """
            Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
            """

        class SetReaderDisplay(StripeObject):
            class Cart(StripeObject):
                class LineItem(StripeObject):
                    amount: int
                    """
                    The amount of the line item. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
                    """
                    description: str
                    """
                    Description of the line item.
                    """
                    quantity: int
                    """
                    The quantity of the line item.
                    """

                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                line_items: List[LineItem]
                """
                List of line items in the cart.
                """
                tax: Optional[int]
                """
                Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
                """
                total: int
                """
                Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
                """
                _inner_class_types = {"line_items": LineItem}

            cart: Optional[Cart]
            """
            Cart object to be displayed by the reader.
            """
            type: Literal["cart"]
            """
            Type of information to be displayed by the reader.
            """
            _inner_class_types = {"cart": Cart}

        failure_code: Optional[str]
        """
        Failure code, only set if status is `failed`.
        """
        failure_message: Optional[str]
        """
        Detailed failure message, only set if status is `failed`.
        """
        process_payment_intent: Optional[ProcessPaymentIntent]
        """
        Represents a reader action to process a payment intent
        """
        process_setup_intent: Optional[ProcessSetupIntent]
        """
        Represents a reader action to process a setup intent
        """
        refund_payment: Optional[RefundPayment]
        """
        Represents a reader action to refund a payment
        """
        set_reader_display: Optional[SetReaderDisplay]
        """
        Represents a reader action to set the reader display
        """
        status: Literal["failed", "in_progress", "succeeded"]
        """
        Status of the action performed by the reader.
        """
        type: Literal[
            "process_payment_intent",
            "process_setup_intent",
            "refund_payment",
            "set_reader_display",
        ]
        """
        Type of action performed by the reader.
        """
        _inner_class_types = {
            "process_payment_intent": ProcessPaymentIntent,
            "process_setup_intent": ProcessSetupIntent,
            "refund_payment": RefundPayment,
            "set_reader_display": SetReaderDisplay,
        }

    if TYPE_CHECKING:

        class CancelActionParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            label: NotRequired["str"]
            """
            Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.
            """
            location: NotRequired["str"]
            """
            The location to assign the reader to.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            registration_code: str
            """
            A code generated by the reader used for registering to an account.
            """

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            device_type: NotRequired[
                "Literal['bbpos_chipper2x', 'bbpos_wisepad3', 'bbpos_wisepos_e', 'simulated_wisepos_e', 'stripe_m2', 'verifone_P400']"
            ]
            """
            Filters readers by device type
            """
            ending_before: NotRequired["str"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            location: NotRequired["str"]
            """
            A location ID to filter the response list to only readers at the specific location
            """
            serial_number: NotRequired["str"]
            """
            Filters readers by serial number
            """
            starting_after: NotRequired["str"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired["Literal['offline', 'online']"]
            """
            A status filter to filter readers to only offline or online readers
            """

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            label: NotRequired["Literal['']|str"]
            """
            The new label of the reader.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """

        class ProcessPaymentIntentParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            payment_intent: str
            """
            PaymentIntent ID
            """
            process_config: NotRequired[
                "Reader.ProcessPaymentIntentParamsProcessConfig"
            ]
            """
            Configuration overrides
            """

        class ProcessPaymentIntentParamsProcessConfig(TypedDict):
            skip_tipping: NotRequired["bool"]
            """
            Override showing a tipping selection screen on this transaction.
            """
            tipping: NotRequired[
                "Reader.ProcessPaymentIntentParamsProcessConfigTipping"
            ]
            """
            Tipping configuration for this transaction.
            """

        class ProcessPaymentIntentParamsProcessConfigTipping(TypedDict):
            amount_eligible: NotRequired["int"]
            """
            Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
            """

        class ProcessSetupIntentParams(RequestOptions):
            customer_consent_collected: bool
            """
            Customer Consent Collected
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            process_config: NotRequired[
                "Reader.ProcessSetupIntentParamsProcessConfig"
            ]
            """
            Configuration overrides
            """
            setup_intent: str
            """
            SetupIntent ID
            """

        class ProcessSetupIntentParamsProcessConfig(TypedDict):
            pass

        class RefundPaymentParams(RequestOptions):
            amount: NotRequired["int"]
            """
            A positive integer in __cents__ representing how much of this charge to refund.
            """
            charge: NotRequired["str"]
            """
            ID of the Charge to refund.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            payment_intent: NotRequired["str"]
            """
            ID of the PaymentIntent to refund.
            """
            refund_application_fee: NotRequired["bool"]
            """
            Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
            """
            reverse_transfer: NotRequired["bool"]
            """
            Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

        class SetReaderDisplayParams(RequestOptions):
            cart: NotRequired["Reader.SetReaderDisplayParamsCart"]
            """
            Cart
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            type: Literal["cart"]
            """
            Type
            """

        class SetReaderDisplayParamsCart(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            line_items: List["Reader.SetReaderDisplayParamsCartLineItem"]
            """
            Array of line items that were purchased.
            """
            tax: NotRequired["int"]
            """
            The amount of tax in cents.
            """
            total: int
            """
            Total balance of cart due in cents.
            """

        class SetReaderDisplayParamsCartLineItem(TypedDict):
            amount: int
            """
            The price of the item in cents.
            """
            description: str
            """
            The description or name of the item.
            """
            quantity: int
            """
            The quantity of the line item being purchased.
            """

        class PresentPaymentMethodParams(RequestOptions):
            amount_tip: NotRequired["int"]
            """
            Simulated on-reader tip amount.
            """
            card_present: NotRequired[
                "Reader.PresentPaymentMethodParamsCardPresent"
            ]
            """
            Simulated data for the card_present payment method.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            interac_present: NotRequired[
                "Reader.PresentPaymentMethodParamsInteracPresent"
            ]
            """
            Simulated data for the interac_present payment method.
            """
            type: NotRequired["Literal['card_present', 'interac_present']"]
            """
            Simulated payment type.
            """

        class PresentPaymentMethodParamsInteracPresent(TypedDict):
            number: NotRequired["str"]
            """
            Card Number
            """

        class PresentPaymentMethodParamsCardPresent(TypedDict):
            number: NotRequired["str"]
            """
            The card number, as a string without any separators.
            """

    action: Optional[Action]
    """
    The most recent action performed by the reader.
    """
    device_sw_version: Optional[str]
    """
    The current software version of the reader.
    """
    device_type: Literal[
        "bbpos_chipper2x",
        "bbpos_wisepad3",
        "bbpos_wisepos_e",
        "simulated_wisepos_e",
        "stripe_m2",
        "verifone_P400",
    ]
    """
    Type of reader, one of `bbpos_wisepad3`, `stripe_m2`, `bbpos_chipper2x`, `bbpos_wisepos_e`, `verifone_P400`, or `simulated_wisepos_e`.
    """
    id: str
    """
    Unique identifier for the object.
    """
    ip_address: Optional[str]
    """
    The local IP address of the reader.
    """
    label: str
    """
    Custom label given to the reader for easier identification.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    location: Optional[ExpandableField["Location"]]
    """
    The location identifier of the reader.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["terminal.reader"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    serial_number: str
    """
    Serial number of the reader.
    """
    status: Optional[str]
    """
    The networking status of the reader.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def _cls_cancel_action(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.CancelActionParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel_action(
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.CancelActionParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @overload
    def cancel_action(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.CancelActionParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @class_method_variant("_cls_cancel_action")
    def cancel_action(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.CancelActionParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Creates a new Reader object.
        """
        return cast(
            "Reader",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Reader.DeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Reader",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @staticmethod
    def delete(sid: str, **params: Unpack["Reader.DeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Reader.DeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.DeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Reader"]:
        """
        Returns a list of Reader objects.
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
    def modify(
        cls, id: str, **params: Unpack["Reader.ModifyParams"]
    ) -> "Reader":
        """
        Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Reader",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_process_payment_intent(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessPaymentIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def process_payment_intent(
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessPaymentIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @overload
    def process_payment_intent(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessPaymentIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_payment_intent")
    def process_payment_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessPaymentIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_process_setup_intent(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessSetupIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def process_setup_intent(
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessSetupIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @overload
    def process_setup_intent(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessSetupIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_setup_intent")
    def process_setup_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.ProcessSetupIntentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_refund_payment(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.RefundPaymentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def refund_payment(
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.RefundPaymentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @overload
    def refund_payment(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.RefundPaymentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @class_method_variant("_cls_refund_payment")
    def refund_payment(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.RefundPaymentParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Reader.RetrieveParams"]
    ) -> "Reader":
        """
        Retrieves a Reader object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_set_reader_display(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.SetReaderDisplayParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def set_reader_display(
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Reader.SetReaderDisplayParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @overload
    def set_reader_display(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.SetReaderDisplayParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @class_method_variant("_cls_set_reader_display")
    def set_reader_display(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Reader.SetReaderDisplayParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    class TestHelpers(APIResourceTestHelpers["Reader"]):
        _resource_cls: Type["Reader"]

        @classmethod
        def _cls_present_payment_method(
            cls,
            reader: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "Reader.PresentPaymentMethodParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=util.sanitize_id(reader)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def present_payment_method(
            reader: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "Reader.PresentPaymentMethodParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @overload
        def present_payment_method(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "Reader.PresentPaymentMethodParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @class_method_variant("_cls_present_payment_method")
        def present_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "Reader.PresentPaymentMethodParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {"action": Action}


Reader.TestHelpers._resource_cls = Reader
