# Student: Imesha Piyumali, ID: u3305049, Date: 17.09.2025

#Case Study 3 — Boolean Circuit Equivalence

#IMPORTANT NOTICE X= a CIRCUIT
#Y= b CIRCUIT


#Circuit Outputs
def circuit_outputs(A: int, B: int, C: int):
    # Complements
    A_ = 1 - A
    B_ = 1 - B
    C_ = 1 - C


#IMPORTANT NOTICE X= a CIRCUIT
#Y= b CIRCUIT

    
    # Circuit X: (A * C * B) + ((A' * C')' * A * B')
    part1 = A and C and B
    part2 = (not (A_ and C_)) and A and B_
    X = int(part1 or part2)

    # Circuit Y: A * (B' + C)
    Y = int(A and (B_ or C))

    return X, Y
#IMPORTANT NOTICE X= a CIRCUIT
#Y= b CIRCUIT

if __name__ == "__main__":
    print("Enter values for A, B, C (0 or 1). Type 'q' to quit.")
    while True:
        user_input = input("A B C: ").strip()
        if user_input.lower() == "q":
            print("Exiting!!!")
            break
        try:
            A_str, B_str, C_str = user_input.split()
            A, B, C = int(A_str), int(B_str), int(C_str)
            if A not in [0,1] or B not in [0,1] or C not in [0,1]:
                raise ValueError
            X, Y = circuit_outputs(A, B, C)
            print(f"Inputs: A={A}, B={B}, C={C} => X={X}, Y={Y}")
        except ValueError:
            print("Invalid Input here. Please enter three values (0 or 1), separated with spaces.")
            
#IMPORTANT NOTICE X= a CIRCUIT
#Y= b CIRCUIT
