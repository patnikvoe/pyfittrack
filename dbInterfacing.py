
# select a mountain
def selectMountain(db):
    mountains = readTableFromDB(tb_mountains,db,index_col="id")
    mountainrange = pd.unique(mountains["mountainrange"])
    index = [int(i) for i in range(1, len(mountainrange)+1)]
    mountainrange = pd.DataFrame(mountainrange,index=index)
    mountainrange.columns = ["mountainrange"]
    print(tabulate(mountainrange,headers = "keys",tablefmt="psql"))
    selection = input("Select Mountainrange: ")
    selection = int(selection)
    selection -= 1
    mountainrange = mountainrange.iloc[selection]
    mountainrange = mountainrange.to_string(header=False,index=False)
    mountainrangeBool = mountains["mountainrange"]== mountainrange
    mountains = mountains[mountainrangeBool]
    print(tabulate(mountains,headers = "keys",tablefmt="psql"))
    selection = input("Select Mountain: ")
    selection = int(selection)

    return selection

# Check!!
def showMountainSummits():
    mountains = readTableFromDB(tb_mountains,Engine,columns=["name","mountainrange"])
    alpineTracks = readTableFromDB(tb_tracksalpine,Engine)
    print(tabulate(alpineTracks,headers = "keys",tablefmt="psql",showindex="never"))

    alpineTracks = alpineTracks["summit"==True]
    print(tabulate(alpineTracks,headers = "keys",tablefmt="psql",showindex="never"))

    pass
