## Script (Python) "bug_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##bind state=state
##parameters=summary='', name='', email='', contentUrl='', bugType='', severity='', description='', referrer_url=''
##title=
##

newid = context.portal_bugtracking.submitBug(summary, email, name, contentUrl, bugType, severity, description)
msg = context.translate("message_bug_return", {"bugid":newid}, domain="rhaptos", default="Your Problem Report number is %d; you will receive an email from the bug tracking system shortly." % newid )

if referrer_url:
    return state.set(status='redirect', next_action='redirect_to:string:%s' % referrer_url, portal_status_message=msg)
else:
    return state.set(status='success', portal_status_message=msg, context=context)


