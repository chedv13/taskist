Taskist.controller('CommonController', function ($scope, PostProvider) {
    $scope.postsData = PostProvider.query({}, function () {
        console.log($scope.postsData[0]);
        //$scope.posts = $scope.postsData.posts;
        //$scope.totalItems = $scope.postsData.meta.total_count;
        //$scope.currentPage = 1;
    });
});