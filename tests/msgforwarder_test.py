from __future__ import unicode_literals, absolute_import
from linemodules.msgforwarder import msgforwarder

event = {
	'message' : {
		'text' : 'Test'
	}
}
msgforwarder.forwardMsgToUser('line_bot_api', event)