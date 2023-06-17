# I declare that my work contains no examples of misconduct, such as plagiarism,collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: …20210457…………………..… 
 
# Date: ……3\12\…2021……………..…

   #Staff version

credit_names_list=['Pass','Deffer','Fail']
credit_list=["not_set","not_set","not_set"]

def check_valid(position):
    is_not_valid = True

    while is_not_valid:
        x=input("Enter your total "+credit_names_list[position]+" credits : ")
        try:
            x=int(x)
            range_values=[0,20,40,60,80,100,120]
            if x not in range_values:
                print("Out of range\n")
                continue
            else:
                if position==2:
                    y = credit_list[0] + credit_list[1] + x
                    if y!=120:
                        print("Total incorrect\n")
                        continue
                    else:
                        is_not_valid = False
                else:
                    is_not_valid = False
        
        except:
            print("Integer Required\n")
            continue


    return x

def outcome():
    credit_list[0] = check_valid(0)
    credit_list[1] = check_valid(1)
    credit_list[2] = check_valid(2)

    if credit_list[0]==120:
        return "Progress",1
    elif credit_list[0]==100:
        return "Progress (module trailer)",2
    elif credit_list[0]==80 or credit_list[0]==60:
        return "Module retriever",3
    elif credit_list[0]==40:
        if credit_list[1]==0:
            return "Exclude",4
        else:
            return "Module retriever",3
    elif credit_list[0]==20:
        if credit_list[1]==0 or credit_list[1]==20:
            return "Exclude",4
        else:
            return "Module retriever",3
    else:
        if credit_list[1]==0 or credit_list[1]==20 or credit_list[1]==40:
            return "Exclude",4
        else:
            return "Module retriever",3

def outcome_counting(n):
    global progress_count,trailer_count,retriever_count,excluded_count
    if n==1:
        progress_count += 1
    elif n==2:
        trailer_count += 1
    elif n==3:
        retriever_count += 1
    else:
        excluded_count += 1

print("Staff Version with Histogram\n")

count = 1
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

result = outcome()
print(result[0]+"\n")
outcome_counting(result[1])

multiple = True

while multiple:
    print("Would you like to enter another set of data?")
    a=input("Enter 'y' for yes or 'q' to quit and view results: ")
    print("")
    if a=='y':
        count += 1
        result = outcome()
        print(result[0]+"\n")
        outcome_counting(result[1])
    else:
        multiple = False
        print('-'*60)
        print("Horizontal Histogram")
        print("Progress %d\t: " %(progress_count) + '*'*progress_count)
        print("Trailer %d\t: " %(trailer_count) + '*'*trailer_count)
        print("Retriever %d\t: " %(retriever_count) + '*'*retriever_count)
        print("Excluded %d\t: " %(excluded_count) + '*'*excluded_count)
        print("")
        print("%d outcomes in total." %(count))
        print('-'*60)

