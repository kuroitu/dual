#
# @Author: kuroitu (2020)
# @email: Skuroitu@gmail.com
#
import numpy as np


from dual import Dual
import dual


def test():
    print("+----------------------+")
    print("| Test of dmath module |")
    print("+----------------------+\n")

    print("定数のテスト", "test construct", "\n")
    print("--結果--", "--result--")
    print("pi = {}".format(dual.pi))
    print("e = {}".format(dual.e))
    print("-------------------------------------------\n")

    print("power, square, sqrt, cbrtのテスト", "test power, square, sqrt, cbrt", "\n")
    x = Dual(3, 1)
    y = Dual([2, 4], [5, 6])
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("power(x, 2) = {}".format(dual.power(x, 2)))
    print("power(y, 3) = {}".format(dual.power(y, 3)))
    print("square(x) = {}".format(dual.square(x)))
    print("square(y) = {}".format(dual.square(y)))
    print("sqrt(x) = {}".format(dual.sqrt(x)))
    print("sqrt(y) = {}".format(dual.sqrt(y)))
    print("cbrt(x) = {}".format(dual.cbrt(x)))
    print("cbrt(y) = {}".format(dual.cbrt(y)))
    print("-------------------------------------------\n")

    print("exp, exp2, expm1のテスト", "test exp, exp2, expm1", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("exp(x) = {}".format(dual.exp(x)))
    print("exp(y) = {}".format(dual.exp(y)))
    print("exp2(x) = {}".format(dual.exp2(x)))
    print("exp2(y) = {}".format(dual.exp2(y)))
    print("expm1(x) = {}".format(dual.expm1(x)))
    print("expm1(y) = {}".format(dual.expm1(y)))
    print("-------------------------------------------\n")

    print("log, logn, log2, log10, log1p, logaddexp, logaddexp2のテスト", \
            "test log, logn, log2, log10, log1p, logaddexp, logaddexp2", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("log(x) = {}".format(dual.log(x)))
    print("log(y) = {}".format(dual.log(y)))
    print("logn(x, 3) = {}".format(dual.logn(x, 3)))
    print("logn(y, 3) = {}".format(dual.logn(y, 3)))
    print("log2(x) = {}".format(dual.log2(x)))
    print("log2(y) = {}".format(dual.log2(y)))
    print("log10(x) = {}".format(dual.log10(x)))
    print("log10(y) = {}".format(dual.log10(y)))
    print("log1p(x) = {}".format(dual.log1p(x)))
    print("log1p(y) = {}".format(dual.log1p(y)))
    print("logaddexp(x, y) = {}".format(dual.logaddexp(x, y)))
    print("logaddexp2(x, y) = {}".format(dual.logaddexp2(x, y)))
    print("-------------------------------------------\n")

    print("sin, cos, tanのテスト", "test sin, cos, tan", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("sin(x) = {}".format(dual.sin(x)))
    print("sin(y) = {}".format(dual.sin(y)))
    print("cos(x) = {}".format(dual.cos(x)))
    print("cos(y) = {}".format(dual.cos(y)))
    print("tan(x) = {}".format(dual.tan(x)))
    print("tan(y) = {}".format(dual.tan(y)))
    print("-------------------------------------------\n")

    print("sinh, cosh, tanhのテスト", "test sinh, cosh, tanh", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("sinh(x) = {}".format(dual.sinh(x)))
    print("sinh(y) = {}".format(dual.sinh(y)))
    print("cosh(x) = {}".format(dual.cosh(x)))
    print("cosh(y) = {}".format(dual.cosh(y)))
    print("tanh(x) = {}".format(dual.tanh(x)))
    print("tanh(y) = {}".format(dual.tanh(y)))
    print("-------------------------------------------\n")

    print("arcsin, arccos, arctan, arctan2のテスト", "test arcsin, arccos, arctan, arctan2", "\n")
    x /= 7
    y /= 5
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("arcsin(x) = {}".format(dual.arcsin(x)))
    print("arcsin(y) = {}".format(dual.arcsin(y)))
    print("arccos(x) = {}".format(dual.arccos(x)))
    print("arccos(y) = {}".format(dual.arccos(y)))
    print("arctan(x) = {}".format(dual.arctan(x)))
    print("arctan(y) = {}".format(dual.arctan(y)))
    print("arctan2(x, y) = {}".format(dual.arctan2(x, y)))
    print("-------------------------------------------\n")

    print("arcsinh, arccosh, arctanhのテスト", "test arcsinh, arccosh, arctanh", "\n")
    x *= 7
    y *= 5
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("arcsinh(x) = {}".format(dual.arcsinh(x)))
    print("arcsinh(y) = {}".format(dual.arcsinh(y)))
    print("arccosh(x) = {}".format(dual.arccosh(x)))
    print("arccosh(y) = {}".format(dual.arccosh(y)))
    print("arctanh(x / 7) = {}".format(dual.arctanh(x / 7)))
    print("arctanh(y / 5) = {}".format(dual.arctanh(y / 5)))
    print("-------------------------------------------\n")

    print("csc, sec, cotのテスト", "test csc, sec, cot", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("csc(x) = {}".format(dual.csc(x)))
    print("csc(y) = {}".format(dual.csc(y)))
    print("sec(x) = {}".format(dual.sec(x)))
    print("sec(y) = {}".format(dual.sec(y)))
    print("cot(x) = {}".format(dual.cot(x)))
    print("cot(y) = {}".format(dual.cot(y)))
    print("-------------------------------------------\n")

    print("csch, sech, cothのテスト", "test csch, sech, coth", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("csch(x) = {}".format(dual.csch(x)))
    print("csch(y) = {}".format(dual.csch(y)))
    print("sech(x) = {}".format(dual.sech(x)))
    print("sech(y) = {}".format(dual.sech(y)))
    print("coth(x) = {}".format(dual.coth(x)))
    print("coth(y) = {}".format(dual.coth(y)))
    print("-------------------------------------------\n")

    print("arccsc, arcsec, arccotのテスト", "test arccsc, arcsec, arccot", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("arccsc(x) = {}".format(dual.arccsc(x)))
    print("arccsc(y) = {}".format(dual.arccsc(y)))
    print("arcsec(x) = {}".format(dual.arcsec(x)))
    print("arcsec(y) = {}".format(dual.arcsec(y)))
    print("arccot(x) = {}".format(dual.arccot(x)))
    print("arccot(y) = {}".format(dual.arccot(y)))
    print("-------------------------------------------\n")

    print("arccsch, arcsech, arccoth, sincのテスト", "test arccsch, arcsech, arccoth, sinc", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("arccsch(x) = {}".format(dual.arccsch(x)))
    print("arccsch(y) = {}".format(dual.arccsch(y)))
    print("arcsech(x / 7) = {}".format(dual.arcsech(x / 7)))
    print("arcsech(y / 5) = {}".format(dual.arcsech(y / 5)))
    print("arccoth(x) = {}".format(dual.arccoth(x)))
    print("arccoth(y) = {}".format(dual.arccoth(y)))
    print("sinc(x) = {}".format(dual.sinc(x)))
    print("sinc(y) = {}".format(dual.sinc(y)))
    print("-------------------------------------------\n")

    print("add, subtract, multiply, divide, dot, matmul ,reciprocalのテスト", \
            "test add, aubtract, multiply, divide, dot, matmul, reciprocal", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("add(x, y) = {}".format(dual.add(x, y)))
    print("subtract(x, y) = {}".format(dual.subtract(x, y)))
    print("multiply(x, y) = {}".format(dual.multiply(x, y)))
    print("divide(x, y) = {}".format(dual.divide(x, y)))
    print("dot(x, y) = {}".format(dual.dot(x, y)))
    print("matmul(x, y) = {}".format(dual.matmul(x, y)))
    print("reciprocal(x) = {}".format(dual.reciprocal(x)))
    print("reciprocal(y) = {}".format(dual.reciprocal(y)))
    print("-------------------------------------------\n")

    print("deg2rad, rad2degのテスト", "test deg2rad, rad2deg", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("deg2rad(x) = {}".format(dual.deg2rad(x)))
    print("deg2rad(y) = {}".format(dual.deg2rad(y)))
    print("rad2deg(x) = {}".format(dual.rad2deg(x)))
    print("rad2deg(y) = {}".format(dual.rad2deg(y)))
    print("-------------------------------------------\n")

    print("floor, trunc, ceilのテスト", "test floor, trunc, ceil", "\n")
    x = Dual(1.523, 0.3432)
    y = Dual([1.842, 3.463542], [5.846, 7.864808])
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("floor(x) = {}".format(dual.floor(x)))
    print("floor(y) = {}".format(dual.floor(y)))
    print("trunc(x) = {}".format(dual.trunc(x)))
    print("trunc(y) = {}".format(dual.trunc(y)))
    print("ceil(x) = {}".format(dual.ceil(x)))
    print("ceil(y) = {}".format(dual.ceil(y)))
    print("-------------------------------------------\n")

    print("round, rint, fixのテスト", "test round, rint, fix", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("round(x) = {}".format(dual.round(x)))
    print("round(y) = {}".format(dual.round(y)))
    print("round(x, 2) = {}".format(dual.round(x, 2)))
    print("round(y, 3) = {}".format(dual.round(y, 3)))
    print("rint(x) = {}".format(dual.rint(x)))
    print("rint(y) = {}".format(dual.rint(y)))
    print("fix(x) = {}".format(dual.fix(x)))
    print("fix(y) = {}".format(dual.fix(y)))
    print("-------------------------------------------\n")

    print("real, imag, conj, absoluteのテスト", "test real, imag, conj, absolute", "\n")
    x = Dual(3, 1)
    y = Dual([2, 1], [5, 6])
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("real(x) = {}".format(dual.real(x)))
    print("real(y) = {}".format(dual.real(y)))
    print("imag(x) = {}".format(dual.imag(x)))
    print("imag(y) = {}".format(dual.imag(y)))
    print("conj(x) = {}".format(dual.conj(x)))
    print("conj(y) = {}".format(dual.conj(y)))
    print("absolute(x) = {}".format(dual.absolute(x)))
    print("absolute(y) = {}".format(dual.absolute(y)))
    print("-------------------------------------------\n")

    print("fmax, fmin, isnan, isfinite, isinのテスト", \
            "test fmax, fmin, isnan. isfinite, isin", "\n")
    x = Dual([1, 5], [2, -3])
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("fmax(x, y) = {}".format(dual.fmax(x, y)))
    print("fmin(x, y) = {}".format(dual.fmin(x, y)))
    print("isnan(x) = {}".format(dual.isnan(x)))
    print("isnan(y) = {}".format(dual.isnan(y)))
    print("isnan(Dual(nan, 1)) = {}".format(dual.isnan(Dual(np.nan, 1))))
    print("isfinite(x) = {}".format(dual.isfinite(x)))
    print("isfinite(y) = {}".format(dual.isfinite(y)))
    print("isfinite(Dual(inf, 1)) = {}".format(dual.isfinite(Dual(np.inf, 1))))
    print("isinf(x) = {}".format(dual.isinf(x)))
    print("isinf(y) = {}".format(dual.isinf(y)))
    print("isinf(Dual(inf, 1)) = {}".format(dual.isinf(Dual(np.inf, 1))))
    print("-------------------------------------------\n")

    print("maximum, minimum, sign, sign_imagのテスト", \
            "test maximum, minimum, sign, sign_imag", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("maximum(x, y) = {}".format(dual.maximum(x, y)))
    print("minimum(x, y) = {}".format(dual.minimum(x, y)))
    print("sign(x) = {}".format(dual.sign(x)))
    print("sign_imag(x) = {}".format(dual.sign_imag(x)))
    print("-------------------------------------------\n")

    print("max, max_imag, min, min_imagのテスト", "test exp, exp2, expm1", "\n")
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("max(x) = {}".format(dual.max(x)))
    print("max_imag(x) = {}".format(dual.max_imag(x)))
    print("min(x) = {}".format(dual.min(x)))
    print("min_imag(x) = {}".format(dual.min_imag(x)))
    print("-------------------------------------------\n")

    print("nanmax, nanmax_imag, nanmin, nanmin_imagのテスト", \
            "test nanmax, nanmax_imag, nanmin, nanmin_imag", "\n")
    y = Dual([1, 4, -3, np.nan, 3], [2, np.nan, 3, 8, -2])
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("--結果--", "--result--")
    print("nanmax(x) = {}".format(dual.nanmax(x)))
    print("nanmax(y) = {}".format(dual.nanmax(y)))
    print("nanmax_imag(x) = {}".format(dual.nanmax_imag(x)))
    print("nanmin_imag(y) = {}".format(dual.nanmax_imag(y)))
    print("nanmin(x) = {}".format(dual.nanmin(x)))
    print("nanmin(y) = {}".format(dual.nanmin(y)))
    print("nanmin_imag(x) = {}".format(dual.nanmin_imag(x)))
    print("nanmin_imag(y) = {}".format(dual.nanmin_imag(y)))
    print("-------------------------------------------\n")


if __name__ == "__main__":
    test()
