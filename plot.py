#
# from datetime import datetime
# import pandas as pd
# from matplotlib import pyplot as plt
# df = pd.read_csv("attendance.csv", header=None)
# ref = df.loc[df[0]=="NONE"]
# df.drop(df[df[0]=="NONE"].index , inplace=True)
# ref= ref[2]
# x = ref.tolist()
# y = list(set(df[0].tolist()))
# ls = []
# cnt = 0
# for i in y:
#     ls.append([])
#     for j in x:
#         if len(df.loc[(df[0]==i) & (df[2]==j)])>=1:
#             ls[cnt].append( (j, 1))
#         else:
#             ls[cnt].append((j, 0))
#     cnt+=1
# for i in range(len(y)):
#     x = pd.DataFrame.from_records(ls[i])
#     plt.plot(x[0], x[1], label= y[i])
#     z = [y[i]]
#     plt.legend(z, loc="lower left")
#     plt.title("Boolean Detection/Attention Tracking")
#     plt.ylabel("1-0")
#     plt.xlabel("Time")
#     plt.show()
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("attendance.csv", header=None)
ref = df.loc[df[0]=="NONE"]
df.drop(df[df[0]=="NONE"].index , inplace=True)
ref= ref[2]
x = ref.tolist()
y = list(set(df[0].tolist()))
ls = []
cnt = 0
for i in y:
    ls.append([])
    for j in x:
        if len(df.loc[(df[0]==i) & (df[2]==j)])>=1:
            ls[cnt].append( (j, 1))
        else:
            ls[cnt].append((j, 0))
    cnt+=1
for i in range(len(y)):
    x = pd.DataFrame.from_records(ls[i])
    plt.plot(x[0], x[1], label= y[i])
plt.legend(y, loc="lower left")
plt.title("Boolean Detection/Attention Tracking")
plt.ylabel("1-0")
plt.xlabel("Time")
plt.show()