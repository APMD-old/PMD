angular.module('movieApp.controllers', []).controller('MovieListController', function($scope, Movie) {
  $scope.movies = Movie.query();
});
