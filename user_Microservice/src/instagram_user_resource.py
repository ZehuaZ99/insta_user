import pymysql

import os


class InstagramUserResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_user_by_id(key):

        sql = "SELECT * FROM user_database.my_users where UserID=%s";
        conn = InstagramUserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_follower_by_id(key):

        sql = "SELECT * FROM user_database.my_follower where FollowerID=%s";
        conn = InstagramUserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_followings_by_id(key):

        sql = "SELECT * FROM user_database.my_following where FollowingID=%s";
        conn = InstagramUserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result
