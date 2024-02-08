# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:00:19 2024

@author: NAMAZIFN
"""

import hypatia




scenario_meta = {
    "blue hydrogen": "blue_hydrogen",
    "ammonia import": "ammonia_import",
    "central offshore": "central_offshore",
    "decentral inland": "decentral_onshore",
    }

def generate_model(scenario:str):
    
    if scenario.lower() not in scenario_meta:
        raise ValueError("Acceptable scenarios are:\n {}".format([*scenario_meta]))
        
    scenario_path = f"scenarios/{scenario_meta[scenario]}"

    
    model = hypatia.Model(
            path = f"{scenario_path}/sets",
            mode = "Planning",
            period_step = 10,
        )
        
    
    model.read_input_data(
            path =  f"{scenario_path}/parameters",
        )

    model.save_dir = f"{scenario_path}/results"
    
    
    return model


if __name__ == "__main__":
    
    for scenario in scenario_meta:
        
        model = generate_model(scenario)
        model.run(solver="gurobi")
        model.to_csv(model.save_dir,sep=";")
    
     
