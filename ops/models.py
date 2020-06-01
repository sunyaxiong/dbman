from django.db import models

# Create your models here.


class DBConf(models.Model):
    ip = models.GenericIPAddressField("IP")
    port = models.IntegerField("端口", default=1433)
    username = models.CharField("用户名", max_length=128)
    password = models.CharField("密码", max_length=128)
    dbname = models.CharField("db名称", max_length=128, null=True, blank=True)
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='created datetime')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='updated datetime')

    def __str__(self):
        return "{}-{}".format(self.ip, self.dbname)


class SentenceTemplate(models.Model):

    sentence = models.TextField()
    desc = models.CharField(max_length=256)
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='created datetime')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='updated datetime')

    def __str__(self):
        return self.desc


class CheckTask(models.Model):

    db = models.ForeignKey(DBConf, verbose_name="目标数据库", on_delete=models.DO_NOTHING, db_constraint=False)
    sentence = models.ForeignKey(SentenceTemplate, verbose_name="语句", on_delete=models.DO_NOTHING, db_constraint=False)
    result = models.TextField("检查结果")
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='created datetime')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='updated datetime')

    def __str__(self):
        return "{}-{}".format(self.dt_created, self.sentence.desc)
