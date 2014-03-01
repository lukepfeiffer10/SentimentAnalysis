/// <reference path="js/backbone.js" />
/// <reference path="js/underscore.js" />

$(function () {
    var Sentence = Backbone.Model.extend({
    });

    var SentenceList = Backbone.Collection.extend({
		url: '/api/sentences/next',
        model: Sentence,
		
		parse: function(response) {
			return response.sentences;
		}
    });

    var SentenceView = Backbone.View.extend({
        tagName: 'span',
        className: 'sentence',

        events: {
            'click': 'editSentiment'
        },

        template: _.template("<%= sentence_txt %>"),

        initialize: function () {

        },

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        },

        editSentiment: function () {
            alert('You clicked me!');
        }
    });

    /*var Sentences = new SentenceList([new Sentence({id: 1, text: "this is a test!", order: 1}),
                                new Sentence({id: 2, text: "this is a test 2.", order: 2}),
                                new Sentence({ id: 3, text: "this is a test 3?", order: 3 })]);*/
								
	var Sentences  = new SentenceList();
	Sentences.fetch({
		parse: true,
		success: function(collection, response, options) {
			collection.each(function(sentence) {
				$('#story').append(new SentenceView({model: sentence}).render().$el);
			});
		}
	});
});