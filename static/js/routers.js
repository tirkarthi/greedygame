var AppRouter = Backbone.Router.extend({

    page_number: 1,

    initialize: function(options) {
	this.options = options || {};
    },

    routes: {
	"page/:page": "page",
	"page/": "page",
	"search/:search": "search",
	"search/:search/page/:page": "search"
    },

    search: function(word, page) {
	page = page || 1;
	this.options.collection.fetch({ async:false, data: $.param({title: word, page: page}) });
	window.page_number = this.page_number;
	this.page_number = page;
    },


    page: function(page) {
	page = page || 1;
	appRouter.navigate("page/" + page, {trigger: false});
	this.options.collection.fetch({ async:false, data: $.param({page: page}) });
	window.page_number = this.page_number;
	this.page_number = page;
    }
});

