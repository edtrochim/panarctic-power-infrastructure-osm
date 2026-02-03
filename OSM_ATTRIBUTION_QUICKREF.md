# Quick Reference: OpenStreetMap Data Attribution

## ⚡ Quick Facts

- **License**: Open Database License (ODbL)
- **Copyright**: © OpenStreetMap contributors
- **Link**: https://www.openstreetmap.org/copyright

## ✅ Minimum Required Attribution

**Every use of OSM data must include:**

```
© OpenStreetMap contributors
```

**Better attribution:**

```
Data © OpenStreetMap contributors, ODbL
https://www.openstreetmap.org/copyright
```

## 📊 Common Use Cases

### Creating Maps
```
✅ Allowed without share-alike
⚠️ Must include: "© OpenStreetMap contributors"
📍 Location: On map, in legend, or caption
```

### Publishing Data
```
⚠️ Requires share-alike (ODbL)
⚠️ Must include: "© OpenStreetMap contributors, ODbL"
⚠️ Must link: https://www.openstreetmap.org/copyright
⚠️ Must keep data open and accessible
```

### Research Papers
```
✅ Analysis results do not require share-alike
⚠️ Must attribute in methods section
⚠️ If sharing processed data, must use ODbL
```

## 🔧 This Workflow

### What It Does
- Extracts OSM power infrastructure data
- Processes and standardizes geometries
- Exports to shapefiles

### Attribution in Outputs
All shapefiles include metadata fields:
- `osm_src`: "OpenStreetMap"
- `osm_lic`: "ODbL"
- `osm_attr`: "© OSM contributors"

### When Using These Shapefiles

**If you create maps/visualizations:**
```
Minimum: © OpenStreetMap contributors
Better: Data © OpenStreetMap contributors, ODbL
```

**If you share the shapefiles:**
```
Required: License under ODbL
Required: Credit OpenStreetMap
Required: Link to copyright page
Required: Keep data open
```

## 📝 Attribution Examples

### In a Map
```
© OpenStreetMap contributors
```

### In a Paper
```
Power infrastructure data from OpenStreetMap (© OpenStreetMap 
contributors, https://www.openstreetmap.org/copyright, ODbL).
```

### In Code
```python
# Data: OpenStreetMap © OSM contributors, ODbL
# https://www.openstreetmap.org/copyright
```

### On a Website
```html
Data © <a href="https://www.openstreetmap.org/copyright">
OpenStreetMap contributors</a>, ODbL
```

## ⚠️ Common Mistakes

❌ **Forgetting attribution entirely**  
✅ Always credit OpenStreetMap

❌ **Attributing to Google Maps or other providers**  
✅ Attribute to OpenStreetMap contributors

❌ **Only crediting osm-flex or this workflow**  
✅ Must credit OpenStreetMap (the data source)

❌ **Restricting access to modified OSM data**  
✅ Keep data open and share under ODbL

## 🔗 More Information

**Full guide**: See `OSM_DATA_LICENSE.md` in this repository

**Official resources**:
- ODbL License: https://opendatacommons.org/licenses/odbl/1-0/
- OSM Copyright: https://www.openstreetmap.org/copyright
- OSM License FAQ: https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ

## 🎯 Remember

1. **Always attribute**: © OpenStreetMap contributors
2. **Link when possible**: https://www.openstreetmap.org/copyright
3. **Share-alike for databases**: Modified data must be ODbL
4. **Maps are free**: Visualizations don't need share-alike
5. **Keep it open**: Don't restrict access to OSM-derived data

---

**When in doubt, attribute OpenStreetMap! 🌍**
