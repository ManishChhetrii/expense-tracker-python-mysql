import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expensetracker"
)

cursor = conn.cursor()

print("EXPENSE TRACKER!")

while True:

    menu=input(  "1: Add Expense\n 2: View Expense\n 3: Total \n 4: Delete \n 5: Exit \n Choose: ") 
    if menu=="1":
        amount= input("Enter your amount here: ")
        category= input("Enter category: ")
        note= input("Enter Note:")

        query = "INSERT INTO expenses (amount, category, note) VALUES (%s, %s, %s)"
        values = (amount, category, note)
        cursor.execute(query, values)
        conn.commit()
    
    if menu =="2":
        cursor.execute("SELECT * FROM expenses")
        data = cursor.fetchall()
        for row in data:
            print(row)
    
    if menu=="3":
        cursor.execute("SELECT SUM(amount) FROM expenses")
        result= cursor.fetchone()
        if result[0] is None:
            print("No expense yet")
        else:
            print("Total Spending: ", result[0])

    elif menu=="4":
        delete= int(input("Enter iD to delete:"))
        query2="DELETE FROM expenses WHERE id= %s"
        value2= (delete,)
        cursor.execute(query2, value2)
        conn.commit()
        print("Expense deleted")

    elif menu=="5":
        print("Thank You.")   
        break   
    else:
        print("Wrong input, Thank You.")
