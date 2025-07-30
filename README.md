# Space Launch Cost per kg to LEO

A simple Python script that compares launch cost per kilogram for five rockets.
It shows you a bar chart 

## Motivation
The cost per kilogram is a key metric for satellite operators, investors, and launch providers, and I like Space.

## Data Source
CSIS Aerospace Security Project  
(https://aerospace.csis.org/data/space-launch-to-low-earth-orbit-how-much-does-it-cost/)

## Files
- `cost_per_kg_chart.py`: the plotting script

## How to run
```bash
pip install -r requirements.txt
python cost_per_kg_chart.py

## Methodology

1. **Data collection**  
   Pulled cost-per-kg figures from the CSIS Aerospace Security Project.  
2. **Data processing**  
   Manually selected five recent launch vehicles and built a small DataFrame.  
3. **Visualization**  
   Created a clean, annotated bar chart in Matplotlib with ggplot styling.

## Key Insights

- **Falcon Heavy** at \$1,500/kg is by far the cheapest—thanks to reusability.  
- **Minotaur IV** at \$30,500/kg is the most expensive, reflecting its niche government role.  
- Mid‑range rockets like **Angara** and **Long March 5** land around \$4,500–7,900/kg.

- **Reusability wins:** SpaceX’s Falcon 9/Falcon Heavy reusable first stages have reduced launch costs, showing how reusability is transforming the economics of space access.  

## Next Steps

- Automate data fetching from the OWID/CSIS CSV.  
- Expand to more rockets and plot cost vs. year to show trends.  
- Build an interactive dashboard in Plotly or Streamlit for live filtering.
