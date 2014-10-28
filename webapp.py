from flask import Flask, render_template, request
from random import choice, sample
import jinja2


app = Flask(__name__)

@app.route("/")
def show_form():
    # return the rendered index.html
    return render_template("index.html")

@app.route("/select")
def select_set():

    name1 = request.args.get("name1")
    name2 = request.args.get("name2")
    name3 = request.args.get("name3")
    name4 = request.args.get("name4")

    job1 = request.args.get("job1")
    job2 = request.args.get("job2")
    job3 = request.args.get("job3")
    job4 = request.args.get("job4")

    car1 = request.args.get("car1")
    car2 = request.args.get("car2")
    car3 = request.args.get("car3")
    car4 = request.args.get("car4")

    city1 = request.args.get("city1")
    city2 = request.args.get("city2")
    city3 = request.args.get("city3")
    city4 = request.args.get("city4")

    if not name1 or not name2 or not name3 or not name4 or not job1 or not job2 or not job3 or not job4 or not car1 or not car2 or not car3 or not car4 or not city1 or not city2 or not city3 or not city4:
      return "What's wrong, is your imagination broken?"

    name_list = [name1, name2, name3, name4]
    job_list = [job1, job2, job3, job4]
    car_list = [car1, car2, car3, car4]
    city_list = [city1, city2, city3, city4]
    mash_list = ["a huge mansion", " a tiny apartment", "a crappy shack", "a decently-sized house"]

    rand_name = choice(name_list)
    rand_job = choice(job_list)
    rand_car = choice(car_list)
    rand_city = choice(city_list)
    rand_mash = choice(mash_list)

    return render_template("form.html", name = rand_name,
                                        job = rand_job,
                                        car = rand_car,
                                        city = rand_city,
                                        mash = rand_mash)

#add button to try again with same parameters
#

# def joel():
#     all = []
#     all.extend([mash1, msh2, mash3, mash4])
#     all.exnted([lover1, lover2, lover3, lover4])
    # =>  all = [mash1, mash2 ..., lover3, lover4... city4] 

    #loop 16x
    #  count 3, set = None
    # [Non, None, None, Ringo, | None, None, SF, None, | ]


# @app.route("/reducelist")
# def reduce_list():

#   name1 = request.args.get("name1")
#   name2 = request.args.get("name2")
#   name3 = request.args.get("name3")
#   name4 = request.args.get("name4")

#   job1 = request.args.get("job1")
#   job2 = request.args.get("job2")
#   job3 = request.args.get("job3")
#   job4 = request.args.get("job4")

#   car1 = request.args.get("car1")
#   car2 = request.args.get("car2")
#   car3 = request.args.get("car3")
#   car4 = request.args.get("car4")

#   city1 = request.args.get("city1")
#   city2 = request.args.get("city2")
#   city3 = request.args.get("city3")
#   city4 = request.args.get("city4")




#   allthings = [name1, name2, name3, name4, job1, job2, job3, job4, car1, car2, car3, car4, city1, city2, city3, city4]
#   # # allthings = ["john", "joe", "bob", "fred", "waiter", "dog-walker", "teacher", "host"]

#   # make list of lists and detect when one inner list has only 1 element
#   x = 3

#   inc = x

#   while len(allthings) > 4:
#       if x < len(allthings):
#           allthings.pop(x)
#           x = x + inc
#       else:
#           x = (len(allthings) / 4)-1
#           inc = inc - 1

#   lover = allthings[0]

#   job = allthings[1]

#   car = allthings[2]

#   city = allthings[3]

#   return render_template("form.html", name1 = name1, job1 = job1)

#   "hey %s, %s, %s, %s" % (name1, job1, car1, city1)

    # myString = ",".join(allthings)
    # return myString

if __name__ == "__main__":
    app.run(debug=True)






