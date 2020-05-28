from django.contrib import admin
from .models import CheckTask, DBConf, SentenceTemplate
from lib.dbsdk import sql_run

# Register your models here.


@admin.register(DBConf)
class DBConfAdmin(admin.ModelAdmin):

    list_display = ("ip", "username", "password", "dbname")


@admin.register(SentenceTemplate)
class SentenceTemplateAdmin(admin.ModelAdmin):
    list_display = ("sentence", "desc")


@admin.register(CheckTask)
class CheckTaskAdmin(admin.ModelAdmin):

    list_display = ("db", "result", "dt_created")

    def save_model(self, request, obj, form, change):
        """
        保存时执行语句进行查询
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """

        # print(obj.db.ip, obj.db.username, obj.db.password, obj.db.dbname, obj.sentence.sentence)

        # 执行语句
        res = sql_run(obj.db.ip, obj.db.username, obj.db.password, obj.db.dbname, obj.sentence.sentence)
        # print("res: ", res)
        if res.get("data"):
            obj.result = res.get("data")
            obj.save()
        else:
            obj.result = res.get("error")
            obj.save()
            print("error: ", res.get("error"))

        return 0
