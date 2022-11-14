from pyramid.view import view_config
import json, random

@view_config(route_name='home', renderer='isekai_title_generator:templates/mytemplate.jinja2')
def my_view(request):

    json_file = open("data.json", "r")
    data = json.load(json_file)

    obj_list = data["objects"]
    verb_list = data["verb"]
    adj_list = data["adj"]
    loc_list = data["location"] 


    x = random.randint(1, 3)

    if x == 1:
        act_obj = random.choice(obj_list)
        act_adj = random.choice(adj_list)
        return {"title": "That Time I Got Reincarnated As A " + act_adj + " " + act_obj}

    if x == 2:
        act_obj = random.choice(obj_list)
        act_loc = random.choice(loc_list)
        return {"title": "Yeah, I Got Reincarnated " + act_loc + " As A " + act_obj + ", So What?"} 

    if x == 3:
        act_obj = random.choice(obj_list)
        act_verb = random.choice(verb_list)
        return {"title": "Hurray! I Have Left My Meaningless Life Behind To Become The " + act_verb + " " + act_obj}
