
def read_values(entry):
    try:
        text = entry.get().replace(",", ".")
        value = float(text)
        if value > 0 :
            return value       
    except ValueError:
        return None