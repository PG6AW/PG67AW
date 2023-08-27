import math
import tkinter as tk

def if_is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2,int(math.pow(num,.5))+1):
        if num % i == 0:
            return False
    return True

def showprime():
    n1 = lower_bound_entry.get()
    n2 = upper_bound_entry.get()
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        output_label.config(text="Please Enter a Correct Number without ambiguous characters!")
        return
    
    if n1 > n2:
        n1, n2 = n2, n1
    
    list1 = []
    for number in range(n1, n2 + 1):
        if if_is_prime(number):
            list1.append(int(number))
    
    if len(list1) > 0:
        output_label.config(text="Here's a list of all prime integers within the bound interval as follows: " + str(list1))
    else:
        output_label.config(text="NO PRIME NUMBER WITHIN THE GIVEN RANGE!")

def check_prime():
    n3 = prime_entry.get()
    try:
        n3 = int(n3)
    except ValueError:
        prime_output_label.config(text="Please enter an integer and try again!")
        return
    
    if if_is_prime(n3):
        prime_output_label.config(text=f"('{n3}') is Prime!")
    else:
        prime_output_label.config(text=f"('{n3}') Ain't Prime!")

root = tk.Tk()
root.configure(bg='purple')
root.title("Prime Number Calculator")

lower_bound_label = tk.Label(root, text="Lowermost bound of calculation range:")
lower_bound_label.configure(bg="blue")
lower_bound_label.pack()
lower_bound_entry = tk.Entry(root)
lower_bound_entry.configure(bg="yellow")
lower_bound_entry.pack()

upper_bound_label = tk.Label(root, text="Uppermost bound of calculation range:")
upper_bound_label.configure(bg="blue")
upper_bound_label.pack()
upper_bound_entry = tk.Entry(root)
upper_bound_entry.configure(bg="yellow")
upper_bound_entry.pack()

show_prime_button = tk.Button(root, text="Show Prime Numbers", command=showprime)
show_prime_button.configure(bg="green")
show_prime_button.pack()

output_label = tk.Label(root)
output_label.configure(bg="orange")
output_label.pack()

overkill_label = tk.Label(root, text="Would you like to check if a specific number is prime?")
overkill_label.configure(bg="blue")
overkill_label.pack()
overkill_var = tk.StringVar(root, value="N")
overkill_radiobutton1 = tk.Radiobutton(root, text="Yes", variable=overkill_var, value="Y")
overkill_radiobutton1.configure(bg="red")
overkill_radiobutton1.pack()
overkill_radiobutton2 = tk.Radiobutton(root, text="No", variable=overkill_var, value="N")
overkill_radiobutton2.configure(bg="red")
overkill_radiobutton2.pack()

prime_label = tk.Label(root, text="Enter the number to know if it's prime or not:")
prime_label.configure(bg="blue")
prime_label.pack()
prime_entry = tk.Entry(root)
prime_entry.configure(bg="yellow")
prime_entry.pack()

check_prime_button = tk.Button(root, text="Check Prime", command=check_prime)
check_prime_button.configure(bg="green")
check_prime_button.pack()

prime_output_label = tk.Label(root)
prime_output_label.configure(bg="orange")
prime_output_label.pack()

root.mainloop()
