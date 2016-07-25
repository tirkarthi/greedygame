
var Track = Backbone.Model.extend({
    initialize: function(options) {
	this.url = options.url;
    },

    defaults: {"title" : "sample title" , "genre" : ["pop"], "rating": 4, "modified": Date() },
});

var TrackItemView = Backbone.View.extend({

    initialize: function() {
        this.save = false;
        this.readOnly = !this.save;
	this.model.bind('change', this.render, this);
    },

    events: {
        'click .track-edit': 'toggleEdit',
	'click .track-delete': 'deleteTrack'
    },

    el: '#my-container',

    deleteTrack: function(e) {
	this.model.destroy();
	location.href = location.origin + "/tracks/";
    },

    toggleEdit: function(e) {
        this.readOnly = this.save;
        this.save = !this.save;
        if (!this.save) {
	    var title = $('.panel-heading', this.$el).text().trim();
	    var genre = $('.tags', this.$el).val().split(',');
	    var rating = $('.rating', this.$el).rateYo("rating");
	    if (title && genre && rating) {
		this.model.set({title: title, genre: genre, rating: rating}, {silent: true});
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
        var readOnly = this.readOnly;
        var rating = this.model.get("rating");
        $('.rating', this.$el).rateYo({ rating: rating, fullStar: true});
        $('.rating', this.$el).rateYo("option", "readOnly", readOnly);
        $('.tags', this.$el).tagsInput({height: '40px', width: '250px'});
        return this;
    },
});
