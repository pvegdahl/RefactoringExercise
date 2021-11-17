import pytest

from refactoring_exercise.billing_statement import (
    Play,
    Performance,
    Invoice,
    billing_statement, NoSuchPlayTypeError,
)

PLAYS = {
    "glass": Play(name="The Glass Menagerie", type="tragedy"),
    "noise": Play(name="Noises Off", type="comedy"),
}


def test_tragedy_under_volume_threshold():
    invoice = Invoice(
        customer="ElectricCompany",
        performances=[Performance(play_id="glass", audience=25)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for ElectricCompany
  The Glass Menagerie: $400.00 (25 seats)
Amount owed is $400.00
You earned 0 credits
"""
    )


def test_tragedy_exactly_volume_threshold():
    invoice = Invoice(
        customer="ElectricCompany",
        performances=[Performance(play_id="glass", audience=30)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for ElectricCompany
  The Glass Menagerie: $400.00 (30 seats)
Amount owed is $400.00
You earned 0 credits
"""
    )


def test_tragedy_over_volume_threshold():
    invoice = Invoice(
        customer="ElectricCompany",
        performances=[Performance(play_id="glass", audience=40)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for ElectricCompany
  The Glass Menagerie: $500.00 (40 seats)
Amount owed is $500.00
You earned 10 credits
"""
    )


def test_comedy_under_volume_threshold():
    invoice = Invoice(
        customer="StairMaster",
        performances=[Performance(play_id="noise", audience=17)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for StairMaster
  Noises Off: $351.00 (17 seats)
Amount owed is $351.00
You earned 1 credits
"""
    )


def test_comedy_exactly_volume_threshold():
    invoice = Invoice(
        customer="StairMaster",
        performances=[Performance(play_id="noise", audience=20)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for StairMaster
  Noises Off: $360.00 (20 seats)
Amount owed is $360.00
You earned 2 credits
"""
    )


def test_comedy_exactly_volume_credit_threshold():
    invoice = Invoice(
        customer="StairMaster",
        performances=[Performance(play_id="noise", audience=30)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for StairMaster
  Noises Off: $490.00 (30 seats)
Amount owed is $490.00
You earned 3 credits
"""
    )


def test_comedy_above_both_thresholds():
    invoice = Invoice(
        customer="StairMaster",
        performances=[Performance(play_id="noise", audience=47)],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for StairMaster
  Noises Off: $626.00 (47 seats)
Amount owed is $626.00
You earned 21 credits
"""
    )


def test_multiple_performances():
    invoice = Invoice(
        customer="BigConglomerate",
        performances=[
            Performance(play_id="noise", audience=86),
            Performance(play_id="glass", audience=99),
        ],
    )
    assert (
        billing_statement(invoice=invoice, plays=PLAYS)
        == """Statement for BigConglomerate
  Noises Off: $938.00 (86 seats)
  The Glass Menagerie: $1090.00 (99 seats)
Amount owed is $2028.00
You earned 133 credits
"""
    )


def test_unknown_play_type_raises_exception():
    plays = {"curtains": Play(name="Curtains", type="musical")}
    invoice = Invoice(
        customer="ConfusedCustomer",
        performances=[
            Performance(play_id="curtains", audience=1),
        ],
    )
    with pytest.raises(NoSuchPlayTypeError):
        billing_statement(invoice=invoice, plays=plays)
