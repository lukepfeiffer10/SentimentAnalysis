/// <reference path="js/backbone.js" />
/// <reference path="js/jquery.js" />
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
            alert(this.model.get("id"));
        }
    });

    var Tag = Backbone.Model.extend({

    });

    var TagView = Backbone.View.extend({
        el: $('#taggingBox'),

        initialize: function () {

        },

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        },
    });
								
    var Sentences = new SentenceList();

    var AppView = Backbone.View.extend({
        el: $('body'),

        events: {
            "click #logout": "logout"
        },

        logout: function() {
            $.ajax({
                type: 'DELETE',
                url: 'api/user/login',
                success: function () {
                    window.location = '/login'
                }
            });
        },
        
        initialize: function () {
            Sentences.fetch({
                parse: true,
                success: function (collection, response, options) {
                    collection.each(function (sentence) {
                        $('#story').append(new SentenceView({ model: sentence }).render().$el);
                    });
                }
            });
        }
    });

    var App = new AppView();
	
});