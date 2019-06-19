from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    #文章唯一ID
    article_id = models.AutoField(primary_key=True)
    #文章标题
    title = models.CharField(u'博客标题', max_length=150)
    #文章的摘要
    brief_content = models.TextField(u'博客摘要', null=True)
    #文章的主要内容
    content = UEditorField(u"文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')
    #content = models.TextField(u'博客正文', null=True)
    #文章的发布日期
    publish_date = models.DateTimeField(u"发布日期", auto_now_add=True,editable=True )
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)



    def __str__(self):
        return self.title