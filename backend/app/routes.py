from fastapi import APIRouter
from pathlib import Path
import geopandas as gpd
import pandas as pd
from .validation import validate_data

router = APIRouter()
DATA_DIR = Path(__file__).parent.parent / "data"
@router.get("/demo")

def run_demo():
  election = gpd.read_file(DATA_DIR / "pa_vest_20.zip")
  precincts = gpd.read_file(DATA_DIR / "pa_vtd_2020_bound.zip")
  result = validate_data(precincts,election)
  return result.to_json()

