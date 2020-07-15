from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DBConf, SentenceTemplate, CheckTask
from lib import dbsdk


def index(request):

    db_list = DBConf.objects.filter()
    print(db_list)

    return render(request, 'inspect_change_list.html', locals())


def sql_run(request):
    if request.method == "POST":
        data = request.POST
        try:
            db_conf = DBConf.objects.get(id=data.get("db_id"))
            sentence = SentenceTemplate.objects.get(id=data.get("sentence_id"))
            res = dbsdk.sql_run(
                db_conf.ip, db_conf.username, db_conf.password, sentence.sentence
            )
            if res.get("data"):
                task = CheckTask.objects.create(
                        db=db_conf,
                        sentence=sentence,
                        result=res.get("data")
                )
            else:
                task = CheckTask.objects.create(
                    db=db_conf,
                    sentence=sentence,
                    result=res.get("error")
                )
                print("error: ", res.get("error"))
            return redirect(f'/admin/ops/checktask/{task.id}/change/')
        except Exception as e:
            print(e)
            messages.error(request, f"任务执行不成功 {e}")
            # TODO 执行sql，保存结果

        return redirect('/admin/ops/inspect/')
