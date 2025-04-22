import numpy as np
def calculate_logistics_recommend(shipment):
    weight = shipment["weight_lb"]; distance = shipment["distance_mi"]; urgency = shipment.get("urgency", "standard")
    options = []
    if weight < 150: options.append({"mode": "parcel", "cost": round(weight*0.08*distance/100+8, 2), "days": 3 if urgency=="standard" else 1})
    if weight < 10000: options.append({"mode": "ltl", "cost": round(weight*0.04*distance/100+45, 2), "days": 5 if urgency=="standard" else 2})
    options.append({"mode": "ftl", "cost": round(distance*3.2, 2), "days": 2 if urgency=="standard" else 1})
    best = min(options, key=lambda x: x["cost"] if urgency=="standard" else x["days"])
    return {"recommended": best, "all_options": options}
if __name__=="__main__":
    print(calculate_logistics_recommend({"weight_lb": 500, "distance_mi": 800, "urgency": "standard"}))
