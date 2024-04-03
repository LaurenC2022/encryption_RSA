# Conversions Tool Set 

def Convert_Text(_string):
    """
    Take in a simple string such as "hello" and outputs the corresponding
    standard list of integers (ascii) for each letter in the word hello.
    
    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    """
    integer_list = []
    
    # convert each letter to an ascii integer and add it to integer_list 
    for letter in _string: 
        k = ord(letter)
        integer_list.append(k)
        
    # Each element in integer_list is 1 letter from the original string
    return integer_list

def Convert_Num(_list):
    """
    Takes in a list of ascii integers
    and outputs the corresponding string.
    
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
    _string = ''
    
    # convert each ascii integer to a letter and add it to string 
    for i in _list:
        _string += chr(i)
        
    return _string

def Convert_Binary_String(_int):
    """
    Converts an integer to it's binary expansion as a string.
    
    For example:
    _int = 345
    bits = "101011001"
    """
    d = _int
    
    if d == 0: 
        return "0"
    
    result = []  
    x_located = False
    x = 0 
    lg_exp = 0

    # count number of 1's and 0's found in given number's binary conversion 
    while (x_located == False):
        if (d - 2**x) > 0:  
            x += 1

        elif (d - 2**x) == 0: 
            lg_exp = x
            x_located = True

        else: 
            lg_exp = x - 1
            x_located = True 

    # fill an array with the correct number of elements to represent given 
    # number 
    for num in range(lg_exp+1): 
        result.append(0)
      
    # Replace 0's with 1's in the correct placement for the binary expantion 
    # for the given integer
    for num in range(lg_exp+1):
        if d - 2**lg_exp > - 1: 
            result[num] = 1
            d = d - 2**lg_exp
            
        lg_exp -= 1
       
    bits = ""
    
    # convert binary integer list to a string 
    for elem in result:
        bits = bits + str(elem)
    
    return bits

# Number Theory Tool Set 

def FME(b, n, m):

    """
    Use fast modular exponentiation algorithm to calculate 
    b^n mod m and return its value
    
    For example:
    
    b = 20
    n = 345
    m = 235
    
    n(base 2) = "101011001"
    
    n = 345 = 256 + 64 + 16 + 8 + 1 
    
    b^n mod m = 20^345 % 235
    
    Remember exponent addition rule: (2^i)*(2^j) = 2^(i+j)
    
    20^345 = 20^(256) * 20^(64) * 20^(16) * 20^(8) * 20^(1)

    Use modular theorem of multiplication:
    
    x = 20^345 % 235 
= ((20^256 % 235)*(20^64 % 235)*(20^16 % 235)*(20^8 % 235)*(20^1 % 235))%235
    
    x = 140
    """
    
    x = 1 
 
    #power is accumulator to find b^(2^i)%m on each pass in for loop
    power = b % m 
    
    #convert n to binary to use as i in the exponent 2^i
    a = Convert_Binary_String(n)
    a = a[::-1] #flip binary string to have least significant digit at a[0] 
    
    #for each digit in the flipped binary form of n
    for i in range(len(a)):
        # if digit is included in binary (ie is a 1), 
        # then calculate 2^i mod m 
        if int(a[i]) == 1:
            
            # Use modular theorem of multiplication:
            # (x1*x2*x3)%m = ((((x1%m)(x2%m))%m)*(x3%m))%m 
    
            x = (x * power)%m
            
        power =  (power*power)%m
    
    return x 

def Euclidean_Alg(a, b):
    """
    Calculate Greatest Common Divisor (gcd) of a and b and return 
    a single integer ('x') which is the gcd of a and b. This 
    algorithm uses the Euclidean algorithm found in number theory 
    to find the gcd.
    
    For example: 
    
    a = 6
    b = 9
    
    b = a(q) + k 
    9 = 6(q) + k 
    9 = 6(1) + 3 << k = 3
    6 = 3(3) + 0 << because k = 0 here, 
                    we know the previous k = 3 is the gcd for 9 and 6 
    
    gcd(a, b) = 3
    
    """
    
    m_ = a
    n_ = b 
    
    while(n_ > 0): 
        
        #update the values for Euclidean algorithm: m_ = n_(q)+k
        k = m_ % n_
        q = m_ // n_
        m_ = n_ 
        n_ = k 
        
        
    return m_

# Key Generating Tool Set 

def Find_Public_Key_e(p, q):
    """
    It takes two primes p and q, where p*q>150, 
    and return two elements as follows:
    
    public key: n
    public key: e
    
    For example: 
    p = 23
    q = 31
    
    (e, n) = (7, 713)
    """

    n = p*q
    t = (p-1)*(q-1)
    
    e = 2 
    
    gcd = Euclidean_Alg(e, t)
    
    # find new e until conditions are met: 
    #     1. check that the n and e are relatively prime, 
    #        gcd(e, n) should return 1 if they are relatively prime 
    #     2. check e is not equal to p or q

    gcd_is_not_1 = (gcd != 1) # should be false to meet conditions
    p_is_e = p == e # should be false to meet conditions
    q_is_e = q == e # should be falseto meet conditions
    
    # conditions_are should be false
    # if any of the conditions are true the conditions_are will be true 
    # and a new e will be found 
    conditions_are = gcd_is_not_1 or p_is_e or q_is_e 
    
    while conditions_are == True:  
        e += 1
         
        gcd = Euclidean_Alg(e, t)
        
        gcd_is_not_1 = gcd != 1 # should be false
        p_is_e = p == e # should be false
        q_is_e = q == e # should be false
    
        conditions_are = gcd_is_not_1 or p_is_e or q_is_e # should be false 
    
    return (e, n)

def Find_Private_Key_d(e, p, q):
    """
    Using extended euclidean algorithm, find the decryption exponent d, 
    such that d is the modular inverse of e

    example: 
    e, p, q = 7, 23, 31 
    
    d = 283
    """
    
    m_ = e 
    n_ = (p-1)*(q-1)
    s1_t1 = (1, 0)
    s2_t2 = (0, 1)
    
    while(n_ > 0): 
        
        # update the values for Euclidean algorithm: 
        # m_ = n_(q)+k and m mod n 
        k = m_ % n_
        q = m_ // n_
        m_ = n_ 
        n_ = k 
        
        #calculate Bezout coefficient, gcd(m_, n_) = s1*(m_) + t1*(n_) 
        s1_t1_hat = s2_t2
        s2_t2_hat = (s1_t1[0]-(q*s2_t2[0]),s1_t1[1]-(q*s2_t2[1]))
        s1_t1 = s1_t1_hat
        s2_t2 = s2_t2_hat
    
    d = s1_t1[0]
    
    return d

# Encode and Decode Tools 

def Encode(n, e, message):
    """
    Message is a string. Encode each letter in message using n, e and
    return the encoded cipher_text.
    
    For example: 
    (e, n) = (7, 713) 
    
    Message = "Hello world!"
    
    cipher_text = [485, 188, 271, 271, 567, 280, 
                    491, 567, 321, 271, 679, 221]
    """
    
    message_ascii = Convert_Text(message)
    cipher_text = []
    
    for i in range(len(message_ascii)):
        
        # encoding equation is cipher_text = (message ^e) mod n 
        encode_char = FME(message_ascii[i], e, n)
        cipher_text.append(encode_char)
        
    return cipher_text

def Decode(n, d, cipher_text):
    """
    Decrypt each integer using n and d.
    Recover the original message as a string. 
    
    For example: 
    d = 283
    n = 713
    cipher_text = [485, 188, 271, 271, 567, 280, 491, 567, 
                    321, 271, 679, 221]
    
    message = "Hello world!"
    """
    message = ''
    decode_list = []
    
    for i in range(len(cipher_text)):
        
        # decoded message to ascii 
        # decoding equation is message = (cipher_text^d) mod n
        decode_number = FME(cipher_text[i], d, n)
        decode_list.append(decode_number)
    
    #convert ascii characters to string of letters
    message = Convert_Num(decode_list) 
    
    return message

# Custom Feature Main Function: 

def main(): 
    """
    In this main function I am writing top level code.
    Top level code is code defined within the file it is used. 
    No imports are used
    
    This main function is a command line application. 
    It is used to encrypt and decrypt messages
    """
    
    active_user = "1" 
    print("Hello user")
    print("p is preset to the value of 13")
    print("q is preset to the value of 37")
    
    p = 13 
    q = 37
    
    en = Find_Public_Key_e(p, q)
    e = en[0] 
    n = en[1] 
    d = Find_Private_Key_d(e, p, q) 
    
    print("For p = 13, and q = 37")
    print("e: ", e)
    print("n: ", n)
    print("d: ",  d)
    
    while active_user == "1": 
        message = input("What message would you like to encoded?")
        cipher_text = Encode(n, e, message)
        print(" ")
        print("Your encoded message is: ", cipher_text)
        print(" ")
        
        decoded_text = Decode(n, d, cipher_text)
        print(" ")
        print("Message after decoding: ", decoded_text)
        print(" ")
                
        active_user = input("Would you like to encode another message? (Please enter 1 for 'yes' or 0 for 'no')")
        print(" ")
        print(" ")
        
# Calling main function & program entry point: 
# This entire cell of code, including all functions, are a python module 
# I have written. 
# The below if statement is a call to run the applicaiton if this 
# application is top level code.
# The If statement below prevents this module from being unintentionally 
# running if imported and resued in a different application

if __name__ == "__main__": 
    main()
