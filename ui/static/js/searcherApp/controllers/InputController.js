angular.module('searcherApp').controller('InputController', function ($scope, AppointmentService, $state) {
    var vm = this;
    vm.submit = function () {
        AppointmentService.getAppointment($scope.registrationNumber).then(function (response) {
            if (response.data) {
                $state.go('results', {appointmentId: $scope.registrationNumber});
            }
        });
    }
});
