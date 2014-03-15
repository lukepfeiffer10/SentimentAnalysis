/// <reference path="js/backbone.js" />
/// <reference path="js/jquery.js" />
/// <reference path="js/underscore.js" />

$(function () {
    var Sentence = Backbone.Model.extend({
    });

    var SentenceList = Backbone.Collection.extend({
		url: '/api/sentences',
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
            var tag = new Tag(_.pick(this.model.attributes, 'id', 'tag_id'));
            this.tagView = new TagView({ model: tag });
        },

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        },

        editSentiment: function () {
            this.tagView.render();
        }
    });

    var Tag = Backbone.Model.extend({

    });

    var TagView = Backbone.View.extend({
        el: $('#taggingBox'),

        events: {
            'click [name="sentiment"]': 'setSentiment'
        },

        template: _.template('<input type="button" value="Positive" id="positive" name="sentiment" data-tagid="1" />' +
                             '<input type="button" value="Neutral" id="neutral" name="sentiment" data-tagid="3" />' +
                             '<input type="button" value="Negative" id="negative" name="sentiment" data-tagid="2" />' +
                             '<span id="sentiment"></span>'),

        initialize: function () {

        },

        render: function () {
            this.$el.html(this.template());
            return this;
        },

        setSentiment: function (ev) {
            $('#sentiment').html(ev.target.id + ' ' + $(ev.target).data('tagid') + ' tagID:' + this.model.get('id'));

        }
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