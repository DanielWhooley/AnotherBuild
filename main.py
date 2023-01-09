from malware_detect_funct.store_data import storedata
from malware_detect_funct.test import test
from malware_detect_funct.train import train

newValues = storedata(train("malware_detect_funct/exe_files"))

testValues = test("malware_detect_funct/exe_files")