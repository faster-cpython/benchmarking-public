
# Results vs. 3.11.0

- fork: JelleZijlstra
- ref: tvobject
- machine: linux-x86_64
- commit hash: 827b9e5
- commit date: 2023-05-02
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                    |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                  |
| html5lib       | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                                   |
| tornado_http   | 122 ms                                                       | 113 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.7 ms: 1.03x faster                                                   |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                    |
| float          | 74.2 ms                                                      | 78.0 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.10x faster                                                    |
| regex_v8       | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                   |
| regex_dna      | 227 ms                                                       | 234 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                   |
| unpickle_pure_python | 241 us                                                       | 204 us: 1.18x faster                                                    |
| json_loads           | 28.7 us                                                      | 25.1 us: 1.14x faster                                                   |
| xml_etree_parse      | 158 ms                                                       | 145 ms: 1.09x faster                                                    |
| xml_etree_process    | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                   |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                   |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                                   |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.06x slower                                                   |
| unpickle_list        | 4.53 us                                                      | 4.83 us: 1.07x slower                                                   |
| xml_etree_generate   | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                   |
| pickle_list          | 3.83 us                                                      | 4.28 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                   |
| python_startup_no_site | 7.76 ms                                                      | 8.47 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                                   |
| mako           | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                   |
| genshi_text    | 26.1 ms                                                      | 24.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                        | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 381 ms: 1.98x faster                                                    |
| generators              | 56.0 ms                                                      | 35.9 ms: 1.56x faster                                                   |
| json_dumps              | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                   |
| fannkuch                | 429 ms                                                       | 346 ms: 1.24x faster                                                    |
| deltablue               | 4.00 ms                                                      | 3.25 ms: 1.23x faster                                                   |
| coroutines              | 27.6 ms                                                      | 22.5 ms: 1.23x faster                                                   |
| chaos                   | 80.9 ms                                                      | 66.2 ms: 1.22x faster                                                   |
| hexiom                  | 7.13 ms                                                      | 5.91 ms: 1.21x faster                                                   |
| mypy2                   | 451 ms                                                       | 376 ms: 1.20x faster                                                    |
| scimark_lu              | 115 ms                                                       | 96.2 ms: 1.19x faster                                                   |
| unpickle_pure_python    | 241 us                                                       | 204 us: 1.18x faster                                                    |
| nqueens                 | 103 ms                                                       | 88.9 ms: 1.16x faster                                                   |
| json_loads              | 28.7 us                                                      | 25.1 us: 1.14x faster                                                   |
| richards                | 48.3 ms                                                      | 42.7 ms: 1.13x faster                                                   |
| go                      | 164 ms                                                       | 147 ms: 1.12x faster                                                    |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                                   |
| logging_format          | 8.11 us                                                      | 7.34 us: 1.10x faster                                                   |
| json                    | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                                   |
| logging_simple          | 7.19 us                                                      | 6.53 us: 1.10x faster                                                   |
| regex_compile           | 158 ms                                                       | 144 ms: 1.10x faster                                                    |
| async_tree_memoization  | 630 ms                                                       | 575 ms: 1.10x faster                                                    |
| genshi_xml              | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                                   |
| async_tree_none         | 519 ms                                                       | 478 ms: 1.09x faster                                                    |
| xml_etree_parse         | 158 ms                                                       | 145 ms: 1.09x faster                                                    |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                   |
| pycparser               | 1.32 sec                                                     | 1.22 sec: 1.09x faster                                                  |
| mdp                     | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                  |
| dulwich_log             | 68.4 ms                                                      | 63.5 ms: 1.08x faster                                                   |
| genshi_text             | 26.1 ms                                                      | 24.3 ms: 1.08x faster                                                   |
| sqlglot_transpile       | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                                   |
| tornado_http            | 122 ms                                                       | 113 ms: 1.07x faster                                                    |
| async_tree_io           | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                                  |
| logging_silent          | 101 ns                                                       | 94.7 ns: 1.06x faster                                                   |
| bench_thread_pool       | 1.01 ms                                                      | 955 us: 1.06x faster                                                    |
| sqlglot_normalize       | 126 ms                                                       | 119 ms: 1.06x faster                                                    |
| raytrace                | 317 ms                                                       | 300 ms: 1.06x faster                                                    |
| html5lib                | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                                   |
| spectral_norm           | 93.3 ms                                                      | 88.9 ms: 1.05x faster                                                   |
| deepcopy_memo           | 38.8 us                                                      | 37.0 us: 1.05x faster                                                   |
| async_tree_cpu_io_mixed | 749 ms                                                       | 716 ms: 1.05x faster                                                    |
| crypto_pyaes            | 83.4 ms                                                      | 80.3 ms: 1.04x faster                                                   |
| deepcopy                | 399 us                                                       | 386 us: 1.03x faster                                                    |
| nbody                   | 90.7 ms                                                      | 87.7 ms: 1.03x faster                                                   |
| thrift                  | 925 us                                                       | 896 us: 1.03x faster                                                    |
| regex_v8                | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                   |
| deepcopy_reduce         | 3.51 us                                                      | 3.44 us: 1.02x faster                                                   |
| pyflate                 | 449 ms                                                       | 439 ms: 1.02x faster                                                    |
| sqlglot_optimize        | 59.8 ms                                                      | 58.7 ms: 1.02x faster                                                   |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                                    |
| comprehensions          | 24.6 us                                                      | 24.3 us: 1.01x faster                                                   |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                    |
| pprint_pformat          | 1.63 sec                                                     | 1.64 sec: 1.01x slower                                                  |
| docutils                | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                  |
| scimark_fft             | 285 ms                                                       | 291 ms: 1.02x slower                                                    |
| pprint_safe_repr        | 784 ms                                                       | 806 ms: 1.03x slower                                                    |
| regex_dna               | 227 ms                                                       | 234 ms: 1.03x slower                                                    |
| pathlib                 | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                                   |
| pidigits                | 251 ms                                                       | 260 ms: 1.03x slower                                                    |
| xml_etree_process       | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                   |
| pickle_dict             | 30.8 us                                                      | 31.9 us: 1.04x slower                                                   |
| scimark_monte_carlo     | 68.2 ms                                                      | 70.8 ms: 1.04x slower                                                   |
| pickle                  | 9.64 us                                                      | 10.0 us: 1.04x slower                                                   |
| unpack_sequence         | 45.6 ns                                                      | 47.6 ns: 1.04x slower                                                   |
| gc_traversal            | 3.85 ms                                                      | 4.02 ms: 1.04x slower                                                   |
| telco                   | 6.86 ms                                                      | 7.19 ms: 1.05x slower                                                   |
| meteor_contest          | 131 ms                                                       | 137 ms: 1.05x slower                                                    |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                   |
| float                   | 74.2 ms                                                      | 78.0 ms: 1.05x slower                                                   |
| sqlite_synth            | 2.50 us                                                      | 2.65 us: 1.06x slower                                                   |
| create_gc_cycles        | 1.61 ms                                                      | 1.71 ms: 1.06x slower                                                   |
| unpickle                | 13.4 us                                                      | 14.3 us: 1.06x slower                                                   |
| unpickle_list           | 4.53 us                                                      | 4.83 us: 1.07x slower                                                   |
| xml_etree_generate      | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.37 ms: 1.08x slower                                                   |
| python_startup_no_site  | 7.76 ms                                                      | 8.47 ms: 1.09x slower                                                   |
| pickle_list             | 3.83 us                                                      | 4.28 us: 1.12x slower                                                   |
| coverage                | 84.8 ms                                                      | 96.0 ms: 1.13x slower                                                   |
| bench_mp_pool           | 4.62 ms                                                      | 5.54 ms: 1.20x slower                                                   |
| async_generators        | 316 ms                                                       | 384 ms: 1.22x slower                                                    |
| dask                    | 410 ms                                                       | 560 ms: 1.36x slower                                                    |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, regex_effbot, pickle_pure_python
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
