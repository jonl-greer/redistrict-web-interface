from fastapi import APIRouter
import geopandas as gpd
import pandas as pd
from .validation import validate_data

router = APIRouter()

@router.get("\demo")

def run_demo():
  gdf1 = gdp.read_file("backend/data/pa_vest_20.zip")
  gdf2 = gdp.read_file("back/data/pa_vtd_2020_bound.zip")
  gdf1 = validate_data(gdf,df)
  return gdf.to_json()

