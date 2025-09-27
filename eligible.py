
def check_eligibility(subject, marks):
    passing_marks = 40  
    if marks >= passing_marks:
        print(f"The candidate is eligible in {subject}.")
    else:
        print(f"The candidate is not eligible in {subject}.")
subject = input("Enter the subject name: ")
marks = float(input(f"Enter the marks obtained in {subject}: "))
check_eligibility(subject, marks)
