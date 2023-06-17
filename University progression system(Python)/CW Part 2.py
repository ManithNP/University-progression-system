# I declare that my work contains no examples of misconduct, such as plagiarism,collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: …20210457…………………..… 
 
# Date: ……1\12\…2021……………..…


#Student version

credit_names_list=['pass','defer','fail']
credit_list=["not_set","not_set","not_set"]

def check_valid(position):
    is_not_valid = True

    while is_not_valid:
        x=input("Please enter your credits at "+credit_names_list[position]+"\t: ")
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

credit_list[0] = check_valid(0)
credit_list[1] = check_valid(1)
credit_list[2] = check_valid(2)

if credit_list[0]==120:
    print("Progress")
elif credit_list[0]==100:
    print("Progress (module trailer)")
elif credit_list[0]==80 or credit_list[0]==60:
    print("Do not Progress - module retriever")
elif credit_list[0]==40:
    if credit_list[1]==0:
        print("Exclude")
    else:
        print("Do not Pragress - module retriever")
elif credit_list[0]==20:
    if credit_list[1]==0 or credit_list[1]==20:
        print("Exclude")
    else:
        print("Do not Pragress - module retriever")
else:
    if credit_list[1]==0 or credit_list[1]==20 or credit_list[1]==40:
        print("Exclude")
    else:
        print("Do not Pragress - module retriever")
