def calculate_paracetamol_volume(weight, strength):
    valid_strengths = [120, 250]
    if not (10 <= weight <= 100):
        raise ValueError("Weight should be between 10 and 100 kg")
    if strength not in valid_strengths:
        raise ValueError("Invalid paracetamol strength. Expected 120 mg/5 ml or 250 mg/5 ml")
    recommended_dose = 15  # mg/kg
    required_dose = weight * recommended_dose
    if strength == 120:
        volume = (required_dose / 120) * 5
    else:
        volume = (required_dose / 250) * 5
    return volume

# 函数调用示例
try:
    weight = 20  # 假设体重为20kg
    strength = 120  # 假设药物浓度为120mg/5ml
    result = calculate_paracetamol_volume(weight, strength)
    print(f"The required volume of paracetamol is {result} ml")
except ValueError as e:
    print(e)