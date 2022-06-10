import numpy as np
import pandas as pd
import time


def find_blink(theta):
    diff = []  # 세타파의 변화량
    try:
        for i in range(len(theta) - 1):
            temp = theta[i + 1] - theta[i]
            diff.append(temp)

        # 전 보다 4%이상 급격하게 증가함을 보임-> 즉, 눈 깜박거렸다!
        for i in range(len(diff)):
            if (diff[i] > 4):
                if (abs(diff[i + 1]) < 2 and abs(diff[i + 2]) < 2):  # 근데 다시 내려가지 않고 꾸준히 지속 된다-> 즉, 의도적으로 계속 깜박이고 있다.
                    if (abs(diff[i + 3]) < 2):
                        return i  # 1을 반환하는건 눈깜박임 검출!
        time.sleep(1)
        return 0  # 0은 아무것도 하지마!

    except:  # 예외 처리를 무시한 이유: 인덱스에 값이 1개 있을 경우 에러 발생....
        return 0
