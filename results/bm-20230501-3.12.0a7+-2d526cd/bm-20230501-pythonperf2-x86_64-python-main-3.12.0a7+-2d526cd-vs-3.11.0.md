
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 286 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                       |
| html5lib       | 70.2 ms                                                                   | 68.0 ms: 1.03x faster                                        |
| tornado_http   | 125 ms                                                                    | 113 ms: 1.11x faster                                         |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 89.2 ms: 1.03x faster                                        |
| float          | 75.7 ms                                                                   | 77.8 ms: 1.03x slower                                        |
| pidigits       | 252 ms                                                                    | 259 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                                     | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 144 ms: 1.07x faster                                         |
| regex_v8       | 24.4 ms                                                                   | 23.5 ms: 1.04x faster                                        |
| regex_dna      | 225 ms                                                                    | 230 ms: 1.02x slower                                         |
| regex_effbot   | 3.31 ms                                                                   | 3.46 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.7 ms: 1.25x faster                                        |
| unpickle_pure_python | 238 us                                                                    | 208 us: 1.15x faster                                         |
| json_loads           | 28.4 us                                                                   | 25.4 us: 1.12x faster                                        |
| xml_etree_parse      | 161 ms                                                                    | 146 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 106 ms                                                                    | 104 ms: 1.01x faster                                         |
| pickle_dict          | 31.1 us                                                                   | 31.8 us: 1.02x slower                                        |
| xml_etree_process    | 55.8 ms                                                                   | 58.6 ms: 1.05x slower                                        |
| unpickle_list        | 4.52 us                                                                   | 4.83 us: 1.07x slower                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 86.2 ms: 1.09x slower                                        |
| unpickle             | 13.0 us                                                                   | 14.6 us: 1.12x slower                                        |
| pickle_list          | 3.78 us                                                                   | 4.41 us: 1.17x slower                                        |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.1 ms: 1.04x slower                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.33 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                                     | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                        |
| mako           | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                        |
| genshi_text    | 26.3 ms                                                                   | 24.6 ms: 1.07x faster                                        |
| Geometric mean | (ref)                                                                     | 1.08x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 378 ms: 1.99x faster                                         |
| generators              | 56.0 ms                                                                   | 36.3 ms: 1.54x faster                                        |
| fannkuch                | 449 ms                                                                    | 338 ms: 1.33x faster                                         |
| coroutines              | 29.5 ms                                                                   | 22.6 ms: 1.31x faster                                        |
| json_dumps              | 13.4 ms                                                                   | 10.7 ms: 1.25x faster                                        |
| deltablue               | 3.99 ms                                                                   | 3.24 ms: 1.23x faster                                        |
| scimark_lu              | 114 ms                                                                    | 94.8 ms: 1.20x faster                                        |
| mypy2                   | 446 ms                                                                    | 377 ms: 1.18x faster                                         |
| hexiom                  | 7.00 ms                                                                   | 5.94 ms: 1.18x faster                                        |
| gc_traversal            | 4.22 ms                                                                   | 3.59 ms: 1.17x faster                                        |
| unpickle_pure_python    | 238 us                                                                    | 208 us: 1.15x faster                                         |
| async_tree_memoization  | 639 ms                                                                    | 560 ms: 1.14x faster                                         |
| chaos                   | 76.2 ms                                                                   | 66.9 ms: 1.14x faster                                        |
| nqueens                 | 101 ms                                                                    | 89.2 ms: 1.13x faster                                        |
| richards                | 49.1 ms                                                                   | 43.7 ms: 1.12x faster                                        |
| json_loads              | 28.4 us                                                                   | 25.4 us: 1.12x faster                                        |
| async_tree_none         | 529 ms                                                                    | 476 ms: 1.11x faster                                         |
| sqlglot_parse           | 1.53 ms                                                                   | 1.38 ms: 1.11x faster                                        |
| tornado_http            | 125 ms                                                                    | 113 ms: 1.11x faster                                         |
| xml_etree_parse         | 161 ms                                                                    | 146 ms: 1.10x faster                                         |
| logging_silent          | 103 ns                                                                    | 93.8 ns: 1.09x faster                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.09 sec: 1.09x faster                                       |
| genshi_xml              | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                        |
| mako                    | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                        |
| mdp                     | 2.73 sec                                                                  | 2.54 sec: 1.07x faster                                       |
| spectral_norm           | 95.1 ms                                                                   | 88.7 ms: 1.07x faster                                        |
| logging_format          | 7.84 us                                                                   | 7.34 us: 1.07x faster                                        |
| json                    | 5.59 ms                                                                   | 5.23 ms: 1.07x faster                                        |
| regex_compile           | 154 ms                                                                    | 144 ms: 1.07x faster                                         |
| genshi_text             | 26.3 ms                                                                   | 24.6 ms: 1.07x faster                                        |
| go                      | 158 ms                                                                    | 148 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 709 ms: 1.06x faster                                         |
| dulwich_log             | 69.1 ms                                                                   | 65.1 ms: 1.06x faster                                        |
| logging_simple          | 6.95 us                                                                   | 6.60 us: 1.05x faster                                        |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.79 ms: 1.05x faster                                        |
| pycparser               | 1.30 sec                                                                  | 1.24 sec: 1.05x faster                                       |
| crypto_pyaes            | 85.0 ms                                                                   | 81.3 ms: 1.04x faster                                        |
| thrift                  | 942 us                                                                    | 904 us: 1.04x faster                                         |
| regex_v8                | 24.4 ms                                                                   | 23.5 ms: 1.04x faster                                        |
| nbody                   | 92.1 ms                                                                   | 89.2 ms: 1.03x faster                                        |
| html5lib                | 70.2 ms                                                                   | 68.0 ms: 1.03x faster                                        |
| pathlib                 | 19.2 ms                                                                   | 18.8 ms: 1.02x faster                                        |
| sqlglot_normalize       | 122 ms                                                                    | 120 ms: 1.01x faster                                         |
| 2to3                    | 289 ms                                                                    | 286 ms: 1.01x faster                                         |
| xml_etree_iterparse     | 106 ms                                                                    | 104 ms: 1.01x faster                                         |
| comprehensions          | 24.7 us                                                                   | 24.5 us: 1.01x faster                                        |
| sqlglot_optimize        | 58.6 ms                                                                   | 58.9 ms: 1.01x slower                                        |
| scimark_sor             | 109 ms                                                                    | 110 ms: 1.01x slower                                         |
| deepcopy_memo           | 37.0 us                                                                   | 37.4 us: 1.01x slower                                        |
| docutils                | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                       |
| regex_dna               | 225 ms                                                                    | 230 ms: 1.02x slower                                         |
| pickle_dict             | 31.1 us                                                                   | 31.8 us: 1.02x slower                                        |
| raytrace                | 303 ms                                                                    | 311 ms: 1.03x slower                                         |
| float                   | 75.7 ms                                                                   | 77.8 ms: 1.03x slower                                        |
| pprint_pformat          | 1.60 sec                                                                  | 1.65 sec: 1.03x slower                                       |
| pidigits                | 252 ms                                                                    | 259 ms: 1.03x slower                                         |
| python_startup          | 10.7 ms                                                                   | 11.1 ms: 1.04x slower                                        |
| pyflate                 | 438 ms                                                                    | 456 ms: 1.04x slower                                         |
| pprint_safe_repr        | 768 ms                                                                    | 802 ms: 1.04x slower                                         |
| regex_effbot            | 3.31 ms                                                                   | 3.46 ms: 1.05x slower                                        |
| xml_etree_process       | 55.8 ms                                                                   | 58.6 ms: 1.05x slower                                        |
| sqlite_synth            | 2.49 us                                                                   | 2.61 us: 1.05x slower                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.29 ms: 1.06x slower                                        |
| scimark_fft             | 276 ms                                                                    | 294 ms: 1.07x slower                                         |
| unpickle_list           | 4.52 us                                                                   | 4.83 us: 1.07x slower                                        |
| meteor_contest          | 129 ms                                                                    | 139 ms: 1.08x slower                                         |
| telco                   | 6.70 ms                                                                   | 7.22 ms: 1.08x slower                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.33 ms: 1.08x slower                                        |
| coverage                | 86.0 ms                                                                   | 92.8 ms: 1.08x slower                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 86.2 ms: 1.09x slower                                        |
| unpickle                | 13.0 us                                                                   | 14.6 us: 1.12x slower                                        |
| bench_mp_pool           | 4.54 ms                                                                   | 5.21 ms: 1.15x slower                                        |
| pickle_list             | 3.78 us                                                                   | 4.41 us: 1.17x slower                                        |
| async_generators        | 318 ms                                                                    | 382 ms: 1.20x slower                                         |
| unpack_sequence         | 45.9 ns                                                                   | 55.5 ns: 1.21x slower                                        |
| dask                    | 418 ms                                                                    | 560 ms: 1.34x slower                                         |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, deepcopy, pickle_pure_python, create_gc_cycles, pickle, scimark_monte_carlo, deepcopy_reduce
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
