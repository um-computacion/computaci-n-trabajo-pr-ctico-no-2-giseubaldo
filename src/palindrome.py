def is_palindrome(text):

    # Limpiar el texto
    cleaned = clean_text(text)

    
    
    if len(cleaned) <= 1:
        return True
    
    # Comparar el texto con su reverso
    return cleaned == cleaned[::-1]