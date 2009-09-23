from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.Expression import Expression
from Products.RhaptosBugTrackingTool import product_globals
from StringIO import StringIO
import string

def install_skindir(self, out, folder):
    skinstool = getToolByName(self, 'portal_skins')
    if folder not in skinstool.objectIds():
        # We need to add Filesystem Directory Views for any directories
        # in our skins/ directory.  These directories should already be
        # configured.
        addDirectoryViews(skinstool, 'skins', product_globals)
        out.write("Added %s directory view to portal_skins\n" % folder)

    # Now we need to go through the skin configurations and insert
    # folder into the configurations.  
    skins = skinstool.getSkinSelections()
    for skin in skins:
        path = skinstool.getSkinPath(skin)
        path = map(string.strip, string.split(path,','))
        if folder not in path:
            try:
                path.insert(path.index('custom') + 1, folder)
            except ValueError:
                path.append(folder)
                
            path = string.join(path, ', ')
            # addSkinSelection will replace existing skins as well.
            skinstool.addSkinSelection(skin, path)
            out.write("Added folder to %s skin\n" % skin)
        else:
            out.write("Skipping %s skin, %s is already set up\n" % (skin, folder))
    

def install(self):
    """Add the tool"""
    out = StringIO()

    # Add the tool
    urltool = getToolByName(self, 'portal_url')
    portal = urltool.getPortalObject();
    props = {}
    try:
        bt = getToolByName(portal, 'portal_bugtracking')
        props=dict(bt.propertyItems())
        portal.manage_delObjects('portal_bugtracking')
        out.write("Removed old portal_bugtracking tool\n")
    except AttributeError:
        pass  # we don't care if its not there
    portal.manage_addProduct['RhaptosBugTrackingTool'].manage_addTool('BugTracking Tool', None)

    bt = getToolByName(portal, 'portal_bugtracking')

    trac_url = props.get('trac_url', 'https://trac.rhaptos.org/trac/rhaptos/newticket')
    trac_xmlrpc = props.get('trac_xmlrpc', 'https://trac.rhaptos.org/trac/rhaptos/xmlrpc')
    bt.manage_addProperty('trac_url', trac_url,'string')
    bt.manage_addProperty('trac_xmlrpc', trac_xmlrpc,'string')

    # Register skins
    install_skindir(self, out, 'rhaptos_bugtrack')
    
    out.write("Adding BugTrack Tool\n")

    # Set up action
    at = getToolByName(portal, 'portal_actions')
    for a in at.listActions():
        if a.id == 'bugreport':
            a.action = Expression('string:$portal_url/bug_submit_form')

    out.write('Set bugreport action\n')
    
    return out.getvalue()
