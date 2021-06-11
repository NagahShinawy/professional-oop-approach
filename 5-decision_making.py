"""
created by Nagaj at 11/06/2021
"""
dollars = float("34.34")
euros = dollars.__mul__(float("0.87"))
print(euros)
if euros.__le__(30):
    print("Ok")

else:
    print("IN ELSE")