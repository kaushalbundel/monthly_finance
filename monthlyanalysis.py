
from Analysis import money_in, money_out, summary, withdrawl_analysis, others_analysis
from Preprocessing import data_preprocessing

file=input("Please enter the name of the file ")
data=data_preprocessing(file)

money_in=money_in(data)
money_out=money_out(data)
withdrawl_analysis=withdrawl_analysis(data)
others_analysis=others_analysis(data)
summary=summary(data)

#printing information
print(" \n INCOME REPORT \n *************************\n")
print(" \n The total deposit for this month are: \n --------------------------- \n", money_in[0])
print(" \n The Incomes for this month came from: \n --------------------------- \n", money_in[1])
print(" \n EXPENSE REPORT \n *************************\n")
print(" \n The total expenses for this month are: \n --------------------------- \n", money_out[0])
print(" \n The top 10 expenses for this month are: \n --------------------------- \n", money_out[1])
print(" \n WITHDRAWL REPORT \n *************************\n")
print(" \n The top withdrawls(category wise) for this month are: \n --------------------------- \n", withdrawl_analysis)
print(" \n OTHER REPORT \n ---------------------------\n",others_analysis)
print(" \n Monthly Summary \n *************************\n")
if summary>0:
    print("The Monthly Profit is: ", summary)
    print("\n Keep it up !!")
else:
    print("The Monthly Loss is: ", summary)
    print("\n You can do better!!")


#if __name__=='__main__':
#    main()

