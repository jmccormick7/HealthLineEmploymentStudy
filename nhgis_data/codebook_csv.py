import csv;
book = input("Codebook (.txt): ");
cname = input("New csv name (.csv): ");
text = open(book, 'r', encoding="utf8");
list1 = [];
list2 = [];
prefix = "";
for line in text.readlines():
    if "Table" in line:
        prefix = line[15:];
        prefix = prefix.replace(" ", "");
        prefix = prefix.replace("\n", "");
        #print(prefix);
    elif ":" in line:
        newline = line[21:];
        newline = newline.replace("\n", "");
        newline = prefix + ": " + newline;
        #print(newline);
        code = line[:19];
        code = code.replace(" ", "");
        code = code.replace("\n", "");
        code = code.replace(":", "");
        list1.append(code);
        list2.append(newline);

with open(cname, "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file);
    writer.writerow(list1);
    writer.writerow(list2);
        
text.close();
