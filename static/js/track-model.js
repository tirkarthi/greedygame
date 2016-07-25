var Track = Backbone.Model.extend({
    defaults: {"title" : "sample title" , "genre" : ["pop"], "rating": 4, "modified": Date() },
    urlRoot: "/api/tracks/",
});
