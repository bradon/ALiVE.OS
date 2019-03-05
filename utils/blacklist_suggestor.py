#!/usr/bin/env python3

"""Suggest new objects to add to the blacklist"""

import argparse


class Category_Count(object):
    """Counters for object blacklistings and uses"""
    
    def __init__(self):
        self.blacklist_count=0
        self.used_count=0
    def blacklist(self):
        self.blacklist_count=self.blacklist_count+1
    def use(self):
        self.used_count = self.used_count+1
    def get_blacklist_count(self):
        return self.blacklist_count
    def get_used_count(self):
        return self.used_count

def grab_section(source, start_section, end_section):
    first_occurance=source.find(start_section)
    if first_occurance == -1:
        return ''
    a =first_occurance+len(start_section)
    b =source[a:-1].find(end_section)
    return source[a:a+b]

def grab_list(source, start_section, end_section):
    a = grab_section(source, start_section, end_section)
    return a.replace('\n','').replace(' ','').split(',')

def add_to_blacklist(object_list,object_dictionary=dict()):
    if object_list[0] == '':
        return
    for l in object_list:
        l_strip = l[l.rfind("\\")+1:-1].replace('.p3d','')
        if not l_strip in object_dictionary:
            object_dictionary[l_strip]=Category_Count()
        object_dictionary[l_strip].blacklist()

def add_to_usedlist(object_list,object_dictionary=dict()):
    if object_list[0] == '':
        return
    for l in object_list:
        l_strip = l[l.rfind("\\")+1:-1].replace('.p3d','')
        if not l_strip in object_dictionary:
            object_dictionary[l_strip]=Category_Count()
        object_dictionary[l_strip].use()

def process_objects(source, object_dictionary=dict()):
    blacklist_start="ALIVE_Indexing_Blacklist = ALIVE_Indexing_Blacklist + ["
    mil_start="ALIVE_militaryBuildingTypes = ALIVE_militaryBuildingTypes + ["
    mil_park_start="ALIVE_militaryParkingBuildingTypes = ALIVE_militaryParkingBuildingTypes + ["
    mil_sup_start="ALIVE_militarySupplyBuildingTypes = ALIVE_militarySupplyBuildingTypes + ["
    mil_hq_start="ALIVE_militaryHQBuildingTypes = ALIVE_militaryHQBuildingTypes + ["
    air_start="ALIVE_airBuildingTypes = ALIVE_airBuildingTypes + ["
    mil_air_start="ALIVE_militaryAirBuildingTypes = ALIVE_militaryAirBuildingTypes + ["
    civ_air_start="ALIVE_civilianAirBuildingTypes = ALIVE_civilianAirBuildingTypes + ["
    heli_start="ALIVE_heliBuildingTypes = ALIVE_heliBuildingTypes + ["
    mil_heli_start="ALIVE_militaryHeliBuildingTypes = ALIVE_militaryHeliBuildingTypes + ["
    civ_heli_start="ALIVE_civilianHeliBuildingTypes = ALIVE_civilianHeliBuildingTypes + ["
    civ_pop_start="ALIVE_civilianPopulationBuildingTypes = ALIVE_civilianPopulationBuildingTypes + ["
    civ_hq_start="ALIVE_civilianHQBuildingTypes = ALIVE_civilianHQBuildingTypes + ["
    civ_settle_start="ALIVE_civilianSettlementBuildingTypes = ALIVE_civilianSettlementBuildingTypes + ["
    civ_power_start="ALIVE_civilianPowerBuildingTypes = ALIVE_civilianPowerBuildingTypes + ["
    civ_comms_start="ALIVE_civilianCommsBuildingTypes = ALIVE_civilianCommsBuildingTypes + ["
    civ_marine_start="ALIVE_civilianMarineBuildingTypes = ALIVE_civilianMarineBuildingTypes + ["
    civ_rail_start="ALIVE_civilianRailBuildingTypes = ALIVE_civilianRailBuildingTypes + ["
    civ_fuel_start="ALIVE_civilianFuelBuildingTypes = ALIVE_civilianFuelBuildingTypes + ["
    civ_con_start="ALIVE_civilianConstructionBuildingTypes = ALIVE_civilianConstructionBuildingTypes + ["
    usedlist_list=[mil_start,mil_park_start,mil_sup_start,mil_hq_start,air_start,mil_air_start,civ_air_start,
                   heli_start,mil_heli_start,civ_heli_start,civ_pop_start,civ_hq_start,civ_settle_start,
                  civ_power_start,civ_comms_start,civ_marine_start,civ_rail_start,civ_fuel_start,civ_con_start]
    add_to_blacklist(grab_list(source, blacklist_start,']'), object_dictionary)
    for i in usedlist_list:
        add_to_usedlist(grab_list(source, i, ']'),object_dictionary)

def do_file(filename, a=dict()):
    file = open(filename, 'r')
    file_contents=file.read()
    process_objects(file_contents, a)

def main():
    parser = argparse.ArgumentParser(description='Suggest objects to add to the blacklist. I suggest piping output to a file with >> filename')
    parser.add_argument('--alivepath', nargs=1, default="P:/x/alive/", help='Path to alive. Defaults tp P:/x/alive/, the standard dev setup')
    parser.add_argument('--minblacklist', nargs=1, default = 1, help='only suggest objects if they are blacklisted in this number of indexes, default 1')
    parser.add_argument('--maxused', nargs=1, default = 0, help='do not usggest objects if they are used this number of times, default 0')
    args = parser.parse_args()
    path_alive = args.alivepath
    path_static_data = path_alive + "addons/main/static/"
    path_existing_blacklist = path_alive + "alive_object_blacklist.txt"
    import os
    a=dict()
    for file in os.listdir(path_static_data):
        if file.endswith(".sqf"):
            if file != 'staticData.sqf':
                do_file(path_static_data+file,a)

    for key in a.keys():
        if (a[key].get_blacklist_count()>= args.minblacklist) and (a[key].get_used_count()<=1):
            print(key)
        
if __name__ == "__main__":
    main()
