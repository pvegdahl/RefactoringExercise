import math
from typing import Dict, NamedTuple, List


class Play(NamedTuple):
    name: str
    type: str


class Performance(NamedTuple):
    play_id: str
    audience: int


class Invoice(NamedTuple):
    customer: str
    performances: List[Performance]


def billing_statement(invoice: Invoice, plays: Dict[str, Play]):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice.customer}\n"

    for performance in invoice.performances:
        play = plays[performance.play_id]
        if play.type == "tragedy":
            this_amount = 40000
            if performance.audience > 30:
                this_amount += 1000 * (performance.audience - 30)
        elif play.type == "comedy":
            this_amount = 30000
            if performance.audience > 20:
                this_amount += 10000 + 500 * (performance.audience - 30)
            this_amount += 300 * performance.audience
        else:
            raise Exception(f"Unknown play type: {play.type}")

        # Add volume credits
        volume_credits += max(0, performance.audience - 30)
        # And extra for every ten comedy attendees
        if play.type == "comedy":
            volume_credits += math.floor(performance.audience / 10)

        # Add the line for this order
        result += f"  {play.name}: ${(this_amount / 100):.2f} ({performance.audience} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is ${(total_amount / 100):.2f}\n"
    result += f"You earned {volume_credits} credits\n"

    return result
