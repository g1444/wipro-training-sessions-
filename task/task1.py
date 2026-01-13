def num_students(a, b, c, d, e, f, g):
    """
    Calculates and prints the number of students in each region of a
    3-subject Venn diagram (English, Maths, Science).

    Parameters:
    a : students studying English
    b : students studying Maths
    c : students studying Science
    d : students studying English & Science
    e : students studying English & Maths
    f : students studying Maths & Science
    g : total students (each studies at least one subject)

    Output:
    Prints counts in a single line in the order:
    Only English, Only Maths, Only Science,
    English & Maths only, English & Science only,
    Maths & Science only, All three
    """

  
    # All values must be within the allowed range
    values = [a, b, c, d, e, f, g]
    if not all(1 <= x <= 10000 for x in values):
        print("Invalid input")
        return

    # Pairwise intersections cannot exceed individual subject counts
    if d > min(a, c) or e > min(a, b) or f > min(b, c):
        print("Invalid input")
        return

    # Total students must be logically valid
    if g < max(a, b, c) or g > (a + b + c):
        print("Invalid input")
        return

    # ---------- CORE CALCULATION ----------
    # Inclusion–Exclusion Principle to find students studying all 3 subjects
    all_three = g - (a + b + c) + (d + e + f)

    # Ensure no negative count
    all_three = max(0, all_three)

    # Students studying exactly two subjects
    eng_math = max(0, e - all_three)
    eng_sci = max(0, d - all_three)
    math_sci = max(0, f - all_three)

    # Students studying exactly one subject
    only_eng = max(0, a - (eng_math + eng_sci + all_three))
    only_math = max(0, b - (eng_math + math_sci + all_three))
    only_sci = max(0, c - (eng_sci + math_sci + all_three))

    # ---------- OUTPUT ----------
    # Print all results in a single line (judge / industry friendly)
    print(
        only_eng,
        only_math,
        only_sci,
        eng_math,
        eng_sci,
        math_sci,
        all_three
    )
