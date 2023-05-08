from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

import mysql.connector


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'teacher_bill'
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

app.config['JSON_AS_ASCII'] = False

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "tearcher-bill"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if mysql.is_connected():
    print("Kết nối MySQL thành công!")
else:
    print("Kết nối MySQL không thành công!")


# giao vien
@app.route("/get_teacher", methods=['GET'])
def get_teacher():
    id = request.args.get('id')

    res = {}
    my_cursor = mysql.cursor()

    if not id:
        my_cursor.execute("SELECT giaovien.id, giaovien.ho_ten, giaovien.ma_so, giaovien.bang_cap_id, "
                          "bangcap.ten_bang_cap, bangcap.he_so_giao_vien "
                          "FROM giaovien INNER JOIN bangcap on giaovien.bang_cap_id = bangcap.id")

        my_result = my_cursor.fetchall()

        res["data"] = []
        for i in my_result:
            res["data"].append({
                'id': i[0],
                'tenGiaoVien': i[1],
                'maGiaoVien': i[2],
                'idBangCap': i[3],
                'bangCap': i[4],
                'heSoGiaoVien': i[5]
            })
    elif int(id):
        my_cursor.execute(f"SELECT giaovien.id, giaovien.ho_ten, giaovien.ma_so, giaovien.bang_cap_id, bangcap.ten_bang_cap, bangcap.he_so_giao_vien FROM giaovien INNER JOIN bangcap on giaovien.bang_cap_id = bangcap.id Where giaovien.id = {int(id)}")

        my_result = my_cursor.fetchall()
        if my_result and len(my_result) > 0:
            res["data"] = {
                'id': my_result[0][0],
                'tenGiaoVien': my_result[0][1],
                'maGiaoVien': my_result[0][2],
                'idBangCap': my_result[0][3],
                'bangCap': my_result[0][4],
                'heSoGiaoVien': my_result[0][5]
            }

    return jsonify(res)


@app.route("/create_teacher", methods=['POST'])
def create_teacher():
    name = request.form['tenGiaoVien']
    ma = request.form['maGiaoVien']
    bang_cap_id = request.form['idBangCap']

    my_cursor = mysql.cursor()
    sql = "INSERT INTO giaovien (ho_ten, ma_so, bang_cap_id) VALUES (%s, %s, %s)"
    val = (name, ma, int(bang_cap_id))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Created successfully'})


@app.route("/update_teacher/<int:id>", methods=['PUT'])
def update_teacher(id):
    name = request.form['tenGiaoVien']
    ma = request.form['maGiaoVien']
    bang_cap_id = request.form['idBangCap']

    my_cursor = mysql.cursor()
    sql = "UPDATE giaovien SET ho_ten = %s, ma_so = %s, bang_cap_id = %s WHERE id = %s"
    val = (name, ma, int(bang_cap_id), int(id))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Updated successfully'})


@app.route("/delete_teacher/<int:id>", methods=['DELETE'])
def delete_teacher(id):
    my_cursor = mysql.cursor()
    sql = f"DELETE FROM giaovien WHERE id = {int(id)}"
    my_cursor.execute(sql)

    mysql.commit()

    return jsonify({'msg': 'Deleted successfully'})


# bang cap
@app.route("/get_degree", methods=["GET"])
def get_degree():
    id = request.args.get('id')

    res = {}
    my_cursor = mysql.cursor()

    if not id:
        my_cursor.execute("SELECT * FROM bangcap")

        my_result = my_cursor.fetchall()

        res["data"] = []
        for i in my_result:
            res["data"].append({
                'id': i[0],
                'bangCap': i[1],
                'heSoGiaoVien': i[2]
            })
    elif int(id):
        my_cursor.execute(f"SELECT * FROM bangcap Where bangcap.id = {int(id)}")

        my_result = my_cursor.fetchall()
        if my_result and len(my_result) > 0:
            res["data"] = {
                'id': my_result[0][0],
                'bangCap': my_result[0][1],
                'heSoGiaoVien': my_result[0][2]
            }

    return jsonify(res)


@app.route("/create_degree", methods=['POST'])
def create_degree():
    bang_cap = request.form['bangCap']
    he_so_giao_vien = request.form['heSoGiaoVien']

    my_cursor = mysql.cursor()
    sql = "INSERT INTO bangcap (ten_bang_cap, he_so_giao_vien) VALUES (%s, %s)"
    val = (bang_cap, float(he_so_giao_vien))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Created successfully'})


@app.route("/update_degree/<int:id>", methods=['PUT'])
def update_degree(id):
    bang_cap = request.form['bangCap']
    he_so_giao_vien = request.form['heSoGiaoVien']

    my_cursor = mysql.cursor()
    sql = "UPDATE bangcap SET ten_bang_cap = %s, he_so_giao_vien = %s WHERE id = %s"
    val = (bang_cap, float(he_so_giao_vien), int(id))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Updated successfully'})


@app.route("/delete_degree/<int:id>", methods=['DELETE'])
def delete_degree(id):
    my_cursor = mysql.cursor()
    sql = f"DELETE FROM bangcap WHERE id = {int(id)}"
    my_cursor.execute(sql)

    mysql.commit()

    return jsonify({'msg': 'Deleted successfully'})


# lop hoc
@app.route("/get_class", methods=["GET"])
def get_class():
    id = request.args.get('id')

    res = {}
    my_cursor = mysql.cursor()

    if not id:
        my_cursor.execute("SELECT * FROM lophoc")

        my_result = my_cursor.fetchall()

        res["data"] = []
        for i in my_result:
            res["data"].append({
                'id': i[0],
                'tenLopHoc': i[1],
                'soSinhVien': i[2],
                'heSoLopHoc': i[3]
            })
    elif int(id):
        my_cursor.execute(f"SELECT * FROM lophoc Where lophoc.id = {int(id)}")

        my_result = my_cursor.fetchall()
        if my_result and len(my_result) > 0:
            res["data"] = {
                'id': my_result[0][0],
                'tenLopHoc': my_result[0][1],
                'soSinhVien': my_result[0][2],
                'heSoLopHoc': my_result[0][3]
            }

    return jsonify(res)


@app.route("/create_class", methods=['POST'])
def create_class():
    ten_lop_hoc = request.form['tenLopHoc']
    so_sinh_vien = request.form['soSinhVien']
    he_so_lop_hoc = request.form['heSoLopHoc']

    my_cursor = mysql.cursor()
    sql = "INSERT INTO lophoc (ten_lop_hoc, so_sinh_vien, he_so_lop_hoc) VALUES (%s, %s, %s)"
    val = (ten_lop_hoc, int(so_sinh_vien), float(he_so_lop_hoc))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Created successfully'})


@app.route("/update_class/<int:id>", methods=['PUT'])
def update_class(id):
    ten_lop_hoc = request.form['tenLopHoc']
    so_sinh_vien = request.form['soSinhVien']
    he_so_lop_hoc = request.form['heSoLopHoc']

    my_cursor = mysql.cursor()
    sql = "UPDATE lophoc SET ten_lop_hoc = %s, so_sinh_vien = %s, he_so_lop_hoc = %s WHERE id = %s"
    val = (ten_lop_hoc, int(so_sinh_vien), float(he_so_lop_hoc), int(id))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Updated successfully'})


@app.route("/delete_class/<int:id>", methods=['DELETE'])
def delete_class(id):
    my_cursor = mysql.cursor()
    sql = f"DELETE FROM lophoc WHERE id = {int(id)}"
    my_cursor.execute(sql)

    mysql.commit()

    return jsonify({'msg': 'Deleted successfully'})


# mon hoc
@app.route("/get_course", methods=["GET"])
def get_course():
    id = request.args.get('id')

    res = {}
    my_cursor = mysql.cursor()

    if not id:
        my_cursor.execute("SELECT * FROM monhoc")

        my_result = my_cursor.fetchall()

        res["data"] = []
        for i in my_result:
            res["data"].append({
                'id': i[0],
                'tenMonHoc': i[1],
                'heSoMonHoc': i[2]
            })
    elif int(id):
        my_cursor.execute(f"SELECT * FROM monhoc Where monhoc.id = {int(id)}")

        my_result = my_cursor.fetchall()
        if my_result and len(my_result) > 0:
            res["data"] = {
                'id': my_result[0][0],
                'tenMonHoc': my_result[0][1],
                'heSoMonHoc': my_result[0][2]
            }

    return jsonify(res)


@app.route("/create_course", methods=['POST'])
def create_course():
    ten_mon_hoc = request.form['tenMonHoc']
    he_so_mon_hoc = request.form['heSoMonHoc']

    my_cursor = mysql.cursor()
    sql = "INSERT INTO monhoc (ten_mon_hoc, he_so_mon_hoc) VALUES (%s, %s)"
    val = (ten_mon_hoc, float(he_so_mon_hoc))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Created successfully'})


@app.route("/update_course/<int:id>", methods=['PUT'])
def update_course(id):
    ten_mon_hoc = request.form['tenMonHoc']
    he_so_mon_hoc = request.form['heSoMonHoc']

    my_cursor = mysql.cursor()
    sql = "UPDATE monhoc SET ten_mon_hoc = %s, he_so_mon_hoc = %s WHERE id = %s"
    val = (ten_mon_hoc, float(he_so_mon_hoc), int(id))
    my_cursor.execute(sql, val)

    mysql.commit()

    return jsonify({'msg': 'Updated successfully'})


@app.route("/delete_course/<int:id>", methods=['DELETE'])
def delete_course(id):
    my_cursor = mysql.cursor()
    sql = f"DELETE FROM monhoc WHERE id = {int(id)}"
    my_cursor.execute(sql)

    mysql.commit()

    return jsonify({'msg': 'Deleted successfully'})


# tien day
@app.route("/get_money", methods=["GET"])
def get_money():
    id = request.args.get('id')

    res = {}
    my_cursor = mysql.cursor()

    if not id:
        my_cursor.execute("SELECT tienday.id, tienday.giao_vien_id, tienday.mon_hoc_id, tienday.lop_hoc_id, tienday.so_tiet, "
                          "tienday.tien_day_mot_gio, tienday.tien_day, monhoc.ten_mon_hoc, monhoc.he_so_mon_hoc, lophoc.ten_lop_hoc, "
                          "lophoc.so_sinh_vien, lophoc.he_so_lop_hoc, giaovien.ho_ten, giaovien.ma_so FROM tienday "
                          "inner join monhoc on tienday.mon_hoc_id = monhoc.id "
                          "inner join lophoc on lophoc.id = tienday.lop_hoc_id "
                          "inner join giaovien on giaovien.id = tienday.giao_vien_id")

        my_result = my_cursor.fetchall()

        res["data"] = []
        for i in my_result:
            res["data"].append({
                'id': i[0],
                'idGiaoVien': i[1],
                'idMonHoc': i[2],
                'idLopHoc': i[3],
                'soTiet': i[4],
                'tienDayMotGio': i[5],
                'tienDay': i[6],
                'tenMonHoc': i[7],
                'heSoMonHoc': i[8],
                'tenLopHoc': i[9],
                'soSinhVien': i[10],
                'heSoLopHoc': i[11],
                'tenGiaoVien': i[12],
                'maGiaoVien': i[13],
            })
    elif int(id):
        my_cursor.execute(f"SELECT tienday.id, tienday.giao_vien_id, tienday.mon_hoc_id, tienday.lop_hoc_id, tienday.so_tiet, tienday.tien_day_mot_gio, tienday.tien_day, monhoc.ten_mon_hoc, monhoc.he_so_mon_hoc, lophoc.ten_lop_hoc, lophoc.so_sinh_vien, lophoc.he_so_lop_hoc, giaovien.ho_ten, giaovien.ma_so FROM tienday inner join monhoc on tienday.mon_hoc_id = monhoc.id inner join lophoc on lophoc.id = tienday.lop_hoc_id inner join giaovien on giaovien.id = tienday.giao_vien_id Where tienday.id = {int(id)}")

        my_result = my_cursor.fetchall()
        if my_result and len(my_result) > 0:
            res["data"] = {
                'id': my_result[0][0],
                'idGiaoVien': my_result[0][1],
                'idMonHoc': my_result[0][2],
                'idLopHoc': my_result[0][3],
                'soTiet': my_result[0][4],
                'tienDayMotGio': my_result[0][5],
                'tienDay': my_result[0][6],
                'tenMonHoc': my_result[0][7],
                'heSoMonHoc': my_result[0][8],
                'tenLopHoc': my_result[0][9],
                'soSinhVien': my_result[0][10],
                'heSoLopHoc': my_result[0][11],
                'tenGiaoVien': my_result[0][12],
                'maGiaoVien': my_result[0][13],
            }

    return jsonify(res)


@app.route("/create_money", methods=['POST'])
def create_money():
    tien_day = None
    he_so_giao_vien = None
    he_so_mon_hoc = None
    he_so_lop_hoc = None
    giao_vien_id = request.form['idGiaoVien']
    mon_hoc_id = request.form['idMonHoc']
    lop_hoc_id = request.form['idLopHoc']
    so_tiet = request.form['soTiet']
    tien_day_mot_gio = request.form['tienDayMotGio']

    my_cursor = mysql.cursor()

    my_cursor.execute(f"select bangcap.he_so_giao_vien FROM bangcap WHERE id = (SELECT giaovien.bang_cap_id FROM giaovien Where giaovien.id = {int(giao_vien_id)})")

    giao_vien_result = my_cursor.fetchall()

    if giao_vien_result and len(giao_vien_result) > 0:
        he_so_giao_vien = giao_vien_result[0][0]

    my_cursor.execute(f"SELECT monhoc.he_so_mon_hoc FROM monhoc Where monhoc.id = {int(mon_hoc_id)}")

    mon_hoc_result = my_cursor.fetchall()

    if mon_hoc_result and len(mon_hoc_result) > 0:
        he_so_mon_hoc = mon_hoc_result[0][0]

    my_cursor.execute(f"SELECT lophoc.he_so_lop_hoc FROM lophoc Where lophoc.id = {int(lop_hoc_id)}")

    lop_hoc_result = my_cursor.fetchall()

    if lop_hoc_result and len(lop_hoc_result):
        he_so_lop_hoc = lop_hoc_result[0][0]

    if he_so_giao_vien and he_so_mon_hoc and he_so_lop_hoc:
        tien_day = float(so_tiet) * int(tien_day_mot_gio) * (float(he_so_mon_hoc) + float(he_so_lop_hoc) + float(he_so_giao_vien))
        sql = "INSERT INTO tienday (giao_vien_id, mon_hoc_id, lop_hoc_id, so_tiet, tien_day_mot_gio, tien_day) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (int(giao_vien_id), int(mon_hoc_id), int(lop_hoc_id), float(so_tiet), int(tien_day_mot_gio), tien_day)
        my_cursor.execute(sql, val)

        mysql.commit()

        return jsonify({'msg': 'Created successfully'})

    return jsonify({'msg': 'Created failed'})


@app.route("/update_money/<int:id>", methods=['PUT'])
def update_money(id):
    tien_day = None
    he_so_giao_vien = None
    he_so_mon_hoc = None
    he_so_lop_hoc = None
    giao_vien_id = request.form['idGiaoVien']
    mon_hoc_id = request.form['idMonHoc']
    lop_hoc_id = request.form['idLopHoc']
    so_tiet = request.form['soTiet']
    tien_day_mot_gio = request.form['tienDayMotGio']

    my_cursor = mysql.cursor()

    my_cursor.execute(f"select bangcap.he_so_giao_vien FROM bangcap WHERE id = (SELECT giaovien.bang_cap_id FROM giaovien Where giaovien.id = {int(giao_vien_id)})")

    giao_vien_result = my_cursor.fetchall()

    if giao_vien_result and len(giao_vien_result) > 0:
        he_so_giao_vien = giao_vien_result[0][0]

    my_cursor.execute(f"SELECT monhoc.he_so_mon_hoc FROM monhoc Where monhoc.id = {int(mon_hoc_id)}")

    mon_hoc_result = my_cursor.fetchall()

    if mon_hoc_result and len(mon_hoc_result) > 0:
        he_so_mon_hoc = mon_hoc_result[0][0]

    my_cursor.execute(f"SELECT lophoc.he_so_lop_hoc FROM lophoc Where lophoc.id = {int(lop_hoc_id)}")

    lop_hoc_result = my_cursor.fetchall()

    if lop_hoc_result and len(lop_hoc_result):
        he_so_lop_hoc = lop_hoc_result[0][0]

    if he_so_giao_vien and he_so_mon_hoc and he_so_lop_hoc:
        tien_day = float(so_tiet) * int(tien_day_mot_gio) * (float(he_so_mon_hoc) + float(he_so_lop_hoc) + float(he_so_giao_vien))
        sql = "UPDATE tienday SET giao_vien_id = %s, mon_hoc_id = %s, lop_hoc_id = %s, so_tiet = %s, tien_day_mot_gio = %s, tien_day = %s WHERE id = %s"
        val = (int(giao_vien_id), int(mon_hoc_id), int(lop_hoc_id), float(so_tiet), int(tien_day_mot_gio), tien_day, int(id))
        my_cursor.execute(sql, val)

        mysql.commit()

        return jsonify({'msg': 'Updated successfully'})

    return jsonify({'msg': 'Updated failed'})


@app.route("/delete_money/<int:id>", methods=['DELETE'])
def delete_money(id):
    my_cursor = mysql.cursor()
    sql = f"DELETE FROM tienday WHERE id = {int(id)}"
    my_cursor.execute(sql)

    mysql.commit()

    return jsonify({'msg': 'Deleted successfully'})


if __name__ == '__main__':
    # http://127.0.0.1:5000/swagger

    app.run(debug=True)
