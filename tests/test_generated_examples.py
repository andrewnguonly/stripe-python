# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function
import stripe


class TestGeneratedExamples(object):
    def test_account_links_post(self, request_mock):
        stripe.AccountLink.create(
            account="acct_xxxxxxxxxxxxx",
            refresh_url="https://example.com/reauth",
            return_url="https://example.com/return",
            type="account_onboarding",
        )
        request_mock.assert_requested(
            "post",
            "/v1/account_links",
        )

    def test_accounts_capabilities_get(self, request_mock):
        stripe.Account.list_capabilities("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/capabilities",
        )

    def test_accounts_capabilities_get_2(self, request_mock):
        stripe.Account.retrieve_capability(
            "acct_xxxxxxxxxxxxx",
            "card_payments",
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
        )

    def test_accounts_capabilities_post(self, request_mock):
        stripe.Account.modify_capability(
            "acct_xxxxxxxxxxxxx",
            "card_payments",
            requested=True,
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
        )

    def test_accounts_delete(self, request_mock):
        stripe.Account.delete("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/acct_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_delete(self, request_mock):
        stripe.Account.delete_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_delete_2(self, request_mock):
        stripe.Account.delete_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_get(self, request_mock):
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
        )

    def test_accounts_external_accounts_get_2(self, request_mock):
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            object="bank_account",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
        )

    def test_accounts_external_accounts_get_3(self, request_mock):
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            object="card",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
        )

    def test_accounts_external_accounts_get_4(self, request_mock):
        stripe.Account.retrieve_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_get_5(self, request_mock):
        stripe.Account.retrieve_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_post(self, request_mock):
        stripe.Account.create_external_account(
            "acct_xxxxxxxxxxxxx",
            external_account="btok_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
        )

    def test_accounts_external_accounts_post_2(self, request_mock):
        stripe.Account.create_external_account(
            "acct_xxxxxxxxxxxxx",
            external_account="tok_xxxx_debit",
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
        )

    def test_accounts_external_accounts_post_3(self, request_mock):
        stripe.Account.modify_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_post_4(self, request_mock):
        stripe.Account.modify_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
        )

    def test_accounts_get(self, request_mock):
        stripe.Account.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/accounts",
        )

    def test_accounts_get_2(self, request_mock):
        stripe.Account.retrieve("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx",
        )

    def test_accounts_login_links_post(self, request_mock):
        stripe.Account.create_login_link("acct_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/login_links",
        )

    def test_accounts_persons_delete(self, request_mock):
        stripe.Account.delete_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
        )

    def test_accounts_persons_get(self, request_mock):
        stripe.Account.list_persons(
            "acct_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons",
        )

    def test_accounts_persons_get_2(self, request_mock):
        stripe.Account.retrieve_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
        )

    def test_accounts_persons_post(self, request_mock):
        stripe.Account.create_person(
            "acct_xxxxxxxxxxxxx",
            first_name="Jane",
            last_name="Diaz",
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons",
        )

    def test_accounts_persons_post_2(self, request_mock):
        stripe.Account.modify_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
        )

    def test_accounts_post(self, request_mock):
        stripe.Account.create(
            type="custom",
            country="US",
            email="jenny.rosen@example.com",
            capabilities={
                "card_payments": {"requested": True},
                "transfers": {"requested": True},
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts",
        )

    def test_accounts_post_2(self, request_mock):
        stripe.Account.modify(
            "acct_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx",
        )

    def test_accounts_reject_post(self, request_mock):
        stripe.Account.reject(
            "acct_xxxxxxxxxxxxx",
            reason="fraud",
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/acct_xxxxxxxxxxxxx/reject",
        )

    def test_application_fees_get(self, request_mock):
        stripe.ApplicationFee.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/application_fees",
        )

    def test_application_fees_get_2(self, request_mock):
        stripe.ApplicationFee.retrieve("fee_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/fee_xxxxxxxxxxxxx",
        )

    def test_application_fees_refunds_get(self, request_mock):
        stripe.ApplicationFee.list_refunds(
            "fee_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds",
        )

    def test_application_fees_refunds_get_2(self, request_mock):
        stripe.ApplicationFee.retrieve_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
        )

    def test_application_fees_refunds_post(self, request_mock):
        stripe.ApplicationFee.create_refund("fee_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds",
        )

    def test_application_fees_refunds_post_2(self, request_mock):
        stripe.ApplicationFee.modify_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
        )

    def test_apps_secrets_delete_post(self, request_mock):
        stripe.apps.Secret.delete_where(
            name="my-api-key",
            scope={"type": "account"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/apps/secrets/delete",
        )

    def test_apps_secrets_find_get(self, request_mock):
        stripe.apps.Secret.find(
            name="sec_123",
            scope={"type": "account"},
        )
        request_mock.assert_requested(
            "get",
            "/v1/apps/secrets/find",
        )

    def test_apps_secrets_get(self, request_mock):
        stripe.apps.Secret.list(
            scope={"type": "account"},
            limit=2,
        )
        request_mock.assert_requested(
            "get",
            "/v1/apps/secrets",
        )

    def test_apps_secrets_get_2(self, request_mock):
        stripe.apps.Secret.list(
            scope={"type": "account"},
            limit=2,
        )
        request_mock.assert_requested(
            "get",
            "/v1/apps/secrets",
        )

    def test_apps_secrets_post(self, request_mock):
        stripe.apps.Secret.create(
            name="sec_123",
            payload="very secret string",
            scope={"type": "account"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/apps/secrets",
        )

    def test_apps_secrets_post_2(self, request_mock):
        stripe.apps.Secret.create(
            name="my-api-key",
            payload="secret_key_xxxxxx",
            scope={"type": "account"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/apps/secrets",
        )

    def test_balance_transactions_get(self, request_mock):
        stripe.BalanceTransaction.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/balance_transactions",
        )

    def test_balance_transactions_get_2(self, request_mock):
        stripe.BalanceTransaction.retrieve("txn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/balance_transactions/txn_xxxxxxxxxxxxx",
        )

    def test_billing_portal_configurations_get(self, request_mock):
        stripe.billing_portal.Configuration.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/billing_portal/configurations",
        )

    def test_billing_portal_configurations_get_2(self, request_mock):
        stripe.billing_portal.Configuration.retrieve("bpc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
        )

    def test_billing_portal_configurations_post(self, request_mock):
        stripe.billing_portal.Configuration.create(
            features={
                "customer_update": {
                    "allowed_updates": ["email", "tax_id"],
                    "enabled": True,
                },
                "invoice_history": {"enabled": True},
            },
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/billing_portal/configurations",
        )

    def test_billing_portal_configurations_post_2(self, request_mock):
        stripe.billing_portal.Configuration.modify(
            "bpc_xxxxxxxxxxxxx",
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
        )

    def test_billing_portal_sessions_post(self, request_mock):
        stripe.billing_portal.Session.create(
            customer="cus_xxxxxxxxxxxxx",
            return_url="https://example.com/account",
        )
        request_mock.assert_requested(
            "post",
            "/v1/billing_portal/sessions",
        )

    def test_charges_capture_post(self, request_mock):
        stripe.Charge.capture("ch_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/charges/ch_xxxxxxxxxxxxx/capture",
        )

    def test_charges_get(self, request_mock):
        stripe.Charge.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/charges",
        )

    def test_charges_get_2(self, request_mock):
        stripe.Charge.retrieve("ch_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/charges/ch_xxxxxxxxxxxxx",
        )

    def test_charges_post(self, request_mock):
        stripe.Charge.create(
            amount=2000,
            currency="usd",
            source="tok_xxxx",
            description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
        )
        request_mock.assert_requested(
            "post",
            "/v1/charges",
        )

    def test_charges_post_2(self, request_mock):
        stripe.Charge.modify(
            "ch_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/charges/ch_xxxxxxxxxxxxx",
        )

    def test_charges_search_get(self, request_mock):
        stripe.Charge.search(
            query="amount>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested(
            "get",
            "/v1/charges/search",
        )

    def test_checkout_sessions_expire_post(self, request_mock):
        stripe.checkout.Session.expire("sess_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/sess_xyz/expire",
        )

    def test_checkout_sessions_expire_post_2(self, request_mock):
        stripe.checkout.Session.expire("cs_test_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx/expire",
        )

    def test_checkout_sessions_get(self, request_mock):
        stripe.checkout.Session.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/checkout/sessions",
        )

    def test_checkout_sessions_get_2(self, request_mock):
        stripe.checkout.Session.retrieve("cs_test_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx",
        )

    def test_checkout_sessions_line_items_get(self, request_mock):
        stripe.checkout.Session.list_line_items("sess_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/checkout/sessions/sess_xyz/line_items",
        )

    def test_checkout_sessions_post(self, request_mock):
        stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            mode="payment",
            shipping_options=[
                {"shipping_rate": "shr_standard"},
                {
                    "shipping_rate_data": {
                        "display_name": "Standard",
                        "delivery_estimate": {
                            "minimum": {"unit": "day", "value": 5},
                            "maximum": {"unit": "day", "value": 7},
                        },
                    },
                },
            ],
        )
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions",
        )

    def test_checkout_sessions_post_2(self, request_mock):
        stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
            mode="payment",
        )
        request_mock.assert_requested(
            "post",
            "/v1/checkout/sessions",
        )

    def test_country_specs_get(self, request_mock):
        stripe.CountrySpec.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/country_specs",
        )

    def test_country_specs_get_2(self, request_mock):
        stripe.CountrySpec.retrieve("US")
        request_mock.assert_requested(
            "get",
            "/v1/country_specs/US",
        )

    def test_coupons_delete(self, request_mock):
        stripe.Coupon.delete("Z4OV52SU")
        request_mock.assert_requested(
            "delete",
            "/v1/coupons/Z4OV52SU",
        )

    def test_coupons_get(self, request_mock):
        stripe.Coupon.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/coupons",
        )

    def test_coupons_get_2(self, request_mock):
        stripe.Coupon.retrieve("Z4OV52SU")
        request_mock.assert_requested(
            "get",
            "/v1/coupons/Z4OV52SU",
        )

    def test_coupons_post(self, request_mock):
        stripe.Coupon.create(
            percent_off=25.5,
            duration="repeating",
            duration_in_months=3,
        )
        request_mock.assert_requested(
            "post",
            "/v1/coupons",
        )

    def test_coupons_post_2(self, request_mock):
        stripe.Coupon.modify(
            "Z4OV52SU",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/coupons/Z4OV52SU",
        )

    def test_credit_notes_get(self, request_mock):
        stripe.CreditNote.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/credit_notes",
        )

    def test_credit_notes_lines_get(self, request_mock):
        stripe.CreditNote.list_lines(
            "cn_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/credit_notes/cn_xxxxxxxxxxxxx/lines",
        )

    def test_credit_notes_post(self, request_mock):
        stripe.CreditNote.create(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        request_mock.assert_requested(
            "post",
            "/v1/credit_notes",
        )

    def test_credit_notes_preview_get(self, request_mock):
        stripe.CreditNote.preview(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        request_mock.assert_requested(
            "get",
            "/v1/credit_notes/preview",
        )

    def test_credit_notes_preview_lines_get(self, request_mock):
        stripe.CreditNote.preview_lines(
            limit=3,
            invoice="in_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/credit_notes/preview/lines",
        )

    def test_credit_notes_void_post(self, request_mock):
        stripe.CreditNote.void_credit_note("cn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/credit_notes/cn_xxxxxxxxxxxxx/void",
        )

    def test_customers_balance_transactions_get(self, request_mock):
        stripe.Customer.list_balance_transactions(
            "cus_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions",
        )

    def test_customers_balance_transactions_get_2(self, request_mock):
        stripe.Customer.retrieve_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            "cbtxn_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions/cbtxn_xxxxxxxxxxxxx",
        )

    def test_customers_balance_transactions_post(self, request_mock):
        stripe.Customer.create_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            amount=-500,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions",
        )

    def test_customers_balance_transactions_post_2(self, request_mock):
        stripe.Customer.modify_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            "cbtxn_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions/cbtxn_xxxxxxxxxxxxx",
        )

    def test_customers_cash_balance_get(self, request_mock):
        stripe.Customer.retrieve_cash_balance("cus_123")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_123/cash_balance",
        )

    def test_customers_cash_balance_post(self, request_mock):
        stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/cash_balance",
        )

    def test_customers_delete(self, request_mock):
        stripe.Customer.delete("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/customers/cus_xxxxxxxxxxxxx",
        )

    def test_customers_funding_instructions_post(self, request_mock):
        stripe.Customer.create_funding_instructions(
            "cus_123",
            bank_transfer={
                "requested_address_types": ["zengin"],
                "type": "jp_bank_transfer",
            },
            currency="usd",
            funding_type="bank_transfer",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/funding_instructions",
        )

    def test_customers_get(self, request_mock):
        stripe.Customer.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/customers",
        )

    def test_customers_get_2(self, request_mock):
        stripe.Customer.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/customers",
        )

    def test_customers_get_3(self, request_mock):
        stripe.Customer.retrieve("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx",
        )

    def test_customers_payment_methods_get(self, request_mock):
        stripe.Customer.list_payment_methods(
            "cus_xyz",
            type="card",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xyz/payment_methods",
        )

    def test_customers_payment_methods_get_2(self, request_mock):
        stripe.Customer.list_payment_methods(
            "cus_xxxxxxxxxxxxx",
            type="card",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/payment_methods",
        )

    def test_customers_post(self, request_mock):
        stripe.Customer.create(
            description="My First Test Customer (created for API docs at https://www.stripe.com/docs/api)",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers",
        )

    def test_customers_post_2(self, request_mock):
        stripe.Customer.modify(
            "cus_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx",
        )

    def test_customers_search_get(self, request_mock):
        stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/search",
        )

    def test_customers_search_get_2(self, request_mock):
        stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/search",
        )

    def test_customers_sources_delete(self, request_mock):
        stripe.Customer.delete_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
        )

    def test_customers_sources_delete_2(self, request_mock):
        stripe.Customer.delete_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
        )

    def test_customers_sources_get(self, request_mock):
        stripe.Customer.list_sources(
            "cus_xxxxxxxxxxxxx",
            object="bank_account",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources",
        )

    def test_customers_sources_get_2(self, request_mock):
        stripe.Customer.list_sources(
            "cus_xxxxxxxxxxxxx",
            object="card",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources",
        )

    def test_customers_sources_get_3(self, request_mock):
        stripe.Customer.retrieve_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
        )

    def test_customers_sources_get_4(self, request_mock):
        stripe.Customer.retrieve_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
        )

    def test_customers_sources_post(self, request_mock):
        stripe.Customer.modify_source(
            "cus_123",
            "card_123",
            account_holder_name="Kamil",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_123/sources/card_123",
        )

    def test_customers_sources_post_2(self, request_mock):
        stripe.Customer.create_source(
            "cus_xxxxxxxxxxxxx",
            source="btok_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources",
        )

    def test_customers_sources_post_3(self, request_mock):
        stripe.Customer.create_source(
            "cus_xxxxxxxxxxxxx",
            source="tok_xxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources",
        )

    def test_customers_sources_post_4(self, request_mock):
        stripe.Customer.modify_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
        )

    def test_customers_sources_post_5(self, request_mock):
        stripe.Customer.modify_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
            name="Jenny Rosen",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
        )

    def test_customers_tax_ids_delete(self, request_mock):
        stripe.Customer.delete_tax_id(
            "cus_xxxxxxxxxxxxx",
            "txi_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "delete",
            "/v1/customers/cus_xxxxxxxxxxxxx/tax_ids/txi_xxxxxxxxxxxxx",
        )

    def test_customers_tax_ids_get(self, request_mock):
        stripe.Customer.list_tax_ids(
            "cus_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/tax_ids",
        )

    def test_customers_tax_ids_get_2(self, request_mock):
        stripe.Customer.retrieve_tax_id(
            "cus_xxxxxxxxxxxxx",
            "txi_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx/tax_ids/txi_xxxxxxxxxxxxx",
        )

    def test_customers_tax_ids_post(self, request_mock):
        stripe.Customer.create_tax_id(
            "cus_xxxxxxxxxxxxx",
            type="eu_vat",
            value="DE123456789",
        )
        request_mock.assert_requested(
            "post",
            "/v1/customers/cus_xxxxxxxxxxxxx/tax_ids",
        )

    def test_disputes_close_post(self, request_mock):
        stripe.Dispute.close("dp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/disputes/dp_xxxxxxxxxxxxx/close",
        )

    def test_disputes_get(self, request_mock):
        stripe.Dispute.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/disputes",
        )

    def test_disputes_get_2(self, request_mock):
        stripe.Dispute.retrieve("dp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/disputes/dp_xxxxxxxxxxxxx",
        )

    def test_disputes_post(self, request_mock):
        stripe.Dispute.modify(
            "dp_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/disputes/dp_xxxxxxxxxxxxx",
        )

    def test_events_get(self, request_mock):
        stripe.Event.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/events",
        )

    def test_events_get_2(self, request_mock):
        stripe.Event.retrieve("evt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/events/evt_xxxxxxxxxxxxx",
        )

    def test_file_links_get(self, request_mock):
        stripe.FileLink.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/file_links",
        )

    def test_file_links_get_2(self, request_mock):
        stripe.FileLink.retrieve("link_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/file_links/link_xxxxxxxxxxxxx",
        )

    def test_file_links_post(self, request_mock):
        stripe.FileLink.create(file="file_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/file_links",
        )

    def test_file_links_post_2(self, request_mock):
        stripe.FileLink.modify(
            "link_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/file_links/link_xxxxxxxxxxxxx",
        )

    def test_files_get(self, request_mock):
        stripe.File.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/files",
        )

    def test_files_get_2(self, request_mock):
        stripe.File.retrieve("file_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/files/file_xxxxxxxxxxxxx",
        )

    def test_financial_connections_accounts_disconnect_post(
        self, request_mock
    ):
        stripe.financial_connections.Account.disconnect("fca_xyz")
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/disconnect",
        )

    def test_financial_connections_accounts_disconnect_post_2(
        self, request_mock
    ):
        stripe.financial_connections.Account.disconnect("fca_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx/disconnect",
        )

    def test_financial_connections_accounts_get(self, request_mock):
        stripe.financial_connections.Account.list()
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts",
        )

    def test_financial_connections_accounts_get_2(self, request_mock):
        stripe.financial_connections.Account.retrieve("fca_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xyz",
        )

    def test_financial_connections_accounts_get_3(self, request_mock):
        stripe.financial_connections.Account.list(
            account_holder={"customer": "cus_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts",
        )

    def test_financial_connections_accounts_get_4(self, request_mock):
        stripe.financial_connections.Account.retrieve("fca_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx",
        )

    def test_financial_connections_accounts_owners_get(self, request_mock):
        stripe.financial_connections.Account.list_owners(
            "fca_xyz",
            ownership="fcaowns_xyz",
        )
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xyz/owners",
        )

    def test_financial_connections_accounts_owners_get_2(self, request_mock):
        stripe.financial_connections.Account.list_owners(
            "fca_xxxxxxxxxxxxx",
            limit=3,
            ownership="fcaowns_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx/owners",
        )

    def test_financial_connections_accounts_refresh_post(self, request_mock):
        stripe.financial_connections.Account.refresh_account(
            "fca_xyz",
            features=["balance"],
        )
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/accounts/fca_xyz/refresh",
        )

    def test_financial_connections_sessions_get(self, request_mock):
        stripe.financial_connections.Session.retrieve("fcsess_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/sessions/fcsess_xyz",
        )

    def test_financial_connections_sessions_get_2(self, request_mock):
        stripe.financial_connections.Session.retrieve("fcsess_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/financial_connections/sessions/fcsess_xxxxxxxxxxxxx",
        )

    def test_financial_connections_sessions_post(self, request_mock):
        stripe.financial_connections.Session.create(
            account_holder={"type": "customer", "customer": "cus_123"},
            permissions=["balances"],
        )
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/sessions",
        )

    def test_financial_connections_sessions_post_2(self, request_mock):
        stripe.financial_connections.Session.create(
            account_holder={
                "type": "customer",
                "customer": "cus_xxxxxxxxxxxxx",
            },
            permissions=["payment_method", "balances"],
            filters={"countries": ["US"]},
        )
        request_mock.assert_requested(
            "post",
            "/v1/financial_connections/sessions",
        )

    def test_identity_verification_reports_get(self, request_mock):
        stripe.identity.VerificationReport.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_reports",
        )

    def test_identity_verification_reports_get_2(self, request_mock):
        stripe.identity.VerificationReport.retrieve("vr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_reports/vr_xxxxxxxxxxxxx",
        )

    def test_identity_verification_sessions_cancel_post(self, request_mock):
        stripe.identity.VerificationSession.cancel("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/cancel",
        )

    def test_identity_verification_sessions_get(self, request_mock):
        stripe.identity.VerificationSession.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_sessions",
        )

    def test_identity_verification_sessions_get_2(self, request_mock):
        stripe.identity.VerificationSession.retrieve("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
        )

    def test_identity_verification_sessions_post(self, request_mock):
        stripe.identity.VerificationSession.create(type="document")
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions",
        )

    def test_identity_verification_sessions_post_2(self, request_mock):
        stripe.identity.VerificationSession.modify(
            "vs_xxxxxxxxxxxxx",
            type="id_number",
        )
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
        )

    def test_identity_verification_sessions_redact_post(self, request_mock):
        stripe.identity.VerificationSession.redact("vs_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/redact",
        )

    def test_invoiceitems_delete(self, request_mock):
        stripe.InvoiceItem.delete("ii_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/invoiceitems/ii_xxxxxxxxxxxxx",
        )

    def test_invoiceitems_get(self, request_mock):
        stripe.InvoiceItem.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/invoiceitems",
        )

    def test_invoiceitems_get_2(self, request_mock):
        stripe.InvoiceItem.retrieve("ii_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/invoiceitems/ii_xxxxxxxxxxxxx",
        )

    def test_invoiceitems_post(self, request_mock):
        stripe.InvoiceItem.create(
            customer="cus_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/invoiceitems",
        )

    def test_invoiceitems_post_2(self, request_mock):
        stripe.InvoiceItem.modify(
            "ii_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/invoiceitems/ii_xxxxxxxxxxxxx",
        )

    def test_invoices_delete(self, request_mock):
        stripe.Invoice.delete("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/invoices/in_xxxxxxxxxxxxx",
        )

    def test_invoices_finalize_post(self, request_mock):
        stripe.Invoice.finalize_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/finalize",
        )

    def test_invoices_get(self, request_mock):
        stripe.Invoice.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/invoices",
        )

    def test_invoices_get_2(self, request_mock):
        stripe.Invoice.retrieve("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/invoices/in_xxxxxxxxxxxxx",
        )

    def test_invoices_get_3(self, request_mock):
        stripe.Invoice.retrieve(
            "in_xxxxxxxxxxxxx",
            expand=["customer"],
        )
        request_mock.assert_requested(
            "get",
            "/v1/invoices/in_xxxxxxxxxxxxx",
        )

    def test_invoices_mark_uncollectible_post(self, request_mock):
        stripe.Invoice.mark_uncollectible("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/mark_uncollectible",
        )

    def test_invoices_pay_post(self, request_mock):
        stripe.Invoice.pay("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/pay",
        )

    def test_invoices_post(self, request_mock):
        stripe.Invoice.create(customer="cus_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices",
        )

    def test_invoices_post_2(self, request_mock):
        stripe.Invoice.modify(
            "in_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx",
        )

    def test_invoices_search_get(self, request_mock):
        stripe.Invoice.search(
            query="total>999 AND metadata['order_id']:'6735'"
        )
        request_mock.assert_requested(
            "get",
            "/v1/invoices/search",
        )

    def test_invoices_send_post(self, request_mock):
        stripe.Invoice.send_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/send",
        )

    def test_invoices_upcoming_get(self, request_mock):
        stripe.Invoice.upcoming(customer="cus_9utnxg47pWjV1e")
        request_mock.assert_requested(
            "get",
            "/v1/invoices/upcoming",
        )

    def test_invoices_void_post(self, request_mock):
        stripe.Invoice.void_invoice("in_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/invoices/in_xxxxxxxxxxxxx/void",
        )

    def test_issuing_authorizations_approve_post(self, request_mock):
        stripe.issuing.Authorization.approve("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/approve",
        )

    def test_issuing_authorizations_decline_post(self, request_mock):
        stripe.issuing.Authorization.decline("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/decline",
        )

    def test_issuing_authorizations_get(self, request_mock):
        stripe.issuing.Authorization.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/issuing/authorizations",
        )

    def test_issuing_authorizations_get_2(self, request_mock):
        stripe.issuing.Authorization.retrieve("iauth_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
        )

    def test_issuing_authorizations_post(self, request_mock):
        stripe.issuing.Authorization.modify(
            "iauth_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
        )

    def test_issuing_cardholders_get(self, request_mock):
        stripe.issuing.Cardholder.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/issuing/cardholders",
        )

    def test_issuing_cardholders_get_2(self, request_mock):
        stripe.issuing.Cardholder.retrieve("ich_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
        )

    def test_issuing_cardholders_post(self, request_mock):
        stripe.issuing.Cardholder.create(
            type="individual",
            name="Jenny Rosen",
            email="jenny.rosen@example.com",
            phone_number="+18888675309",
            billing={
                "address": {
                    "line1": "1234 Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94111",
                },
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/cardholders",
        )

    def test_issuing_cardholders_post_2(self, request_mock):
        stripe.issuing.Cardholder.modify(
            "ich_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
        )

    def test_issuing_cards_get(self, request_mock):
        stripe.issuing.Card.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/issuing/cards",
        )

    def test_issuing_cards_get_2(self, request_mock):
        stripe.issuing.Card.retrieve("ic_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/cards/ic_xxxxxxxxxxxxx",
        )

    def test_issuing_cards_post(self, request_mock):
        stripe.issuing.Card.create(
            cardholder="ich_xxxxxxxxxxxxx",
            currency="usd",
            type="virtual",
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/cards",
        )

    def test_issuing_cards_post_2(self, request_mock):
        stripe.issuing.Card.modify(
            "ic_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/cards/ic_xxxxxxxxxxxxx",
        )

    def test_issuing_disputes_get(self, request_mock):
        stripe.issuing.Dispute.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/issuing/disputes",
        )

    def test_issuing_disputes_get_2(self, request_mock):
        stripe.issuing.Dispute.retrieve("idp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/disputes/idp_xxxxxxxxxxxxx",
        )

    def test_issuing_disputes_post(self, request_mock):
        stripe.issuing.Dispute.create(
            transaction="ipi_xxxxxxxxxxxxx",
            evidence={
                "reason": "fraudulent",
                "fraudulent": {"explanation": "Purchase was unrecognized."},
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/disputes",
        )

    def test_issuing_disputes_submit_post(self, request_mock):
        stripe.issuing.Dispute.submit("idp_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/issuing/disputes/idp_xxxxxxxxxxxxx/submit",
        )

    def test_issuing_transactions_get(self, request_mock):
        stripe.issuing.Transaction.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/issuing/transactions",
        )

    def test_issuing_transactions_get_2(self, request_mock):
        stripe.issuing.Transaction.retrieve("ipi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
        )

    def test_issuing_transactions_post(self, request_mock):
        stripe.issuing.Transaction.modify(
            "ipi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
        )

    def test_mandates_get(self, request_mock):
        stripe.Mandate.retrieve("mandate_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/mandates/mandate_xxxxxxxxxxxxx",
        )

    def test_payment_intents_apply_customer_balance_post(self, request_mock):
        stripe.PaymentIntent.apply_customer_balance("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/apply_customer_balance",
        )

    def test_payment_intents_cancel_post(self, request_mock):
        stripe.PaymentIntent.cancel("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/cancel",
        )

    def test_payment_intents_capture_post(self, request_mock):
        stripe.PaymentIntent.capture("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/capture",
        )

    def test_payment_intents_confirm_post(self, request_mock):
        stripe.PaymentIntent.confirm(
            "pi_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/confirm",
        )

    def test_payment_intents_get(self, request_mock):
        stripe.PaymentIntent.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/payment_intents",
        )

    def test_payment_intents_get_2(self, request_mock):
        stripe.PaymentIntent.retrieve("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx",
        )

    def test_payment_intents_increment_authorization_post(self, request_mock):
        stripe.PaymentIntent.increment_authorization(
            "pi_xxxxxxxxxxxxx",
            amount=2099,
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/increment_authorization",
        )

    def test_payment_intents_post(self, request_mock):
        stripe.PaymentIntent.create(
            amount=1099,
            currency="eur",
            automatic_payment_methods={"enabled": True},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents",
        )

    def test_payment_intents_post_2(self, request_mock):
        stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents",
        )

    def test_payment_intents_post_3(self, request_mock):
        stripe.PaymentIntent.modify(
            "pi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx",
        )

    def test_payment_intents_post_4(self, request_mock):
        stripe.PaymentIntent.create(
            amount=200,
            currency="usd",
            payment_method_data={"type": "p24", "p24": {"bank": "blik"}},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents",
        )

    def test_payment_intents_search_get(self, request_mock):
        stripe.PaymentIntent.search(
            query="status:'succeeded' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/payment_intents/search",
        )

    def test_payment_intents_verify_microdeposits_post(self, request_mock):
        stripe.PaymentIntent.verify_microdeposits("pi_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
        )

    def test_payment_intents_verify_microdeposits_post_2(self, request_mock):
        stripe.PaymentIntent.verify_microdeposits(
            "pi_xxxxxxxxxxxxx",
            amounts=[32, 45],
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
        )

    def test_payment_links_get(self, request_mock):
        stripe.PaymentLink.retrieve("pl_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/payment_links/pl_xyz",
        )

    def test_payment_links_get_2(self, request_mock):
        stripe.PaymentLink.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/payment_links",
        )

    def test_payment_links_get_3(self, request_mock):
        stripe.PaymentLink.retrieve("plink_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/payment_links/plink_xxxxxxxxxxxxx",
        )

    def test_payment_links_line_items_get(self, request_mock):
        stripe.PaymentLink.list_line_items("pl_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/payment_links/pl_xyz/line_items",
        )

    def test_payment_links_post(self, request_mock):
        stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_links",
        )

    def test_payment_links_post_2(self, request_mock):
        stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_links",
        )

    def test_payment_links_post_3(self, request_mock):
        stripe.PaymentLink.modify(
            "plink_xxxxxxxxxxxxx",
            active=False,
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_links/plink_xxxxxxxxxxxxx",
        )

    def test_payment_method_configurations_get(self, request_mock):
        stripe.PaymentMethodConfiguration.list(application="foo")
        request_mock.assert_requested(
            "get",
            "/v1/payment_method_configurations",
        )

    def test_payment_method_configurations_get_2(self, request_mock):
        stripe.PaymentMethodConfiguration.retrieve("foo")
        request_mock.assert_requested(
            "get",
            "/v1/payment_method_configurations/foo",
        )

    def test_payment_method_configurations_post(self, request_mock):
        stripe.PaymentMethodConfiguration.create(
            acss_debit={"display_preference": {"preference": "none"}},
            affirm={"display_preference": {"preference": "none"}},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_method_configurations",
        )

    def test_payment_method_configurations_post_2(self, request_mock):
        stripe.PaymentMethodConfiguration.modify(
            "foo",
            acss_debit={"display_preference": {"preference": "on"}},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_method_configurations/foo",
        )

    def test_payment_methods_attach_post(self, request_mock):
        stripe.PaymentMethod.attach(
            "pm_xxxxxxxxxxxxx",
            customer="cus_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx/attach",
        )

    def test_payment_methods_detach_post(self, request_mock):
        stripe.PaymentMethod.detach("pm_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx/detach",
        )

    def test_payment_methods_get(self, request_mock):
        stripe.PaymentMethod.list(
            customer="cus_xxxxxxxxxxxxx",
            type="card",
        )
        request_mock.assert_requested(
            "get",
            "/v1/payment_methods",
        )

    def test_payment_methods_get_2(self, request_mock):
        stripe.PaymentMethod.retrieve("pm_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx",
        )

    def test_payment_methods_post(self, request_mock):
        stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2024,
                "cvc": "314",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods",
        )

    def test_payment_methods_post_2(self, request_mock):
        stripe.PaymentMethod.modify(
            "pm_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/pm_xxxxxxxxxxxxx",
        )

    def test_payouts_cancel_post(self, request_mock):
        stripe.Payout.cancel("po_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payouts/po_xxxxxxxxxxxxx/cancel",
        )

    def test_payouts_get(self, request_mock):
        stripe.Payout.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/payouts",
        )

    def test_payouts_get_2(self, request_mock):
        stripe.Payout.retrieve("po_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/payouts/po_xxxxxxxxxxxxx",
        )

    def test_payouts_post(self, request_mock):
        stripe.Payout.create(
            amount=1100,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/payouts",
        )

    def test_payouts_post_2(self, request_mock):
        stripe.Payout.modify(
            "po_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/payouts/po_xxxxxxxxxxxxx",
        )

    def test_payouts_reverse_post(self, request_mock):
        stripe.Payout.reverse("po_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/payouts/po_xxxxxxxxxxxxx/reverse",
        )

    def test_plans_delete(self, request_mock):
        stripe.Plan.delete("price_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/plans/price_xxxxxxxxxxxxx",
        )

    def test_plans_get(self, request_mock):
        stripe.Plan.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/plans",
        )

    def test_plans_get_2(self, request_mock):
        stripe.Plan.retrieve("price_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/plans/price_xxxxxxxxxxxxx",
        )

    def test_plans_post(self, request_mock):
        stripe.Plan.create(
            amount=2000,
            currency="usd",
            interval="month",
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/plans",
        )

    def test_plans_post_2(self, request_mock):
        stripe.Plan.create(
            amount=2000,
            currency="usd",
            interval="month",
            product={"name": "My product"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/plans",
        )

    def test_plans_post_3(self, request_mock):
        stripe.Plan.modify(
            "price_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/plans/price_xxxxxxxxxxxxx",
        )

    def test_prices_get(self, request_mock):
        stripe.Price.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/prices",
        )

    def test_prices_get_2(self, request_mock):
        stripe.Price.retrieve("price_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/prices/price_xxxxxxxxxxxxx",
        )

    def test_prices_post(self, request_mock):
        stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            currency_options={
                "uah": {"unit_amount": 5000},
                "eur": {"unit_amount": 1800},
            },
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/prices",
        )

    def test_prices_post_2(self, request_mock):
        stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/prices",
        )

    def test_prices_post_3(self, request_mock):
        stripe.Price.modify(
            "price_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/prices/price_xxxxxxxxxxxxx",
        )

    def test_prices_search_get(self, request_mock):
        stripe.Price.search(
            query="active:'true' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/prices/search",
        )

    def test_products_delete(self, request_mock):
        stripe.Product.delete("prod_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/products/prod_xxxxxxxxxxxxx",
        )

    def test_products_get(self, request_mock):
        stripe.Product.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/products",
        )

    def test_products_get_2(self, request_mock):
        stripe.Product.retrieve("prod_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/products/prod_xxxxxxxxxxxxx",
        )

    def test_products_post(self, request_mock):
        stripe.Product.create(name="Gold Special")
        request_mock.assert_requested(
            "post",
            "/v1/products",
        )

    def test_products_post_2(self, request_mock):
        stripe.Product.modify(
            "prod_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/products/prod_xxxxxxxxxxxxx",
        )

    def test_products_search_get(self, request_mock):
        stripe.Product.search(
            query="active:'true' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/products/search",
        )

    def test_promotion_codes_get(self, request_mock):
        stripe.PromotionCode.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/promotion_codes",
        )

    def test_promotion_codes_get_2(self, request_mock):
        stripe.PromotionCode.retrieve("promo_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    def test_promotion_codes_post(self, request_mock):
        stripe.PromotionCode.create(coupon="Z4OV52SU")
        request_mock.assert_requested(
            "post",
            "/v1/promotion_codes",
        )

    def test_promotion_codes_post_2(self, request_mock):
        stripe.PromotionCode.modify(
            "promo_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/promotion_codes/promo_xxxxxxxxxxxxx",
        )

    def test_quotes_accept_post(self, request_mock):
        stripe.Quote.accept("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx/accept",
        )

    def test_quotes_cancel_post(self, request_mock):
        stripe.Quote.cancel("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx/cancel",
        )

    def test_quotes_finalize_post(self, request_mock):
        stripe.Quote.finalize_quote("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx/finalize",
        )

    def test_quotes_get(self, request_mock):
        stripe.Quote.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/quotes",
        )

    def test_quotes_get_2(self, request_mock):
        stripe.Quote.retrieve("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/quotes/qt_xxxxxxxxxxxxx",
        )

    def test_quotes_line_items_get(self, request_mock):
        stripe.Quote.list_line_items("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/quotes/qt_xxxxxxxxxxxxx/line_items",
        )

    def test_quotes_pdf_get(self, request_mock):
        stripe.Quote.pdf("qt_xxxxxxxxxxxxx")
        request_mock.assert_requested_stream(
            "get",
            "/v1/quotes/qt_xxxxxxxxxxxxx/pdf",
        )

    def test_quotes_post(self, request_mock):
        stripe.Quote.create(
            customer="cus_xxxxxxxxxxxxx",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
        )
        request_mock.assert_requested(
            "post",
            "/v1/quotes",
        )

    def test_quotes_post_2(self, request_mock):
        stripe.Quote.modify(
            "qt_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/quotes/qt_xxxxxxxxxxxxx",
        )

    def test_radar_early_fraud_warnings_get(self, request_mock):
        stripe.radar.EarlyFraudWarning.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/radar/early_fraud_warnings",
        )

    def test_radar_early_fraud_warnings_get_2(self, request_mock):
        stripe.radar.EarlyFraudWarning.retrieve("issfr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/early_fraud_warnings/issfr_xxxxxxxxxxxxx",
        )

    def test_radar_value_list_items_delete(self, request_mock):
        stripe.radar.ValueListItem.delete("rsli_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
        )

    def test_radar_value_list_items_get(self, request_mock):
        stripe.radar.ValueListItem.list(
            limit=3,
            value_list="rsl_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_list_items",
        )

    def test_radar_value_list_items_get_2(self, request_mock):
        stripe.radar.ValueListItem.retrieve("rsli_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
        )

    def test_radar_value_list_items_post(self, request_mock):
        stripe.radar.ValueListItem.create(
            value_list="rsl_xxxxxxxxxxxxx",
            value="1.2.3.4",
        )
        request_mock.assert_requested(
            "post",
            "/v1/radar/value_list_items",
        )

    def test_radar_value_lists_delete(self, request_mock):
        stripe.radar.ValueList.delete("rsl_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    def test_radar_value_lists_get(self, request_mock):
        stripe.radar.ValueList.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_lists",
        )

    def test_radar_value_lists_get_2(self, request_mock):
        stripe.radar.ValueList.retrieve("rsl_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    def test_radar_value_lists_post(self, request_mock):
        stripe.radar.ValueList.create(
            alias="custom_ip_xxxxxxxxxxxxx",
            name="Custom IP Blocklist",
            item_type="ip_address",
        )
        request_mock.assert_requested(
            "post",
            "/v1/radar/value_lists",
        )

    def test_radar_value_lists_post_2(self, request_mock):
        stripe.radar.ValueList.modify(
            "rsl_xxxxxxxxxxxxx",
            name="Updated IP Block List",
        )
        request_mock.assert_requested(
            "post",
            "/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
        )

    def test_refunds_cancel_post(self, request_mock):
        stripe.Refund.cancel("re_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/refunds/re_xxxxxxxxxxxxx/cancel",
        )

    def test_refunds_get(self, request_mock):
        stripe.Refund.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/refunds",
        )

    def test_refunds_get_2(self, request_mock):
        stripe.Refund.retrieve("re_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/refunds/re_xxxxxxxxxxxxx",
        )

    def test_refunds_post(self, request_mock):
        stripe.Refund.create(charge="ch_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/refunds",
        )

    def test_refunds_post_2(self, request_mock):
        stripe.Refund.modify(
            "re_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/refunds/re_xxxxxxxxxxxxx",
        )

    def test_reporting_report_runs_get(self, request_mock):
        stripe.reporting.ReportRun.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_runs",
        )

    def test_reporting_report_runs_get_2(self, request_mock):
        stripe.reporting.ReportRun.retrieve("frr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_runs/frr_xxxxxxxxxxxxx",
        )

    def test_reporting_report_runs_post(self, request_mock):
        stripe.reporting.ReportRun.create(
            report_type="balance.summary.1",
            parameters={
                "interval_start": 1522540800,
                "interval_end": 1525132800,
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/reporting/report_runs",
        )

    def test_reporting_report_types_get(self, request_mock):
        stripe.reporting.ReportType.list()
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_types",
        )

    def test_reporting_report_types_get_2(self, request_mock):
        stripe.reporting.ReportType.retrieve("balance.summary.1")
        request_mock.assert_requested(
            "get",
            "/v1/reporting/report_types/balance.summary.1",
        )

    def test_reviews_approve_post(self, request_mock):
        stripe.Review.approve("prv_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/reviews/prv_xxxxxxxxxxxxx/approve",
        )

    def test_reviews_get(self, request_mock):
        stripe.Review.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/reviews",
        )

    def test_reviews_get_2(self, request_mock):
        stripe.Review.retrieve("prv_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/reviews/prv_xxxxxxxxxxxxx",
        )

    def test_setup_attempts_get(self, request_mock):
        stripe.SetupAttempt.list(
            limit=3,
            setup_intent="si_xyz",
        )
        request_mock.assert_requested(
            "get",
            "/v1/setup_attempts",
        )

    def test_setup_intents_cancel_post(self, request_mock):
        stripe.SetupIntent.cancel("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/cancel",
        )

    def test_setup_intents_confirm_post(self, request_mock):
        stripe.SetupIntent.confirm(
            "seti_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/confirm",
        )

    def test_setup_intents_get(self, request_mock):
        stripe.SetupIntent.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/setup_intents",
        )

    def test_setup_intents_get_2(self, request_mock):
        stripe.SetupIntent.retrieve("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx",
        )

    def test_setup_intents_post(self, request_mock):
        stripe.SetupIntent.create(payment_method_types=["card"])
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents",
        )

    def test_setup_intents_post_2(self, request_mock):
        stripe.SetupIntent.modify(
            "seti_xxxxxxxxxxxxx",
            metadata={"user_id": "3435453"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx",
        )

    def test_setup_intents_verify_microdeposits_post(self, request_mock):
        stripe.SetupIntent.verify_microdeposits("seti_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
        )

    def test_setup_intents_verify_microdeposits_post_2(self, request_mock):
        stripe.SetupIntent.verify_microdeposits(
            "seti_xxxxxxxxxxxxx",
            amounts=[32, 45],
        )
        request_mock.assert_requested(
            "post",
            "/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
        )

    def test_shipping_rates_get(self, request_mock):
        stripe.ShippingRate.list()
        request_mock.assert_requested(
            "get",
            "/v1/shipping_rates",
        )

    def test_shipping_rates_get_2(self, request_mock):
        stripe.ShippingRate.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/shipping_rates",
        )

    def test_shipping_rates_get_3(self, request_mock):
        stripe.ShippingRate.retrieve("shr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/shipping_rates/shr_xxxxxxxxxxxxx",
        )

    def test_shipping_rates_post(self, request_mock):
        stripe.ShippingRate.create(
            display_name="Sample Shipper",
            fixed_amount={"currency": "usd", "amount": 400},
            type="fixed_amount",
        )
        request_mock.assert_requested(
            "post",
            "/v1/shipping_rates",
        )

    def test_shipping_rates_post_2(self, request_mock):
        stripe.ShippingRate.create(
            display_name="Ground shipping",
            type="fixed_amount",
            fixed_amount={"amount": 500, "currency": "usd"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/shipping_rates",
        )

    def test_shipping_rates_post_3(self, request_mock):
        stripe.ShippingRate.modify(
            "shr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/shipping_rates/shr_xxxxxxxxxxxxx",
        )

    def test_sigma_scheduled_query_runs_get(self, request_mock):
        stripe.sigma.ScheduledQueryRun.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/sigma/scheduled_query_runs",
        )

    def test_sigma_scheduled_query_runs_get_2(self, request_mock):
        stripe.sigma.ScheduledQueryRun.retrieve("sqr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/sigma/scheduled_query_runs/sqr_xxxxxxxxxxxxx",
        )

    def test_sources_get(self, request_mock):
        stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/sources/src_xxxxxxxxxxxxx",
        )

    def test_sources_get_2(self, request_mock):
        stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/sources/src_xxxxxxxxxxxxx",
        )

    def test_sources_post(self, request_mock):
        stripe.Source.modify(
            "src_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/sources/src_xxxxxxxxxxxxx",
        )

    def test_subscription_items_delete(self, request_mock):
        stripe.SubscriptionItem.delete("si_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    def test_subscription_items_get(self, request_mock):
        stripe.SubscriptionItem.list(subscription="sub_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscription_items",
        )

    def test_subscription_items_get_2(self, request_mock):
        stripe.SubscriptionItem.retrieve("si_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    def test_subscription_items_post(self, request_mock):
        stripe.SubscriptionItem.create(
            subscription="sub_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
            quantity=2,
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items",
        )

    def test_subscription_items_post_2(self, request_mock):
        stripe.SubscriptionItem.modify(
            "si_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/si_xxxxxxxxxxxxx",
        )

    def test_subscription_items_usage_record_summaries_get(self, request_mock):
        stripe.SubscriptionItem.list_usage_record_summaries(
            "si_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/subscription_items/si_xxxxxxxxxxxxx/usage_record_summaries",
        )

    def test_subscription_items_usage_records_post(self, request_mock):
        stripe.SubscriptionItem.create_usage_record(
            "si_xxxxxxxxxxxxx",
            quantity=100,
            timestamp=1571252444,
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_items/si_xxxxxxxxxxxxx/usage_records",
        )

    def test_subscription_schedules_cancel_post(self, request_mock):
        stripe.SubscriptionSchedule.cancel("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/cancel",
        )

    def test_subscription_schedules_get(self, request_mock):
        stripe.SubscriptionSchedule.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/subscription_schedules",
        )

    def test_subscription_schedules_get_2(self, request_mock):
        stripe.SubscriptionSchedule.retrieve("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
        )

    def test_subscription_schedules_post(self, request_mock):
        stripe.SubscriptionSchedule.create(
            customer="cus_xxxxxxxxxxxxx",
            start_date=1676070661,
            end_behavior="release",
            phases=[
                {
                    "items": [{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
                    "iterations": 12,
                },
            ],
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules",
        )

    def test_subscription_schedules_post_2(self, request_mock):
        stripe.SubscriptionSchedule.modify(
            "sub_sched_xxxxxxxxxxxxx",
            end_behavior="release",
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
        )

    def test_subscription_schedules_release_post(self, request_mock):
        stripe.SubscriptionSchedule.release("sub_sched_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/release",
        )

    def test_subscriptions_delete(self, request_mock):
        stripe.Subscription.cancel("sub_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/subscriptions/sub_xxxxxxxxxxxxx",
        )

    def test_subscriptions_discount_delete(self, request_mock):
        stripe.Subscription.delete_discount("sub_xyz")
        request_mock.assert_requested(
            "delete",
            "/v1/subscriptions/sub_xyz/discount",
        )

    def test_subscriptions_get(self, request_mock):
        stripe.Subscription.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/subscriptions",
        )

    def test_subscriptions_get_2(self, request_mock):
        stripe.Subscription.retrieve("sub_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/subscriptions/sub_xxxxxxxxxxxxx",
        )

    def test_subscriptions_post(self, request_mock):
        stripe.Subscription.create(
            customer="cus_xxxxxxxxxxxxx",
            items=[{"price": "price_xxxxxxxxxxxxx"}],
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscriptions",
        )

    def test_subscriptions_post_2(self, request_mock):
        stripe.Subscription.modify(
            "sub_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/subscriptions/sub_xxxxxxxxxxxxx",
        )

    def test_subscriptions_search_get(self, request_mock):
        stripe.Subscription.search(
            query="status:'active' AND metadata['order_id']:'6735'",
        )
        request_mock.assert_requested(
            "get",
            "/v1/subscriptions/search",
        )

    def test_tax_calculations_line_items_get(self, request_mock):
        stripe.tax.Calculation.list_line_items("xxx")
        request_mock.assert_requested(
            "get",
            "/v1/tax/calculations/xxx/line_items",
        )

    def test_tax_calculations_post(self, request_mock):
        stripe.tax.Calculation.create(
            currency="usd",
            line_items=[{"amount": 1000, "reference": "L1"}],
            customer_details={
                "address": {
                    "line1": "354 Oyster Point Blvd",
                    "city": "South San Francisco",
                    "state": "CA",
                    "postal_code": "94080",
                    "country": "US",
                },
                "address_source": "shipping",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/tax/calculations",
        )

    def test_tax_codes_get(self, request_mock):
        stripe.TaxCode.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/tax_codes",
        )

    def test_tax_codes_get_2(self, request_mock):
        stripe.TaxCode.retrieve("txcd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/tax_codes/txcd_xxxxxxxxxxxxx",
        )

    def test_tax_rates_get(self, request_mock):
        stripe.TaxRate.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/tax_rates",
        )

    def test_tax_rates_get_2(self, request_mock):
        stripe.TaxRate.retrieve("txr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/tax_rates/txr_xxxxxxxxxxxxx",
        )

    def test_tax_rates_post(self, request_mock):
        stripe.TaxRate.create(
            display_name="VAT",
            description="VAT Germany",
            jurisdiction="DE",
            percentage=16,
            inclusive=False,
        )
        request_mock.assert_requested(
            "post",
            "/v1/tax_rates",
        )

    def test_tax_rates_post_2(self, request_mock):
        stripe.TaxRate.modify(
            "txr_xxxxxxxxxxxxx",
            active=False,
        )
        request_mock.assert_requested(
            "post",
            "/v1/tax_rates/txr_xxxxxxxxxxxxx",
        )

    def test_tax_transactions_create_from_calculation_post(self, request_mock):
        stripe.tax.Transaction.create_from_calculation(
            calculation="xxx",
            reference="yyy",
        )
        request_mock.assert_requested(
            "post",
            "/v1/tax/transactions/create_from_calculation",
        )

    def test_terminal_configurations_delete(self, request_mock):
        stripe.terminal.Configuration.delete("uc_123")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/uc_123",
        )

    def test_terminal_configurations_delete_2(self, request_mock):
        stripe.terminal.Configuration.delete("tmc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    def test_terminal_configurations_get(self, request_mock):
        stripe.terminal.Configuration.list()
        request_mock.assert_requested(
            "get",
            "/v1/terminal/configurations",
        )

    def test_terminal_configurations_get_2(self, request_mock):
        stripe.terminal.Configuration.retrieve("uc_123")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/configurations/uc_123",
        )

    def test_terminal_configurations_get_3(self, request_mock):
        stripe.terminal.Configuration.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/terminal/configurations",
        )

    def test_terminal_configurations_get_4(self, request_mock):
        stripe.terminal.Configuration.retrieve("tmc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    def test_terminal_configurations_post(self, request_mock):
        stripe.terminal.Configuration.create()
        request_mock.assert_requested(
            "post",
            "/v1/terminal/configurations",
        )

    def test_terminal_configurations_post_2(self, request_mock):
        stripe.terminal.Configuration.modify(
            "uc_123",
            tipping={"usd": {"fixed_amounts": [10]}},
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/configurations/uc_123",
        )

    def test_terminal_configurations_post_3(self, request_mock):
        stripe.terminal.Configuration.create(
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/configurations",
        )

    def test_terminal_configurations_post_4(self, request_mock):
        stripe.terminal.Configuration.modify(
            "tmc_xxxxxxxxxxxxx",
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
        )

    def test_terminal_connection_tokens_post(self, request_mock):
        stripe.terminal.ConnectionToken.create()
        request_mock.assert_requested(
            "post",
            "/v1/terminal/connection_tokens",
        )

    def test_terminal_locations_delete(self, request_mock):
        stripe.terminal.Location.delete("tml_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    def test_terminal_locations_get(self, request_mock):
        stripe.terminal.Location.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/terminal/locations",
        )

    def test_terminal_locations_get_2(self, request_mock):
        stripe.terminal.Location.retrieve("tml_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    def test_terminal_locations_post(self, request_mock):
        stripe.terminal.Location.create(
            display_name="My First Store",
            address={
                "line1": "1234 Main Street",
                "city": "San Francisco",
                "postal_code": "94111",
                "state": "CA",
                "country": "US",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/locations",
        )

    def test_terminal_locations_post_2(self, request_mock):
        stripe.terminal.Location.modify(
            "tml_xxxxxxxxxxxxx",
            display_name="My First Store",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/locations/tml_xxxxxxxxxxxxx",
        )

    def test_terminal_readers_cancel_action_post(self, request_mock):
        stripe.terminal.Reader.cancel_action("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/cancel_action",
        )

    def test_terminal_readers_delete(self, request_mock):
        stripe.terminal.Reader.delete("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    def test_terminal_readers_get(self, request_mock):
        stripe.terminal.Reader.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/terminal/readers",
        )

    def test_terminal_readers_get_2(self, request_mock):
        stripe.terminal.Reader.retrieve("tmr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    def test_terminal_readers_post(self, request_mock):
        stripe.terminal.Reader.create(
            registration_code="puppies-plug-could",
            label="Blue Rabbit",
            location="tml_1234",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers",
        )

    def test_terminal_readers_post_2(self, request_mock):
        stripe.terminal.Reader.modify(
            "tmr_xxxxxxxxxxxxx",
            label="Blue Rabbit",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
        )

    def test_terminal_readers_process_payment_intent_post(self, request_mock):
        stripe.terminal.Reader.process_payment_intent(
            "tmr_xxxxxxxxxxxxx",
            payment_intent="pi_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_payment_intent",
        )

    def test_terminal_readers_process_setup_intent_post(self, request_mock):
        stripe.terminal.Reader.process_setup_intent(
            "tmr_xxxxxxxxxxxxx",
            setup_intent="seti_xxxxxxxxxxxxx",
            customer_consent_collected=True,
        )
        request_mock.assert_requested(
            "post",
            "/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_setup_intent",
        )

    def test_test_helpers_customers_fund_cash_balance_post(self, request_mock):
        stripe.Customer.TestHelpers.fund_cash_balance(
            "cus_123",
            amount=30,
            currency="eur",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/customers/cus_123/fund_cash_balance",
        )

    def test_test_helpers_issuing_authorizations_capture_post(
        self, request_mock
    ):
        stripe.issuing.Authorization.TestHelpers.capture(
            "example_authorization",
            capture_amount=100,
            close_authorization=True,
            purchase_details={
                "flight": {
                    "departure_at": 1633651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1633651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/authorizations/example_authorization/capture",
        )

    def test_test_helpers_issuing_authorizations_expire_post(
        self, request_mock
    ):
        stripe.issuing.Authorization.TestHelpers.expire(
            "example_authorization"
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/authorizations/example_authorization/expire",
        )

    def test_test_helpers_issuing_authorizations_increment_post(
        self, request_mock
    ):
        stripe.issuing.Authorization.TestHelpers.increment(
            "example_authorization",
            increment_amount=50,
            is_amount_controllable=True,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/authorizations/example_authorization/increment",
        )

    def test_test_helpers_issuing_authorizations_post(self, request_mock):
        stripe.issuing.Authorization.TestHelpers.create(
            amount=100,
            amount_details={"atm_fee": 10, "cashback_amount": 5},
            authorization_method="chip",
            card="foo",
            currency="usd",
            is_amount_controllable=True,
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "bar",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "foo",
                "state": "bar",
                "terminal_id": "foo",
            },
            network_data={"acquiring_institution_id": "foo"},
            verification_data={
                "address_line1_check": "mismatch",
                "address_postal_code_check": "match",
                "cvc_check": "match",
                "expiry_check": "mismatch",
            },
            wallet="apple_pay",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/authorizations",
        )

    def test_test_helpers_issuing_authorizations_reverse_post(
        self, request_mock
    ):
        stripe.issuing.Authorization.TestHelpers.reverse(
            "example_authorization",
            reverse_amount=20,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/authorizations/example_authorization/reverse",
        )

    def test_test_helpers_issuing_cards_shipping_deliver_post(
        self, request_mock
    ):
        stripe.issuing.Card.TestHelpers.deliver_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/deliver",
        )

    def test_test_helpers_issuing_cards_shipping_fail_post(self, request_mock):
        stripe.issuing.Card.TestHelpers.fail_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/fail",
        )

    def test_test_helpers_issuing_cards_shipping_return_post(
        self, request_mock
    ):
        stripe.issuing.Card.TestHelpers.return_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/return",
        )

    def test_test_helpers_issuing_cards_shipping_ship_post(self, request_mock):
        stripe.issuing.Card.TestHelpers.ship_card("card_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/cards/card_123/shipping/ship",
        )

    def test_test_helpers_issuing_transactions_create_force_capture_post(
        self, request_mock
    ):
        stripe.issuing.Transaction.TestHelpers.create_force_capture(
            amount=100,
            card="foo",
            currency="usd",
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "US",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "10001",
                "state": "NY",
                "terminal_id": "foo",
            },
            purchase_details={
                "flight": {
                    "departure_at": 1633651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1533651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/transactions/create_force_capture",
        )

    def test_test_helpers_issuing_transactions_create_unlinked_refund_post(
        self, request_mock
    ):
        stripe.issuing.Transaction.TestHelpers.create_unlinked_refund(
            amount=100,
            card="foo",
            currency="usd",
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "bar",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "foo",
                "state": "bar",
                "terminal_id": "foo",
            },
            purchase_details={
                "flight": {
                    "departure_at": 1533651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1533651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/transactions/create_unlinked_refund",
        )

    def test_test_helpers_issuing_transactions_refund_post(self, request_mock):
        stripe.issuing.Transaction.TestHelpers.refund(
            "example_transaction",
            refund_amount=50,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/issuing/transactions/example_transaction/refund",
        )

    def test_test_helpers_refunds_expire_post(self, request_mock):
        stripe.Refund.TestHelpers.expire("re_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/refunds/re_123/expire",
        )

    def test_test_helpers_test_clocks_advance_post(self, request_mock):
        stripe.test_helpers.TestClock.advance(
            "clock_xyz",
            frozen_time=142,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xyz/advance",
        )

    def test_test_helpers_test_clocks_advance_post_2(self, request_mock):
        stripe.test_helpers.TestClock.advance(
            "clock_xxxxxxxxxxxxx",
            frozen_time=1675552261,
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx/advance",
        )

    def test_test_helpers_test_clocks_delete(self, request_mock):
        stripe.test_helpers.TestClock.delete("clock_xyz")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    def test_test_helpers_test_clocks_delete_2(self, request_mock):
        stripe.test_helpers.TestClock.delete("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
        )

    def test_test_helpers_test_clocks_get(self, request_mock):
        stripe.test_helpers.TestClock.list()
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks",
        )

    def test_test_helpers_test_clocks_get_2(self, request_mock):
        stripe.test_helpers.TestClock.retrieve("clock_xyz")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xyz",
        )

    def test_test_helpers_test_clocks_get_3(self, request_mock):
        stripe.test_helpers.TestClock.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks",
        )

    def test_test_helpers_test_clocks_get_4(self, request_mock):
        stripe.test_helpers.TestClock.retrieve("clock_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
        )

    def test_test_helpers_test_clocks_post(self, request_mock):
        stripe.test_helpers.TestClock.create(
            frozen_time=123,
            name="cogsworth",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks",
        )

    def test_test_helpers_test_clocks_post_2(self, request_mock):
        stripe.test_helpers.TestClock.create(frozen_time=1577836800)
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/test_clocks",
        )

    def test_test_helpers_treasury_inbound_transfers_fail_post(
        self, request_mock
    ):
        stripe.treasury.InboundTransfer.TestHelpers.fail(
            "ibt_123",
            failure_details={"code": "account_closed"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/fail",
        )

    def test_test_helpers_treasury_inbound_transfers_return_post(
        self, request_mock
    ):
        stripe.treasury.InboundTransfer.TestHelpers.return_inbound_transfer(
            "ibt_123",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/return",
        )

    def test_test_helpers_treasury_inbound_transfers_succeed_post(
        self, request_mock
    ):
        stripe.treasury.InboundTransfer.TestHelpers.succeed("ibt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/inbound_transfers/ibt_123/succeed",
        )

    def test_test_helpers_treasury_outbound_transfers_fail_post(
        self, request_mock
    ):
        stripe.treasury.OutboundTransfer.TestHelpers.fail("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/fail",
        )

    def test_test_helpers_treasury_outbound_transfers_post_post(
        self, request_mock
    ):
        stripe.treasury.OutboundTransfer.TestHelpers.post("obt_123")
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/post",
        )

    def test_test_helpers_treasury_outbound_transfers_return_post(
        self, request_mock
    ):
        stripe.treasury.OutboundTransfer.TestHelpers.return_outbound_transfer(
            "obt_123",
            returned_details={"code": "account_closed"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/outbound_transfers/obt_123/return",
        )

    def test_test_helpers_treasury_received_credits_post(self, request_mock):
        stripe.treasury.ReceivedCredit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/received_credits",
        )

    def test_test_helpers_treasury_received_debits_post(self, request_mock):
        stripe.treasury.ReceivedDebit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/treasury/received_debits",
        )

    def test_tokens_get(self, request_mock):
        stripe.Token.retrieve("tok_xxxx")
        request_mock.assert_requested(
            "get",
            "/v1/tokens/tok_xxxx",
        )

    def test_tokens_post(self, request_mock):
        stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": "5",
                "exp_year": "2023",
                "cvc": "314",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_tokens_post_2(self, request_mock):
        stripe.Token.create(
            bank_account={
                "country": "US",
                "currency": "usd",
                "account_holder_name": "Jenny Rosen",
                "account_holder_type": "individual",
                "routing_number": "110000000",
                "account_number": "000123456789",
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_tokens_post_3(self, request_mock):
        stripe.Token.create(pii={"id_number": "000000000"})
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_tokens_post_4(self, request_mock):
        stripe.Token.create(
            account={
                "individual": {"first_name": "Jane", "last_name": "Doe"},
                "tos_shown_and_accepted": True,
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_tokens_post_5(self, request_mock):
        stripe.Token.create(
            person={
                "first_name": "Jane",
                "last_name": "Doe",
                "relationship": {"owner": True},
            },
        )
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_tokens_post_6(self, request_mock):
        stripe.Token.create(cvc_update={"cvc": "123"})
        request_mock.assert_requested(
            "post",
            "/v1/tokens",
        )

    def test_topups_cancel_post(self, request_mock):
        stripe.Topup.cancel("tu_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/topups/tu_xxxxxxxxxxxxx/cancel",
        )

    def test_topups_get(self, request_mock):
        stripe.Topup.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/topups",
        )

    def test_topups_get_2(self, request_mock):
        stripe.Topup.retrieve("tu_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/topups/tu_xxxxxxxxxxxxx",
        )

    def test_topups_post(self, request_mock):
        stripe.Topup.create(
            amount=2000,
            currency="usd",
            description="Top-up for Jenny Rosen",
            statement_descriptor="Top-up",
        )
        request_mock.assert_requested(
            "post",
            "/v1/topups",
        )

    def test_topups_post_2(self, request_mock):
        stripe.Topup.modify(
            "tu_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/topups/tu_xxxxxxxxxxxxx",
        )

    def test_transfers_get(self, request_mock):
        stripe.Transfer.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/transfers",
        )

    def test_transfers_get_2(self, request_mock):
        stripe.Transfer.retrieve("tr_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/transfers/tr_xxxxxxxxxxxxx",
        )

    def test_transfers_post(self, request_mock):
        stripe.Transfer.create(
            amount=400,
            currency="usd",
            destination="acct_xxxxxxxxxxxxx",
            transfer_group="ORDER_95",
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers",
        )

    def test_transfers_post_2(self, request_mock):
        stripe.Transfer.modify(
            "tr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/tr_xxxxxxxxxxxxx",
        )

    def test_transfers_reversals_get(self, request_mock):
        stripe.Transfer.list_reversals(
            "tr_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals",
        )

    def test_transfers_reversals_get_2(self, request_mock):
        stripe.Transfer.retrieve_reversal(
            "tr_xxxxxxxxxxxxx",
            "trr_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "get",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
        )

    def test_transfers_reversals_post(self, request_mock):
        stripe.Transfer.create_reversal(
            "tr_xxxxxxxxxxxxx",
            amount=100,
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals",
        )

    def test_transfers_reversals_post_2(self, request_mock):
        stripe.Transfer.modify_reversal(
            "tr_xxxxxxxxxxxxx",
            "trr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
        )

    def test_treasury_credit_reversals_get(self, request_mock):
        stripe.treasury.CreditReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/credit_reversals",
        )

    def test_treasury_credit_reversals_get_2(self, request_mock):
        stripe.treasury.CreditReversal.retrieve("credrev_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/credit_reversals/credrev_xxxxxxxxxxxxx",
        )

    def test_treasury_credit_reversals_post(self, request_mock):
        stripe.treasury.CreditReversal.create(
            received_credit="rc_xxxxxxxxxxxxx",
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/credit_reversals",
        )

    def test_treasury_debit_reversals_get(self, request_mock):
        stripe.treasury.DebitReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/debit_reversals",
        )

    def test_treasury_debit_reversals_get_2(self, request_mock):
        stripe.treasury.DebitReversal.retrieve("debrev_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/debit_reversals/debrev_xxxxxxxxxxxxx",
        )

    def test_treasury_debit_reversals_post(self, request_mock):
        stripe.treasury.DebitReversal.create(received_debit="rd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/debit_reversals",
        )

    def test_treasury_financial_accounts_features_get(self, request_mock):
        stripe.treasury.FinancialAccount.retrieve_features("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
        )

    def test_treasury_financial_accounts_get(self, request_mock):
        stripe.treasury.FinancialAccount.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts",
        )

    def test_treasury_financial_accounts_get_2(self, request_mock):
        stripe.treasury.FinancialAccount.retrieve("fa_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
        )

    def test_treasury_financial_accounts_post(self, request_mock):
        stripe.treasury.FinancialAccount.create(
            supported_currencies=["usd"],
            features={},
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/financial_accounts",
        )

    def test_treasury_financial_accounts_post_2(self, request_mock):
        stripe.treasury.FinancialAccount.modify(
            "fa_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
        )

    def test_treasury_inbound_transfers_cancel_post(self, request_mock):
        stripe.treasury.InboundTransfer.cancel("ibt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx/cancel",
        )

    def test_treasury_inbound_transfers_get(self, request_mock):
        stripe.treasury.InboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/inbound_transfers",
        )

    def test_treasury_inbound_transfers_get_2(self, request_mock):
        stripe.treasury.InboundTransfer.retrieve("ibt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx",
        )

    def test_treasury_inbound_transfers_post(self, request_mock):
        stripe.treasury.InboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            origin_payment_method="pm_xxxxxxxxxxxxx",
            description="InboundTransfer from my bank account",
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/inbound_transfers",
        )

    def test_treasury_outbound_payments_cancel_post(self, request_mock):
        stripe.treasury.OutboundPayment.cancel("bot_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_payments/bot_xxxxxxxxxxxxx/cancel",
        )

    def test_treasury_outbound_payments_get(self, request_mock):
        stripe.treasury.OutboundPayment.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_payments",
        )

    def test_treasury_outbound_payments_get_2(self, request_mock):
        stripe.treasury.OutboundPayment.retrieve("bot_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_payments/bot_xxxxxxxxxxxxx",
        )

    def test_treasury_outbound_payments_post(self, request_mock):
        stripe.treasury.OutboundPayment.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            customer="cus_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            description="OutboundPayment to a 3rd party",
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_payments",
        )

    def test_treasury_outbound_transfers_cancel_post(self, request_mock):
        stripe.treasury.OutboundTransfer.cancel("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx/cancel",
        )

    def test_treasury_outbound_transfers_get(self, request_mock):
        stripe.treasury.OutboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_transfers",
        )

    def test_treasury_outbound_transfers_get_2(self, request_mock):
        stripe.treasury.OutboundTransfer.retrieve("obt_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx",
        )

    def test_treasury_outbound_transfers_post(self, request_mock):
        stripe.treasury.OutboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            amount=500,
            currency="usd",
            description="OutboundTransfer to my external bank account",
        )
        request_mock.assert_requested(
            "post",
            "/v1/treasury/outbound_transfers",
        )

    def test_treasury_received_credits_get(self, request_mock):
        stripe.treasury.ReceivedCredit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_credits",
        )

    def test_treasury_received_credits_get_2(self, request_mock):
        stripe.treasury.ReceivedCredit.retrieve("rc_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_credits/rc_xxxxxxxxxxxxx",
        )

    def test_treasury_received_debits_get(self, request_mock):
        stripe.treasury.ReceivedDebit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_debits",
        )

    def test_treasury_received_debits_get_2(self, request_mock):
        stripe.treasury.ReceivedDebit.retrieve("rd_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/received_debits/rd_xxxxxxxxxxxxx",
        )

    def test_treasury_transaction_entries_get(self, request_mock):
        stripe.treasury.TransactionEntry.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transaction_entries",
        )

    def test_treasury_transaction_entries_get_2(self, request_mock):
        stripe.treasury.TransactionEntry.retrieve("trxne_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transaction_entries/trxne_xxxxxxxxxxxxx",
        )

    def test_treasury_transactions_get(self, request_mock):
        stripe.treasury.Transaction.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transactions",
        )

    def test_treasury_transactions_get_2(self, request_mock):
        stripe.treasury.Transaction.retrieve("trxn_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/treasury/transactions/trxn_xxxxxxxxxxxxx",
        )

    def test_webhook_endpoints_delete(self, request_mock):
        stripe.WebhookEndpoint.delete("we_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "delete",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )

    def test_webhook_endpoints_get(self, request_mock):
        stripe.WebhookEndpoint.list(limit=3)
        request_mock.assert_requested(
            "get",
            "/v1/webhook_endpoints",
        )

    def test_webhook_endpoints_get_2(self, request_mock):
        stripe.WebhookEndpoint.retrieve("we_xxxxxxxxxxxxx")
        request_mock.assert_requested(
            "get",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )

    def test_webhook_endpoints_post(self, request_mock):
        stripe.WebhookEndpoint.create(
            url="https://example.com/my/webhook/endpoint",
            enabled_events=["charge.failed", "charge.succeeded"],
        )
        request_mock.assert_requested(
            "post",
            "/v1/webhook_endpoints",
        )

    def test_webhook_endpoints_post_2(self, request_mock):
        stripe.WebhookEndpoint.modify(
            "we_xxxxxxxxxxxxx",
            url="https://example.com/new_endpoint",
        )
        request_mock.assert_requested(
            "post",
            "/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
        )
