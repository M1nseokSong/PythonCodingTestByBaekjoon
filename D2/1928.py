# Base64 Decoder
t = int(input())

decoder = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9','+','/']
bin_2 = [32, 16, 8, 4, 2, 1]
bin_8 = [128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(t):
    string = input()
    print('#%d' %(_+1), end=' ')
    buffer = []
    turn = 0
    for i in string:
        i_to_bin = [0, 0, 0, 0, 0, 0]
        i = decoder.index(i)
        for j in range(6):
            if i >= bin_2[j]:
                i_to_bin[j] = 1
                i -= bin_2[j]
            buffer.append(i_to_bin[j])
    for _ in range(len(buffer)//8):
        result = 0
        j = 0
        for i in range(turn,turn+8):
            result += buffer[i] * bin_8[j]
            j += 1
        turn += 8
        print(chr(result), end='')
    print()


# encoding : AAA(24비트)-> ord로 아스키문자로 바꿈 -> 2진수로 8비트씩 바꿈-> 6비트씩 4개로 쪼갬 -> 그 값을 문자로 바꿈
# decoding : 문자를 값으로 바꿈 -> 2진수로 6비트씩 4개로 쪼갬 -> 8비트씩 바꿈 -> chr로 아스키로 바꿈

# TGlm -> 19 6 37 38 -> 010011 000110 100101 100110 -> 01001100 01101001 01100110 -> 76 105 102 -> chr(76) chr(105) chr(102)