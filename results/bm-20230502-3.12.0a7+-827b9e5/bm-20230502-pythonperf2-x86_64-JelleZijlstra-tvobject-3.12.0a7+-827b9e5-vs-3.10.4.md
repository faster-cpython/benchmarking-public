
# Results vs. 3.10.4

- fork: JelleZijlstra
- ref: tvobject
- machine: linux-x86_64
- commit hash: 827b9e5
- commit date: 2023-05-02
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                    |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                  |
| html5lib       | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                                   |
| tornado_http   | 152 ms                                                       | 113 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                        | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.7 ms: 1.57x faster                                                   |
| float          | 110 ms                                                       | 78.0 ms: 1.41x faster                                                   |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                        | 1.32x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.35x faster                                                    |
| regex_v8       | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                   |
| regex_dna      | 259 ms                                                       | 234 ms: 1.11x faster                                                    |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 204 us: 1.57x faster                                                    |
| pickle_pure_python   | 457 us                                                       | 320 us: 1.43x faster                                                    |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                                   |
| xml_etree_process    | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                   |
| json_loads           | 30.0 us                                                      | 25.1 us: 1.19x faster                                                   |
| xml_etree_parse      | 162 ms                                                       | 145 ms: 1.11x faster                                                    |
| xml_etree_generate   | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                    |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                                   |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                                   |
| pickle_list          | 4.11 us                                                      | 4.28 us: 1.04x slower                                                   |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                                   |
| unpickle_list        | 4.49 us                                                      | 4.83 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                   |
| genshi_text    | 31.5 ms                                                      | 24.3 ms: 1.29x faster                                                   |
| genshi_xml     | 64.7 ms                                                      | 53.5 ms: 1.21x faster                                                   |
| Geometric mean | (ref)                                                        | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.25 ms: 2.30x faster                                                   |
| asyncio_tcp             | 782 ms                                                       | 381 ms: 2.06x faster                                                    |
| go                      | 259 ms                                                       | 147 ms: 1.77x faster                                                    |
| logging_silent          | 166 ns                                                       | 94.7 ns: 1.75x faster                                                   |
| richards                | 74.1 ms                                                      | 42.7 ms: 1.74x faster                                                   |
| scimark_lu              | 164 ms                                                       | 96.2 ms: 1.70x faster                                                   |
| sqlglot_parse           | 2.26 ms                                                      | 1.38 ms: 1.63x faster                                                   |
| raytrace                | 488 ms                                                       | 300 ms: 1.63x faster                                                    |
| chaos                   | 107 ms                                                       | 66.2 ms: 1.62x faster                                                   |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.62x faster                                                    |
| generators              | 58.0 ms                                                      | 35.9 ms: 1.61x faster                                                   |
| hexiom                  | 9.52 ms                                                      | 5.91 ms: 1.61x faster                                                   |
| pyflate                 | 697 ms                                                       | 439 ms: 1.59x faster                                                    |
| unpickle_pure_python    | 321 us                                                       | 204 us: 1.57x faster                                                    |
| nbody                   | 137 ms                                                       | 87.7 ms: 1.57x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                       | 70.8 ms: 1.55x faster                                                   |
| spectral_norm           | 136 ms                                                       | 88.9 ms: 1.53x faster                                                   |
| sqlglot_transpile       | 2.71 ms                                                      | 1.79 ms: 1.51x faster                                                   |
| crypto_pyaes            | 118 ms                                                       | 80.3 ms: 1.47x faster                                                   |
| async_tree_none         | 700 ms                                                       | 478 ms: 1.46x faster                                                    |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                                  |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                   |
| fannkuch                | 496 ms                                                       | 346 ms: 1.43x faster                                                    |
| async_tree_memoization  | 824 ms                                                       | 575 ms: 1.43x faster                                                    |
| pickle_pure_python      | 457 us                                                       | 320 us: 1.43x faster                                                    |
| float                   | 110 ms                                                       | 78.0 ms: 1.41x faster                                                   |
| html5lib                | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                                   |
| pycparser               | 1.66 sec                                                     | 1.22 sec: 1.36x faster                                                  |
| logging_simple          | 8.90 us                                                      | 6.53 us: 1.36x faster                                                   |
| json_dumps              | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                                   |
| coroutines              | 30.4 ms                                                      | 22.5 ms: 1.35x faster                                                   |
| regex_compile           | 194 ms                                                       | 144 ms: 1.35x faster                                                    |
| tornado_http            | 152 ms                                                       | 113 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed | 952 ms                                                       | 716 ms: 1.33x faster                                                    |
| deepcopy_memo           | 48.9 us                                                      | 37.0 us: 1.32x faster                                                   |
| pprint_pformat          | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                  |
| pprint_safe_repr        | 1.05 sec                                                     | 806 ms: 1.30x faster                                                    |
| logging_format          | 9.57 us                                                      | 7.34 us: 1.30x faster                                                   |
| thrift                  | 1.16 ms                                                      | 896 us: 1.30x faster                                                    |
| xml_etree_process       | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                   |
| bench_mp_pool           | 7.18 ms                                                      | 5.54 ms: 1.30x faster                                                   |
| genshi_text             | 31.5 ms                                                      | 24.3 ms: 1.29x faster                                                   |
| nqueens                 | 112 ms                                                       | 88.9 ms: 1.27x faster                                                   |
| dulwich_log             | 80.1 ms                                                      | 63.5 ms: 1.26x faster                                                   |
| unpack_sequence         | 59.5 ns                                                      | 47.6 ns: 1.25x faster                                                   |
| mypy2                   | 466 ms                                                       | 376 ms: 1.24x faster                                                    |
| scimark_fft             | 359 ms                                                       | 291 ms: 1.24x faster                                                    |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                    |
| sqlglot_normalize       | 144 ms                                                       | 119 ms: 1.21x faster                                                    |
| genshi_xml              | 64.7 ms                                                      | 53.5 ms: 1.21x faster                                                   |
| sqlglot_optimize        | 70.3 ms                                                      | 58.7 ms: 1.20x faster                                                   |
| json_loads              | 30.0 us                                                      | 25.1 us: 1.19x faster                                                   |
| mdp                     | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                                  |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.37 ms: 1.19x faster                                                   |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                                    |
| docutils                | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                  |
| deepcopy                | 454 us                                                       | 386 us: 1.18x faster                                                    |
| deepcopy_reduce         | 4.03 us                                                      | 3.44 us: 1.17x faster                                                   |
| json                    | 5.96 ms                                                      | 5.12 ms: 1.16x faster                                                   |
| regex_v8                | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                   |
| sqlite_synth            | 2.97 us                                                      | 2.65 us: 1.12x faster                                                   |
| xml_etree_parse         | 162 ms                                                       | 145 ms: 1.11x faster                                                    |
| comprehensions          | 26.9 us                                                      | 24.3 us: 1.11x faster                                                   |
| regex_dna               | 259 ms                                                       | 234 ms: 1.11x faster                                                    |
| pathlib                 | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                                   |
| xml_etree_generate      | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                                   |
| async_generators        | 422 ms                                                       | 384 ms: 1.10x faster                                                    |
| create_gc_cycles        | 1.82 ms                                                      | 1.71 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                    |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                    |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                   |
| meteor_contest          | 137 ms                                                       | 137 ms: 1.00x slower                                                    |
| unpickle                | 14.2 us                                                      | 14.3 us: 1.01x slower                                                   |
| pickle                  | 9.94 us                                                      | 10.0 us: 1.01x slower                                                   |
| pickle_list             | 4.11 us                                                      | 4.28 us: 1.04x slower                                                   |
| pickle_dict             | 30.0 us                                                      | 31.9 us: 1.06x slower                                                   |
| unpickle_list           | 4.49 us                                                      | 4.83 us: 1.08x slower                                                   |
| python_startup_no_site  | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                                   |
| gc_traversal            | 3.45 ms                                                      | 4.02 ms: 1.16x slower                                                   |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                   |
| dask                    | 463 ms                                                       | 560 ms: 1.21x slower                                                    |
| coverage                | 64.0 ms                                                      | 96.0 ms: 1.50x slower                                                   |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                            |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x
