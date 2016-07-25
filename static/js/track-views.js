
var TrackItemView = Backbone.View.extend({

    initialize: function() {
        this.save = false;
        this.readOnly = !this.save;
    },

    events: {
        'click .track-edit': 'toggleEdit',
	'click .genre-delete': 'deleteTrack'
    },

    deleteTrack: function() {
	this.model.destroy();
	this.$el.remove();
	Backbone.history.loadUrl(Backbone.history.fragment);
    },

    toggleEdit: function(e) {
        this.readOnly = this.save;
        this.save = !this.save;
        if (!this.save) {
	    var title = $('.panel-heading', this.$el).text().trim();
	    var tags = $('.tags', this.$el).val();
	    var rating = $('.rating', this.$el).rateYo("rating");
	    if (title && tags && rating) {
		this.model.set({title: title, genre: tags.split(","), rating: rating}, {silent: true});
		this.model.save({silent: true});
	    }
        }
        this.render();
	$('.tags', this.$el).tagsInput({height: '40px', width: '250px'});
    },

    track_tpl: _.template($('#item-template').html()),

    render: function() {
        var context = $.extend({}, this.model.toJSON(), {save: this.save });
        this.$el.html(this.track_tpl(context));
        var rating = this.model.get("rating");
        $('.rating', this.$el).rateYo({ rating: rating });
	$('.rating').rateYo({fullStar: true});
	$('.rating', this.$el).rateYo("option", "readOnly", this.readOnly);
        return this;
    },
});


var addView = Backbone.View.extend({
    events: {
	'click #save-item': 'saveTrack',
	'click #search-item': 'searchTrack'
    },

    addTpl: _.template($('#add-item-template').html()),

    searchTrack: function(e) {
	var search_term = $('#search', this.$el).val().trim();
	appRouter.search_term = search_term;
	if (search_term) {
	    appRouter.navigate("search/" + search_term + "/page/1", {trigger: true});
	}
    },

    clearview: function() {
	$('#track', this.$el).val('');
	$('.rating', this.$el).rateYo();
    },

    saveTrack: function(e) {
	var track = new Track();
	var title = $('#track', this.$el).val().trim();
	var rating = Math.round($('.rating', this.$el).rateYo("rating"));
	var genre = $('.tags', this.$el).val();
	if (title && rating && genre) {
	    var genres = genre.split(",");
	    track.set({rating: rating, title: title, genre: genres});
	    track.save();
	    Backbone.history.loadUrl(Backbone.history.fragment);
	    this.clearview();
	}
    },

    render: function() {
	this.$el.html(this.addTpl());
	return this;
    }
});

var TrackListView = Backbone.View.extend({

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
            var track1_view = new TrackItemView({model: item});
            this.$el.append(track1_view.render().el);
        }, this);

        var paginatorView = new PaginatorView({next: this.collection.next, previous: this.collection.previous});
        this.$el.append(paginatorView.render().el);

	$('.rating').rateYo({fullStar: true});
	$('.tags', this.$el).tagsInput({height: '40px', width: '250px'});
        return this;
    },

});
