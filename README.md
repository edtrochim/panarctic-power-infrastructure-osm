# Pan-Arctic Power Infrastructure from OpenStreetMap

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OSM](https://img.shields.io/badge/data-OpenStreetMap-7EBC6F.svg)](https://www.openstreetmap.org)
[![osm-flex](https://img.shields.io/badge/powered%20by-osm--flex-blue)](https://github.com/osm-flex/osm-flex)

Automated extraction and standardization of power infrastructure data from OpenStreetMap for Arctic energy system analysis using the `osm-flex` Python package.

## 📋 Overview

This repository provides a workflow to extract and standardize power grid infrastructure from OpenStreetMap across Arctic regions. Built on the powerful [`osm-flex`](https://github.com/osm-flex/osm-flex) library, it processes OSM data to create clean, GIS-ready datasets of substations, transmission lines, and support structures.

**Key Features:**
- 🔧 **Built on osm-flex**: Leverages the comprehensive osm-flex extraction library
- 🌍 **Multi-region support**: Alaska, Canada, Greenland, Russia Far East
- 🔌 **Complete infrastructure**: Substations, transmission lines, poles, towers, and more
- 📍 **Geometry standardization**: Converts mixed geometry types to consistent point/line formats
- 🗺️ **Arctic-optimized**: Uses EPSG:3413 (Arctic Polar Stereographic) for accurate calculations
- 📊 **Quality control**: Automated validation and summary statistics
- 📦 **Export formats**: GIS-ready shapefiles for analysis and visualization

## 🎯 Purpose

This tool was developed to support Arctic energy infrastructure research by providing clean, standardized datasets from OpenStreetMap. While OSM is an excellent data source, it requires significant processing to:
- Standardize mixed geometry types (points, polygons, linestrings)
- Filter relevant power infrastructure features
- Transform coordinates for Arctic analysis
- Export to formats suitable for GIS and spatial analysis

The workflow is designed to be reusable for anyone working with Arctic power infrastructure data.

## 🚀 Quick Start

### Google Colab (Recommended)

The easiest way to get started is with the Jupyter notebook:

1. Open `Extract_OSM_data.ipynb` in [Google Colab](https://colab.research.google.com/)
2. Run all cells (Runtime → Run all)
3. Download generated shapefiles from `/root/osm/outputs/`

The notebook includes all dependencies (including `osm-flex`) and setup.

### Local Installation

```bash
# Clone repository
git clone https://github.com/yourusername/panarctic-power-infrastructure-osm.git
cd panarctic-power-infrastructure-osm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install osm-flex and dependencies
pip install -r requirements.txt

# Run extraction
python extract_osm_power_infrastructure.py
```

### About osm-flex

This workflow is built on [`osm-flex`](https://github.com/osm-flex/osm-flex), a powerful Python library for extracting and processing OpenStreetMap data. osm-flex provides:
- Fast PBF file processing
- Flexible feature filtering
- Automatic geometry handling
- Integration with GeoPandas

Learn more at: https://github.com/osm-flex/osm-flex  
License: GPL-3.0

### Command-Line Options

```bash
# Extract all regions (default)
python extract_osm_power_infrastructure.py

# Extract specific regions
python extract_osm_power_infrastructure.py --regions alaska canada

# Specify output directory
python extract_osm_power_infrastructure.py --output ./my_data/osm

# Show all options
python extract_osm_power_infrastructure.py --help
```

## 📊 Data Coverage

### Infrastructure Counts by Region

| Region | Substations | Transmission Lines | Poles & Towers | Last Updated |
|--------|-------------|-------------------|----------------|--------------|
| Alaska | 148 | ~1,090 | ~17,000 | 2024-07 |
| Canada | 5,972 | ~45,000 | ~380,000 | 2024-07 |
| Greenland | 15 | ~50 | ~200 | 2024-07 |
| Russia (Far East) | 3,745 | ~18,000 | ~150,000 | 2024-07 |
| **Total** | **9,880** | **~64,000** | **~547,000** | - |

### Feature Types Extracted

The workflow extracts and processes the following OSM power infrastructure:

**Substations** (`power=substation`):
- High-voltage switching stations
- Distribution substations
- Converter stations
- Standardized to point centroids for spatial analysis

**Transmission Lines** (`power=line`, `power=minor_line`, `power=cable`):
- High-voltage transmission (>100kV)
- Medium-voltage distribution
- Underground cables
- Maintained as linestring geometries with detailed voltage attributes

**Support Structures** (`power=pole`, `power=tower`):
- Transmission towers (lattice, monopole)
- Distribution poles (wood, concrete, steel)
- Portal structures
- Standardized to point locations for density analysis

*Note: Coverage reflects OpenStreetMap data quality as of extraction date. Canada has the most comprehensive infrastructure documentation.*

## 🗂️ Repository Structure

```
panarctic-power-infrastructure-osm/
├── README.md                           # Main documentation
├── Extract_OSM_data.ipynb              # Jupyter notebook workflow
├── extract_osm_power_infrastructure.py # Command-line script
├── requirements.txt                     # Python dependencies
├── CITATION.cff                        # Citation metadata
├── LICENSE                             # MIT License (code only)
├── OSM_DATA_LICENSE.md                 # ⚠️ OSM ODbL license guide (READ THIS!)
├── OSM_ATTRIBUTION_QUICKREF.md         # Quick attribution reference
├── CONTRIBUTING.md                     # Contributor guidelines
├── .gitignore                          # Git ignore rules
├── data/                               # Data directory (git-ignored)
│   ├── osm/
│   │   ├── pbf/                       # Downloaded OSM files
│   │   └── outputs/                   # Generated shapefiles
│   └── README.md                      # Data documentation
├── docs/                              # Additional documentation
│   ├── methodology.md                 # Detailed methodology
│   ├── data_quality.md               # Quality assessment
│   └── gee_integration.md            # Google Earth Engine guide
└── examples/                          # Usage examples
    ├── basic_extraction.py
    └── regional_analysis.py
```

**⚠️ IMPORTANT**: Before using or sharing OSM data, read `OSM_DATA_LICENSE.md` to understand OpenStreetMap's ODbL license requirements.

## 🔧 Methodology

### Core Technology: osm-flex

This workflow is powered by [`osm-flex`](https://github.com/osm-flex/osm-flex), a Python library for efficient OSM data extraction:

```python
import osm_flex.extract as ex

# Extract all power infrastructure
gdf_power = ex.extract_cis('alaska-latest.osm.pbf', 'power')
```

osm-flex handles the complexity of:
- Parsing compressed OSM PBF files
- Extracting features based on OSM tags
- Converting to GeoPandas GeoDataFrames
- Managing mixed geometry types

### Data Sources

OSM data is sourced from [Geofabrik](https://download.geofabrik.de/) regional extracts:

- **Alaska**: `north-america/us/alaska-latest.osm.pbf`
- **Canada**: `north-america/canada-latest.osm.pbf`
- **Greenland**: `north-america/greenland-latest.osm.pbf`
- **Russia Far East**: `russia/far-eastern-fed-district-latest.osm.pbf`

### Processing Pipeline

#### 1. **Download**
Fetch latest OSM PBF files from Geofabrik using automated downloads.

#### 2. **Extract with osm-flex**
Use `osm-flex` to extract all `power=*` features from OSM data:
- Points (poles, towers, generators)
- Polygons (substations, power plants)
- Linestrings (transmission lines, cables)

#### 3. **Filter by Feature Type**
Separate infrastructure into distinct categories:

**Substations**: `power=substation`
- Includes switching stations, distribution substations, converter stations
- Mixed geometries (points and polygons)

**Transmission Lines**: `power IN (line, minor_line, cable)`
- Overhead transmission lines (various voltages)
- Underground cables
- Line geometries with voltage attributes

**Support Structures**: `power IN (pole, tower, portal)`
- Transmission towers (lattice, tubular, guyed)
- Distribution poles (wood, concrete, steel)
- Portal structures
- Point and small polygon geometries

#### 4. **Standardize Geometries**

**For Substations** (convert to centroids):
```python
def convert_to_centroids(gdf, target_crs='EPSG:3413'):
    # Reproject to Arctic Polar Stereographic
    gdf = gdf.to_crs(target_crs)
    # Buffer small geometries, calculate centroids
    gdf['geometry'] = gdf.geometry.centroid
    return gdf
```

**For Poles & Towers** (convert to points):
```python
def standardize_to_points(gdf, target_crs='EPSG:3413'):
    # Handle mixed point/polygon geometries
    # Convert small polygons to centroids
    # Maintain point locations
    return gdf
```

**For Lines** (maintain linestrings):
- Keep original line geometries
- Extract voltage and cable attributes
- Clean and validate line connectivity

#### 5. **Coordinate Transformation**

**EPSG:3413** (NSIDC Sea Ice Polar Stereographic North) is used for processing:
- Accurate distance calculations at high latitudes
- Preserves area and shape in Arctic regions
- Standard for Arctic spatial analysis

Final outputs provided in:
- **EPSG:3413** (for Arctic analysis and least-cost routing)
- **EPSG:4326** (WGS84, for general GIS use)

#### 6. **Export**
Generate shapefiles for each:
- Region-specific datasets (Alaska, Canada, etc.)
- Feature-specific datasets (substations, lines, poles)
- Combined Pan-Arctic dataset
- Summary statistics (CSV)

## 📦 Output Files

The workflow generates the following shapefiles in the output directory:

### Regional Substations
```
outputs/
├── alaska_substations.shp              # Alaska substations (148 features)
├── canada_substations.shp              # Canada substations (5,972 features)
├── greenland_substations.shp           # Greenland substations (15 features)
├── russia_far_east_substations.shp     # Russia substations (3,745 features)
└── panarctic_all_substations.shp       # Combined dataset (9,880 features)
```

### Transmission Lines
```
outputs/
├── alaska_lines.shp                    # Alaska transmission lines
├── canada_lines.shp                    # Canada transmission lines
├── greenland_lines.shp                 # Greenland transmission lines
├── russia_far_east_lines.shp           # Russia transmission lines
└── panarctic_all_lines.shp             # Combined lines dataset
```

### Support Structures (Poles & Towers)
```
outputs/
├── alaska_poles_towers.shp             # Alaska support structures
├── canada_poles_towers.shp             # Canada support structures
├── greenland_poles_towers.shp          # Greenland support structures
├── russia_far_east_poles_towers.shp    # Russia support structures
└── panarctic_all_poles_towers.shp      # Combined structures dataset
```

### Summary Statistics
```
outputs/
└── extraction_summary.csv              # Counts and statistics
```

### Metadata & Attribution

**IMPORTANT**: All generated shapefiles include metadata fields documenting their OSM origin:
- `data_source`: "OpenStreetMap"
- `osm_license`: "ODbL"
- `attribution`: "© OpenStreetMap contributors"

When using these files, always preserve and display this attribution as required by the ODbL license.

### Attribute Schema

#### Substations
| Field | Type | Description |
|-------|------|-------------|
| `osm_id` | Integer | OpenStreetMap feature ID |
| `power` | String | Feature type (always 'substation') |
| `voltage` | String | Voltage level(s) in volts (e.g., '230000;138000') |
| `name` | String | Facility name (if available) |
| `utility` | String | Operating utility/company |
| `region` | String | Region identifier |
| `geometry` | Point | Geographic coordinates |

#### Transmission Lines
| Field | Type | Description |
|-------|------|-------------|
| `osm_id` | Integer | OpenStreetMap feature ID |
| `power` | String | Line type (line, minor_line, cable) |
| `voltage` | String | Voltage level(s) in volts |
| `cables` | Integer | Number of cables/conductors |
| `circuits` | Integer | Number of circuits |
| `location` | String | underground, overhead, underwater |
| `region` | String | Region identifier |
| `geometry` | LineString | Line coordinates |

#### Poles & Towers
| Field | Type | Description |
|-------|------|-------------|
| `osm_id` | Integer | OpenStreetMap feature ID |
| `power` | String | Structure type (pole, tower, portal) |
| `material` | String | Construction material (wood, steel, concrete) |
| `structure` | String | Structure design (lattice, tubular, guyed) |
| `height` | Float | Structure height in meters |
| `region` | String | Region identifier |
| `geometry` | Point | Geographic coordinates |

## 🌐 Use Cases & Integration

This dataset can be used for various Arctic energy analyses:

### Spatial Analysis
- Grid connectivity and clustering analysis
- Service area delineation
- Infrastructure density mapping
- Transmission corridor identification

### GIS Integration
```python
import geopandas as gpd

# Load substations
substations = gpd.read_file('panarctic_all_substations.shp')

# Analyze by region
regional_counts = substations.groupby('region').size()

# Filter by voltage
hv_substations = substations[substations['voltage'].str.contains('230000', na=False)]
```

### Google Earth Engine Integration
Upload shapefiles as Earth Engine assets for:
- Least-cost path analysis
- Proximity analysis with other datasets
- Friction surface development
- Network analysis

```javascript
// Import uploaded asset
var substations = ee.FeatureCollection('users/your-username/panarctic_substations');

// Buffer analysis
var service_areas = substations.map(function(point) {
  return point.buffer(50000);  // 50km service radius
});
```

### QGIS/ArcGIS
- Direct import of shapefiles
- Combine with other Arctic datasets
- Create transmission corridor maps
- Perform network analysis

## 🔗 Related Tools

- **[osm-flex](https://github.com/osm-flex/osm-flex)** - The core extraction library powering this workflow (GPL-3.0)
- **[GeoPandas](https://geopandas.org/)** - Geospatial data manipulation in Python
- **[Geofabrik](https://download.geofabrik.de/)** - OSM regional extract provider
- **[Google Earth Engine](https://earthengine.google.com/)** - Cloud-based geospatial analysis platform

## 🛠️ Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code style
flake8 .
black --check .
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 Data Quality & Limitations

### Known Limitations

- **OSM Completeness**: Coverage varies significantly by region. Canada has excellent coverage while Greenland is limited.
- **Attribute Accuracy**: Voltage, height, and material fields are often missing or inconsistent
- **Temporal Currency**: Data reflects OSM state at extraction time (July 2024)
- **Geometry Precision**: Some features mapped as areas, others as points
- **Russia Data**: Limited validation due to language barriers and accessibility
- **Voltage Ambiguity**: Multiple voltage levels sometimes listed in single field

### Quality Control

The workflow includes automated checks for:
- Geometry validity
- Coordinate system consistency
- Duplicate features
- Missing critical attributes
- Spatial extent validation

See [docs/data_quality.md](docs/data_quality.md) for detailed quality assessment.

### Validation Recommendations

When using this data:
1. Cross-reference with utility company data where available
2. Validate voltage levels for specific substations
3. Check currency of infrastructure (OSM may lag real-world changes)
4. Verify pole/tower counts against aerial imagery
5. Consider regional OSM mapping patterns and biases

## 📄 License

### Code License

This project's **code** (Python scripts, Jupyter notebook, documentation) is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use the code commercially
- ✅ Modify the code
- ✅ Distribute the code
- ✅ Use privately

### OpenStreetMap Data License

**IMPORTANT**: The **extracted data** (shapefiles, GeoDataFrames) is derived from OpenStreetMap and is licensed under the **[Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/)**.

**© OpenStreetMap contributors**

#### ODbL Requirements

When using the extracted OSM data, you **MUST**:

1. **Attribute OpenStreetMap**: 
   - Include: `© OpenStreetMap contributors`
   - Link to: https://www.openstreetmap.org/copyright
   - Example: "Data © OpenStreetMap contributors, ODbL"

2. **Share-Alike**:
   - If you modify or build upon this data, you must distribute the result under ODbL
   - Derivative databases must remain open

3. **Keep Open**:
   - Do not apply additional legal or technical restrictions
   - Data must remain freely accessible

#### Proper Attribution Examples

**In a paper**:
```
Power infrastructure data derived from OpenStreetMap 
(© OpenStreetMap contributors, https://www.openstreetmap.org/copyright, ODbL).
```

**In a map/visualization**:
```
Map data © OpenStreetMap contributors, ODbL
```

**In code/metadata**:
```python
# Data source: OpenStreetMap
# License: Open Database License (ODbL)
# © OpenStreetMap contributors
# https://www.openstreetmap.org/copyright
```

#### What ODbL Means for Your Research

- ✅ You can use the data in research and publications
- ✅ You can create maps, visualizations, and analyses
- ✅ You can combine with other datasets
- ⚠️ You must credit OpenStreetMap contributors
- ⚠️ Modified datasets must be shared under ODbL
- ⚠️ Cannot restrict access to derived data

More info: https://osmfoundation.org/wiki/Licence

### osm-flex Library License

The **osm-flex** library used for data extraction is licensed under **GPL-3.0**.
- Repository: https://github.com/osm-flex/osm-flex
- You are using osm-flex as a library (not modifying it)
- No GPL requirements apply to your MIT-licensed scripts

## 📚 Citation

If you use this workflow or data in your research, please cite:

```bibtex
@software{panarctic_osm_power,
  title={Pan-Arctic Power Infrastructure from OpenStreetMap},
  author={Trochim, Erin},
  year={2025},
  url={https://github.com/yourusername/panarctic-power-infrastructure-osm}
}
```

And acknowledge the underlying data source:
```
Data extracted from OpenStreetMap (© OpenStreetMap contributors, ODbL) 
using osm-flex (GPL-3.0 License).
```

## 🤝 Acknowledgments

- **OpenStreetMap Contributors**: For mapping Arctic infrastructure across thousands of volunteer hours
- **[osm-flex Team](https://github.com/osm-flex/osm-flex)**: For developing and maintaining the excellent osm-flex library (GPL-3.0)
- **[Geofabrik](https://www.geofabrik.de/)**: For providing reliable OSM regional extracts
- **Arctic Research Community**: For data validation, feedback, and use cases

## 📧 Contact

**Author**: Erin Trochim  
**Project Link**: [https://github.com/yourusername/panarctic-power-infrastructure-osm](https://github.com/yourusername/panarctic-power-infrastructure-osm)

For questions, issues, or collaboration opportunities, please use the [GitHub Issues](https://github.com/yourusername/panarctic-power-infrastructure-osm/issues) page.

## 🔗 Links

- [📦 osm-flex Library](https://github.com/osm-flex/osm-flex)
- [🗺️ OpenStreetMap](https://www.openstreetmap.org)
- [📥 Geofabrik Downloads](https://download.geofabrik.de/)
- [🐛 Issue Tracker](https://github.com/yourusername/panarctic-power-infrastructure-osm/issues)
- [💬 Discussions](https://github.com/yourusername/panarctic-power-infrastructure-osm/discussions)

---

<p align="center">
  <i>Supporting Arctic energy research through open data and reproducible methods</i><br>
  <i>Built with osm-flex • Powered by OpenStreetMap</i>
</p>
