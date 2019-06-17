import pymysql.cursors


class message:

    def __init__(self, host, user, password, db, charset):
        self.host = host
        self.user = user
        self._password = password  # 私有属性
        self._db = db       # 私有属性
        self.charset = charset

    def conn(self):
        connection = pymysql.connect(host=self.host, user=self.user, password=self._password, db=self._db, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = "select `user_attribute_value`.`value` from `user_attribute_value` left join `user_attribute` on `user_attribute_value`.`user_attribute_id` = `user_attribute`.`id` where (`user_attribute_value`.`user_id` = '1' and `user_attribute`.`group` = 'user' and `user_attribute`.`status` = 1) order by `sort` asc"
                cursor.execute(sql)
                result = cursor.fetchall()
                for item in result:
                    print(item.values())

        finally:
            connection.close()


mes = message('localhost', 'root', 'root', 'userdb', 'utf8mb4')

mes.conn()