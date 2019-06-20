import pymysql.cursors


class message:

    def __init__(self, host, user, password, db, charset):
        self.host = host
        self.user = user
        self._password = password  # 私有属性
        self._db = db       # 私有属性
        self.charset = charset

    def conn(self, user_id):
        connection = pymysql.connect(host=self.host, user=self.user, password=self._password, db=self._db, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)
        values = ""

        # 剔除无效值
        value_Wipe = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '[]', None, '', '无', int]

        try:
            with connection.cursor() as cursor:
                # 查询user信息
                sql_user = "SELECT real_name, address_now, sex, detail_address FROM user WHERE user_id=%s"

                # 查询user_attribute_value信息
                sql_attribute = "select `user_attribute_value`.`value` from `user_attribute_value` left join `user_attribute` on `user_attribute_value`.`user_attribute_id` = `user_attribute`.`id` where (`user_attribute_value`.`user_id` =%s and `user_attribute`.`group` = 'user' and `user_attribute`.`status` = 1) order by `sort` asc"

                if cursor.execute(sql_user, user_id) > 0:  # 查询成功

                    for items in cursor.fetchall():

                        for item in items:
                           if items[item] not in value_Wipe and type(items[item]) not in value_Wipe:
                               values += items[item]

                        if items['sex'] == 1:
                            sex_n = "男"
                            values += sex_n
                        elif items['sex'] == 2:
                            sex_w = "女"
                            values += sex_w

                    if cursor.execute(sql_attribute, user_id) > 0:  # 执行查询操作
                        resultst = cursor.fetchall()
                        resultst.pop(-1)

                        for item in resultst:  # 查询结果
                             # 数据处理
                             if item['value'] not in value_Wipe and (item['value'][0] != '[' and item['value'][-1] != ']'):
                                 values += item['value'].strip()

                    return values

                else:

                    return -1  # 没有用户返回-1

        finally:
            connection.close()


# mess_text = message('localhost', 'root', 'root', 'userdb', 'utf8mb4').conn(user_id=3)  # 调用messageDB获取会员信息



