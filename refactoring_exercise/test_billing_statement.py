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

def test_true():
    assert True


# Tests
# Comedy
#   Less than 20
#   Exactly 20
#   More than 20
#   More than 30
# Both
# Volume credits
