# ===========================================================================
# eXe 
# Copyright 2004-2005, University of Auckland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================
"""
ForumBlock can render and process ForumIdevices as XHTML
"""

import logging
import gettext
from exe.webui.block import Block
from exe.webui       import common

log = logging.getLogger(__name__)
_   = gettext.gettext


# ===========================================================================
class ForumBlock(Block):
    """
    ForumBlock can render and process ForumIdevices as XHTML
    """
    def __init__(self, parent, idevice):
        """
        Initialize a new Block object
        """
        Block.__init__(self, parent, idevice)
        self.idevice = idevice


    def process(self, request):
        """
        Process the request arguments from the web server
        """
        Block.process(self, request)
        
        if "name"+self.id in request.args:
            self.idevice.forumName = request.args["name"+self.id][0]
            
        if "type"+self.id in request.args:
            self.idevice.type = request.args["type"+self.id][0]

        if "introduction"+self.id in request.args:
            self.idevice.introduction = request.args["introduction"+self.id][0]
            
        if "studentpost"+self.id in request.args:
            self.idevice.studentpost = request.args["studentpost"+self.id][0]
            
        if "groupmode"+self.id in request.args:
            self.idevice.groupmode = request.args["groupmode"+self.id][0]
       
        if "visible"+self.id in request.args:
            self.idevice.visible = request.args["visible"+self.id][0]
        
        if "subject"+self.id in request.args:
            self.idevice.discussionSubject = request.args["subject"+self.id][0]
            
        if "message"+self.id in request.args:
            self.idevice.discussionMessage = request.args["message"+self.id][0]
            
        if "subscription"+self.id in request.args:
            self.idevice.subscription = request.args["subscription"+self.id][0]
            
    def renderEdit(self, style):
        """
        Returns an XHTML string with the form element for editing this block
        """
       
        introduction = self.idevice.introduction.replace("\r", "")
        introduction = introduction.replace("\n","\\n")
        introduction = introduction.replace("'","\\'")
        message      = self.idevice.discussionMessage.replace("\r", "")
        message      = message.replace("\n","\\n")
        message      = message.replace("'","\\'")
        
        typeArr    = [[_(u'A single simple discussion'),       'single'],
                      [_(u'Each person posts one discussion'), 'eachuser'],
                      [_(u'Standard forum for general use'),   'general']]
        
        postArr    = [[_(u'Discussions and replies are allowed'),     '2'],
                      [_(u'No discussions, but replies are allowed'), '1'],
                      [_(u'No discussions, no replies'),              '0']]
        
        subscArr   = [[_(u'No'),             '0'], 
                      [_(u'Yes, forever'),   '1'], 
                      [_(u'Yes, initially'), '2']]
        
        groupArr   = [[_(u'No groups'),       '0'], 
                      [_(u'Separate groups'), '1'], 
                      [_(u'Visible groups'),  '2']]
        
        visibleArr = [[_(u'Show'), '1'], 
                      [_(u'Hide'), '0']]

        
        html  = u"<div class=\"iDevice\" class=\"forum\">\n"
        
        html += u"<b>%s</b>" % _(u"Forum name:") 
        html += common.elementInstruc("name"+self.id, 
                                      self.idevice.nameInstruc)+ u"<br/>\n"
        
        html += common.textInput("name"+self.id, self.idevice.forumName)+ "\n"
        html += u"<br/><b>%s</b>" % _(u"Forum type:") 
        html += common.elementInstruc("type"+self.id, 
                                      self.idevice.typeInstruc)+ u"<br/>"
        html += common.select("type"+self.id, 
                              typeArr, selection=self.idevice.type) 
        html += u"<br/><b>%s</b>" % _(u"Forum introduction:") 
        html += common.elementInstruc("introduction"+self.id, 
                                      self.idevice.introInstruc)+ u"<br/>"
        html += common.richTextArea("introduction"+self.id, 
                                    introduction)
        html += u"<b>%s</b>" % _(u"Can a student post to this forum?:")
        html += common.elementInstruc("studentpost"+self.id, 
                                      self.idevice.postInstruc)+ "<br/>"
        html += common.select("studentpost"+self.id, postArr, 
                              selection=self.idevice.studentpost) + "\n"
        html += u"<br/><b>%s</b>" % _(u"Force everyone to be subscribed?:")
        
        html += common.elementInstruc("subscription"+self.id, 
                                      self.idevice.subscInstruc)+ "<br/>"
        html += common.select("subscription"+self.id, subscArr, 
                              selection=self.idevice.subscription) + "\n"
        html += u"<br/><b>%s</b>" % _(u"Group mode:")
        html += common.elementInstruc("groupmode"+self.id, 
                                      self.idevice.groupInstruc)+ u"<br/>"
        html += common.select("groupmode"+self.id, groupArr, 
                              selection=self.idevice.groupmode) + "\n"
        html += "<br/><b>%s</b>" % _(u"Visible to students:")
        html += common.elementInstruc("visible"+self.id, 
                                      self.idevice.visibleInstruc)+ u"<br/>"
        html += common.select("visible"+self.id, visibleArr, 
                              selection=self.idevice.visible) + u"\n"
        html += u"<br/><br/><b>%s</b>" % _(u"Discussion topic:") + u"<br/>"
        html += u"<b>%s</b>" % _(u"Subject:") 
        html += common.elementInstruc("subject"+self.id, 
                                      self.idevice.subjectInstruc)+ u"<br/>"
        html += common.textInput("subject"+self.id, 
                                 self.idevice.discussionSubject)+ u"<br/>"
        html += u"<b>%s</b>" % _(u"Message:") 
        html += common.elementInstruc("message"+self.id, 
                                      self.idevice.messageInstruc)+ u"<br/>"
        html += common.richTextArea("message"+self.id, 
                                    message)

        html += u"<br/>" + self.renderEditButtons()
        html += u"</div>\n"
        return html
    
    def renderPreview(self, style):
        """
        Returns an XHTML string for previewing this block
        """
        html  = u"<br/><b>%s</b><br/>" % _(u"Forum Discussion")
        html += u"<b>%s</b><br/>" % self.idevice.forumName
        html += u"<b>%s</b><br/>\n" % _(u"Discussion Topic")
        html += u"<b>%s</b><br/>\n" % _(u"Subject")
        html += u"<!--Forum%slink-->\n" % self.id
        html += u"<br/>\n" 
        html += self.idevice.discussionMessage + u"<br/>\n"
        html += self.renderViewButtons()
        return html

    def renderView(self, style):
        """
        Returns an XHTML string for viewing this block
        """
        html  = u"<br/><b>%s</b><br/>" % _(u"Forum Discussion")
        html += u"<b>%s</b><br/>" % self.idevice.forumName
        html += u"<b>%s</b><br/>\n" % _(u"Discussion Topic")
        html += u"<b>%s</b><br/>\n" % _(u"Subject")
        html += u"<!--Forum%slink-->\n" % self.id
        html += self.idevice.discussionSubject + u"<br/>\n" 
        html += self.idevice.discussionMessage + u"<br/>\n"
        return html
    
    def renderForumStr(self):
        """
        returning XLM string for this forum
        """
        xml  = "<forum>\n" 
        xml += "<name>%s</name>\n" % self.idevice.forumName
        xml += "<id>Forum%s</id>\n" % self.id
        xml += "<type>%s</type>\n" % self.idevice.type
        xml += "<introduction><![CDATA["
        xml += self.idevice.introduction
        xml += "]]></introduction>\n" 
        xml += "<studentpost>%s</studentpost>\n" % self.idevice.studentpost
        xml += "<subscription>%s</subscription>\n" % self.idevice.subscription
        xml += "<tracking>1</tracking>\n"
        xml += "<attachmentsize></attachmentsize>\n"
        xml += "<ratings>0</ratings>\n"
        xml += "<groupmode>%s</groupmode>\n" % self.idevice.groupmode
        xml += "<visible>%s</visible>\n" % self.idevice.visible
        xml += "</forum>"
        xml += "<discussion>\n"
        xml += "<discussionId>Forum%s</discussionId>\n" % self.id
        xml += "<subject>%s</subject>\n" % self.idevice.discussionSubject
        xml += "<message><![CDATA["
        xml += self.idevice.discussionMessage
        xml += "]]></message>\n" 
        xml += "<subscription>send me</subscription>\n" 
        xml += "</discussion>\n"
        
        return xml
    
  

# ===========================================================================
