# OpenStreetMap Data License & Attribution Guide

## 📋 Overview

All power infrastructure data extracted by this workflow is derived from **OpenStreetMap (OSM)** and is subject to the **Open Database License (ODbL)**.

**© OpenStreetMap contributors**

## ⚖️ Open Database License (ODbL)

Full license: https://opendatacommons.org/licenses/odbl/1-0/

### Key Points

The ODbL is a **"share-alike"** license for databases. It allows you to:

✅ **Use**: Access, use, and download the data  
✅ **Modify**: Create derivative works and modifications  
✅ **Distribute**: Share and redistribute the data  
✅ **Commercial Use**: Use data for commercial purposes  

**BUT** you must:

⚠️ **Attribute**: Give credit to OpenStreetMap contributors  
⚠️ **Share-Alike**: Distribute modifications under ODbL  
⚠️ **Keep Open**: Don't restrict access with additional terms  

## 📝 Attribution Requirements

### What You Must Include

Every use of OSM data must include:

1. **Copyright notice**: `© OpenStreetMap contributors`
2. **License identifier**: `ODbL` or link to license
3. **Link to copyright page**: https://www.openstreetmap.org/copyright

### Attribution Examples

#### In Research Papers

```
Pan-Arctic power infrastructure locations were extracted from OpenStreetMap 
(© OpenStreetMap contributors, https://www.openstreetmap.org/copyright), 
licensed under the Open Database License (ODbL).
```

#### In Map Visualizations

```
Map data © OpenStreetMap contributors, ODbL
```

#### In Data Files/Metadata

```yaml
source: OpenStreetMap
copyright: © OpenStreetMap contributors
license: Open Database License (ODbL)
license_url: https://opendatacommons.org/licenses/odbl/1-0/
attribution_url: https://www.openstreetmap.org/copyright
```

#### On Websites/Apps

```html
<p>Data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>, 
ODbL</p>
```

#### In GIS Software

When exporting maps or creating visualizations:
- Add text box: "© OpenStreetMap contributors, ODbL"
- Include in legend or map margin
- Add to metadata/description fields

## 🔄 Share-Alike Requirements

### When Share-Alike Applies

You must share modifications under ODbL when you:

- ❗ Add new attributes to OSM data
- ❗ Correct or update OSM data
- ❗ Combine OSM data with other data to create a new database
- ❗ Create a substantial derivative of the OSM database

### When Share-Alike Does NOT Apply

You do NOT need to share under ODbL when you:

- ✅ Create maps or visualizations (these are "produced works")
- ✅ Perform analysis and share results/statistics
- ✅ Use OSM data as input to models/algorithms
- ✅ Extract subsets without modification
- ✅ Simply change the format (e.g., shapefile → GeoJSON)

### How to Share Modifications

If you modify the data:

1. **Document changes**: Describe what you modified
2. **License under ODbL**: State that modified data is ODbL
3. **Make available**: Provide access to modified database
4. **Attribute original**: Still credit OpenStreetMap

Example:
```
This dataset is based on OpenStreetMap data (© OpenStreetMap contributors, ODbL).
Modifications include: [describe your changes].
Modified data is available at: [URL] and is licensed under ODbL.
```

## 📊 Common Use Cases

### ✅ Allowed Without Share-Alike

**Creating Maps**:
```
You can create maps using OSM data without licensing your map under ODbL.
Attribution required: Yes
Share-alike: No (maps are "produced works")
```

**Research Analysis**:
```
You can analyze OSM data and publish results/statistics.
Attribution required: Yes
Share-alike: No (analysis results are not a database)
```

**Combining with Other Data for Analysis**:
```
You can combine OSM with other datasets for analysis.
Attribution required: Yes
Share-alike: Only if you distribute the combined database
```

### ⚠️ Requires Share-Alike

**Distributing Enhanced Database**:
```
If you add attributes (e.g., operating hours, ownership) and share the enhanced database.
Attribution required: Yes
Share-alike: Yes (must distribute under ODbL)
```

**Creating Improved/Corrected Dataset**:
```
If you correct errors and distribute the corrected dataset.
Attribution required: Yes
Share-alike: Yes (must distribute under ODbL)
```

## 🌐 This Workflow's Outputs

### What This Workflow Does

This workflow:
1. Extracts power infrastructure from OSM using osm-flex
2. Filters for specific feature types (substations, lines, poles)
3. Standardizes geometries (polygons → centroids)
4. Transforms coordinate systems (EPSG:3413, EPSG:4326)
5. Exports to shapefiles

### Attribution for This Workflow's Outputs

When using shapefiles from this workflow, you must attribute:

**OpenStreetMap** (for the data):
```
Data © OpenStreetMap contributors, ODbL
https://www.openstreetmap.org/copyright
```

**This Workflow** (optional but appreciated):
```
Extracted using panarctic-power-infrastructure-osm
https://github.com/yourusername/panarctic-power-infrastructure-osm
```

### Is This a Derivative Database?

The workflow outputs are:
- ✅ **Substantial extracts** of OSM data (specific geographic regions)
- ✅ **Filtered** for specific features (power infrastructure)
- ✅ **Transformed** geometries and coordinates
- ⚠️ **Still subject to ODbL** as a derivative database

If you distribute these shapefiles **as data files**, they must be:
- Attributed to OpenStreetMap
- Licensed under ODbL
- Kept open and accessible

If you use them to **create maps/analysis**, those outputs are "produced works" and do not require ODbL licensing.

## 🎓 Academic Use

### Publishing Research

**In your paper**:
- Attribute OSM in methods section
- Include in acknowledgments
- Add to data availability statement

**Example methods section**:
```
Power infrastructure locations were obtained from OpenStreetMap 
(© OpenStreetMap contributors, licensed under ODbL, 
https://www.openstreetmap.org/copyright). Data was extracted 
using osm-flex and filtered for substations, transmission lines, 
and support structures across Alaska, Canada, Greenland, and 
Russia's Far Eastern Federal District.
```

**Data Availability Statement**:
```
Source data from OpenStreetMap is available at 
https://www.openstreetmap.org under the Open Database License (ODbL). 
Processed datasets are available from the authors upon request.
```

### Supplementary Data

If you publish the extracted shapefiles as supplementary data:
- ✅ Include OSM attribution in README
- ✅ License as ODbL (required)
- ✅ Link to OpenStreetMap copyright page
- ✅ Document processing steps

## 🔗 Additional Resources

- **ODbL Full Text**: https://opendatacommons.org/licenses/odbl/1-0/
- **OSM Copyright**: https://www.openstreetmap.org/copyright
- **OSM License FAQ**: https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ
- **Attribution Guidelines**: https://wiki.osmfoundation.org/wiki/Licence/Attribution_Guidelines

## ❓ Common Questions

### Can I use OSM data commercially?
**Yes**, the ODbL allows commercial use with attribution.

### Do I need to pay for OSM data?
**No**, OSM data is free to use.

### Can I restrict access to maps I create?
**Yes**, maps are "produced works" and can be restricted. The underlying data cannot.

### Can I combine OSM with proprietary data?
**Yes**, but if you distribute the combined database, it must be under ODbL.

### What if I only use a few data points?
**Still attribute**. All use of OSM data requires attribution, regardless of quantity.

### Can I add OSM data to Google Maps/ArcGIS Online?
**Yes**, but ensure attribution is visible and data remains accessible.

## 📧 Questions?

For legal questions about OSM licensing:
- OSM Legal FAQ: https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ
- OSMF License Working Group: https://wiki.osmfoundation.org/wiki/Licence

For questions about this workflow:
- GitHub Issues: https://github.com/yourusername/panarctic-power-infrastructure-osm/issues

---

**Remember**: When in doubt, attribute OpenStreetMap contributors and keep data open! 🌍
