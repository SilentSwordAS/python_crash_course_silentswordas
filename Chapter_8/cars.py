def car_info(manufacturer, model, **add_info):
    add_info["manufacturer's name"] = manufacturer
    add_info["model_name"] = model
    return add_info

print(car_info("subaru","outback",color="blue",tow_package=True))