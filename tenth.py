alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
want_e_or_d = input('type e for encryption and d for decryption: ')
shift_key = input('type shift key: ')
value = input('type value: ')
E_result=''
if want_e_or_d == 'e':
    for alphabet in value:
        if alphabet == ' ':
            E_result += ' '
        else:


            x = alphabets.index(alphabet)
            n = int(shift_key)
            E = (x + n) % 26
            E_result += alphabets[E]
    print(f'the encryption result is {E_result}')
else:
    for alphabet in value:
        if alphabet == ' ':
            E_result += ' '
        else:
            x = alphabets.index(alphabet)
            n = int(shift_key)
            E = (x - n) % 26
            E_result += alphabets[E]
    print(f'the decryption result is {E_result}')




