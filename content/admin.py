from django.contrib import admin
from .models import Company, Device, Content, Program, Schedule, Statistics


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_id', 'name', 'status', 'last_connected', 'company')
    search_fields = ('device_id', 'name')
    list_filter = ('status', 'company')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    search_fields = ('name',)
    list_filter = ('company',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'program', 'content_type')
    search_fields = ('name', 'program__name')
    list_filter = ('content_type', 'program')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'program', 'scheduled_at')
    search_fields = ('program__name',)
    list_filter = ('scheduled_at',)


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'program', 'total_views', 'last_updated')
    search_fields = ('device__name', 'program__name')
    list_filter = ('last_updated',)
