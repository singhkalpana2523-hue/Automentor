def analyze_code(code):
    issues = []

    # Empty or very small code
    if len(code.strip()) < 20:
        issues.append("Code is too short to analyze properly")

    # Iteration over non-iterable
    if "for" in code and "in" in code:
        if "range" not in code and "[" not in code:
            issues.append("Loop may be iterating over a non-iterable object")

    # Overwriting built-in functions
    if "sum =" in code:
        issues.append("Built-in function 'sum' is overwritten")

    if "list =" in code or "dict =" in code:
        issues.append("Built-in data type name is overwritten")

    # Missing output
    if "print(" not in code and "return" not in code:
        issues.append("No output or return statement found")

    # Infinite loop risk
    if "while" in code and "print" in code and "break" not in code:
        issues.append("Possible infinite loop detected")

    # Comparison vs assignment mistake
    if "if" in code and " =" in code and "==" not in code:
        issues.append("Possible assignment used instead of comparison in condition")

    return issues
