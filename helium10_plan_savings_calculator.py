#!/usr/bin/env python3
"""
Helium 10 Subscription Savings & Promo Code Calculator 2026.
"""
import argparse

PLANS = {
    "starter": {"monthly": 39.0, "annual": 348.0},
    "platinum": {"monthly": 99.0, "annual": 948.0},
    "diamond": {"monthly": 279.0, "annual": 2748.0}
}

def calculate(plan, months, coupon):
    p = PLANS.get(plan.lower(), PLANS["platinum"])
    if coupon == "annual":
        annual_total = p["annual"]
        equiv_monthly = annual_total / 12.0
        savings = (p["monthly"] * 12.0) - annual_total
        print("=" * 60)
        print(f"Helium 10 Annual Plan Calculator - Plan: {plan.upper()}")
        print("=" * 60)
        print(f"Annual Prepaid Total:    ${annual_total:.2f}/year")
        print(f"Effective Monthly Cost:  ${equiv_monthly:.2f}/month")
        print(f"Annual Savings vs Month: ${savings:.2f}/year")
        print("=" * 60)
        return equiv_monthly
    elif coupon == "20off6":
        first_6 = p["monthly"] * 0.80 * min(6, months)
        remaining = p["monthly"] * max(0, months - 6)
        total = first_6 + remaining
        savings = (p["monthly"] * months) - total
        print("=" * 60)
        print(f"Helium 10 20% Off 6 Months Calculator - Plan: {plan.upper()}")
        print("=" * 60)
        print(f"Evaluation Period:       {months} months")
        print(f"Total Spend:             ${total:.2f}")
        print(f"Total Coupon Savings:    ${savings:.2f}")
        print("=" * 60)
        return total
    else:
        total = p["monthly"] * months
        print(f"Standard Spend: ${total:.2f}")
        return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Helium 10 Calculator")
    parser.add_argument("--plan", default="platinum", choices=["starter", "platinum", "diamond"])
    parser.add_argument("--months", type=int, default=12)
    parser.add_argument("--coupon", default="annual", choices=["annual", "20off6", "none"])
    args = parser.parse_args()
    calculate(args.plan, args.months, args.coupon)
