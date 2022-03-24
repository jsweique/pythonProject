from PIL import Image
import pytesseract


def tes(list):
    list1 = []
    for i in list:
        if i.isdigit():
            list1.append(i)
    return list1


img = Image.open(r'C:\Users\zheng\Desktop\yanzheng.png')
# print(pytesseract.image_to_string(img))
list2 = list(pytesseract.image_to_string(img))
print(pytesseract.image_to_string(img))
#print(list2)
list3 = tes(list2)
print(''.join(list3))
