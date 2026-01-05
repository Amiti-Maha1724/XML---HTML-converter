from lxml import etree

# File paths
xml_path = "employees.xml"
xsl_path = "style.xsl"
output_path = "index.html"

try:
    # Parse the files
    xml_tree = etree.parse(xml_path)
    xsl_tree = etree.parse(xsl_path)

    # Perform transformation
    transform = etree.XSLT(xsl_tree)
    result = transform(xml_tree)

    # Write to HTML file
    with open(output_path, "wb") as f:
        f.write(etree.tostring(result, pretty_print=True, method="html"))

    print(f"Done! Successfully created {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")