#!/usr/bin/env python3
"""
Fix OpenAPI schemas to resolve 'Cannot take allOf a non-object' errors.

The issue: Parent schemas that are referenced in 'allOf' should not contain
'oneOf' or 'discriminator' properties, as this creates an invalid schema structure
that openapi-python-client cannot process.

Solution: Remove 'oneOf' and 'discriminator' from parent schemas that are
used as base schemas in 'allOf' inheritance patterns.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Set


def find_schemas_used_in_allof(schemas: Dict) -> Set[str]:
    """Find all schema names that are referenced in allOf blocks."""
    schemas_in_allof = set()
    
    for schema_name, schema_def in schemas.items():
        if 'allOf' in schema_def:
            for item in schema_def['allOf']:
                if '$ref' in item:
                    # Extract schema name from reference like "#/components/schemas/SchemaName"
                    ref_parts = item['$ref'].split('/')
                    if len(ref_parts) >= 4 and ref_parts[-2] == 'schemas':
                        referenced_schema = ref_parts[-1]
                        schemas_in_allof.add(referenced_schema)
    
    return schemas_in_allof


def fix_openapi_schema(file_path: Path) -> bool:
    """
    Fix OpenAPI schema file by removing oneOf/discriminator from schemas used in allOf.
    
    Returns True if changes were made, False otherwise.
    """
    print(f"\nProcessing {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'components' not in data or 'schemas' not in data['components']:
        print(f"  No schemas found in {file_path.name}")
        return False
    
    schemas = data['components']['schemas']
    schemas_in_allof = find_schemas_used_in_allof(schemas)
    
    print(f"  Found {len(schemas_in_allof)} schemas used in allOf")
    
    changes_made = False
    fixed_schemas = []
    
    for schema_name in schemas_in_allof:
        if schema_name not in schemas:
            continue
            
        schema_def = schemas[schema_name]
        
        # Check if this schema has oneOf or discriminator
        has_oneof = 'oneOf' in schema_def
        has_discriminator = 'discriminator' in schema_def
        
        if has_oneof or has_discriminator:
            if has_oneof:
                print(f"  Removing 'oneOf' from {schema_name}")
                del schema_def['oneOf']
                changes_made = True
            
            if has_discriminator:
                print(f"  Removing 'discriminator' from {schema_name}")
                del schema_def['discriminator']
                changes_made = True
            
            fixed_schemas.append(schema_name)
    
    if changes_made:
        # Write the fixed schema back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ Fixed {len(fixed_schemas)} schemas in {file_path.name}")
        for schema in fixed_schemas:
            print(f"    - {schema}")
    else:
        print(f"  No changes needed for {file_path.name}")
    
    return changes_made


def main():
    """Fix all OpenAPI schema files in the openapi_schemas directory."""
    openapi_dir = Path(__file__).parent / 'openapi_schemas'
    
    if not openapi_dir.exists():
        print(f"Error: Directory {openapi_dir} does not exist")
        sys.exit(1)
    
    json_files = list(openapi_dir.glob('*.json'))
    
    if not json_files:
        print(f"Error: No JSON files found in {openapi_dir}")
        sys.exit(1)
    
    print(f"Found {len(json_files)} OpenAPI schema file(s) to process")
    
    total_changes = 0
    for json_file in sorted(json_files):
        if fix_openapi_schema(json_file):
            total_changes += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Modified {total_changes} file(s)")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
