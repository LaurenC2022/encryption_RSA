# Rivest-Shamir-Adleman Algorithm

Rivest-Shamir-Adleman (RSA) is an encoding and decoding algorithm used for document encryption. 

- [Overview](#overview)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

RSA encryption happens when the algorithm generates public and private keys to cipher and decipher text. 
To cipher text, the public keys are used. Each letter is converted to ascii integers, and encoded using the public keys with modular arithmetic. 
Anyone with the public key can encode messages, but only users who have the private key can decode the message.

To decode messages, modular arithmetic is preformed on the encoded message and the modular inverse, private key. 
My implementation serves as a model of RSA, but is not secure. 

The project can be improved by using larger integers to use in key generation, and combine encoded letters into one string or groups of string. 

## My process

### Built with 

- Python 

### What I learned 

I learned the math behind the RSA algorithm, considered time, space complexity, and basic agile development. The RSA algorithm uses modular inverses as keys to encode and decode messages. It also uses the euclidean algorithm. I learned to do the arithmatic on paper and then coded this RSA software to preform these arithmetic calculations. The time and space complexity is much better due to fast modular exponentiation. That is using base 2 conversion to calculate modular arithmetic. The pow() function is an example of fast modular exponentiation in python. This repo has helped me develop my coding skills by forcing me to use basic agile development principles like get it working and keep it working.

I learned all of these topics for the first time while working on this project and I enjoyed learning and building this project.

### Continued development

The next step would be to improve how keys are generated. I do not handle negative keys well. To fix the bug, I would need to calculate another, positive modular multiplicative inverse. To do this, I should remember: a and b are modularly congruent if and only if m divides a-b. (page 609 of BOOK: Discrete Mathematics and Its Application by Kenneth H. Rosen) 

I could also add pictures and more examples to this readme file. 

## Author

- Website - [Lauren Collins](https://www.LaurenCollins.dev)


## Acknowledgments

I build this project as part of a university assignment. The name of the project and university have been omited per professor's instructions. 