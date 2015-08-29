window.Taskist = angular.module('taskist', ['ngRoute', 'ngResource', 'akoenig.deckgrid'])
    .config(function ($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }).config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/blog/posts',
                controller: 'MainCtrl'
            });
    });
