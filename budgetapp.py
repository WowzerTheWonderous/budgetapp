import csv
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import pyperclip as pc
from tkinter.messagebox import askyesno, askquestion
import datetime
from os.path import exists

file_exists = exists("bills.csv")
if (file_exists == False):
    f = open("bills.csv", "x")
    billFields = ['Service', 'Amount', 'Date']
    billList = 'bills.csv'
    with open(billList, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(billFields)

else:
    pass

billFields =['Service', 'Amount', 'Date']
billList = 'bills.csv'
billData = []
content = u'\N{COPYRIGHT SIGN}'.encode('utf-8')
text = content.decode('utf-8')
serviceList = ['Mortgage', 'Honda', 'Electric', 'Gas', 'Sewer', 
'Water', 'Phone', 'Internet', 'Hospital', 'Sweetwater', 
'Student Loans', 'Spotify', 'Disney+', 'Discovery+', 'Paramount+', 
'Netflix']
class App:

    def mainApp():
        app = Tk()
        app.geometry("800x800")
        app.title("Bill Keyper by MathiesenWare.com")
                
        appFrame = Frame(
            app, 
            bg="black")
        appFrame.config(
            width="800", 
            height="800")
        appFrame.pack()

        appHeaderFrame = Frame(
            appFrame, 
            bg="black")
        appHeaderFrame.place(
            x=0, 
            y=0, 
            anchor=NW)
        appHeaderFrame.config(
            width="800", 
            height="100")

        appHeader = Label(
            appHeaderFrame, 
            text="Bill Keyper\nBy MathiesenWare.com", 
            bg="black", 
            fg="white")
        appHeader.place(
            relx=0.5, 
            x=0, 
            y=0, 
            anchor=N)

        appFooterFrame = Frame(
            appFrame, 
            bg="black")
        appFooterFrame.config(
            width="800", 
            height="55")
        appFooterFrame.place(
            relx=0.5, 
            rely=0.9, 
            x=0, 
            y=0, 
            anchor=N)

        appFooter = Label(
            appFooterFrame, 
            text=f"Copyright: {text} 2022 - Joseph T. Mathiesen @ " +
            "www.mathiesenware.com",
            bg="black", 
            fg="white")
        appFooter.place(
            relx=0.5, 
            x=0,
            rely=0.5, 
            y=10, 
            anchor=S)

        def mainMenu():

            def goToCurBills():
                mainFrame.destroy()
                curBillsView()
            
            def goToNxtBills():
                mainFrame.destroy()
                nxtBillsView()
            
            def goToAddBills():
                mainFrame.destroy()
                addBillsView()
            
            def goToCalendar():
                mainFrame.destroy()
                calendarView()
            
            def quitProgram():
                confirmation = askyesno(
                    title="Confirmation",
                    message = "Are you sure you want to quit?")
                if confirmation:

                    app.destroy()
            
            mainFrame = Frame(
                appFrame, 
                bg="#fbfbfb")
            mainFrame.config(
                width=800, 
                height=350)
            mainFrame.place(
                x=0, 
                y=270, 
                anchor=W)

            mainOptionsFrame = Frame(
                mainFrame, 
                bg="black")
            mainOptionsFrame.place(
                x=0, 
                y=0, 
                anchor=NW)
            mainOptionsFrame.config(
                width=800, 
                height=350)

            mainOptionsHeader = Label(
                mainOptionsFrame, 
                text="Please select an option", 
                bg="black", 
                fg="white")
            mainOptionsHeader.place(
                relx=0.5, 
                x=0, 
                y=25, 
                anchor=N)

            #Options
            #Option 1: View This Month's Bills
            viewCurMonth = Button(
                mainOptionsFrame, 
                text="View Current Month's Bills", 
                bg="#90EE90", 
                fg="black", 
                width=50, 
                command=goToCurBills)
            viewCurMonth.place(
                relx=0.5, 
                x=0, 
                rely=0.3, 
                anchor=CENTER)
            #Option 2: View Next Month's Bills
            viewNxtMonth = Button(
                mainOptionsFrame,
                text="View Next Month's Bills",
                bg="#90EE90",
                fg="black", 
                width=50, 
                command=goToNxtBills)
            viewNxtMonth.place(
                relx=0.5, 
                x=0, 
                rely=0.4, 
                anchor=CENTER)
            #Option 3: Add Bill
            addBillBtn = Button(
                mainOptionsFrame, 
                text="Add a Bill", 
                bg="#90EE90", 
                fg="black", 
                width=50, 
                command=goToAddBills)
            addBillBtn.place(
                relx=0.5, 
                x=0, 
                rely=0.5, 
                anchor=CENTER)
            #Option 4: View Calendar
            viewCalendarBtn = Button(
                mainOptionsFrame, 
                text="View Calendar", 
                bg="#90EE90", 
                fg="black", 
                width=50, 
                command=goToCalendar)
            viewCalendarBtn.place(
                relx=0.5, 
                x=0, 
                rely=0.6, 
                anchor=CENTER)
            #Option 5: Quit Program
            quitProgramBtn = Button(
                mainOptionsFrame, 
                text="Quit Program", 
                bg="#90EE90", 
                fg="#000000", 
                width=50, 
                command=quitProgram)
            quitProgramBtn.place(
                relx=0.5, 
                x=0, 
                rely=0.7, 
                anchor=CENTER)

        def curBillsView():
            def goToMainMenu():
                with open(billList, 'w', newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                billDataFrame.destroy()
                initializeBillSheet()
                with open(billList, 'r', newline="") as csvfile:
                    csvreader = csv.reader(csvfile)
                    for row in csvreader:
                        billData.clear()
                curBills.destroy()
                mainMenu()

            curBills = Frame(appFrame)
            curBills.config(
                bg="#ffffff", 
                width="795", 
                height="325")
            curBills.pack()

            curBillsHeader = Label(
                curBills, 
                text="Bills This Month")
            curBillsHeader.config(
                bg="#000000", 
                fg="#ffffff")
            curBillsHeader.place(
                relx=0.5, 
                x=0, 
                rely=0.1, 
                y=0, 
                anchor=N)

            billDataFrame = Frame(curBills, relief="raised", 
                bg="black")
            billDataFrame.config(width=700, height=700)
            billDataFrame.place(relx=0.5, rely=0.5, x=0, y=0, 
                anchor=CENTER)

            billTable = ttk.Treeview(billDataFrame)

            billTable['columns'] = ['Service', 'Amount', 'Date']

            billTable.column("#0", width=0, stretch=NO)
            billTable.column("Service", anchor=CENTER, width=155)
            billTable.column("Amount", anchor=CENTER, width=155)
            billTable.column("Date", anchor=CENTER, width=155)

            billTable.heading("#0", text="", anchor=CENTER)
            billTable.heading("Service", text="Service", 
                anchor=CENTER)
            billTable.heading("Amount", text="Amount", anchor=CENTER)
            billTable.heading("Date", text="Date", anchor=CENTER)

            for i in range(len(billData)):
                billTable.insert(parent='', index='end', iid=i, 
                    text='', values=(billData[i]))

            billTable.pack()
            clearButton = Button(curBills, text="Clear Bill Data", 
                bg="#90EE90", fg="#000000")
            clearButton.place(relx=0.2, rely=0.9, anchor=CENTER)

            mainMenuButton = Button(curBills, text="Main Menu", 
                bg="#90EE90", fg="#000000")
            mainMenuButton.place(relx=0.5, rely=0.9, anchor=CENTER)


        def nxtBillsView():
            def goToMainMenu():
                nxtBills.destroy()
                mainMenu()
            nxtBills = Frame(appFrame)
            nxtBills.config(
                bg="white", 
                width="795", 
                height="325")
            nxtBills.pack()

            nxtBillsHeader = Label(nxtBills, 
                text="Next Months Bills")
            nxtBillsHeader.config(
                bg="white", 
                fg="black")
            nxtBillsHeader.place(
                relx=0.5, 
                x=0, 
                rely=0.1, 
                y=0, 
                anchor=N)

        def addBillsView():
            def goToMainMenu():
                addBills.destroy()
                mainMenu()
            
            def showNewBill():
                def addNewBillToBillSheet(service, amount, date):
                    itemData = [service, amount, date]
                    with open(billList, 'r', newline="") as csvfile:
                        csvreader = csv.reader(csvfile)
                    billData.clear()
                    billData.append(itemData)
                    billAmountEntry.delete(0, END)
                    with open(billList, 'a', newline="") as csvfile:   
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerows(billData)
                    newBillFrame.destroy()

                newBillFrame = Frame(addBills, bg="#000000")
                newBillFrame.place(x=0, y=290, anchor=W)
                newBillFrame.config(width=800, height=100)

                newBillServiceHidden = Label(newBillFrame, 
                    text=f"{serviceEntry.get()}")
                newBillService = Label(newBillFrame, 
                    text=f"Service: {newBillServiceHidden.cget('text')}",
                     bg="#000000", fg="#ffffff")
                newBillService.place(rely=0.65, anchor=SW)

                newBillAmountHidden = Label(newBillFrame, 
                    text=f"{billAmountEntry.get()}")
                newBillAmount = Label(newBillFrame, 
                    text=f"Amount: {newBillAmountHidden.cget('text')}", 
                    bg="#000000", fg="#ffffff")
                newBillAmount.place(rely=0.65, anchor=SW)

                newBilllDateHidden = Label(newBillFrame, 
                    text=f"{billDateEntry.get()}")
                newBillDate = Label(newBillFrame, 
                    text=f"Date: {newBillDateHidden.cget('text')}", 
                    bg="#000000", fg="#ffffff")
                newBillDate.place(rely=0.8, anchor=SW)

                addNewBillData = Button(newBillFrame, text="Add Bill", 
                    bg="#90EE90", fg="#000000", 
                    command=lambda: addNewBillToBillSheet
                    (str(newBillServiceHidden.cget('text')),
                    str(newBillAmountHidden.cget('text')), 
                    str(newBilllDateHidden.cget('text'))))
                addNewBillData.place(relx=0.8, rely=0.8, anchor=SW)                 

            addBills = Frame(appFrame)
            addBills.config(
                bg="#000000", 
                width=800, 
                height=350)
            addBills.place(
                x=0, 
                y=270, 
                anchor=W)

            addBillsHeader = Label(
                addBills, 
                text="Add a Bill")
            addBillsHeader.config(
                bg="#000000", 
                fg="#ffffff")
            addBillsHeader.place(
                relx=0.5, 
                x=0, 
                rely=0.1, 
                y=0, 
                anchor=N)
            
            addFormFrame = Frame(
                addBills,
                bg="#000000")
            addFormFrame.place(
                x=0, 
                y=0, 
                anchor=NW)
            addFormFrame.config(
                width=800,
                height=350)
            
            addFormHeader = Label(
                addFormFrame, 
                text="Please fill out the form", 
                bg="#000000", 
                fg="#ffffff")
            addFormHeader.place(
                relx=0.5, 
                x=0, 
                y=25, 
                anchor=N)
            
            # Form

            #Service Field
            serviceEntryLabel = Label(
                addFormFrame, 
                text="Service", 
                bg="#000000", 
                fg="#ffffff")
            serviceEntryLabel.place(
                relx=0.15, 
                rely=0.2, 
                anchor=CENTER)
            value_inside = StringVar(app)
            serviceEntry = OptionMenu(
                addFormFrame,
                value_inside,
                *serviceList, 
                )
            serviceEntry.place(
                relx=0.5, 
                rely=0.2, 
                anchor=W)

            #Amount Field
            billAmountEntryLabel = Label(
                addFormFrame, 
                text="Enter Amount Due", 
                bg="#000000", 
                fg="#ffffff")
            billAmountEntryLabel.place(
                relx=0.15, 
                rely=0.4, 
                anchor=CENTER)

            billAmountEntry = Entry(
                addFormFrame, 
                width=25)
            billAmountEntry.place(
                relx=0.5, 
                rely=0.4, 
                anchor=W)

            #Date Due
            billDateEntryLabel = Label(
                addFormFrame, 
                text="Due Date", 
                bg="#000000", 
                fg="#ffffff")
            billDateEntryLabel.place(
                relx=0.15, 
                rely= 0.6, 
                anchor=CENTER)

            billDateEntry = DateEntry(
                addFormFrame, 
                selectmode='day',
                width=25)
            billDateEntry.place(
                relx=0.5, 
                rely=0.6, 
                anchor=W)

            addBillBtn = Button(
                addFormFrame, 
                text="Add Bill", 
                command=showNewBill
                )
            addBillBtn.place(
                relx=0.5, 
                rely=0.8, 
                anchor=CENTER)
            
        def calendarView():
            calFrame = Frame(appFrame)
            calFrame.config(
                bg="white",
                width="495",
                height="325")
            calFrame.pack()

            calHeader = Label(
                calFrame, 
                text="Calendar")
            calHeader.config(
                bg="white", 
                fg="black")
            calHeader.place(
                relx=0.5,
                x=0, 
                rely=0.1, 
                y=0, 
                anchor=N)           
        def goToMainMenu():
                calFrame.destroy()
                mainMenu()

        mainMenu()
        app.mainloop()
App.mainApp()