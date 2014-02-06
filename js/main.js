/// <reference path="js/backbone.js" />
/// <reference path="js/underscore.js" />

$(function () {
    var Sentence = Backbone.Model.extend({

    });

    var SentenceList = Backbone.Collection.extend({
        model: Sentence
    });

    var SentenceView = Backbone.View.extend({
        tagName: 'span',
        className: 'sentence',

        events: {
            'click': 'editSentiment'
        },

        template: _.template("<%= text %>"),

        initialize: function () {

        },

        render: function () {
            this.$el.html(this.template(this.attributes));
            return this;
        },

        editSentiment: function () {
            alert('You clicked me!');
        }
    });

    var Sentences = new SentenceList([new Sentence({id: 1, text: "this is a test!", order: 1}),
                                new Sentence({id: 2, text: "this is a test 2.", order: 2}),
                                new Sentence({ id: 3, text: "this is a test 3?", order: 3 })]);

    Sentences.each(function (sentence) {
        $('#story').append(new SentenceView(sentence).render().$el);
    });
});