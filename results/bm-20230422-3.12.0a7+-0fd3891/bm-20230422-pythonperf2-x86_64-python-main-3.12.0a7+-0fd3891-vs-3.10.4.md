
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.48 ms: 1.29x faster                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                       |
| html5lib       | 96.3 ms                                                      | 67.8 ms: 1.42x faster                                        |
| tornado_http   | 151 ms                                                       | 119 ms: 1.26x faster                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 86.6 ms: 1.53x faster                                        |
| float          | 109 ms                                                       | 79.1 ms: 1.38x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 143 ms: 1.34x faster                                         |
| regex_dna      | 261 ms                                                       | 232 ms: 1.12x faster                                         |
| regex_v8       | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 205 us: 1.55x faster                                         |
| pickle_pure_python   | 451 us                                                       | 315 us: 1.43x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.2 ms: 1.33x faster                                        |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                        |
| xml_etree_generate   | 94.1 ms                                                      | 84.5 ms: 1.11x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.96 us: 1.04x faster                                        |
| pickle               | 10.1 us                                                      | 10.2 us: 1.00x slower                                        |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                        |
| unpickle             | 13.3 us                                                      | 14.2 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                        |
| django_template | 52.0 ms                                                      | 38.6 ms: 1.35x faster                                        |
| genshi_text     | 31.7 ms                                                      | 24.9 ms: 1.27x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 54.1 ms: 1.17x faster                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.30 ms: 2.29x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 376 ms: 2.09x faster                                         |
| go                      | 264 ms                                                       | 145 ms: 1.82x faster                                         |
| logging_silent          | 165 ns                                                       | 94.2 ns: 1.75x faster                                        |
| scimark_lu              | 164 ms                                                       | 94.7 ms: 1.73x faster                                        |
| richards                | 73.9 ms                                                      | 43.3 ms: 1.70x faster                                        |
| pyflate                 | 731 ms                                                       | 437 ms: 1.68x faster                                         |
| raytrace                | 491 ms                                                       | 300 ms: 1.64x faster                                         |
| hexiom                  | 9.54 ms                                                      | 5.84 ms: 1.63x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.63x faster                                        |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.63x faster                                         |
| chaos                   | 108 ms                                                       | 66.4 ms: 1.62x faster                                        |
| spectral_norm           | 138 ms                                                       | 86.5 ms: 1.59x faster                                        |
| generators              | 57.0 ms                                                      | 36.4 ms: 1.57x faster                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.8 ms: 1.56x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 205 us: 1.55x faster                                         |
| nbody                   | 132 ms                                                       | 86.6 ms: 1.53x faster                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.78 ms: 1.51x faster                                        |
| mako                    | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                        |
| crypto_pyaes            | 119 ms                                                       | 80.4 ms: 1.47x faster                                        |
| fannkuch                | 496 ms                                                       | 341 ms: 1.46x faster                                         |
| pickle_pure_python      | 451 us                                                       | 315 us: 1.43x faster                                         |
| logging_simple          | 9.24 us                                                      | 6.49 us: 1.42x faster                                        |
| html5lib                | 96.3 ms                                                      | 67.8 ms: 1.42x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.14 sec: 1.41x faster                                       |
| json_dumps              | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                        |
| async_tree_none         | 698 ms                                                       | 498 ms: 1.40x faster                                         |
| async_tree_memoization  | 822 ms                                                       | 587 ms: 1.40x faster                                         |
| logging_format          | 9.94 us                                                      | 7.15 us: 1.39x faster                                        |
| float                   | 109 ms                                                       | 79.1 ms: 1.38x faster                                        |
| thrift                  | 1.23 ms                                                      | 906 us: 1.35x faster                                         |
| coroutines              | 30.6 ms                                                      | 22.6 ms: 1.35x faster                                        |
| django_template         | 52.0 ms                                                      | 38.6 ms: 1.35x faster                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.7 us: 1.34x faster                                        |
| regex_compile           | 191 ms                                                       | 143 ms: 1.34x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 58.2 ms: 1.33x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.31x faster                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 733 ms: 1.30x faster                                         |
| chameleon               | 9.62 ms                                                      | 7.48 ms: 1.29x faster                                        |
| nqueens                 | 114 ms                                                       | 89.0 ms: 1.28x faster                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.66 sec: 1.28x faster                                       |
| genshi_text             | 31.7 ms                                                      | 24.9 ms: 1.27x faster                                        |
| tornado_http            | 151 ms                                                       | 119 ms: 1.26x faster                                         |
| pprint_safe_repr        | 1.03 sec                                                     | 815 ms: 1.26x faster                                         |
| scimark_fft             | 359 ms                                                       | 288 ms: 1.25x faster                                         |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 64.9 ms: 1.24x faster                                        |
| json_loads              | 30.3 us                                                      | 24.5 us: 1.24x faster                                        |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.21x faster                                         |
| mypy2                   | 466 ms                                                       | 387 ms: 1.20x faster                                         |
| docutils                | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                       |
| bench_thread_pool       | 1.14 ms                                                      | 964 us: 1.18x faster                                         |
| deepcopy                | 457 us                                                       | 388 us: 1.18x faster                                         |
| json                    | 5.94 ms                                                      | 5.05 ms: 1.18x faster                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 59.6 ms: 1.18x faster                                        |
| genshi_xml              | 63.5 ms                                                      | 54.1 ms: 1.17x faster                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.35 ms: 1.17x faster                                        |
| pathlib                 | 21.3 ms                                                      | 18.4 ms: 1.16x faster                                        |
| sympy_expand            | 603 ms                                                       | 524 ms: 1.15x faster                                         |
| mdp                     | 2.95 sec                                                     | 2.57 sec: 1.15x faster                                       |
| pylint                  | 562 ms                                                       | 491 ms: 1.14x faster                                         |
| unpack_sequence         | 59.7 ns                                                      | 52.6 ns: 1.14x faster                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.45 us: 1.13x faster                                        |
| regex_dna               | 261 ms                                                       | 232 ms: 1.12x faster                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.61 ms: 1.12x faster                                        |
| sqlite_synth            | 2.96 us                                                      | 2.65 us: 1.12x faster                                        |
| xml_etree_generate      | 94.1 ms                                                      | 84.5 ms: 1.11x faster                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                        |
| sympy_str               | 358 ms                                                       | 324 ms: 1.11x faster                                         |
| xml_etree_parse         | 160 ms                                                       | 145 ms: 1.10x faster                                         |
| comprehensions          | 27.3 us                                                      | 25.0 us: 1.09x faster                                        |
| async_generators        | 419 ms                                                       | 386 ms: 1.09x faster                                         |
| regex_v8                | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                        |
| sympy_sum               | 193 ms                                                       | 182 ms: 1.06x faster                                         |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.96 us: 1.04x faster                                        |
| meteor_contest          | 142 ms                                                       | 137 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                        |
| telco                   | 7.14 ms                                                      | 7.05 ms: 1.01x faster                                        |
| pickle                  | 10.1 us                                                      | 10.2 us: 1.00x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.56 ms: 1.03x slower                                        |
| pickle_dict             | 29.5 us                                                      | 30.9 us: 1.05x slower                                        |
| unpickle                | 13.3 us                                                      | 14.2 us: 1.07x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                        |
| dask                    | 478 ms                                                       | 560 ms: 1.17x slower                                         |
| regex_effbot            | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                        |
| coverage                | 71.1 ms                                                      | 90.9 ms: 1.28x slower                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                 |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
