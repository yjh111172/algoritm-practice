def get_name(student_info,target_no,):
    return student_info.get(target_no, "?")
sample_info = {
        39: "Justin",
        14: "John",
        67: "Mike",
        105: "Summer"
    }
print (get_name(sample_info , 105))
print (get_name(sample_info , 777))