Rivest-Shamir-Adleman (RSA) is an encoding and decoding algorithm used for document encryption. RSA encryption happens when the algorithm generates public and private keys to cipher and decipher text. 
To cipher text, the public keys are used. Each letter is converted to ascii integers, and encoded using the public keys with modular arithmetic. 
Anyone with the public key can encode messages, but only users who have the private key can decode the message.

To decode messages, modular arithmetic is preformed on the encoded message and the modular inverse, private key. 
My implementation serves as a model of RSA, but is not secure. 
The project can be improved by using larger integers to use in key generation, and combine encoded letters into one string or groups of string. 
The next step would be to improve how keys are generated. I do not handle negative keys well. 
To fix the bug, I would need to calculate another, positive modular multiplicative inverse. 

This repo uses a Main function. 
I have comments and doc strings in each function to better explain what is happening in my implementation of RSA cryptography below.
When using this program as top leve, the user will input a message and the application will produce the encoded list of characters. 
To check that the message can be decoded, a call to the decoding function is made and the decoded message is outputted to the command line.

By calling the main function I have created the program entry point. This project is a python module I have written. 
The last if statement, found at the bottom of the code cell below, is a call to run the applicaiton if this application is top level code. 
This If statement prevents my module from being unintentionally run in the future and when imported to a different application.

The if statement looks like this:

if __name__ == "__main__": 
main()

In conclusion, this repo has helped me develop my coding skills by forcing me to use basic agile development principles. 

