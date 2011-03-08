from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class Asset(db.Model):
    uuid = db.StringProperty()
    name = db.StringProperty()
    
    @classmethod
    def by_uuid(cls, uuid):
        asset = cls.all(keys_only=True).filter('uuid =', uuid).get()
        return asset
    
    
class Handler(webapp.RequestHandler):
    
    def get(self, uuid):
        name = self.request.get('name')
        existing = Asset.by_uuid(uuid)
        if existing:
            # entity exists. we get it and update the name.
            # the uuid is the same for all items in the list on
            # the script
            asset = db.get(existing)
            asset.name = name
            asset.put()
            resp = 'updated an existing entity'
        else:
            # the entity does not exist yet. 
            # create a new one
            asset = Asset(uuid=uuid, name=name)
            asset.put()
            resp = 'created a new entity'
        self.response.out.write(resp)
        



def application():
    return webapp.WSGIApplication([('/(.*)/?', Handler)])

def main():
    run_wsgi_app(application())

if __name__ == "__main__":
    main()        

