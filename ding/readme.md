# File inclusion attacking script-LFI Suite
Using LFI Suite to realise local file inclusion attack

## LFI Suite github
https://github.com/D35m0nd142/LFISuite.git

## Run the programme(on linux)
- first locate to the directory

- run the programme with python  
`python lfisuite.py`

## Some introduciton
- the UI of this tool is well designed. There are two main functions: Exploiter and Scanner.   

The Exploiter aims to get the shell of the targeted web application server. You can choose the method of attack corresponding to the characters including in the targeted URL, or just use "auto-attack" option and try the attack phrases you want(in a .txt file). Some more information may be required for the attack(ex. cookie).  

The Scanner aims to find the feasible attack phrases when given an URL.

## Command to get a reverse shell
- after having a shell of the target web application, enter in a new terminal:  
`nc -lvp 1234`
- enter "reverseshell" in the shell of the target web application, then follow the instruction. 



