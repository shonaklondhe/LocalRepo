from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Tip Calculator")
root.geometry("750x600+50+50")
f = ("century", 17, "bold")
ft = ("Airal", 30, "bold")

def calculate():

	bill = entBill.get()
	tip = entTip.get() 
	person = entPeople.get()

	try :
		bill = float(bill)
		if not bill < 10000.0 or bill < 0.0 :
			showerror("Invalid input", "bill must be between 0 to 10000.")
			return

		tip = float(tip)
		if not tip < 100.0 or bill < 0.0 :
			showerror("Invalid input", "tip must be between 0 to 100.0")
			return


		person = int(person)
		if not person < 10.0 or person < 1.0 :
			showerror("Invalid input", "persons must be from 1 to 10.0")
			return

		calculated_tip = tip / 100
		calculated_tip = round(calculated_tip, 2)
		total_bill = bill + (bill * calculated_tip)
		total_bill = round(total_bill, 2)
		tip_per_person = (bill * calculated_tip) / person
		tip_per_person = round(tip_per_person, 2)
		Total_PerPp2 = total_bill / person
		Total_PerPp2 = round(Total_PerPp2, 2)

		labBill_amount2.configure(text = bill)
		labBill_WithTip2.configure(text= total_bill)
		labTip_PerPerson2.configure(text= tip_per_person)
		labTotal_PerPp2.configure(text= Total_PerPp2)

	except Exception as e:
		# =======================bill EXCEPTIONS===========================
		if not bill :
			showerror("Invalid input","bill amount cannot be empty")
		elif not str(bill).replace(".", "").isdigit():
			showerror("Invalid input","bill amount cannot contain text, special characters, spaces or negative no.")


		#=======================tip EXCEPTIONS=============================

		if not tip :
			showerror("Invalid input","tip amount cannot be empty")

		elif not str(tip).replace(".", "").isdigit():
			showerror("Invalid input","tip amount cannot contain text, special characters, spaces or negative no.")

		# =======================no of people EXCEPTIONS===========================
		if not person :
			showerror("Invalid input","person must be atleast 1")
		elif not str(person).replace(".", "").isdigit():
			showerror("Invalid input","person  cannot contain text, special characters, spaces or negative no.")


def clr():
	entBill.delete(0, END)
	entTip.delete(0, END)
	entPeople.delete(0, END)
	entBill.focus()

labTitle = Label(root, text="Tip calculator", font=ft, fg="green")
labTitle.pack(pady=10)
labBill = Label(root, text="Bill", font=f)
labBill.place(x=20 ,y=100)
labTip = Label(root, text="Tip%", font=f)
labTip.place(x=20 ,y=170)
labPeople = Label(root, text="Number of People", font=f)
labPeople.place(x=20 ,y=240)

labBill_amount = Label(root, text="Bill Amount" + "\n" + "\u20b9" , font=f, bg="grey12", fg="white", width=10, height=2)
labBill_amount.place(x=10 ,y=370)
labBill_amount2 = Label(root, font=f, bg="grey81", width=10, height=3)
labBill_amount2.place(x=10 ,y=435)

labBill_WithTip = Label(root, text="Bill With Tip" + "\n" + "\u20b9" , font=f, bg="grey12", fg="white", width=11, height=2)
labBill_WithTip.place(x=170 ,y=370)
labBill_WithTip2 = Label(root, font=f, bg="grey81", width=11, height=3)
labBill_WithTip2.place(x=170 ,y=435)

labTip_PerPerson = Label(root, text="Tip Per-Person" + "\n" + "\u20b9" , font=f, bg="grey12", fg="white", width=12, height=2)
labTip_PerPerson.place(x=346 ,y=370)
labTip_PerPerson2 = Label(root, font=f, bg="grey81", width=12, height=3)
labTip_PerPerson2.place(x=346 ,y=435)

labTotal_PerPpl = Label(root, text="Total Per-People" + "\n" + "\u20b9" , font=f, bg="grey12", fg="white", width=13, height=2)
labTotal_PerPpl.place(x=538 ,y=370)
labTotal_PerPp2 = Label(root, font=f, bg="grey81", width=13, height=3)
labTotal_PerPp2.place(x=538 ,y=435)

entBill = Entry(root, font=f)
entBill.place(x=250 ,y=100)
entTip = Entry(root, font=f)
entTip.place(x=250 ,y=170)
entPeople = Entry(root, font=f)
entPeople.place(x=250 ,y=240)

btnCalculate = Button(root, text="Calculate", font=f, bg="green", fg="white", width=8, command=calculate)
btnCalculate.place(x=270 ,y=300)
btnClear = Button(root, text="Clear", font=f, bg="green", fg="white", width=4, command=clr)
btnClear.place(x=410 ,y=300)

root.mainloop()