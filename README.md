# findPassword
Finds the correct combination of your master password from an unencoded password phrase. This script has been used to recover my Bitwarden password and only helps if you *remember* your password phrase but *forgot* your one to one encoding combination.
## Requirements
- Bitwarden CLI
```Powershell
# For Windows users using chocolatey package manager
choco install bitwarden-cli
```
Check out this [link](https://github.com/bitwarden/cli) for installation instructions.
## How it works
Let's say your unencoded password phrase is *myBigMasterPassword* and you may have encoded your password phrase with a single encoding combination subset of replacing **s** with **$**. The total number of combinations for this encoding:  
<sup>n</sup>C<sub>0</sub> + <sup>n</sup>C<sub>1</sub> + ... + <sup>n</sup>C<sub>n-1</sub> + <sup>n</sup>C<sub>n</sub> = 2<sup>n</sup>  
   where n = number of **s** present in your passphrase.  
## To Do
- Modify the script for any number of encodings
