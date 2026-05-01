#file errpr
try:
    file=open("newfile")
    a_dict={"key":"valiue"}
    print(a_dict["fghjk"])
except FileNotFoundError:
    with open("newfile","w") as file:
        file.write("hello")
except KeyError as error_message: #hold the value of error
    print(f"the key {error_message} does not exist")

else:  #only works if except fails ie no error occured
    content=file.read()
    print(content)
finally: #no matter what it runs
    raise KeyError  #raise an error intentionally

