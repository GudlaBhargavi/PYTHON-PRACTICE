def is_rotation(s1, s2):
    # Lengths must be equal and not empty
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    
    # Check if s2 is substring of s1 + s1
    return s2 in (s1 + s1)


# Example usage
s1 = "abcd"
s2 = "cdab"

if is_rotation(s1, s2):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")