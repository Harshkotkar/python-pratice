def main():
    try:
        book_list=[]
        infile=open("bookslist.txt",'r')
        line=infile.readline()
        while line:
            book_list.append(line.rstrip("\n").split(","))
            line=infile.readline()
        infile.close()
    except FileNotFoundError:
        print("file is not defiend properly recheck the file name ")
    print("starting a new book list")
    book_list=[]


    print(book_list)
    choice= 0
    while choice!=4:
        print("******book manager*********")
        print("1)add the book")
        print("2)look the book")
        print("3)display the all books")
        print("4)exit the program")
        choice=int(input())

        if choice==1:
            print("adding the book--->")
            book_id=input("Enter the book id")
            book_name=input("Enter the book name")
            book_author=input("enter the author name")
            book_pages=input("enter the total pags of the book")
            book_list.append([book_id,book_name,book_author,book_pages])

        elif choice==2:
            print("looking for the book")
            keyword=input("enter the name of the book to searched")
            for book in book_list:
                if keyword in book:
                    print(book)

        elif choice==3:
            print("all the books")
            for i in range(len(book_list)):
                print(book_list[i])

        elif choice==4:
            print("bye bye")

    #saving the book into the text file
    file=open("bookslist.txt",'w')
    for book in book_list:
        file.write(",".join(book)+"\n")
    file.close()


    print("program terminated")


if __name__=="__main__":
    main()