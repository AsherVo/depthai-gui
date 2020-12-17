from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from common import PreviewNode, HostNode


class FramePreviewNode(HostNode, PreviewNode):
    def __init__(self, name):
        super(FramePreviewNode, self).__init__(name)
        self.frame = self.createInputPin('frame', 'FramePin')
        self.frame.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addInputStruct(StructureType.Multi)
        helper.addInputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Display'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def _fun(self, *args, **kwargs):
        while True:
            self.display_frame = self.queue.get()['data']
