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


def test_true():
    assert True


# Tests
# Tragedy
#   Less than 30
#   Exactly 30
#   More than 30
# Comedy
#   Less than 20
#   Exactly 20
#   More than 20
#   More than 30
# Both
# Volume credits
