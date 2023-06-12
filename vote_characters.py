# Use the bookDAO file from past exercises
################## Done need to add a Function to clear the table





import mysql.connector
import db_configuration as cfg
class VotesCharacters:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.db_mysql['host']
        self.user=       cfg.db_mysql['user']
        self.password=   cfg.db_mysql['password']
        self.database=   cfg.db_mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         

   # Create entries inside the Votes table with the votes made by each Ip address
    def createVote(self, values):
    
        cursor = self.getcursor()
        sql="INSERT into votes (charactername, ipaddress) values (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    # Counting the amount of votes 
    def countCharactersVotes(self,charactername):
        cursor = self.getcursor()
        
        ## how to use count on SQL https://www.datacamp.com/tutorial/count-sql-function?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=143216588777&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=657040116606&utm_targetid=aud-517318242147:dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=1007835&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-n-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-mayftyc23&gclid=CjwKCAjwvdajBhBEEiwAeMh1U8mrMfDxyoW6MtMGugmMER8uYf4vOaOmtiFcmi7Yar8JcWwir9Rl7RoCfOYQAvD_BwE
        sql="Select COUNT(*) as vote from votes WHERE charactername like %s"
        values = (charactername,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        count = result[0]
        self.closeAll()
        return count

    def convertToDictionary(self, result):
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    
    # Creating a table that will hold the Votes for the Characters and IP addresses from where the votes came from.
    def createVoteTable(self):
        cursor = self.getcursor()
        sql="CREATE TABLE votes (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, charactername VARCHAR(250), ipaddress VARCHAR(250));"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

    # Creating a Databese using the name in the config file
    def createDatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
        )
        self.cursor = self.connection.cursor()
        sql = "CREATE database " + self.database
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

votesCharacters = VotesCharacters()

if __name__ == "__main__":
   
   #Creating the databse and the vote table. Just need to be run once.

    #votesCharacters.createDatabase()
    #votesCharacters.createVoteTable()

    #data = ("Karl", "252.552.354.225") # ok
    #vote = votesCharacters.createVote(data) # ok
    #count = votesCharacters.countCharactersVotes("Karl")
    #print(count)

    print("test")


