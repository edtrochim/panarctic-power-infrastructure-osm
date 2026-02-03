# OpenStreetMap Data: Complete Documentation

## 📚 What Was Added

Your repository now has **comprehensive OpenStreetMap data licensing documentation**:

### 1. **OSM_DATA_LICENSE.md** (Main Guide)
Complete 300+ line guide covering:
- ✅ Full ODbL license explanation
- ✅ Attribution requirements and examples
- ✅ Share-alike requirements (when they apply)
- ✅ Common use cases (maps, research, databases)
- ✅ Academic publishing guidance
- ✅ FAQ section
- ✅ Official resource links

### 2. **OSM_ATTRIBUTION_QUICKREF.md** (Quick Reference)
One-page quick reference for:
- ⚡ Minimum required attribution
- ⚡ Common use cases
- ⚡ Attribution examples (maps, papers, code, web)
- ⚡ Common mistakes to avoid
- ⚡ Links to full documentation

### 3. **Enhanced README.md**
Completely rewritten license section with:
- 📝 Clear separation: code (MIT) vs. data (ODbL)
- 📝 Detailed ODbL requirements
- 📝 Multiple attribution examples
- 📝 What ODbL means for researchers
- 📝 Note about osm-flex (GPL-3.0)

### 4. **Updated Notebook**
Modified `export_to_shapefile()` function:
- 🔧 Automatically adds OSM attribution fields to ALL shapefiles
- 🔧 Fields: `osm_src`, `osm_lic`, `osm_attr`
- 🔧 Ensures compliance with ODbL requirements
- 🔧 Documented in function docstring

---

## ⚖️ Three Licenses in Your Repository

Your repository involves **three different licenses**:

### 1. Your Code: MIT License ✅
```
Files: Python scripts, Jupyter notebook, documentation
License: MIT
Copyright: Erin Trochim, 2025
Freedom: Use, modify, distribute freely
```

### 2. osm-flex Library: GPL-3.0 ✅
```
Software: osm-flex (dependency)
License: GPL-3.0
URL: https://github.com/osm-flex/osm-flex
Impact: None (you're using as library, not modifying)
```

### 3. OSM Data: ODbL ⚠️
```
Data: All extracted power infrastructure
License: Open Database License (ODbL)
Copyright: © OpenStreetMap contributors
Requirements: Attribution, Share-alike, Keep open
```

---

## 🔑 Key ODbL Requirements

### Always Required
✅ **Attribution**: Credit "© OpenStreetMap contributors"  
✅ **Link**: https://www.openstreetmap.org/copyright  
✅ **License Name**: Mention "ODbL"

### Share-Alike (When Distributing Modified Data)
⚠️ **Modified databases**: Must share under ODbL  
⚠️ **Enhanced datasets**: Must remain open  
⚠️ **Combined databases**: ODbL applies to whole

### Not Required for "Produced Works"
✅ **Maps/visualizations**: Can be proprietary  
✅ **Analysis results**: Don't need share-alike  
✅ **Statistics**: Normal copyright applies

---

## 📊 Your Shapefiles

### What They Include (Automatically)

Every shapefile exported by this workflow now includes:

| Field | Value | Purpose |
|-------|-------|---------|
| `osm_src` | "OpenStreetMap" | Data source |
| `osm_lic` | "ODbL" | License identifier |
| `osm_attr` | "© OSM contributors" | Attribution text |

### How to Use Them

**For maps/visualizations:**
```
Just add: © OpenStreetMap contributors
(Your map doesn't need to be ODbL)
```

**For sharing data files:**
```
Must: License under ODbL
Must: Credit OpenStreetMap
Must: Link to copyright page
Must: Keep data accessible
```

**For research papers:**
```
Methods: "Data from OpenStreetMap (© OSM contributors, ODbL)"
Supplementary data: Must be ODbL if shared
Analysis/results: Normal copyright
```

---

## 📋 Attribution Examples

### In Your Paper
```
Power infrastructure locations were obtained from OpenStreetMap 
(© OpenStreetMap contributors, https://www.openstreetmap.org/copyright, 
licensed under ODbL).
```

### In a Map
```
© OpenStreetMap contributors
```

### In Code Comments
```python
# Data: OpenStreetMap © OSM contributors, ODbL
# https://www.openstreetmap.org/copyright
```

### On Website
```html
Data © <a href="https://www.openstreetmap.org/copyright">
OpenStreetMap contributors</a>, ODbL
```

---

## ✅ Compliance Checklist

When using this workflow's outputs:

- [ ] I've read `OSM_DATA_LICENSE.md`
- [ ] I understand ODbL requirements
- [ ] I've included OSM attribution
- [ ] I've linked to https://www.openstreetmap.org/copyright
- [ ] If sharing data, I'm using ODbL license
- [ ] If making maps, I've added "© OSM contributors"
- [ ] I'm not restricting access to OSM-derived data

---

## 📖 Where to Find Information

### Quick Questions
→ `OSM_ATTRIBUTION_QUICKREF.md` (one-page reference)

### Detailed Information
→ `OSM_DATA_LICENSE.md` (comprehensive guide)

### Official Resources
- ODbL License: https://opendatacommons.org/licenses/odbl/1-0/
- OSM Copyright: https://www.openstreetmap.org/copyright
- OSM FAQ: https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ

---

## 🎯 Summary

Your repository now provides:

✅ **Clear license documentation** (code vs. data)  
✅ **Comprehensive ODbL guidance**  
✅ **Automatic attribution** in shapefiles  
✅ **Quick reference** for common cases  
✅ **Academic publishing** guidance  
✅ **Multiple examples** for different uses  

**Result**: Anyone using this workflow understands their OSM data obligations! 🌍

---

## ⚠️ Common Questions

**Q: Can I use this data commercially?**  
A: Yes! ODbL allows commercial use with attribution.

**Q: Do I need to make my maps ODbL?**  
A: No! Maps are "produced works" and can use any license.

**Q: What if I only use a few data points?**  
A: Still attribute. All OSM data requires attribution.

**Q: Can I combine with proprietary data?**  
A: Yes, but if you share the combined database, it must be ODbL.

**Q: What about the shapefiles this workflow creates?**  
A: They contain OSM data, so they're ODbL. Attribution is automatic.

---

**When in doubt: Attribute OpenStreetMap and keep data open!**
