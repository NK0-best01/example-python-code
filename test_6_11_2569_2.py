box = {}
myInput = str(input()).upper()
print(f"ประโยคที่ป้อนเข้ามา: {myInput}")
words = myInput.split()
print(f"จำนวนคำทั้งหมด: {words}")
# แยกคำในประโยคออกเป็นคำ ๆ โดยใช้ช่องว่างเป็นตัวแบ่ง
for item in words:
# วนลูปเพื่อเช็คคำแต่ละคำใน array words
  box[item] = box.get(item, 0) + 1
# เช็คหากเจอคำซ้ำใน box ให้เพิ่มค่า count ของคำนั้นขึ้น 1
sorted_counts = sorted(box.items(), key=lambda x: x[1], reverse=True)
# เรียงลำดับ box ตามจำนวนคำซ้ำจากมากไปน้อย
print(f"จำนวนคำที่ซ้ำกัน: {sorted_counts}")
# พิมพ์จำนวนคำซ้ำทั้งหมด
for item, count in sorted_counts:
    print(f"ค่า {item} ซ้ำกัน {count} ครั้ง")
# พิมพ์คำและจำนวนครั้งที่ซ้ำกันของแต่ละคำ
    
