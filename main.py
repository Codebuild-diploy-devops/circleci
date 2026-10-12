def convert_to_uppercase(text: str) -> str:
    """Converts a given string to uppercase."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()

if __name__ == "__main__":
    sample_text = "hello world"
    result = convert_to_uppercase(sample_text)
    print(f"Original: {sample_text}")
    print(f"Uppercase: {result}")
