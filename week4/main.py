from math_operations import basic_operations, power_operation, apply_operations

result_basic = basic_operations(6, 3)
print("Basic Operations Result:", result_basic)

result_power = power_operation(6, 2)
print("Power Operation Result:", result_power)

result_power_modulo = power_operation(7, 4, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

operations = [
    (lambda x, y: x + y, (8, 2)),
    (lambda x, y: x * y, (1, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
