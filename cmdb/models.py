from django.db import models

# Create your models here.
class Assets(models.Model):
    """服务器"""
    host_type_choice = (
        (0,'web服务器'),
        (1,'mysql服务器'),
        (2,'redis服务器'),
        (3,'mongodb服务器'),
    )
    host_name = models.CharField(max_length=64,verbose_name='主机名')
    cloud_sn = models.CharField(max_length=128,verbose_name='云厂商sn')
    host_type = models.SmallIntegerField(choices=host_type_choice,verbose_name='服务器类型',default=0)
    pub_ip1 = models.GenericIPAddressField(blank=True,null=True)
    pub_ip2 = models.GenericIPAddressField(blank=True,null=True)
    pri_ip1 = models.GenericIPAddressField(blank=True,null=True)
    pri_ip2 = models.GenericIPAddressField(blank=True,null=True)
    cpu_num = models.DecimalField(max_digits=256,decimal_places = 10,default=4 )
    mem_total = models.FloatField(default=8)
    disk_total1 = models.FloatField()
    disk_total2 = models.FloatField(null=True)
    c_time = models.DateTimeField(verbose_name='资产录入时间',default='1970-01-01 00:00:00')
    u_time = models.DateTimeField(verbose_name='最近更新时间',default='1970-01-01 00:00:00')
    is_deleted = models.SmallIntegerField(verbose_name='是否已下架',default=0)
    memo = models.CharField(max_length=256,)

    def __str__(self):
        return self.host_name

    class Meta:
        verbose_name = '服务器'

class Asset_status(models.Model):
    host_name = models.ForeignKey(Assets, on_delete=False)
    load_avg = models.FloatField()
    cpu_used = models.FloatField()
    mem_used = models.FloatField()
    dist_used = models.FloatField()

    def __str__(self):
        return self.host_name

    class Meta:
        verbose_name = '服务器资源状态'

class Business(models.Model):
    """业务线"""

    project_name = models.CharField(max_length=128,)
    is_deleted = models.SmallIntegerField(verbose_name='业务是否下线',default=0)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = '业务线'