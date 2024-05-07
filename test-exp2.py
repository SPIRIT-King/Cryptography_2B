import numpy as np
pred_keyword="1110100111"
pred_keyword_list = [int(keyword) for keyword in list(pred_keyword)]
pred_keyword_list_used = pred_keyword_list[:6]
level=3
K = []
for i in range(level):
    K.append(pred_keyword_list_used[i:level+i])
K = np.array(K)
K_inv = np.linalg.inv(K)

k_list = pred_keyword_list_used[-3:]

print(K)
print(K_inv%2)
print(k_list)
print(np.dot( k_list,K_inv)%2)