import random

class CouponCollector:
    @staticmethod
    def generate_random_coupon(n):
        return random.randint(1, n)
    
    @staticmethod
    def collect_coupons(n):
        coupons_collected = set()
        random_numbers_generated = 0

        while len(coupons_collected) < n:
            new_coupon = CouponCollector.generate_random_coupon(n)
            random_numbers_generated += 1
            coupons_collected.add(new_coupon)
        
        return random_numbers_generated


n = int(input("Enter the number of distinct coupon numbers: "))

total_random_numbers_needed = CouponCollector.collect_coupons(n)
print(f"Total random numbers needed to collect all distinct coupons: {total_random_numbers_needed}")
