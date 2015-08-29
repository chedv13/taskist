Taskist.controller('MainCtrl', function ($scope, PostProvider) {
    $scope.postsData = PostProvider.query({}, function () {
        $scope.posts = $scope.postsData;

        console.log($scope.posts);

        //$scope.posts = $scope.postsData.posts;
        //$scope.totalItems = $scope.postsData.meta.total_count;
        //$scope.currentPage = 1;
    });
});