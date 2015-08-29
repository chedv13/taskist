Taskist.provider('PostProvider', function () {
    this.$get = ['$resource', function ($resource) {
        return $resource('/posts/:_id.json', {}, {
            query: {
                method: 'GET',
                isArray: false
            }
        });
    }];
});
