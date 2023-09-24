examples = """
# Show part details for 19999-99?
MATCH (p:parts) WHERE p.part_id = "19999-99" RETURN ' Part Name:' +p.part_name+' | Part Description: '+p.part_description' as response

# Who is the supplier of the part 19999-99?
MATCH (p:parts)-[:SUPPLIED_BY]->(s:suppliers) WHERE p.part_id = "19999-99" RETURN ' Supplier id: ' + s.supplier_id + ' | Supplier Name: '+s.supplier_name as response

# The alternate parts for 19999-99
MATCH (a)-[:ALTERNATE_OF]->(b) WHERE b.part_id = "19999-99"  RETURN ' Alternate Part: ' + a.part_id + ' | Part Name: '+ a.part_name as response
"""

node_properties = """
[
    {
        "properties": [
            "part_id",
            "supplier_id",
            "part_name",
            "part_description",
            "alternate_part_id"
        ],
        "labels": "parts"
    },
    {
        "properties": [
            "supplier_id",
            "part_cost",
            "transportation_cost",
            "labour_cost",
            "total_cost"
        ],
        "labels": "cost"
    },
    {
        "properties": [
            "supplier_id",
            "supplier_name",
            "location"
        ],
        "labels": "suppliers"
    }
]
"""

relationships_props = """
[
    {
        "source": "parts",
        "relationship": "ALTERNATE_OF",
        "target": [
            "parts"
        ]
    },
    {
        "source": "parts",
        "relationship": "SUPPLIED_BY",
        "target": [
            "suppliers"
        ]
    },
    {
        "source": "suppliers",
        "relationship": "HAS",
        "target": [
            "cost"
        ]
    }
]
"""