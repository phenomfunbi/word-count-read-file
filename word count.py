

def count_words():
    
    #text = read_file_content("story.txt")
    # [assignment] Add your code here

   # return {"as": 10, "would": 20}
    g = open('story.txt') 
    file = g.read()

    count = dict()
    words = file.split()

    for word in words:
           if word in count:
               count[word] += 1
           else:
                count[word] = 1
    return count

print(count_words())

