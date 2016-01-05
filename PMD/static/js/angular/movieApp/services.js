angular.module('movieApp.services', []).factory('Movie', function($resource) {
  return $resource('/api/movies/:id', { id: '@id' }, {
    update: {
      method: 'PUT'
    }
  });
});
