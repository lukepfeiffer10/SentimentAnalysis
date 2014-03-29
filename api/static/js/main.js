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
		},

		render: function (collection, response, options) {
		    collection.each(function (sentence) {
		        $('#story').append(new SentenceView({ model: sentence }).render().$el);
		    });
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
            var tag = new Tag(_.pick(this.model.attributes, 'id', 'tag_id'));
            var tagView = new TagView({ model: this.model, parent: this });
            if ($('#taggingBox').length === 1) {
                $('#taggingBox').remove();
            }
            $('#story').parent().append(tagView.render().$el);
        }
    });

    var Tag = Backbone.Model.extend({
        url: 'api/sentences'
    });

    var TagView = Backbone.View.extend({
        tagName: 'div',
        id: 'taggingBox',

        events: {
            'click [name="sentiment"]': 'setSentiment'
        },

        template: _.template('<input type="button" value="Positive" id="positive" name="sentiment" data-tagid="1" class="<% if (tag_id === 1) { %> selected <% } %>" />' +
                             '<input type="button" value="Neutral" id="neutral" name="sentiment" data-tagid="3" class="<% if (tag_id === 3) { %> selected <% } %>" />' +
                             '<input type="button" value="Negative" id="negative" name="sentiment" data-tagid="2" class="<% if (tag_id === 2) { %> selected <% } %>" />'),

        initialize: function (options) {
            this.parent = options.parent;
        },

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        },

        setSentiment: function (ev) {
            $('input[name="sentiment"]').removeClass("selected");
            $(ev.target).addClass('selected');
            this.parent.$el.removeClass('negative').removeClass('neutral').removeClass('positive').addClass(ev.target.id);
            this.model.set('tag_id', $(ev.target).data('tagid'));
            this.model.save(this.model.attributes, {
                success: function (model, response, options) {
                    if (response[0].status === 1) {
                        Sentences.fetch({
                            parse: true,
                            success: Sentences.render
                        });
                    }
                }
            });
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
                success: Sentences.render
            });
        }
    });

    var App = new AppView();
	
});