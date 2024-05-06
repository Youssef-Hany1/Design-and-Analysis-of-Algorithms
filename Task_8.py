import random

def find_fake_box(boxes, real_weight, fake_weight):
    total_weight = sum(sum(boxes[i][:i+1]) for i in range(len(boxes)))
    expected_total_weight = real_weight * sum(range(1, len(boxes) + 1))
    weight_difference = expected_total_weight - total_weight
    fake_box_number = weight_difference // (real_weight - fake_weight)
    fake_box_number = max(1, min(fake_box_number, len(boxes)))
    return fake_box_number, real_weight, fake_weight

# Generate random weights for the real and fake metals
weight_of_real_metal = random.randint(2, 100)
weight_of_fake_metal = weight_of_real_metal - 1

# Create 50 boxes, each containing 50 pieces of metal with the real weight
boxes = [[weight_of_real_metal for _ in range(50)] for _ in range(50)]

# Randomly select one box to contain pieces of metal with fake weight
fake_box_index = random.randint(0, 49)
boxes[fake_box_index] = [weight_of_fake_metal for _ in range(50)]

# Find the fake box using the function
fake_box_number, real_weight, fake_weight = find_fake_box(boxes, weight_of_real_metal, weight_of_fake_metal)

# Print the results
print(f"The fake box is box number {fake_box_number}, with fake weight {fake_weight} kg while the real weight is {real_weight} kg")
