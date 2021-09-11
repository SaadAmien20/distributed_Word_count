def word_count(file):
    try:
        file_dataset = open(file,"r") 
        file_count_result = open("result.txt","w")

        wordcount=dict()

        for word in file_dataset.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

        word_count_sorted = dict(sorted(wordcount.items(),key=lambda item: item[1],reverse=True))
        for i in word_count_sorted:
                file_count_result.write( i + ":"+ str(word_count_sorted[i])+ "\n" )    
    except:
        print ("there are a problem in file path, Please check it")



    
if __name__=="__main__":
# you can pass file path here,please put it between double quotations
    word_count()