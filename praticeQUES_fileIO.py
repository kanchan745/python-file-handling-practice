f = open("pratice.txt","w")
f.write("Hii everyone\n We re learning File I/O \n")
f.write ("using Java .\n like programming in Java...")

'''waf that replace occurance of java with python in above file'''

'''f = open("pratice.txt","r")
data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)'''

'''with open ("pratice.txt",'w')as f:
    f.write(new_data)#for over write....'''
   
    
    
# word = 'learning'    
# with open ("pratice.txt", 'r') as f:
#     data = f.read()
    
#     if (data.find(word)!= -1):
#         print("found")
        
#     else:
#         print("not found")    


'''WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD learning OCCUR FIRST PRINT -1 IF WORD NOT FOUND'''

# def check_for_word():
#     word = 'learning'
#     with open("pratice.txt","r")as f:
#         data = f.read()
#         if (word in data):
#             print("found")
            
#         else:
#             print("not found")
            
#passe = type casting 
'''count = 0           
with open("File_i/Pratiice_no.txt",'r')as f:
    data= f.read() 
    
    nums = data.split(",")
    for val in nums:
        if (int(val)%2 == 0):
            count+= 1
    print(count) '''        
    
    
    
    # num = ''
    # for i in range(len(data)):
    #     if (data[i]==','):
    #         print(int(num))
    #         num = ''
    #     else:
    #         num += data[i]        
        
                