import myfunction as r
import function as f

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : "))

print("Enter elements :")
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst)

print("\nOpersstion : \n 0.All  \n 1.Mean \n 2.Median \n 3.Mode \n 4.Mid Range \n 4.Variance \n 5.Staderd Deviation")
key=input("Enter Operation \n")

print("Operation using User Defined Function :\n")
if key == '0':
    r.mean(lst)
    r.median(lst)
    r.mr(lst)
    r.variance(lst)
    r.sd(lst)
    r.mode(lst)
    f.mode(lst)
    
elif key=='1':
    r.mean(lst)
elif key=='2':
    r.median(lst)
elif key=='3':
    r.mode(lst)
    f.mode(lst)
elif key=='4':
    r.mr(lst)
elif key=='5':
    r.var(lst)
elif key=='':
    r.sd(lst)
else:
    print("Wrong Input")
        
    


print("\nOperation using Library Defined Function :\n")

f.mean(lst)
f.median(lst)
f.variance(lst)
f.sd(lst)
f.mode(lst)
