
Data_Flow = ["Tampering", "Information", "Disclosure"]
Data_Store =  ["Tampering", "Information", "Disclosure"]
Interactor = ["Spoofing", "Repudiation"]
Process = ["Spoofing","Tampering", "Repudiation", "Information", "Disclosure" "Repudiation"]
MultiProcess = ["Spoofing","Tampering", "Repudiation", "Information", "Disclosure" "Repudiation"]

x = "What is the SYMBOL: "

print("Choose the DFD symbol: \n")
print("1 --> Data Flow")
print("2 --> Data Store")
print("3 --> Interactor")
print("4 --> Process")
print("5 --> Multiprocess \n")

threat = int(input(x))
if threat == 1:
    print("For a Data Flow these are the threat types: \n")
    print(Data_Flow)

elif threat == 2:
    print("For a Data Store these are the threat types: \n")
    print(Data_Store)

elif threat == 3:
    print("For an INTERACTOR  these are the threat types: \n")
    print(Interactor)

elif threat == 4:
    print("For a PROCESS these are the threat types: \n " )
    print(Process)

elif threat == 5:
    print("For a MULTIPROCESS these are the threat types:\n ")
    print(MultiProcess)

else:
    print("This is the end")
