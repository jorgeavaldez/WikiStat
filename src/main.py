import WikiRequests

def loadQuery(w):
    w.queryPage(raw_input("Query> "))

if __name__ == "main":
    wr = WikiRequests()
    loadQuery(wr)
    selection = ""

    while selection is not "q":

        if selection is "w":
            loadQuery(wr)
            selection = ""

        elif selection is not "n" and selection is not "":
            print("Invalid selection, try again.")
            print("Type 'n' to go to the next page.")
            print("Type 'w' to input another query.")
            print("Type 'q' to quit.")
            selection = raw_input("~> ")
            print("")

        else:
            try:
                page = wr.pages.next()

            except StopIteration:
                print("No more pages. Exited.")
                break

            if page:
                print(page["extract"].encode("utf-8"))
                print("")
                print("Type 'n' to go to the next page.")
                print("Type 'w' to input another query.")
                print("Type 'q' to quit.")
                selection = raw_input("~> ")
                print("")

            elif selection is "w" and not page:
                print("No pages found :(")
                break

    if selection is "q":
        print("Exited.")
