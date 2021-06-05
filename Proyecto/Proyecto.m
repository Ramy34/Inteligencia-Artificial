>> input = (xlsread('SinCos.xlsx','A2:A62834'))';
>> seno = (xlsread('SinCos.xlsx','B2:B62834'))';
>> coseno = (xlsread('SinCos.xlsx','C2:C62834'))';
>> target = [seno; coseno];
>> net = newff([-3.1416 3.1416], [6, 2],{'tansig', 'tansig'}, 'trainlm'); 
>> net.trainParam.epochs = 1000;
>> net.trainParam.goal = 0.000001;
>> net = train(net,input,target);
>> salida = sim(net,input);
>> plot(input,target,'-',input,salida,'--')
>> legend('Objetivo Seno','Objetivo Coseno','Red Seno', 'Red Coseno')