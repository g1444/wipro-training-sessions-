import subprocess
# result=subprocess.run(
#     ["cmd","/c","dir"],
#     capture_output=True,
#     text=True)
# print(result.stdout)
# # subprocess.run(["notepad"])


# result1=subprocess.run(["cmd","/c","echo hello world"],capture_output=True,text=True)
# print(result1.stdout)
resultls=subprocess.run(["dir"],shell=True,capture_output=True,text=True)
print(resultls.stdout)

subprocess.run(["python","TC_tuple.py"])