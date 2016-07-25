
var GenreItemView = Backbone.View.extend({

    initialize: function() {
        this.save = false;
        this.readOnly = !this.save;
	this.model.bind('change', this.render, this);
    },

    events: {
        'click .genre-edit': 'toggleEdit',
	'click .genre-delete': 'deleteGenre'
    },

    deleteGenre: function(e) {
	this.model.destroy();
	this.$el.remove();
	Backbone.history.loadUrl(Backbone.history.fragment);
    },

    toggleEdit: function(e) {
        this.readOnly = this.save;
        this.save = !this.save;
        if (!this.save) {
	    this.model.set("title", $('.panel-heading', this.$el).text().trim());
	    this.model.save();
        }
        this.render();
    },

    genre_tpl: _.template($('#item-template').html()),

    render: function() {
        var context = $.extend({}, this.model.toJSON() , {save: this.save});
        this.$el.html(this.genre_tpl(context));
        return this;
    },
});

var GenreCollection = Backbone.Collection.extend({
    model: Genre,
    page: 1,
    count: 10,
    previous: null,
    next: null,
    url: "/api/genres/",

    parse: function(data) {
	window.app.max_page_number = Math.ceil(data.count / window.app.page_size);
        this.count = data.count;
        this.next = data.next;
        this.previous = data.previous;
        return data.results;
    },
});

var genreCollection = new GenreCollection();

var addView = Backbone.View.extend({
    events: {
	'click #save-item': 'saveTrack',
	'click #search-item': 'searchTrack'
    },

    addTpl: _.template($('#add-item-template').html()),

    searchTrack: function(e) {
	e.preventDefault();
	var search_term = $('#search', this.$el).val().trim();
	appRouter.search_term = search_term;
	if (search_term) {
	    appRouter.navigate("search/" + search_term + "/page/1", {trigger: true});
	}
    },

    clearview: function() {
	$('#track', this.$el).val('');
    },

    saveTrack: function(e) {
	e.preventDefault();
	var track = new Genre();
	var title = $('#track', this.$el).val().trim();
	if (title) {
	    track.set("title", title);
	    track.save();
	    this.clearview();
	}
	genreCollection.fetch({async: false});
    },

    render: function() {
	this.$el.html(this.addTpl());
	return this;
    }
});


var GenreListView = Backbone.View.extend({

    el: '#my-container',

    initialize: function() {
	this.collection.bind('change', this.render, this);
	this.collection.bind('reset', this.render, this);
    },

    render: function() {

        this.$el.empty();

	var AddView = new addView();
        this.$el.append(AddView.render().el);

        this.collection.each(function(item) {
            var genre1_view = new GenreItemView({model: item});
            this.$el.append(genre1_view.render().el);
        }, this);

        var paginatorView = new PaginatorView({next: this.collection.next, previous: this.collection.previous});
        this.$el.append(paginatorView.render().el);

        return this;
    },

});

var genre_list_view = new GenreListView({collection: genreCollection });
var appRouter = new AppRouter({collection: genreCollection});
Backbone.history.start();
appRouter.navigate("page/", {trigger: true});
