my_dict = {"max":7777,"min":2222,"avg":3456}
print("Dict:",my_dict)
print("Existing value:",my_dict["max"])
print("Not existing value:",my_dict.get("dif"))
my_dict.update({"res":32141,
               "pass":86548})
print("Dleted value:",my_dict.pop("max"))
print("Modified dict:",my_dict)

my_set = {2,3,4,2,3,4,4,5,5,True,True,"Str","Rst","Str"}
print("Set:",set(my_set))
my_set = set(my_set)
my_set.add(12)
my_set.add(21)
print("Deleted value:",2)
print("Modified set:",my_set)