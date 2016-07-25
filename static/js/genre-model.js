var Genre = Backbone.Model.extend({
    defaults: {"title" : "sample title", "modified": Date() },
    urlRoot: "/api/genres/",
});
