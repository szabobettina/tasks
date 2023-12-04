from typing import NamedTuple

Coupon = NamedTuple("Coupon", [("store", str), ("product", str), ("discount", int)])

def line_to_coupon(line):
    tokens = line.split(";")
    return Coupon(tokens[0], tokens[1], int(tokens[2]))

def distinct_stores(coupons):
    d_s = set()
    for coupon in coupons:
        d_s.add(coupon.store)
    return d_s

def main():
    coupons = []
    while True:
        line = input()
        if line == "END":
            break
        coupons.append(line_to_coupon(line))

    d_s = distinct_stores(coupons)
    for s in d_s:
        print(s)

from src import prog_test_v2

if __name__ == "__main__":
    main()
    #prog_test_v2.test()