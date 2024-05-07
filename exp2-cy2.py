import numpy as np
def LFSR_vig(pred_keyword, level):
    """
    根据推测出的密钥序列和线性反馈以为寄存器的级数，推算线性以为寄存器的递推关系式
    :param pred_keyword:推测的密钥序列
    :param level:线性移位寄存器的级数
    :return 递推关系的系数
    """
    pred_keyword_list = [int(keyword) for keyword in list(pred_keyword)]
    pred_keyword_list_used = pred_keyword_list[:2*level]
    # 构造矩阵
    K = []
    for i in range(level):
        K.append(pred_keyword_list_used[i:level+i])
    K = np.array(K)
    K_inv = np.linalg.inv(K)%2
    k_list = pred_keyword_list_used[-3:]
    k_list = np.array(k_list)
    return np.dot(K_inv, k_list)

if __name__ == "__main__":
    pred_keyword = "1110100111"
    
    


    