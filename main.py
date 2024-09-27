
def calc_multiplications(intVal, floatVal):
    result_int_float = int(intVal) * float(floatVal)
    result_int_int = int(intVal) * int(floatVal)

    print(f"{intVal}(int) * {floatVal}(float) = {result_int_float:,} Int * Int = {result_int_int:,}")

calc_multiplications(1683, 9971)
calc_multiplications(2399, 6995)
calc_multiplications(2401, 6997)
calc_multiplications(2797, 5999)
calc_multiplications(2797, -5999)
calc_multiplications(-2797, -5999)
calc_multiplications(3055, 6111)
calc_multiplications(3055, 6995)
