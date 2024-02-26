'''
Database fnctions
'''
import sqlite3

class database():

    def __init__(self, app) -> None:
        self.con = sqlite3.connect(app.config['database'])
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS main 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, ...);""")

    def _check_db_exists(self):
        '''
        A quick check to create the table if it doesn't exist
        '''
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS main 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    projectid VARCHAR(255), 
                    threadid VARCHAR(255),
                    author VARCHAR(255), 
                    unix_timestamp VARCHAR(255),
                    music_name VARCHAR(255), 
                    music_url VARCHAR(255), 
                    music_thumb  VARCHAR(255), 
                    music_author  VARCHAR(255),
                    video_url VARCHAR(255), 
                    hashtags VARCHAR(255),
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS user_tags 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    projectid VARCHAR(255), 
                    file VARCHAR(255), 
                    tags VARCHAR(255),
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS features 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    projectid VARCHAR(255), 
                    feature VARCHAR(255), 
                    value VARCHAR(255),
                    );""")
        cur.close()

    def insert_row(self, projectid, threadid, author, unix_timestamp, music_name, music_id,
                   music_url, music_thumb, music_author, video_url, hashtags):
        '''
           Insert row from CSV
        '''
        cur = self.con.cursor()
        #project, threadid, author, unix_timestamp, music_name, music_id, 
        #music_url, video_url, hashtags
        cur.execute("""
        INSERT INTO main VALUES
        ({}, {}, {}, {}, {}, {}, {}, {}, {})
        """.format(projectid, threadid, author, unix_timestamp, music_name, music_id,
                   music_url, music_thumb, music_author, video_url, hashtags))
        self.con.commit()
        cur.close()

    def insert_tags(self, projectid, filename, tag):
        '''
           Insert into tag table
        '''
        cur = self.con.cursor()

        cur.execute("""
        INSERT INTO user_tag VALUES
        ({}, {}, {}).
         """.format(projectid, filename, tag))
        self.con.commit()
        cur.close()

    def insert_features(self, projectid, field, value):
        '''
           Insert into feature table
        '''
        cur = self.con.cursor()

        cur.execute("""
        INSERT INTO features VALUES
        ({}, {}, {}).
         """.format(projectid, field, value))
        self.con.commit()
        cur.close()

    def get_data_by_id(self, filename):
        '''
        Get the original data by project id
        :param filename - string of filename
        :return file_results - array
        '''
        cur = self.con.cursor()
        file_results = cur.fetchall("SELECT * FROM user_tags WHERE tags={}".format(filename))
        cur.close()
        return file_results
    
    def get_data_by_tag(self, tags):
        '''
        Get the original data by tag
        :param tags - string of tag
        :return file_results - array
        '''

        cur = self.con.cursor()
        tag_results = cur.fetchall("SELECT * FROM user_tags WHERE tags={}".format(tags))
        cur.close()
        return tag_results
    
    def get_data_by_tags(self, tags):
        '''
        Get the original data by tags
        :param tags - string of tag
        :return file_results - array
        '''
        tag = ','.join(tags)
        cur = self.con.cursor()
        tag_results = cur.fetchall("SELECT * FROM user_tags WHERE tags in ({})".format(tag))
        cur.close()
        return tag_results
    
    def get_data_by_project_id(self, id):
        '''
        Get the original data by project id
        :param id - string of projectid
        :return project_results - array
        '''
        cur = self.con.cursor()
        project_results = cur.fetchall("SELECT * FROM main WHERE projectid = {}".format(id))
        cur.close()
        return project_results