var PaginatorView = Backbone.View.extend({

    events: {
	'click .page': 'navigate'
    },

    navigate: function(e) {
	var max_page_number = window.app.max_page_number;
	var elem = $(e.currentTarget);
	var page_number = elem.attr('id');
	if (page_number <= max_page_number) {
	    if(appRouter.search_term) {
		appRouter.navigate('search/'+ appRouter.search_term + '/page/' + page_number, {trigger: true});
	    } else {
		appRouter.navigate('page/' + page_number, {trigger: true});
	    }
	}
    },

    render: function() {
	var max_page_number = window.app.max_page_number;
	var next_page = this.options.next ? parseInt(this.options.next.match(/page=(\d+)/)[1]) + 1 : max_page_number + 1;
	var previous_page = 1;
	if (this.options.previous) {
	    var match = this.options.previous.match(/page=(\d+)/);
	    if (match) {
		previous_page = parseInt(match[1]);
	    }
	}
	next_page = next_page + 1 <= max_page_number ? next_page + 1 : max_page_number + 1;
	var range = _.range(previous_page, next_page);
	this.paginator_tpl = _.template($('#pagination-template').html());
        var page_results = { next: this.options.next, previous: this.options.previous };
        this.$el.html(this.paginator_tpl({range: range}));
        return this;
    }
});
