def remove_bracket_algebra_eqs(equestion):
    all_brackets="(){}[]"
    for bracket in equestion:
        if bracket in all_brackets:
            equestion=equestion.replace(bracket,"")
    return equestion

equestion=input("Enter an algebraic equation:")
print("the equation after removing all brackets is:",remove_bracket_algebra_eqs(equestion))