from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Content, Device, Schedule
import json

@csrf_exempt
def content_api(request, device_id):
    """
    Возвращает список контента для устройства по его ID.
    """
    if request.method == 'GET':
        try:
            device = Device.objects.get(device_id=device_id)
            schedule = Schedule.objects.filter(program__company=device.company)
            content_list = [
                {
                    "program": s.program.name,
                    "scheduled_at": s.scheduled_at,
                    "content": [
                        {
                            "name": item.name,
                            "type": item.content_type,
                            "url": item.content.url
                        }
                        for item in Content.objects.filter(program=s.program)
                    ]
                }
                for s in schedule
            ]
            return JsonResponse({"status": "success", "content": content_list}, status=200)
        except Device.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Device not found"}, status=404)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)


def device_status(request):
    """
    Возвращает статус всех зарегистрированных устройств.
    """
    devices = Device.objects.all()
    status_data = [
        {
            "name": device.name,
            "device_id": device.device_id,
            "status": device.status,
            "last_connected": device.last_connected
        }
        for device in devices
    ]
    return JsonResponse({"devices": status_data})
