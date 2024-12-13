from .src.metodos_univariable.interval_halving import interval_halving
from .src.metodos_univariable.fibonacci import fibonacci_search
from .src.metodos_univariable.golden_section import golden_section_search
from .src.metodos_univariable.newton_raphson import newton_raphson_method
from .src.metodos_univariable.bisection import bisection_method
from .src.metodos_univariable.secante import secant_method

from .src.metodos_multivariable.caminata_aleatoria import met_random_walk
from .src.metodos_multivariable.nelder_mead_simplex import simplex_search_meth
from .src.metodos_multivariable.met_hooke_jeeves import hooke_jeeves
from .src.metodos_multivariable.met_cauchy import cauchy
from .src.metodos_multivariable.met_fletcher_reeves import fletcher_reeves
from .src.metodos_multivariable.met_newton import newton_method

from .src.funciones_prueba.funcionesunivariable import caja,caso1,caso2,caso3,caso4,funcion_clase,lata
from .src.funciones_prueba.funcionesmultivariable import ackley_function,beale_function,booth_function,bukin_functionN6,Crossintray_function,Easom_function,Eggholder_function,goldstein_price_function,Himmelblaus_function,Holder_table_function,Levi_functionN13,matyas_function,McCormick_function,rastrigin,rosenbrock_funt,Schaffer_functionN2,Schaffer_functionN4,shekel,sphere_function,StyblinskiTang_function,Three_hump_camel_function