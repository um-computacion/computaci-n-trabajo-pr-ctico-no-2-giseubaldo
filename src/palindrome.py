def is_palindrome(text):

    # Limpiar el texto
    cleaned = clean_text(text)

    
    
    if len(cleaned) <= 1:
        return True
    
    # Comparar el texto con su reverso
    return cleaned == cleaned[::-1]

def clean_text(text):
    
    text = text.lower()
    
    # Eliminar todo lo que no sea una letra o un número
    cleaned_text = ''
    for char in text:
        if char.isalnum():  # Verifica si es una letra o un número
            cleaned_text += char

    return cleaned_text

def compare_characters(text):

    return text == text[::-1]