#!/usr/bin/env python3
"""
Extract OSM Power Infrastructure for Pan-Arctic Analysis

This script downloads and processes OpenStreetMap data for power infrastructure
across Arctic regions using the osm-flex library (https://github.com/osm-flex/osm-flex).

Extracts:
- Substations (power=substation)
- Transmission lines (power=line|minor_line|cable)
- Support structures (power=pole|tower|portal)

Data License: OpenStreetMap © OSM contributors, ODbL
https://www.openstreetmap.org/copyright

Usage:
    python extract_osm_power_infrastructure.py [--regions REGIONS] [--output OUTPUT_DIR]

Example:
    python extract_osm_power_infrastructure.py --regions alaska canada --output ./data/osm

Author: Erin Trochim
Date: 2025
"""

import os
import sys
import argparse
import urllib.request
from pathlib import Path
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import osm_flex.extract as ex


# Configuration
REGIONS = {
    'alaska': 'https://download.geofabrik.de/north-america/us/alaska-latest.osm.pbf',
    'canada': 'https://download.geofabrik.de/north-america/canada-latest.osm.pbf',
    'greenland': 'https://download.geofabrik.de/north-america/greenland-latest.osm.pbf',
    'russia_far_east': 'https://download.geofabrik.de/russia/far-eastern-fed-district-latest.osm.pbf'
}


def convert_to_centroids(gdf, buffer_distance=1, target_crs='EPSG:3413'):
    """
    Convert polygon geometries to point centroids for substation locations.
    
    Parameters
    ----------
    gdf : GeoDataFrame
        Input GeoDataFrame with mixed geometry types
    buffer_distance : float
        Buffer distance for Points/LineStrings in target CRS units (meters)
    target_crs : str
        Arctic Polar Stereographic projection for accurate distance calculations
    
    Returns
    -------
    GeoDataFrame
        GeoDataFrame with point geometries representing centroids
    """
    original_crs = gdf.crs
    
    if target_crs:
        gdf = gdf.to_crs(target_crs)
    
    gdf['geometry'] = gdf.geometry.apply(
        lambda geom: geom.buffer(buffer_distance) 
        if geom.geom_type in ['Point', 'LineString'] 
        else geom
    )
    
    gdf['geometry'] = gdf['geometry'].apply(
        lambda geom: geom 
        if geom.geom_type in ['Polygon', 'MultiPolygon'] 
        else Polygon(geom)
    )
    
    gdf['geometry'] = gdf.geometry.centroid
    
    if target_crs:
        gdf = gdf.to_crs(original_crs)
    
    return gdf


def download_osm_data(region_name, url, output_dir):
    """
    Download OSM PBF file for a specified region.
    
    Parameters
    ----------
    region_name : str
        Name of the region
    url : str
        Geofabrik download URL for the OSM PBF file
    output_dir : str
        Directory to save downloaded files
    
    Returns
    -------
    str
        Path to downloaded file
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir, f"{region_name}-latest.osm.pbf")
    
    print(f"Downloading {region_name} OSM data...")
    urllib.request.urlretrieve(url, output_path)
    print(f"✓ Downloaded to {output_path}")
    
    return output_path


def extract_power_infrastructure(pbf_path, feature_type='power'):
    """
    Extract power infrastructure features from OSM PBF file.
    
    Parameters
    ----------
    pbf_path : str
        Path to OSM PBF file
    feature_type : str
        OSM feature type to extract
    
    Returns
    -------
    GeoDataFrame
        Power infrastructure features with geometry and attributes
    """
    print(f"Extracting {feature_type} features from {pbf_path}...")
    gdf = ex.extract_cis(pbf_path, feature_type)
    print(f"✓ Extracted {len(gdf)} features")
    return gdf


def filter_substations(gdf_power):
    """Filter power infrastructure data to extract only substations."""
    gdf_substations = gdf_power[gdf_power['power'] == 'substation'].copy()
    print(f"✓ Filtered {len(gdf_substations)} substations")
    return gdf_substations


def filter_transmission_lines(gdf_power):
    """Filter power infrastructure to extract transmission lines."""
    gdf_lines = gdf_power[gdf_power['power'].isin(['line', 'minor_line', 'cable'])].copy()
    print(f"✓ Filtered {len(gdf_lines)} transmission line segments")
    return gdf_lines


def export_to_shapefile(gdf, output_path, region_name):
    """
    Export GeoDataFrame to shapefile format with OSM attribution.
    
    Adds required ODbL attribution fields to comply with OpenStreetMap license.
    
    Parameters
    ----------
    gdf : GeoDataFrame
        GeoDataFrame to export
    output_path : str
        Directory path for output
    region_name : str
        Name for output file
        
    Returns
    -------
    str
        Path to exported shapefile
        
    Notes
    -----
    OSM data is licensed under ODbL and requires attribution.
    See: https://www.openstreetmap.org/copyright
    """
    # Add OSM attribution metadata (required by ODbL license)
    gdf_export = gdf.copy()
    gdf_export['osm_src'] = 'OpenStreetMap'
    gdf_export['osm_lic'] = 'ODbL'
    gdf_export['osm_attr'] = '© OSM contributors'
    
    # Export to shapefile
    Path(output_path).mkdir(parents=True, exist_ok=True)
    output_file = os.path.join(output_path, f"{region_name}_substations.shp")
    gdf_export.to_file(output_file)
    print(f"✓ Exported to {output_file} (with OSM attribution)")
    return output_file


def process_region(region_name, url, pbf_dir, output_dir):
    """
    Process a single region: download, extract, filter, and export.
    
    Parameters
    ----------
    region_name : str
        Name of the region
    url : str
        Geofabrik URL for OSM data
    pbf_dir : str
        Directory to store PBF files
    output_dir : str
        Directory to store output shapefiles
    
    Returns
    -------
    tuple
        (substations GeoDataFrame, lines GeoDataFrame)
    """
    print(f"\n{'='*60}")
    print(f"Processing {region_name.upper()}")
    print(f"{'='*60}\n")
    
    # Download
    pbf_path = download_osm_data(region_name, url, pbf_dir)
    
    # Extract all power infrastructure
    gdf_power = extract_power_infrastructure(pbf_path)
    
    # Filter substations
    gdf_substations = filter_substations(gdf_power)
    gdf_substations = convert_to_centroids(gdf_substations)
    
    # Filter transmission lines
    gdf_lines = filter_transmission_lines(gdf_power)
    
    # Export
    export_to_shapefile(gdf_substations, output_dir, region_name)
    
    return gdf_substations, gdf_lines


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Extract OSM power infrastructure for Pan-Arctic analysis'
    )
    parser.add_argument(
        '--regions',
        nargs='+',
        choices=list(REGIONS.keys()) + ['all'],
        default=['all'],
        help='Regions to process (default: all)'
    )
    parser.add_argument(
        '--pbf-dir',
        default='./data/osm/pbf',
        help='Directory to store downloaded PBF files'
    )
    parser.add_argument(
        '--output',
        default='./data/osm/outputs',
        help='Output directory for shapefiles'
    )
    
    args = parser.parse_args()
    
    # Determine which regions to process
    if 'all' in args.regions:
        regions_to_process = REGIONS
    else:
        regions_to_process = {k: v for k, v in REGIONS.items() if k in args.regions}
    
    print(f"\n{'='*60}")
    print(f"PAN-ARCTIC OSM POWER INFRASTRUCTURE EXTRACTION")
    print(f"{'='*60}")
    print(f"Processing {len(regions_to_process)} region(s): {', '.join(regions_to_process.keys())}")
    print(f"Output directory: {args.output}")
    print(f"{'='*60}\n")
    
    # Process each region
    all_substations = []
    all_lines = []
    
    for region_name, url in regions_to_process.items():
        try:
            substations, lines = process_region(
                region_name, url, args.pbf_dir, args.output
            )
            
            # Add region identifier
            substations = substations.assign(region=region_name)
            lines = lines.assign(region=region_name)
            
            all_substations.append(substations)
            all_lines.append(lines)
            
        except Exception as e:
            print(f"✗ Error processing {region_name}: {e}")
            continue
    
    # Combine all regions
    if all_substations:
        print(f"\n{'='*60}")
        print("COMBINING DATASETS")
        print(f"{'='*60}\n")
        
        gdf_panarctic_substations = pd.concat(all_substations, ignore_index=True)
        gdf_panarctic_lines = pd.concat(all_lines, ignore_index=True)
        
        # Export combined datasets
        export_to_shapefile(gdf_panarctic_substations, args.output, 'panarctic_all')
        
        # Add OSM attribution to lines (required by ODbL)
        gdf_panarctic_lines['osm_src'] = 'OpenStreetMap'
        gdf_panarctic_lines['osm_lic'] = 'ODbL'
        gdf_panarctic_lines['osm_attr'] = '© OSM contributors'
        
        lines_output = os.path.join(args.output, 'panarctic_lines.shp')
        gdf_panarctic_lines.to_file(lines_output)
        print(f"✓ Exported transmission lines to {lines_output} (with OSM attribution)")
        
        # Generate summary
        summary_stats = gdf_panarctic_substations.groupby('region').size().reset_index(name='substations')
        summary_stats['transmission_lines'] = gdf_panarctic_lines.groupby('region').size().values
        summary_stats.loc[len(summary_stats)] = ['Total', 
                                                   len(gdf_panarctic_substations),
                                                   len(gdf_panarctic_lines)]
        
        print(f"\n{'='*60}")
        print("EXTRACTION SUMMARY")
        print(f"{'='*60}")
        print(summary_stats.to_string(index=False))
        print(f"{'='*60}\n")
        
        # Save summary
        summary_path = os.path.join(args.output, 'extraction_summary.csv')
        summary_stats.to_csv(summary_path, index=False)
        print(f"✓ Summary saved to {summary_path}\n")
        
        print("✓ Extraction complete!")
    else:
        print("\n✗ No data was successfully extracted.")
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
