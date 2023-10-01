import rdflib

brick_path = r"C:\Users\WillDavidson\Documents\R&D\Tagging Model and Ontology\ontologies\brick\brick_20230830.ttl"
switch_path = r"C:\Users\WillDavidson\Documents\R&D\Tagging Model and Ontology\ontologies\switch\switch_v1-3-6.ttl"

g = rdflib.Graph().parse(brick_path, format="turtle").parse(switch_path, format="turtle")

