/// <reference path="js/backbone.js" />
/// <reference path="js/jquery.js" />
/// <reference path="js/underscore.js" />

$(function () {
    var Sentence = Backbone.Model.extend({
    });

    var SentenceList = Backbone.Collection.extend({
        model: Sentence
    });

    var SentenceView = Backbone.View.extend({

        template: _.template("<%= sentence_txt %>"),

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        }
    });

    var Cluster = Backbone.Model.extend({
        initialize: function (attributes, options) {
            this.sentences = new SentenceList(attributes.sentences);
        }
    });

    var ClusterList = Backbone.Collection.extend({
        url: '/api/clusters',
        model: Cluster,

        parse: function (response) {
            return response.sentences;
        },

        render: function (collection, response, options) {
            collection.set(response);
            collection.each(function (cluster) {
                $('#content').append(new SentenceClusterView({ collection: cluster.sentences }).render().$el);
            });
        }
    });

    var SentenceClusterView = Backbone.View.extend({
        tagName: 'div',
        className: 'sentenceCluster',

        events: {
        },
        
        initialize: function () {

        },

        render: function () {
            var container = $('<div class="sentenceContainer">')
            this.collection.each(function (sentence) {
                container.append(new SentenceView({ model: sentence }).render().$el);
            }, this);
            this.$el.append(container);
            return this;
        }
    });

    var ClusterDetailsView = Backbone.View.extend({
        tagName: 'span',

        events: {
        },

        template: _.template("<%= sentence_txt %>"),

        initialize: function () {

        },

        render: function () {
            this.$el.html(this.template(this.model.attributes));
            return this;
        }
    });

    var Clusters = new ClusterList();

    var AppView = Backbone.View.extend({
        el: $('body'),

        initialize: function () {
            Clusters.fetch({
                success: Clusters.render
            });
        }
    });

    var App = new AppView();

});