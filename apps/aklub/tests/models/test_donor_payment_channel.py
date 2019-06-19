# -*- coding: utf-8 -*-

# Author: Petr Dlouhý <petr.dlouhy@auto-mat.cz>
#
# Copyright (C) 2017 o.s. Auto*Mat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
import datetime

from django.test import TestCase

from freezegun import freeze_time

from model_mommy import mommy
from model_mommy.recipe import Recipe

from ..utils import ICON_FALSE


@freeze_time("2010-5-1")
class TestNoUpgrade(TestCase):
    """ Test TerminalCondition.no_upgrade() """

    def setUp(self):
        self.donor_payment_channel = Recipe(
            "aklub.DonorPaymentChannel",
            campaign__name="Foo campaign",
            user__first_name="Foo user",
        )

    def test_not_regular(self):
        """ Test DonorPaymentChannel with regular_payments=False returns False """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="onetime",
        )
        self.assertEqual(
            donor_payment_channel.no_upgrade,
            False,
        )

    def test_not_regular_for_one_year(self):
        """ Test DonorPaymentChannel that is not regular for at leas one year """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="regular",
        )
        self.assertEqual(
            donor_payment_channel.no_upgrade,
            False,
        )

    def test_no_last_year_payments(self):
        """ Test DonorPaymentChannel that has zero payments from last year """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="regular",
            payment_set=[
                mommy.make("Payment", date=datetime.date(year=2010, month=4, day=1)),
            ],
        )
        donor_payment_channel.save()
        self.assertEqual(
            donor_payment_channel.no_upgrade,
            False,
        )

    def test_missing_payments(self):
        """ Test DonorPaymentChannel that has different amount on payments before one year """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="regular",
            payment_set=[
                mommy.make("Payment", date=datetime.date(year=2010, month=4, day=1), amount=100),
                mommy.make("Payment", date=datetime.date(year=2009, month=3, day=1), amount=200),
            ],
        )
        donor_payment_channel.save()
        self.assertEqual(
            donor_payment_channel.no_upgrade,
            False,
        )

    def test_regular(self):
        """ Test DonorPaymentChannel that has regular payments """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="regular",
            payment_set=[
                mommy.make("Payment", date=datetime.date(year=2010, month=4, day=1), amount=100),
                mommy.make("Payment", date=datetime.date(year=2009, month=3, day=1), amount=100),
            ],
        )
        donor_payment_channel.save()
        self.assertEqual(
            donor_payment_channel.no_upgrade,
            True,
        )


@freeze_time("2016-6-1")
class TestExtraMoney(TestCase):
    """ Test TerminalCondition.extra_money() """

    def setUp(self):
        self.donor_payment_channel = Recipe(
            "aklub.DonorPaymentChannel",
            campaign__name="Foo campaign",
            user__first_name="Foo user",
        )

    def test_extra_payment(self):
        """ Test DonorPaymentChannel with extra payment """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_amount=100,
            regular_payments="regular",
            regular_frequency="monthly",
            payment_set=[
                mommy.make("Payment", date=datetime.date(year=2016, month=5, day=5), amount=250),
            ],
        )
        donor_payment_channel.save()
        self.assertEqual(donor_payment_channel.extra_money, 150)
        self.assertEqual(donor_payment_channel.extra_payments(), "150&nbsp;Kč")

    def test_payment_too_old(self):
        """ Test that if the payment is older than 27 days, it is not counted in  """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_amount=100,
            regular_payments="regular",
            regular_frequency="monthly",
            payment_set=[
                mommy.make("Payment", date=datetime.date(year=2016, month=5, day=4), amount=250),
            ],
        )
        donor_payment_channel.save()
        self.assertEqual(donor_payment_channel.extra_money, None)
        self.assertEqual(donor_payment_channel.extra_payments(), ICON_FALSE)

    def test_no_extra_payment(self):
        """ Test DonorPaymentChannel with extra payment """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_amount=100,
            regular_payments="regular",
            regular_frequency="monthly",
        )
        donor_payment_channel.save()
        self.assertEqual(donor_payment_channel.extra_money, None)
        self.assertEqual(donor_payment_channel.extra_payments(), ICON_FALSE)

    def test_no_frequency(self):
        """ Test DonorPaymentChannel with no regular frequency """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_amount=100,
            regular_payments="regular",
            regular_frequency=None,
        )
        donor_payment_channel.save()
        self.assertEqual(donor_payment_channel.extra_money, None)
        self.assertEqual(donor_payment_channel.extra_payments(), ICON_FALSE)

    def test_not_regular(self):
        """ Test when DonorPaymentChannel is not regular """
        donor_payment_channel = self.donor_payment_channel.make(
            regular_payments="onetime",
        )
        self.assertEqual(donor_payment_channel.extra_money, None)
        self.assertEqual(donor_payment_channel.extra_payments(), ICON_FALSE)


class TestNameFunctions(TestCase):
    """ Test DonorPaymentChannel.person_name(), DonorPaymentChannel.__str__() """

    def setUp(self):
        self.donor_payment_channel = mommy.make(
            "aklub.DonorPaymentChannel",
            event__name="Foo campaign",
            user__last_name="User 1",
            user__first_name="Test",
            user__email="test@test.com",
            VS=1234,
        )

    def test_user_person_name(self):
        self.assertEqual(self.donor_payment_channel.person_name(), 'User 1 Test')

    def test_str(self):
        self.assertEqual(self.donor_payment_channel.__str__(), 'Payment channel: test@test.com - 1234')