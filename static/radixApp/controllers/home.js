"use strict";
angular.module("radixPiApp")

    .controller('HomeCtrl', ['$scope', "Notification", "$http", "$timeout", "$q",
        function ($scope, Notification, $http, $timeout, $q) {
            console.log("HomeCtrl");
            console.log(window.location.protocol);
            var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

            var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/radix/temperature");
            console.log(ws_scheme + '://' + window.location.host + "/radix/");
            var chatsock1 = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/radix/humidity");
           
            chatsock.onopen = function() {
                console.log("Connectado con WebSocket! ");
                chatsock.send("Connected!");
                $scope.panels[0].options = {
                chart: {
                    type: 'lineChart',
                    height: 180,
                    margin : {
                        top: 20,
                        right: 20,
                        bottom: 40,
                        left: 55
                    },
                    x: function(d){ return d.x; },
                    y: function(d){ return d.y; },
                    useInteractiveGuideline: true,
                    duration: 500,    
                    yAxis: {
                        tickFormat: function(d){
                        return d3.format('.01f')(d);
                        }
                    }
                }
            };

            $scope.panels[0].options.chart.yDomain = [0,50];

            $scope.panels[0].data = [{ values: [], key: 'Temperatura' }];
        
            $scope.panels[0].run = true;

            };

            

            var x= 1;

            

            chatsock.onmessage = function(message) {
                console.log("home.js chatsock1: Received Sock message! "+ message.data);
                console.log(message.data);

                $scope.panels[0].lastvalue = message.data

                $scope.panels[0].data[0].values.push({ x: x,	y: message.data});
                $scope.panels[0].history.push({ x: x,	y: message.data});
                if ($scope.panels[0].data[0].values.length > 20) $scope.panels[0].data[0].values.shift();
                x++;
                $scope.$apply(); 
	    
            };
            
            console.log(chatsock.readyState);

            if (chatsock.readyState == WebSocket.OPEN) {
            chatsock.onopen();
            }

            chatsock1.onopen = function() {
                console.log("Connectado con WebSocket! ");
                chatsock1.send("Connected!");
                $scope.panels[1].options = {
                chart: {
                    type: 'lineChart',
                    height: 180,
                    margin : {
                        top: 20,
                        right: 20,
                        bottom: 40,
                        left: 55
                    },
                    x: function(d){ return d.x; },
                    y: function(d){ return d.y; },
                    useInteractiveGuideline: true,
                    duration: 500,    
                    yAxis: {
                        tickFormat: function(d){
                        return d3.format('.01f')(d);
                        }
                    }
                }
            };


            $scope.panels[1].options.chart.yDomain = [0,80];

            $scope.panels[1].data = [{ values: [], key: 'Humedad' }];
        
            $scope.panels[1].run = true;
            };

            

            var x1= 1;

            

            chatsock1.onmessage = function(message) {
                console.log("home.js chatsock1: Received Sock message! "+ message.data);
                console.log(message.data);

                $scope.panels[1].lastvalue = message.data

                $scope.panels[1].data[0].values.push({ x: x1,	y: message.data});
                $scope.panels[1].history.push({ x: x1,	y: message.data});
                if ($scope.panels[1].data[0].values.length > 20) $scope.panels[1].data[0].values.shift();
                x1++;
                $scope.$apply(); 
	    
            };




        }])

;