#regexString = 'color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><span>BUTTON_11</span></div></div></div></foreignObject><text x="310" y="169" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">REPLACED</text></switch></g><rect x="43" y="183" width="175" height="18" fill="#ffffff"'
#expectedString = 'color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><span>REPLACED</span></div></div></div></foreignObjec t><text x="310" y="169" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">REPLACED</text></switch></g><rect x="43" y="183" width="175" height="18" fill="#ffffff"'

#buttonID = 11
#regexSearch = "\\b" + "BUTTON_" + str(buttonID) + "\\b"
#print(regexSearch)
#regexString = re.sub(regexSearch,"REPLACED",regexString)

#stringCompare = regexString == expectedString

#print("String is: " + str(stringCompare))

import unittest
import src.functions.helper as helper

class TestHelperFunctions(unittest.TestCase):

    def test_temporary_path(self):
        device = "Test"
        mode = "Mode"
        expectedPath = "./temp/" + device + "_" + mode + ".svg"
        path = helper.getTempPath(device,mode)
        self.assertEqual(path,expectedPath)

if __name__ == '__main__':
    unittest.main()