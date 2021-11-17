from refactoring_exercise.billing_statement import (
    Play,
    Performance,
    Invoice,
    billing_statement,
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
  The Glass Menagerie: $400.0 (25 seats)
Amount owed is $400.0
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
  The Glass Menagerie: $400.0 (30 seats)
Amount owed is $400.0
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
  The Glass Menagerie: $500.0 (40 seats)
Amount owed is $500.0
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
  Noises Off: $351.0 (17 seats)
Amount owed is $351.0
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
  Noises Off: $360.0 (20 seats)
Amount owed is $360.0
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
  Noises Off: $490.0 (30 seats)
Amount owed is $490.0
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
  Noises Off: $626.0 (47 seats)
Amount owed is $626.0
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
  Noises Off: $938.0 (86 seats)
  The Glass Menagerie: $1090.0 (99 seats)
Amount owed is $2028.0
You earned 133 credits
"""
    )
