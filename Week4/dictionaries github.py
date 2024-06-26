import sys

# List to store loan calculations
loan_calculations = []

def calculate_monthly_instalment(principal, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = loan_term * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment

def calculate_total_amount_payable(monthly_payment, loan_term):
    return monthly_payment * loan_term * 12

def calculate_dsr(monthly_income, monthly_commitments):
    total_commitments = sum(monthly_commitments)
    dsr = (total_commitments / monthly_income) * 100
    return dsr

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate new loan")
        print("2. Display all previous loan calculations")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            principal = float(input("Enter the principal loan amount: "))
            annual_interest_rate = float(input("Enter the annual interest rate: "))
            loan_term = int(input("Enter the loan term in years: "))
            monthly_income = float(input("Enter the applicant's monthly income: "))
            num_commitments = int(input("Enter the number of other monthly financial commitments: "))

            monthly_commitments = []
            for i in range(num_commitments):
                commitment = float(input(f"Enter monthly financial commitment {i + 1}: "))
                monthly_commitments.append(commitment)

            monthly_payment = calculate_monthly_instalment(principal, annual_interest_rate, loan_term)
            total_amount_payable = calculate_total_amount_payable(monthly_payment, loan_term)
            dsr = calculate_dsr(monthly_income, monthly_commitments)

            loan_calculations.append({
                'Principal': principal,
                'Annual Interest Rate': annual_interest_rate,
                'Loan Term': loan_term,
                'Monthly Income': monthly_income,
                'Monthly Commitments': monthly_commitments,
                'Monthly Instalment': monthly_payment,
                'Total Amount Payable': total_amount_payable,
                'DSR': dsr
            })

            print("\nLoan Details:")
            print(f"Monthly Instalment: ${monthly_payment:.2f}")
            print(f"Total Amount Payable: ${total_amount_payable:.2f}")
            print(f"Debt Service Ratio (DSR): {dsr:.2f}%")
            
            if dsr <= 70:
                print("Congratulations! You are eligible for the loan.")
            else:
                print("Sorry, you are not eligible for the loan based on the Debt Service Ratio (DSR).")

        elif choice == '2':
            if not loan_calculations:
                print("No previous loan calculations.")
            else:
                print("\nPrevious Loan Calculations:")
                for index, calculation in enumerate(loan_calculations, start=1):
                    print(f"\nCalculation {index}:")
                    for key, value in calculation.items():
                        print(f"{key}: {value}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()