# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 16:41
# @Author  : Lvp
# @File    : createDB.py
import sqlite3
import os


base_path = os.getcwd().replace('\\', '/')


def build_db():

    conn = sqlite3.connect(f'{base_path}/sequence.db')
    cursor = conn.cursor()

    drop_task = """drop table task"""
    drop_parmas = """drop table params"""

    # cursor.execute(drop_parmas)
    # cursor.execute(drop_task)

    create_task = """CREATE TABLE IF NOT EXISTS task(
                        id INTEGER PRIMARY KEY,
                        taskNm TEXT not null,
                        taskType TEXT,
                        startTime TIMESTAMP default (datetime('now', 'localtime')),
                        endTime TEXT,
                        timeInter TEXT,
                        taskStatus TEXT,
                        taskResult TEXT)"""

    create_params = """CREATE TABLE IF NOT EXISTS params(
                        id INTEGER PRIMARY KEY,
                        taskNm TEXT not null,
                        taskType TEXT,
                        sampleNm TEXT,
                        barcode TEXT,
                        filepath TEXT)"""

    create_user = """CREATE TABLE IF NOT EXISTS users_(
                            id INTEGER PRIMARY KEY,
                            userNm TEXT not null,
                            pwd TEXT,
                            createTime TIMESTAMP default (datetime('now', 'localtime')))"""

    cursor.execute(create_task)
    cursor.execute(create_params)
    cursor.execute(create_user)

    s_sql = """select * from users_ where userNm=?"""
    result = cursor.execute(s_sql, ('999', ))
    data = result.fetchone()
    user_data = ('999', '11111')
    if not data:
        i_sql = """insert into users_(userNm, pwd) values (?,?)"""
        cursor.execute(i_sql, user_data)
    else:
        u_sql = """update users_ set pwd=? where userNm=?"""
        cursor.execute(u_sql, user_data)
    conn.commit()


if __name__ == '__main__':
    build_db()

