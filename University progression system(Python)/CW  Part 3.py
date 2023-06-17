# I declare that my work contains no examples of misconduct, such as plagiarism,collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: …20210457…………………..… 
 
# Date: ……7\12\…2021……………..…

   


 #Full code

f=open("Output.txt","w")

credit_names_list=['Pass','Deffer','Fail']
credit_list=["not_set","not_set","not_set"]

def check_valid(position):
    is_not_valid = True

    while is_not_valid:
        x=input("Enter your total "+credit_names_list[position]+" credits : ")
        try:            #check wether the input value is an integer
            x=int(x)
            range_values=[0,20,40,60,80,100,120] #check the range
            if x not in range_values:
                print("Out of range\n")
                continue
            else:
                if position==2:
                    y = credit_list[0] + credit_list[1] + x   #Adding the credit values 0f pass defer and fail
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
        return "Progress",1,credit_list
    elif credit_list[0]==100:
        return "Progress (module trailer)",2,credit_list
    elif credit_list[0]==80 or credit_list[0]==60:
        return "Module retriever",3,credit_list
    elif credit_list[0]==40:
        if credit_list[1]==0:
            return "Exclude",4,credit_list
        else:
            return "Module retriever",3,credit_list
    elif credit_list[0]==20:
        if credit_list[1]==0 or credit_list[1]==20:
            return "Exclude",4,credit_list
        else:
            return "Module retriever",3,credit_list
    else:
        if credit_list[1]==0 or credit_list[1]==20 or credit_list[1]==40:
            return "Exclude",4,credit_list
        else:
            return "Module retriever",3,credit_list

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
out_list=[]

result = outcome()
print(result[0]+"\n")
outcome_counting(result[1])
out=result[0]+" - %d, %d, %d" %(result[2][0],result[2][1],result[2][2])
out_list.append(out)

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
        out=result[0]+" - %d, %d, %d" %(result[2][0],result[2][1],result[2][2])
        out_list.append(out)
    elif a=='q':
        multiple = False
        counts=[progress_count, trailer_count, retriever_count, excluded_count]
        print('-'*60)
        print("")
        print("Horizontal Histogram")
        print("Progress %d\t: " %(counts[0]) + '*'*counts[0])
        print("Trailer %d\t: " %(counts[1]) + '*'*counts[1])
        print("Retriever %d\t: " %(counts[2]) + '*'*counts[2])
        print("Excluded %d\t: " %(counts[3]) + '*'*counts[3])
        print("")
        print("%d outcomes in total.\n" %(count))
        print('-'*60)

        print("")
        print("Vertical Histogram")
        print("Progress\tTrailer \tRetriever\tExcluded")
        for i in range(1,max(counts)+1):
            a=" "
            b=" "
            c=" "
            d=" "
            if i<=counts[0]:
                a='*'
            if i<=counts[1]:
                b='*'
            if i<=counts[2]:
                c='*'
            if i<=counts[3]:
                d='*'
            print("    %s\t\t   %s\t\t    %s\t\t   %s" %(a,b,c,d))
        print("\n"+'-'*60)

        print("")
        for i in range(len(out_list)):
            print(out_list[i])
            f.write(out_list[i]+"\n")
        print("")
        print('-'*60)
        
f.close()
