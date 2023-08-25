
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                                       |
| tornado_http   | 152 ms                                                       | 114 ms: 1.34x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.3 ms: 1.61x faster                                                        |
| float          | 110 ms                                                       | 78.9 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.33x faster                                                         |
| regex_dna      | 259 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.57x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.35x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                                        |
| json_loads           | 30.0 us                                                      | 25.2 us: 1.19x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.06x faster                                                         |
| unpickle_list        | 4.49 us                                                      | 4.61 us: 1.03x slower                                                        |
| pickle               | 9.94 us                                                      | 10.5 us: 1.05x slower                                                        |
| unpickle             | 14.2 us                                                      | 15.0 us: 1.06x slower                                                        |
| pickle_list          | 4.11 us                                                      | 4.41 us: 1.07x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 33.3 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.25 ms: 2.30x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 380 ms: 2.06x faster                                                         |
| logging_silent          | 166 ns                                                       | 92.4 ns: 1.79x faster                                                        |
| go                      | 259 ms                                                       | 146 ms: 1.77x faster                                                         |
| richards                | 74.1 ms                                                      | 44.5 ms: 1.66x faster                                                        |
| scimark_lu              | 164 ms                                                       | 99.5 ms: 1.65x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 5.86 ms: 1.62x faster                                                        |
| nbody                   | 137 ms                                                       | 85.3 ms: 1.61x faster                                                        |
| generators              | 58.0 ms                                                      | 36.0 ms: 1.61x faster                                                        |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                                         |
| pyflate                 | 697 ms                                                       | 437 ms: 1.60x faster                                                         |
| chaos                   | 107 ms                                                       | 67.8 ms: 1.58x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 205 us: 1.57x faster                                                         |
| raytrace                | 488 ms                                                       | 316 ms: 1.54x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 72.3 ms: 1.52x faster                                                        |
| spectral_norm           | 136 ms                                                       | 90.2 ms: 1.51x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.81 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.09 sec: 1.48x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 80.3 ms: 1.47x faster                                                        |
| async_tree_none         | 700 ms                                                       | 476 ms: 1.47x faster                                                         |
| async_tree_memoization  | 824 ms                                                       | 572 ms: 1.44x faster                                                         |
| pickle_pure_python      | 457 us                                                       | 318 us: 1.44x faster                                                         |
| float                   | 110 ms                                                       | 78.9 ms: 1.40x faster                                                        |
| fannkuch                | 496 ms                                                       | 357 ms: 1.39x faster                                                         |
| coroutines              | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 703 ms: 1.35x faster                                                         |
| json_dumps              | 14.2 ms                                                      | 10.5 ms: 1.35x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                                       |
| tornado_http            | 152 ms                                                       | 114 ms: 1.34x faster                                                         |
| regex_compile           | 194 ms                                                       | 145 ms: 1.33x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 37.2 us: 1.31x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.78 us: 1.31x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 808 ms: 1.30x faster                                                         |
| xml_etree_process       | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.51 us: 1.27x faster                                                        |
| nqueens                 | 112 ms                                                       | 88.9 ms: 1.27x faster                                                        |
| mypy2                   | 466 ms                                                       | 377 ms: 1.24x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 64.8 ms: 1.23x faster                                                        |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| scimark_fft             | 359 ms                                                       | 298 ms: 1.21x faster                                                         |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                                       |
| json_loads              | 30.0 us                                                      | 25.2 us: 1.19x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 59.2 ms: 1.19x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 958 us: 1.19x faster                                                         |
| deepcopy                | 454 us                                                       | 383 us: 1.19x faster                                                         |
| docutils                | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.44 ms: 1.17x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.46 us: 1.16x faster                                                        |
| json                    | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.61 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.62 us: 1.13x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 52.7 ns: 1.13x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                        |
| regex_dna               | 259 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                                        |
| comprehensions          | 26.9 us                                                      | 24.5 us: 1.10x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 148 ms: 1.09x faster                                                         |
| async_generators        | 422 ms                                                       | 389 ms: 1.08x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 105 ms: 1.06x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| meteor_contest          | 137 ms                                                       | 138 ms: 1.01x slower                                                         |
| telco                   | 7.14 ms                                                      | 7.26 ms: 1.02x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.61 us: 1.03x slower                                                        |
| pickle                  | 9.94 us                                                      | 10.5 us: 1.05x slower                                                        |
| unpickle                | 14.2 us                                                      | 15.0 us: 1.06x slower                                                        |
| pickle_list             | 4.11 us                                                      | 4.41 us: 1.07x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 33.3 us: 1.11x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                        |
| dask                    | 463 ms                                                       | 563 ms: 1.22x slower                                                         |
| coverage                | 64.0 ms                                                      | 90.6 ms: 1.42x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x
