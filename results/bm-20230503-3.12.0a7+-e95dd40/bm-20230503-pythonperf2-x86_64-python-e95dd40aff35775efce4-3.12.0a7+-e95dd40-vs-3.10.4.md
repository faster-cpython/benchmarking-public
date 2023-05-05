
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| tornado_http   | 151 ms                                                       | 114 ms: 1.32x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 85.3 ms: 1.55x faster                                                        |
| float          | 109 ms                                                       | 78.9 ms: 1.39x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 145 ms: 1.31x faster                                                         |
| regex_dna      | 261 ms                                                       | 232 ms: 1.13x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.8 ms: 1.09x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 205 us: 1.56x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 318 us: 1.42x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.8 ms: 1.32x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 85.6 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 109 ms                                                       | 105 ms: 1.04x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.61 us: 1.03x faster                                                        |
| pickle               | 10.1 us                                                      | 10.5 us: 1.03x slower                                                        |
| pickle_list          | 4.11 us                                                      | 4.41 us: 1.07x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 33.3 us: 1.13x slower                                                        |
| unpickle             | 13.3 us                                                      | 15.0 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.25 ms: 2.32x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 380 ms: 2.07x faster                                                         |
| go                      | 264 ms                                                       | 146 ms: 1.81x faster                                                         |
| logging_silent          | 165 ns                                                       | 92.4 ns: 1.78x faster                                                        |
| pyflate                 | 731 ms                                                       | 437 ms: 1.67x faster                                                         |
| richards                | 73.9 ms                                                      | 44.5 ms: 1.66x faster                                                        |
| scimark_lu              | 164 ms                                                       | 99.5 ms: 1.65x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 5.86 ms: 1.63x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.39 ms: 1.62x faster                                                        |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                                         |
| chaos                   | 108 ms                                                       | 67.8 ms: 1.59x faster                                                        |
| generators              | 57.0 ms                                                      | 36.0 ms: 1.58x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 205 us: 1.56x faster                                                         |
| raytrace                | 491 ms                                                       | 316 ms: 1.55x faster                                                         |
| nbody                   | 132 ms                                                       | 85.3 ms: 1.55x faster                                                        |
| spectral_norm           | 138 ms                                                       | 90.2 ms: 1.53x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 72.3 ms: 1.50x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.81 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.09 sec: 1.48x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 80.3 ms: 1.48x faster                                                        |
| async_tree_none         | 698 ms                                                       | 476 ms: 1.47x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 572 ms: 1.44x faster                                                         |
| pickle_pure_python      | 451 us                                                       | 318 us: 1.42x faster                                                         |
| fannkuch                | 496 ms                                                       | 357 ms: 1.39x faster                                                         |
| float                   | 109 ms                                                       | 78.9 ms: 1.39x faster                                                        |
| coroutines              | 30.6 ms                                                      | 22.4 ms: 1.36x faster                                                        |
| logging_simple          | 9.24 us                                                      | 6.78 us: 1.36x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 703 ms: 1.35x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.34x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.51 us: 1.32x faster                                                        |
| tornado_http            | 151 ms                                                       | 114 ms: 1.32x faster                                                         |
| deepcopy_memo           | 49.2 us                                                      | 37.2 us: 1.32x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 58.8 ms: 1.32x faster                                                        |
| regex_compile           | 191 ms                                                       | 145 ms: 1.31x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.65 sec: 1.28x faster                                                       |
| nqueens                 | 114 ms                                                       | 88.9 ms: 1.28x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 808 ms: 1.27x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 64.8 ms: 1.24x faster                                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| mypy2                   | 466 ms                                                       | 377 ms: 1.24x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                         |
| scimark_fft             | 359 ms                                                       | 298 ms: 1.21x faster                                                         |
| json_loads              | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| deepcopy                | 457 us                                                       | 383 us: 1.19x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 958 us: 1.19x faster                                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 59.2 ms: 1.18x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.53 sec: 1.16x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.44 ms: 1.15x faster                                                        |
| json                    | 5.94 ms                                                      | 5.18 ms: 1.15x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 52.7 ns: 1.13x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.46 us: 1.13x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.62 us: 1.13x faster                                                        |
| regex_dna               | 261 ms                                                       | 232 ms: 1.13x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.61 ms: 1.12x faster                                                        |
| comprehensions          | 27.3 us                                                      | 24.5 us: 1.11x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.4 ms: 1.10x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 85.6 ms: 1.10x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.8 ms: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| async_generators        | 419 ms                                                       | 389 ms: 1.08x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 105 ms: 1.04x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| unpickle_list           | 4.73 us                                                      | 4.61 us: 1.03x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| meteor_contest          | 142 ms                                                       | 138 ms: 1.02x faster                                                         |
| telco                   | 7.14 ms                                                      | 7.26 ms: 1.02x slower                                                        |
| pickle                  | 10.1 us                                                      | 10.5 us: 1.03x slower                                                        |
| pickle_list             | 4.11 us                                                      | 4.41 us: 1.07x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.76 ms: 1.09x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 33.3 us: 1.13x slower                                                        |
| unpickle                | 13.3 us                                                      | 15.0 us: 1.13x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                        |
| dask                    | 478 ms                                                       | 563 ms: 1.18x slower                                                         |
| coverage                | 71.1 ms                                                      | 90.6 ms: 1.28x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
