private["_worldName"];
 _worldName = tolower(worldName);
 ["SETTING UP MAP: cup_kunduz"] call ALiVE_fnc_dump;
 ALIVE_Indexing_Blacklist = [];
 ALIVE_airBuildingTypes = [];
 ALIVE_militaryParkingBuildingTypes = [];
 ALIVE_militarySupplyBuildingTypes = [];
 ALIVE_militaryHQBuildingTypes = [];
 ALIVE_militaryAirBuildingTypes = [];
 ALIVE_civilianAirBuildingTypes = [];
 ALiVE_HeliBuildingTypes = [];
 ALIVE_militaryHeliBuildingTypes = [];
 ALIVE_civilianHeliBuildingTypes = [];
 ALIVE_militaryBuildingTypes = [];
 ALIVE_civilianPopulationBuildingTypes = [];
 ALIVE_civilianHQBuildingTypes = [];
 ALIVE_civilianPowerBuildingTypes = [];
 ALIVE_civilianCommsBuildingTypes = [];
 ALIVE_civilianMarineBuildingTypes = [];
 ALIVE_civilianRailBuildingTypes = [];
 ALIVE_civilianFuelBuildingTypes = [];
 ALIVE_civilianConstructionBuildingTypes = [];
 ALIVE_civilianSettlementBuildingTypes = [];
 if(tolower(_worldName) == "cup_kunduz") then {
ALIVE_militaryBuildingTypes = ALIVE_militaryBuildingTypes + ["airport_tower","radar","bunker","cargo_house_v","cargo_patrol_","research","mil_wall","fortification","razorwire","dome","deerstand","vez"];
ALIVE_militaryParkingBuildingTypes = ALIVE_militaryParkingBuildingTypes + ["bunker","cargo_house_v","cargo_patrol_","research","bunker"];
ALIVE_militarySupplyBuildingTypes = ALIVE_militarySupplyBuildingTypes + ["barrack","cargo_hq_","miloffices","cargo_house_v","cargo_patrol_","research","barrack","mil_house","mil_controltower"];
ALIVE_militaryHQBuildingTypes = ALIVE_militaryHQBuildingTypes + ["barrack","cargo_hq_","miloffices","cargo_tower","barrack","mil_house","mil_controltower"];
ALIVE_airBuildingTypes = ALIVE_airBuildingTypes + ["hangar","hangar"];
ALIVE_civilianAirBuildingTypes = ALIVE_civilianAirBuildingTypes + ["hangar","runway_beton","runway_main","runway_secondary","ss_hangar","hangar_2","hangar","runway_beton","runway_end","runway_main","runway_secondary"];
ALIVE_civilianPopulationBuildingTypes = ALIVE_civilianPopulationBuildingTypes + ["church","hospital","amphitheater","chapel_v","households","hospital","houseblock","generalstore","house"];
ALIVE_civilianHQBuildingTypes = ALIVE_civilianHQBuildingTypes + ["offices","a_office01","a_office02","a_municipaloffice"];
ALIVE_civilianSettlementBuildingTypes = ALIVE_civilianSettlementBuildingTypes + ["church","hospital","amphitheater","chapel_v","households","hospital","houseblock","generalstore","house"];
ALIVE_civilianPowerBuildingTypes = ALIVE_civilianPowerBuildingTypes + ["dp_main","spp_t","pec_","powerstation","trafostanica"];
ALIVE_civilianCommsBuildingTypes = ALIVE_civilianCommsBuildingTypes + ["communication_f","ttowerbig_","illuminanttower","vysilac_fm","telek","tvtower"];
ALIVE_civilianMarineBuildingTypes = ALIVE_civilianMarineBuildingTypes + ["crane","lighthouse","nav_pier","pier_","crane","lighthouse","nav_pier","pier_","pier"];
ALIVE_civilianRailBuildingTypes = ALIVE_civilianRailBuildingTypes + ["rail_house","rail_station","rail_platform","rails_bridge","stationhouse"];
ALIVE_civilianFuelBuildingTypes = ALIVE_civilianFuelBuildingTypes + ["fuelstation","dp_bigtank","fuelstation","expedice","indpipe","komin","ind_stack_big","ind_tankbig","fuel_tank_big"];
ALIVE_civilianConstructionBuildingTypes = ALIVE_civilianConstructionBuildingTypes + ["wip","bridge_highway","ind_mlyn_01","ind_pec_01","wip","sawmillpen","workshop"];
};
