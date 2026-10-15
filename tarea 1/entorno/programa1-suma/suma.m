args = argv();

if length(args) >= 2
    x = str2double(args{1});
    y = str2double(args{2});
else
    x_input = input("Ingrese el numero 1: ", "s");
    x = str2double(x_input);
    if isnan(x)
        x = 0.1;
    endif

    y_input = input("Ingrese el numero 2: ", "s");
    y = str2double(y_input);
    if isnan(y)
        y = 0.2;
    endif
endif

resultado = x + y;
printf("%.17g\n", resultado);