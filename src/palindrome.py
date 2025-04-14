def is_palindrome(palabra:str) -> bool:  
    palabra = palabra.replace(" ", "").lower().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")