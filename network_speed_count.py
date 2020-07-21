# because the net bandwidth unit is bit, the save unit is byte(字节),
# the ratio is 8 bit = 1 byte
bandwidth = 100
ratio = 8 

per_second_download_MB = bandwidth / ratio
print(per_second_download_MB)