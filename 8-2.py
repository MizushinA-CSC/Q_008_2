# 文字列S中から、最も長い回文を見つけ、その文字列を出力する
import sys

# 標準入力の代わり
#S: str = "banana"

# 標準入力と入力エラー処理
S = str(input())

if(len(S) < 1 or len(S) > 100):
    print(f"Error：不適切な長さの文字列が入力されました S={len(S)}")
    sys.exit()


# main処理
result: str = ""

# 文字列反転の方法
# (1) result = "".join(list(reversed(S)))
# (2) result = S[::-1]

if(len(S) == 1):
    result = S
elif(S == S[::-1]):
    result = S
else:
    # length = len(S)-1, len(S)-2, ... , 1
    for length in range(len(S) - 1, 0, -1):
        # i = 0, 1, ... , len(S)-length
        for i in range(len(S) - length + 1):
            tmp = S[i:(length + i)]
            #print(f"{i}文字目から{length}文字 : {tmp}")
            if(tmp == tmp[::-1]):
                result = tmp
                break   # BREAK inner loop
        else:
            continue   # Finish inner loop without BREAK
        break   # BREAK outer loop


print(result)
