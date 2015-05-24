__author__ = 'zhangyanni'
"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import os
import glob
from xblock.core import XBlock
from xblock.fields import Scope, Integer,String
from xblock.fragment import Fragment


class JennytreeXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
        )
    #add by jenny
    lab = String(default="",scope=Scope .user_state ,help="lab")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the JennytreeXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/jennytree.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/jennytree.css"))
        frag.add_javascript(self.resource_string("static/js/src/jennytree.js"))
        frag.add_javascript(self.resource_string("static/js/src/jquery.js"))

        frag.add_javascript(self.resource_string("static/js/src/jstree.min.js"))
        frag.add_css(self.resource_string("static/jstree/dist/themes/default/style.min.css"))
        frag.initialize_js('JennytreeXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    #传入参数：path是路径名，parent是父节点的编号，jsonstr是把遍历路径后生成的json串，Id是每一个节点的Id。
    #ToJson实现把一个路径进行无限递归，生成json串，
    def ToJson(self,path,parent,jsonstr,Id):
        for i,fn in enumerate(glob.glob(path + os.sep + '*' )):
            if os.path.isdir(fn):
                jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(fn)+'''","children":['''
                parent=Id
                Id+=1
                for j,li in enumerate(glob.glob(fn + os.sep + '*' )):
                    if os.path.isdir(li):
                        jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(li)+'''","children":['''
                        parent=Id
                        Id+=1
                        ToJson(li,parent,jsonstr,Id)
                        jsonstr+="]}"
                        if j<len(glob.glob(fn + os.sep + '*' ))-1:
                            jsonstr+=","
                    else:
                        jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(li)+'''","type":"leaf"}'''
                        Id+=1
                        if j<len(glob.glob(fn + os.sep + '*' ))-1:
                            jsonstr+=","
                jsonstr+="]}"
                if i<len(glob.glob(path + os.sep + '*' ))-1:
                    jsonstr+=","
            else:

                jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(fn)+'''","type":"leaf"}'''
                Id+=1
                if i<len(glob.glob(path + os.sep + '*' ))-1:
                    jsonstr+=","
          return jsonstr
    #getJson传入参数路径名，返回转换后的josn串。返回值用作生成jstree目录树的数据源
    def getJson(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        path=data['path']


        jsonstr="["
        parent=0
        Id=0
        jsonstr=ToJson(path,parent,jsonstr,Id)+"]"
        return jsonstr





    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("JennytreeXBlock",
             """<vertical_demo>
                <jennytree/>
                <jennytree/>
                <jennytree/>
                </vertical_demo>
             """),
            ]
