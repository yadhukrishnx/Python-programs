# Creating a file
filename1=open("samplefile.txt","w") 
fname1=filename1.name
print("Filename::",fname1)
content=""" This is a sample file operation example and here the file is accessed in write mode and contents are added This is a sample file operation example and here the file is accessed in write mode and contents are added . in this mode ov
erwriting of contents may happen"""
# filename1.write(input("Enter the contents for file file ")) 
filename1.write(content) 

#Opening that file 
filename1=open("samplefile.txt","r") # opening file A Read mpde
content=filename1.read() # reading file contents to a variable called content
print("Contents : ",content)

# Appending 