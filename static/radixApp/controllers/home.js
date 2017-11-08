"use strict";
angular.module("radixPiApp")

    .controller('HomeCtrl', ['$scope', "Notification", "$http", "$timeout", "$q",
        function ($scope, Notification, $http, $timeout, $q) {
            console.log("HomeCtrl");
            console.log(window.location.protocol);
            var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

            var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/radix/");
            console.log(ws_scheme + '://' + window.location.host + "/radix/");
            var data = []
            chatsock.onopen = function() {
                console.log("Connectado con WebSocket! ");
                chatsock.send("Connected!");
            };

            chatsock.onmessage = function(message) {
                console.log("sensor.js: Received Sock message! "+ message.data);
                console.log(message.data);
                var chart = {
                        "manageresize": "1",    // averiguar bien para que sirve                                    
                        "numdisplaysets": "12", // cantidad de valores a mostrar                                    
                        "showrealtimevalue": "0",   // muestra el ultimo valor abajo de la grafica 
                        //"rotatelabels": "1",  // gira 90 grados el label del eje x
                        //"slantlabels": "1",   // inclina el label del eje x (hay que usarlo con rotatelabels)
                        //"xAxisName": xAxisName,
                        "yaxisname": "Valor",
                        "yaxisminvalue": "Tiempo",
                        "yaxismaxvalue": "200",
                        // Anchor: Circulo de cada valor                                    
                        "anchorradius": "3",
                        "anchorbgcolor": "0377D0",
                        "anchorbordercolor": "FFFFFF",
                        "anchorborderthickness": "0",
                        "anchoralpha": "90",
                        // borde de la grafica
                        "showplotborder": "1",
                        "plotborderthickness": "2",
                        "plotBorderAlpha": "25",
                        "plotbordercolor": "0007D0",
                        "plotfillcolor": "0377D0",                                    
                        // "numvdivlines": "2", // poner ejes verticales en la grafica                                     
                        // "canvaspadding": "0",    // supongo que para darle padding a la grafica. Revisar.
                        "bgColor": "#ffffff",
                        "showBorder": "0",
                        "showCanvasBorder": "0",                                    
                        "usePlotGradientColor": "0",
                        "plotFillAlpha": "50",
                        "showXAxisLine": "1",
                        "axisLineAlpha": "25",
                        "divLineAlpha": "10",
                        "showValues": "1",
                        "showAlternateHGridColor": "0",
                        "captionFontSize": "14",
                        "subcaptionFontSize": "14",
                        "subcaptionFontBold": "0",
                        "toolTipColor": "#ffffff",
                        "toolTipBorderThickness": "0",
                        "toolTipBgColor": "#000000",
                        "toolTipBgAlpha": "80",
                        "toolTipBorderRadius": "2",
                        "toolTipPadding": "5",
                        //------------------------
                        "refreshinterval": "1",
                        "exportEnabled": "1",
                        "exportAtClientSide": "1",   // ahora mismo solamente funciona en Chrome y Firefox
                        "exportFormats": "PNG=Guardar como PNG|JPG=Guardar como JPG|SVG=Guardar como SVG|PDF=Guardar como PDF",
                        "exportTargetWindow": "_self",
                        "exportFileName": "Gráfico de Temperatura"
                }
                $scope.datasource1 = {};
                $scope.datasource1.chart = chart;

                $scope.datasource1.categories = [{
                    "category": [{
                        "label": "12"
                    }]
                }];

                $scope.datasource1.dataset = [{
                    // "seriesname": "Temperatura",
                    // "showvalues": "0",
                    "data": [{
                        "value": message.data
                    }]
                }];
            };
            console.log(chatsock.readyState);

            if (chatsock.readyState == WebSocket.OPEN) {
            chatsock.onopen();
            }




        }])

;