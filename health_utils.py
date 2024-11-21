def calculate_bmi(height, weight):
    """Calculer l'Indice de Masse Corporelle (BMI)."""
    try:
        return round(weight / (height ** 2), 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def calculate_bmr(height, weight, age, gender):
    """Calculer le Métabolisme de Base (BMR) en fonction de l'équation de Harris-Benedict."""
    try:
        if gender.lower() == 'male':
            return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
        elif gender.lower() == 'female':
            return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
        else:
            return "Invalid gender"
    except Exception as e:
        return str(e)
