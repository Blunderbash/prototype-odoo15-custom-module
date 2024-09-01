# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.payment.tests.common import PaymentCommon


class StripeCommon(PaymentCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.stripe = cls._prepare_acquirer('stripe', update_values={
            'stripe_secret_key': 'sk_test_key',
            'stripe_publishable_key': 'pk_test_key',
            'stripe_webhook_secret': 'ws_test_key',
            'payment_icon_ids': [(5, 0, 0)],
        })

        cls.acquirer = cls.stripe
