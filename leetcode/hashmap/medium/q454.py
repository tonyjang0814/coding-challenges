class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # METHOD 1 uses less memory but more operation.
        # A + B = - (C + D)
        a_b= dict()
        n = len(A)
        
        for i in range(n):
            for j in range(n):
                sum_ = A[i] + B[j]
                if sum_ in a_b:
                    a_b[sum_] += 1
                else:
                    a_b[sum_] = 1
        
        count = 0
        for i in range(n):
            for j in range(n):
                sum_ = C[i] + D[j]
                if -sum_ in a_b:
                    count += a_b[-sum_]
        return count
        
        
        
        
        #   METHOD 2: uses more memory but less operation.
        
#         _A,_B,_C,_D = dict(),dict(),dict(),dict()
#         for i in range(len(A)):
#             if A[i] in _A:
#                 _A[A[i]] += 1
#             else:
#                 _A[A[i]] = 1
#             if B[i] in _B:
#                 _B[B[i]] += 1
#             else:
#                 _B[B[i]] = 1
#             if C[i] in _C:
#                 _C[C[i]] += 1
#             else:
#                 _C[C[i]] = 1
#             if D[i] in _D:
#                 _D[D[i]] += 1
#             else:
#                 _D[D[i]] = 1
        
#         contents1,contents2=dict(),dict()
#         for i in _A:
#             for j in _B:
#                 if i+j in contents1:
#                     contents1[i+j] += _A[i]*_B[j]
#                 else:
#                     contents1[i+j] = _A[i]*_B[j]
        
#         for i in _C:
#             for j in _D:
#                 if i+j in contents2:
#                     contents2[i+j] += _C[i]*_D[j]
#                 else:
#                     contents2[i+j] = _C[i]*_D[j]
        
#         count = 0
#         for i in contents1:
#             if -1*i in contents2:
#                 count += contents1[i]*contents2[-1*i]
#         return count