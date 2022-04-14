file1=open("sample1.txt","r")
data_a= file1.read()
print(data_a)
file2=open("sample2.txt","r")
data_b= file2.read()
print(data_b)

file1 = open("sample1.txt","w")#write mode
file1.write(data_b)
file1.close()

file2=open("sample2.txt","w")
file2.write(data_a)
file2.close()


