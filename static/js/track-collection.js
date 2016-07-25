var TrackCollection = Backbone.Collection.extend({
    model: Track,
    page: 1,
    count: 10,
    previous: null,
    next: null,
    url: "/api/tracks/",

    parse: function(data) {
	window.app.max_page_number = Math.ceil(data.count / window.app.page_size);
        this.count = data.count;
        this.next = data.next;
        this.previous = data.previous;
        return data.results
    },
});

