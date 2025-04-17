//
// This Stan program defines a simple model, with a
// vector of values 'y' modeled as normally distributed
// with mean 'mu' and standard deviation 'sigma'.
//
// Learn more about model development with Stan at:
//
//    http://mc-stan.org/users/interfaces/rstan.html
//    https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started
//

// Functions

functions {
  real pert_distribution_lpdf(real x, real a, real b, real c) {
    // Validación de parámetros
    if (a >= b) reject("a debe ser menor que b");
    if (c <= a || c >= b) reject("c debe estar entre a y b");
    
    // Cálculo de parámetros Beta
    real alpha = 1 + 4 * (c - a) / (b - a);
    real beta = 1 + 4 * (b - c) / (b - a);
    
    // Validación adicional
    if (alpha <= 0 || beta <= 0) reject("alpha y beta deben ser positivos");
    
    // Transformación a [0,1] con verificación
    real x_scaled = (x - a) / (b - a);
    if (x_scaled < 0 || x_scaled > 1) reject("x_scaled debe estar en [0,1]");
    
    return beta_lpdf(x_scaled | alpha, beta) - log(b - a);
  }
}



// The input data is a vector 'y' of length 'N'.
data {
  real a;       // Mínimo
  real b;       // Máximo
  real c;       // Moda
}

// The parameters accepted by the model. Our model
// accepts two parameters 'mu' and 'sigma'.
parameters {
  real<lower=a, upper=b> x;  // Variable con distribución PERT
}

// The model to be estimated. We model the output
// 'y' to be normally distributed with mean 'mu'
// and standard deviation 'sigma'.
model {
  // Distribución Beta escalada
  target += pert_distribution_lpdf(x | a, b, c);
}

