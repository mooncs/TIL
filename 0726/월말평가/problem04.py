# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # n만큼 밀린 알파벳을 담을 빈 문자열 new_word를 선언
    new_word=''
    
    # 입력한 문자열의 문자 하나씩을 w로 불러온다.
    for w in word:
        # 대문자는 대문자로, 소문자는 소문자로 암호화하기 때문에 대문자일 경우와 소문자일 경우를 분리
        if w.isupper():
            # 대문자는 65~90까지이기 때문에 90을 넘어가면 26을 빼줌으로써 다시 65부터 시작하도록 한다.
            if ord(w) + n > 90:
                # ord(w)를 통해 문자를 10진수 값으로 바꾸고
                # ord(w)+n을 통해 n만큼 알파벳을 밀어준다.
                # chr(ord(w)+n)을 통해 10진수 값을 알파벳으로 변환
                # 변환된 알파벳 문자열을 new_word에 더해준다
                new_word += chr( ord(w) + n - 26)
            else:
                new_word += chr( ord(w) + n )
        elif w.islower():
            # 소문자의 경우 97~122까지이기 때문에 122를 넘어가면 26을 빼줌으로써 다시 97부터 시작하도록 한다.
            if ord(w) + n > 122:
                new_word += chr( ord(w) + n - 26)
            else:
                new_word += chr( ord(w) + n )
        

    # 최종적으로 더해진 문자열 new_word를 반환
    return new_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx