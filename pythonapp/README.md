this python app was created to be a solution in case we fail in the main_app(web application)
this tkinter windows allow you to create and connect branches only and generate the code c# and we can also add a button that allow you to generate the dll code by using this python script :

    import subprocess
    # Read the C# code from the text file
	with open("code.txt", "r") as text_file:
	    code = text_file.read()
	# Write the C# code to a new file with the .cs extension
	with open("code.cs", "w") as code_file:
	    code_file.write(code)
	# Compile the C# code to a DLL using the C# compiler (csc.exe)
	subprocess.run(["csc", "/target:library", "code.cs"])
	# The DLL file will be created in the same directory as the C# code file
