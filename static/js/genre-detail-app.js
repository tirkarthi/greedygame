var Genre = Backbone.Model.extend({
    initialize: function(options) {
	this.url = options.url;
    },
    defaults: {"title" : "sample title", "modified": Date() },
});

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

    el: '#my-container',

    deleteGenre: function(e) {
	this.model.destroy();
	location.href = location.origin + "/genres/";
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
        var context = $.extend({}, this.model.toJSON(), {save: this.save, id: this.model.get("id") });
        this.$el.html(this.genre_tpl(context));
        return this;
    },
});

