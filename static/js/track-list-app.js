
var trackCollection = new TrackCollection();
var track_list_view = new TrackListView({collection: trackCollection });

var appRouter = new AppRouter({collection: trackCollection});
Backbone.history.start();
appRouter.navigate("page/1", {trigger: true});

