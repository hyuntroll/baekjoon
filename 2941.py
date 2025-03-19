# # N = 20

# score_dict = {'A+': 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
# score_sum = 0
# h_sum = 0

# for i in range(20):
#     # current_sum = 0
#     name, score, d = input().split()
#     if d == 'P':
#         # N -= 1
#         continue
#     score_sum += float(score) * score_dict[d]
#     h_sum += float(score)

# print(format(score_sum / h_sum, ".6f"))

'''
크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
'''

string = input()

# rpelace한 다음 길이 

string = string.replace("c=", "P")
string = string.replace("c-", "P")
string = string.replace("dz=", "P")
string = string.replace("d-", "P")
string = string.replace("lj", "P")
string = string.replace("nj", "P")
string = string.replace("s=", "P")
string = string.replace("z=", "P")

print(len(string))