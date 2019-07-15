from flask import  Flask,render_template,request,url_for,redirect,session,flash
from database import config
import  pymysql,os
from werkzeug.utils import secure_filename

from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
# app.config.from_object(config)
# app.secret_key = 'item'
# pymysql.install_as_MySQLdb()
# db.SQLAlchemy(app)
app.secret_key = 'item'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/taskid",methods=['GET','POST'])
def taskid():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='GET':
        taskid = request.args.get('taskid')
        sql = "SELECT id,name,status,machine_status,report_status FROM t_task where id = '%s' order by created_datetime desc" %(taskid)
        print(sql)
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return  render_template("taskid.html",u=u)

    else:
        if request.method == 'POST':
            taskid = request.form.get('taskid')
            reportstus = request.form.get('reportstus')

            sql = ("update  t_task set report_status= '%s'  where "
                   "id='%s';" % (reportstus, taskid)
                   )
            print('sql： ' + sql)
            try:
                cur.execute(sql)
                conn.commit()
                u = cur.rowcount()
                print(u)
                if u != 1:
                    raise Exception('更新失败')
                else:
                    flash('更新成功！')
            except Exception as e:
                print(e)
                flash('更新失败')
                conn.rollback()
            finally:
                conn.close()
            return render_template("index.html")

@app.route("/taskduty",methods=['GET','POST'])
def taskduty():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        dutyrelation = request.form.get('dutyrelation')
        if(dutyrelation ==''):
            flash('taskID 不能为空')
            return render_template("sturelation.html")
        else:
            #支持模糊查询
            sql = "SELECT id,task_id,class_id,student_id,student_name,exam_no,status,exam_status,ip_address,seat_no from t_task_student_relation where task_id ='%s' ORDER BY exam_status desc" %(dutyrelation)
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        if (len(u)==0):
            return render_template("index.html")
        else:
            return  render_template("sturelation.html",u=u)

@app.route("/updatestu",methods=['GET','POST'])
def updatestu():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        respform = request.form
        print(respform['stuid'])

        exam_status = request.form.get('exam_status')
        ip = request.form.get('ip')
        seat_no = request.form.get('seat_no')
        taskid = request.form.get('taskid')
        stuid = request.form.get('stuid')

        print('exam_status:'+exam_status)
        print('ip:' + ip)
        print('seat_no:' + seat_no)

        sql = ("update  t_task_student_relation set exam_status= '%s' , ip_address ='%s' , seat_no ='%s' where "
               "task_id='%s' and student_id ='%s' ;" %(exam_status,ip,seat_no,taskid,stuid)
               )
        print('sql： '+sql)
        try:
            cur.execute(sql)
            conn.commit()
            u = cur.rowcount()
            if u != 1:
                raise Exception('更新失败' +stuid)
        except Exception as e:
            print(e)
            flash('更新失败'+e)
            conn.rollback()
        finally:
            conn.close()
        return  render_template("index.html")

@app.route("/searchanswer",methods=['GET','POST'])
def searchanswer():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        taskid= request.form.get('taskid')
        sql = "SELECT * FROM t_stu_answer where task_id = '%s'" %(taskid)
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return  render_template("studentanswer.html",u=u)


@app.route("/insertanswer",methods=['GET','POST'])
def insertanswer():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        tableid = request.form.get('tableid')
        question_id = request.form.get('question_id')
        subquestion_no = request.form.get('subquestion_no')
        task_id = request.form.get('task_id')
        respondents_id = request.form.get('respondents_id')
        student_id = request.form.get('student_id')
        snapshot_id = request.form.get('snapshot_id')
        answer_type = request.form.get('answer_type')
        mark = float(request.form.get('mark'))
        score = float(request.form.get('score'))
        machine_score = float(request.form.get('machine_score'))
        manual_score = float(request.form.get('manual_score'))
        manual_detail = request.form.get('manual_detail')
        if(manual_detail != 'None'):
            manual_detail = float(manual_detail)
        arbitration_score = float(request.form.get('arbitration_score'))
        file_id = request.form.get('file_id')
        if(file_id != 'None'):
            file_id = float(file_id)
        machine_status = request.form.get('machine_status')
        machine_reason = request.form.get('machine_reason')
        if(machine_reason != 'None'):
            machine_reason = float(machine_reason)
        created_by = request.form.get('created_by')
        created_datetime = request.form.get('created_datetime')
        updated_by = request.form.get('updated_by')
        updated_datetime = int(request.form.get('updated_datetime'))
        version = int(request.form.get('version'))
        is_deleted = int(request.form.get('is_deleted'))
        data_version = int(request.form.get('data_version'))
        pattern_id = request.form.get('pattern_id')
        subjective_and_objective = request.form.get('subjective')
        student_answers = request.form.get('student_answers')
        right_answers = request.form.get('right_answers')
        rank_score = float(request.form.get('rank_score'))
        mark_ratio = request.form.get('mark_ratio')
        pronunciation_score = request.form.get('pronunciation_score')
        if(pronunciation_score !='None'):
            pronunciation_score = float(pronunciation_score)
        fluency_score = request.form.get('fluency_score')
        if(fluency_score !='None'):
            fluency_score = float(fluency_score)
        integrity_score = request.form.get('integrity_score')
        if(integrity_score !='None'):
            integrity_score =float(integrity_score)
        rhythm_score = request.form.get('rhythm_score')
        if(rhythm_score != 'None'):
            rhythm_score=float(rhythm_score)
        evaluation_engine = request.form.get('evaluation_engine')
        if(evaluation_engine !='None'):
            evaluation_engine =float(evaluation_engine)
        question_no = request.form.get('question_no')
        question_name = request.form.get('question_name')
        if(file_id =='None'):
            sql = "insert into  t_stu_answer (id, question_id, subquestion_no, task_id," \
                  "respondents_id, student_id, snapshot_id, answer_type, mark, score, machine_score, manual_score,arbitration_score," \
                  "machine_status,created_by, created_datetime, updated_by, updated_datetime, version, is_deleted," \
                  "data_version, pattern_id, subjective_and_objective," \
                  "student_answers, right_answers, rank_score, mark_ratio, question_no,"\
                  "question_name) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                  "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
                  tableid, question_id, subquestion_no, task_id,
                  respondents_id, student_id, snapshot_id, answer_type, mark, score, machine_score, manual_score,
                  arbitration_score, machine_status,
                  created_by, created_datetime, updated_by, updated_datetime, version, is_deleted,
                  data_version, pattern_id, subjective_and_objective,
                  student_answers, right_answers, rank_score, mark_ratio, question_no,
                  question_name)
        else:
            sql = "insert into  t_stu_answer values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                  "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
                      tableid, question_id, subquestion_no, task_id,
                      respondents_id, student_id, snapshot_id, answer_type, mark, score, machine_score, manual_score,
                      manual_detail, arbitration_score, file_id, machine_status,
                      machine_reason, created_by, created_datetime, updated_by, updated_datetime, version, is_deleted,
                      data_version, pattern_id, subjective_and_objective,
                      student_answers, right_answers, rank_score, mark_ratio, pronunciation_score, fluency_score,
                      integrity_score, rhythm_score, evaluation_engine, question_no,
                      question_name)
        print('sql:'+sql)
        try:
            cur.execute(sql)
            conn.commit()
            u = cur.rowcount()
            if u != 1:
                raise Exception('插入失败'+student_id)

        except Exception as e:
            print(e)
            flash('数据库插入失败'+e)
            conn.rollback()
        finally:
            conn.close()
            return render_template("index.html")




@app.route("/sturespond",methods=['GET','POST'])
def sturespond():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        taskid= request.form.get('taskid')
        sql = "SELECT * FROM t_stu_respondents where task_id = '%s'" %(taskid)
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return  render_template("sturespondents.html",u=u)



@app.route("/instspon",methods=['GET','POST'])
def instspon():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        tableid = request.form.get('tableid')
        snapshot_id = request.form.get('snapshot_id')
        respondents_name = request.form.get('respondents_name')
        respondents_status = request.form.get('respondents_status')
        respondents_md5 = request.form.get('respondents_md5')
        need_file_count = int(request.form.get('need_file_count'))
        file_count = int(request.form.get('file_count'))
        zero_count = int(request.form.get('zero_count'))
        answer_process = request.form.get('answer_process')
        paper_name = request.form.get('paper_name')
        elapsed_time = request.form.get('elapsed_time')
        if(elapsed_time != 'None'):
            elapsed_time = int(elapsed_time)
        is_deleted = int(request.form.get('is_deleted'))
        data_version = request.form.get('data_version')
        if(data_version !='None'):
            data_version = int(data_version)
        created_by = request.form.get('created_by')
        created_datetime = int(request.form.get('created_datetime'))
        updated_by = request.form.get('updated_by')
        updated_datetime = int(request.form.get('updated_datetime'))
        version = int(request.form.get('version'))
        class_id = request.form.get('class_id')
        task_id = request.form.get('task_id')
        student_id = request.form.get('student_id')
        full_mark = float(request.form.get('full_mark'))
        total_score = float(request.form.get('total_score'))
        file_id = int(request.form.get('file_id'))
        machine_status = request.form.get('machine_status')
        machine_reason = request.form.get('machine_reason')
        duration = request.form.get('duration')
        print(duration)
        print(data_version)
        print(elapsed_time)
        if(duration !='None'):
            duration = int(duration)
        if(duration =='None' and data_version =='None' and elapsed_time=='None'):
            sql = "insert into  t_stu_respondents (id, snapshot_id, respondents_name, respondents_status," \
                  "respondents_md5, need_file_count, file_count, zero_count, answer_process, paper_name, is_deleted," \
                  "created_by,created_datetime, updated_by, updated_datetime, version, class_id," \
                  "task_id, student_id, full_mark," \
                  "total_score, file_id, machine_status, "\
                  "machine_reason) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                  "'%s','%s','%s','%s','%s','%s','%s','%s');" % (tableid, snapshot_id, respondents_name, respondents_status,
                  respondents_md5, need_file_count, file_count, zero_count, answer_process, paper_name, is_deleted,
                  created_by,created_datetime, updated_by, updated_datetime, version, class_id,
                  task_id, student_id, full_mark,
                  total_score, file_id, machine_status, machine_reason)
        print('sql:'+sql)
        try:
            cur.execute(sql)
            conn.commit()
            u = cur.rowcount()
            if u != 1:
                raise Exception('插入失败'+student_id)

        except Exception as e:
            print(e)
            flash('数据库插入失败'+e)
            conn.rollback()
        finally:
            conn.close()
            return render_template("index.html")



@app.route("/searchstatus",methods=['GET','POST'])
def searchstatus():
    conn = pymysql.connect(host='10.18.32.132', user='mysql', password='P@ssword1', db='tsmk_service', charset='utf8')
    cur = conn.cursor()
    if request.method =='POST':
        taskid = request.form.get('taskid')
        print('taskid'+taskid)
        sql = "SELECT id,name,status,machine_status,report_status FROM t_task where id = '%s' order by created_datetime desc" %(taskid)
        print(sql)
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return  render_template("uptaskstatus.html",u=u)



@app.route("/upload",methods=['POST','GET'])
def upload():
    if request.method =="POST":
        f =request.file['upfile']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static\uploads', secure_filename(f.filename))
        f.save(upload_path)

    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)