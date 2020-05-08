from django.shortcuts import render
from DataBase.models import Users, Cars, Tasks
import json
import logging

logging.basicConfig(level=logging.INFO,
                    filename='err_view.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)


def index(request):
    user_info = {'name': 'Chris'}
    return render(request, 'index.html', user_info)


# gather overview
def gather(cl):
    overview = {
        "car_count": 0,
        "car_names": [],
        "car_power": [],
        "power_style": [],
        "task_count": 0,
        "task_progress": 0,
        "finished": 0
    }
    p_style = ["bg-danger", "bg-warning", "bg-info", "bg-success", ""]
    for car in cl:
        overview["car_count"] += 1
        overview["car_names"].append(car['carname'])
        overview["car_power"].append(int(car['battery']))
        overview["power_style"].append(p_style[int(car['battery']) // 25])
        for task in car['tasks']:
            if int(task['status'] == 100):
                overview['finished'] += 1
            else:
                overview['task_count'] += 1
                overview['task_progress'] += int(task['status'])
    logging.info(json.dumps(overview))
    return overview


g_ud = {}


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fname = email.split('@', 1)[0]
        pswd = request.POST.get('password')
        message = "Please check your username or password."
        if email.strip() and pswd:
            # todo:validate email and password prototype
            try:
                user = Users.objects.get(firstname=fname)
            except:
                message = f"User {fname} not found!"
                return render(request, 'login.html', {'message': message})
            u_cars = json.loads(user.cars)
            # print(type(u_cars))
            car_list = []
            for cid in u_cars:
                car = Cars.objects.get(id=cid)
                info = json.loads(car.info)
                ctask = []
                for tid in json.loads(car.tasks):
                    t = Tasks.objects.get(id=tid)
                    task = {
                        'tid': tid,
                        'taskname': t.taskname,
                        'info': t.info,
                        'status': t.status
                    }
                    ctask.append(task)
                c = {
                    'cid': cid,
                    'carname': car.carname,
                    'battery': info['battery'],
                    'status': info['status'],
                    'tasks': ctask
                }
                car_list.append(c)
            overview = gather(car_list)
            u_dict = {
                'name': user.username,
                'car_count': overview['car_count'],
                'task_count': overview['task_count'],
                'task_progress': overview['task_progress'] // (overview['task_count']),
                'finished': overview['finished'],
                'car_name0': overview['car_names'][0],
                'car_power0': overview['car_power'][0],
                'car_ps0': overview['power_style'][0],
                'car_name1': overview['car_names'][1],
                'car_power1': overview['car_power'][1],
                'car_ps1': overview['power_style'][1],
                'car_name2': overview['car_names'][2],
                'car_power2': overview['car_power'][2],
                'car_ps2': overview['power_style'][2],
            }
            g_ud = u_dict
            if user.password == pswd:
                return render(request, 'user.html', u_dict)
            return render(request, 'login.html', {'message': message})
        else:
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html', )


def notfound(request):
    return render(request, '404.html')


import socket


def control(request):
    UDP_IP = '192.168.39.138'
    UDP_PORT = 9999

    def call():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cmd = "RUN"
        s.sendto(cmd.encode(), (UDP_IP, UDP_PORT))
        s.close()

    call()

    return render(request, 'user.html', g_ud)
