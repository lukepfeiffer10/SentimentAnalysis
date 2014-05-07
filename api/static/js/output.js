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
            this.totalWords = collection.models.reduce(function (memo, value, key) {
                return memo + value.get("length");
            }, 0);
            collection.each(function (cluster, index) {
                var container = $('<div class="cluster">');
                container.append(new SentenceClusterView({ collection: cluster.sentences }).render().$el);
                container.append(new ClusterDetailsView({ model: cluster, number: index + 1, totalWordCount: this.totalWords }).render().$el);
                $('#content').append(container);
            }, this);
            
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
        tagName: 'div',
        className: 'clusterDetails',

        events: {
        },

        template: _.template("Cluster <%= number %><br/>" +
                             "Emotion: <%= sentiment %><br/>" + 
                             "Weight: <%= weight %><br/>" + 
                             "Story Percentage: <%= length %> / <%= total %>"),

        initialize: function (options) {
            this.number = options.number;
            this.total = options.totalWordCount;
        },

        render: function () {
            var viewAttributes = this.model.attributes;
            viewAttributes.number = this.number;
            viewAttributes.total = this.total;
            this.$el.html(this.template(viewAttributes));
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