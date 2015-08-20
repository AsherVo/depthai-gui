from AbstractGraph import *


class AGSumNode(AGNode):
    def __init__(self, name, graph):
        super(AGSumNode, self).__init__(name, graph)
        self.name = name
        self.graph = graph
        self.inputA = self.add_input_port('inpA', AGPortDataTypes.tNumeric)
        self.inputB = self.add_input_port('inpB', AGPortDataTypes.tNumeric)
        self.output = self.add_output_port('out', AGPortDataTypes.tNumeric)
        portAffects(self.inputA, self.output)
        portAffects(self.inputB, self.output)

    def compute(self):

        inpA_data = self.inputA.get_data()
        inpB_data = self.inputB.get_data()

        result = inpA_data + inpB_data

        self.output.set_data(result, False)