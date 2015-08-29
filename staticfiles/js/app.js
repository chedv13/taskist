window.Taskist = angular.module('taskist', ['ngRoute', 'ngResource'])
    .config(function ($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }).config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/templates/index.html'
            })
    });
