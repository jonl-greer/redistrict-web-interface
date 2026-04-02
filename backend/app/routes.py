from fastapi import APIRouter
import geopandas as gpd
import pandas as pd
from .validation import validate_data

router = APIRouter()

@router.get("/demo")

def run_demo():
  election = gpd.read_file("zip:///data/pa_vest_20.zip")
  precincts = gpd.read_file("zip:///data/pa_vtd_2020_bound.zip")
  result = validate_data(precints,elections)
  return result.to_json()

