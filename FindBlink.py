from scipy.signal import find_peaks


def find_blink(data):
    print(data, type(data))
    fs = 230
    # data = data.loc[:['EEG_Fp1']]
    print(data, type(data))

    x_new = data.loc[-5*fs:]

    print('-----------------------------')
    print(x_new, type(x_new))
    # x_new = x
    # print(x_new)

    peaks, _ = find_peaks(x_new, height=0.0002, distance=40)
    cnt = len(peaks)

    print(cnt)

    if cnt >= 7:
        # print(peaks[-1])
        print(peaks)
        return peaks[-1]

    return 0
