from django.http import HttpResponse
from DataBase.models import Users, Cars, Tasks

import random


def gen_phone():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return '{}-{}-{}'.format(first, second, last)


# create user set
import json


# initialize
def init_user(request):
    names = [
        "Judy Mccarthy",
        "Leanna Le",
        "Jae Levine",
        "Romana Witt",
        "Eloisa Steele",
        "Halle Ireland",
        "Maude Kirkpatrick",
        "Monique Busby",
        "Sarah-Louise Atkinson",
        "Emily Delgado",
        "Fahmida Mccormick",
        "Jorge Wong",
        "Anderson Burt",
        "Donte Frank",
        "Martin Holman",
        "Shakir Trujillo",
        "Rajan Hayden",
        "Daisy-Mae Healy",
        "Ben Thompson",
        "Safah Barry",
        "Matilda Klein",
        "Menachem Perry",
        "Asim Andrew",
        "Sama Broadhurst",
        "Johnny Hickman",
        "Anthony Kumar",
        "Seb Byrne",
        "Bethaney Case",
        "Chanelle Shah",
        "Zakk Mccullough",
        "Rocco Black",
        "Paisley Dupont",
        "Cristina Medrano",
        "Larry Bryan",
        "Kenan Webster",
        "Yvie Fischer",
        "Hanan Spence",
        "Monika Choi",
        "Sarina Humphries",
        "Chantelle Knowles",
        "Dalton Leach",
        "Amy-Leigh Shea",
        "Carley Green",
        "Roman Frey",
        "Lina Beck",
        "Kirsten Johns",
        "Amara Gunn",
        "Rome Kaur",
        "Chanel Morrow",
        "Gus Connelly",
        "Coral Ortega",
        "Dhruv Moody",
        "Dakota Myers",
        "Isabel Person",
        "Anabel Beaumont",
        "Kingsley Bevan",
        "Arman Norman",
        "Ayub Pruitt",
        "Havin Cole",
        "Erika Justice",
        "Lily-Mae Penn",
        "Judah Strong",
        "Nela Robinson",
        "Milana Clarke",
        "Nyla Horne",
        "Nuala Salter",
        "Ellisha Camacho",
        "Misty Sharpe",
        "Safaa Stevenson",
        "Pharrell Blaese",
        "Tammy Gibbs",
        "Kadeem Bull",
        "Kuba Abbott",
        "Nadeem Cook",
        "Brielle Benitez",
        "Moshe Leigh",
        "Blade Bannister",
        "Kristin Sexton",
        "Sana Travers",
        "Aiza Burke",
        "Olli Connolly",
        "Eddison Head",
        "Aviana Flowers",
        "Iosif Jensen",
        "Dewi Johnston",
        "Izabelle Wade",
        "Aaran Atherton",
        "Waqar Kearns",
        "Nannie Chamberlain",
        "Milli Hassan",
        "Jenna Rodriguez",
        "Florrie Farmer",
        "Misbah Leblanc",
        "Jillian Kim",
        "Justine Hendrix",
        "Eva-Rose Wilkes",
        "Francesca Gray",
        "Conal Lester",
        "Presley Schaefer",
        "Lily-Rose Goodwin"
    ]

    new_users = []

    for user in names:
        firstname, lastname = user.strip().split()
        nu = (
            firstname[:2] + lastname[:2],
            "password",
            firstname,
            lastname,
            firstname + "@email.com",
            lastname + "'s home",
            gen_phone(),
            json.dumps([random.randint(1, 100) for _ in range(3)])
        )
        new_users.append(nu)
    for cdd in new_users:
        u = Users(username=cdd[0],
                  password=cdd[1],
                  firstname=cdd[2],
                  lastname=cdd[3],
                  email=cdd[4],
                  address=cdd[5],
                  tel=cdd[6],
                  cars=cdd[7],
                  )
        u.save()
    return HttpResponse("<p>Inited!</p>")


# show all
def get_user(request):
    ls = Users.objects.all()
    res = ""
    for u in ls:
        res += u.username + " "
    return HttpResponse("<p>" + res + "</p>")


def init_car(request):
    cnames = [
        "Ravinder Maddox",
        "Jagdeep Grant",
        "Cleo William",
        "Evan Bauer",
        "Kaci Sweeney",
        "Darin Mckenna",
        "Levi O'Gallagher",
        "Lennie Hopkins",
        "Ronny Stewart",
        "Kaycee Salinas",
        "Juno Myers",
        "August Howells",
        "Haley Sullivan",
        "Rayan Williams",
        "Rayyan Malone",
        "Nile Houston",
        "Cody Mays",
        "Yassin Davison",
        "Carson Calvert",
        "Carmen Figueroa",
        "Maddison Gates",
        "Ayomide Stuart",
        "Ariya Guerra",
        "Nora Murray",
        "Keanu Ellis",
        "Brook Velasquez",
        "Marlie Houghton",
        "Ezra Nolan",
        "Asha Cuevas",
        "Joel Iles",
        "Blaine Short",
        "Iman Melia",
        "Geoffrey Trevino",
        "Verity Alfaro",
        "Alfie Duncan",
        "Marian Ward",
        "Amar Hollis",
        "Jordan Parra",
        "Ashlee Person",
        "Robbie Horton",
        "Keegan Suarez",
        "Jocelyn Aguilar",
        "Amara Choi",
        "Rayhan Hastings",
        "Lamar Gilbert",
        "Rian Espinoza",
        "Anika Dudley",
        "Rebekah Roth",
        "Lee Morrow",
        "Katerina Burrows",
        "Darcy Christensen",
        "Ada Sadler",
        "Harpreet Stafford",
        "Callan Dickens",
        "Noor Nicholls",
        "Jaiden Page",
        "Teagan Holder",
        "Sami Craig",
        "Emaan Duffy",
        "Reo Cruz",
        "Remi Oconnor",
        "Marissa Plummer",
        "Divine Hendrix",
        "Francis Savage",
        "Shelly Gallegos",
        "Terry Pickett",
        "Gurdeep Broughton",
        "Shayne Wagner",
        "Armani Edwards",
        "Kaisha Stone",
        "Jamie-Leigh Ruiz",
        "Dilan Boyle",
        "Zion Parrish",
        "Katrina Ford",
        "Lenny Mccarthy",
        "Israel Traynor",
        "Tyla Bannister",
        "Reegan Cash",
        "Jaylan O'Doherty",
        "Charley Haynes",
        "Tiegan Mcguire",
        "Amman Bryan",
        "Lennox Guzman",
        "Jaden Rogers",
        "Kacey Carr",
        "Taha Mendoza",
        "Miller Rojas",
        "Billie Oconnell",
        "Brodie Mcnally",
        "Lea Ferguson",
        "Juliet Sweet",
        "Miley Cornish",
        "Reese Wickens",
        "Mica Horner",
        "Jordyn Richmond",
        "Aston Valdez",
        "Camille Chase",
        "Dante Sanders",
        "Tobi Mccann",
        "Tegan Scott",
    ]
    new_cars = []

    for car in cnames:
        carname = car.strip()
        info = {
            'battery': random.randint(1, 100),
            'status': ['idle', 'busy', 'stopped', 'missed'][random.randint(0, 3)]
        }
        nc = (
            carname,
            json.dumps(info),
            json.dumps([random.randint(1, 100) for _ in range(3)])
        )
        new_cars.append(nc)
    for cdd in new_cars:
        c = Cars(carname=cdd[0],
                 info=cdd[1],
                 tasks=cdd[2]
                 )
        c.save()
    return HttpResponse("<p>Inited!</p>")


# show all
def get_car(request):
    ls = Cars.objects.all()
    res = ""
    for u in ls:
        res += u.info + "<br>"
    return HttpResponse("<p>" + res + "</p>")


# creat tasks
def init_task(request):
    new_tasks = []
    name_cdd = ['wondering', 'explore', 'deliver', 'collect']
    if_cdd = ['from a to b', 'from b to c', 'from c to a']
    for _ in range(100):
        nt = (name_cdd[random.randint(0, 3)], if_cdd[random.randint(0, 2)], random.randint(1, 100))
        t = Tasks(taskname=nt[0],
                  info=nt[1],
                  status=nt[2])
        t.save()
    return HttpResponse("<p>Inited!</p>")


# show all
def get_task(request):
    ls = Tasks.objects.all()
    res = ""
    for t in ls:
        res += t.info + "<br>"
    return HttpResponse("<p>" + res + "</p>")
