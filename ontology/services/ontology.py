from py4j.java_gateway import JavaGateway

class Ontology:
    def __init__(self):
        self.gateway = JavaGateway()
        self.ontology = gateway.entry_point.getOntology()