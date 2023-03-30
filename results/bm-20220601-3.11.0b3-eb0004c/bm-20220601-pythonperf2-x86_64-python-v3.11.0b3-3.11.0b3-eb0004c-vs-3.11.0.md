
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 284 ms: 1.02x faster                                             |
| chameleon      | 7.50 ms                                                                   | 7.60 ms: 1.01x slower                                            |
| docutils       | 2.86 sec                                                                  | 2.83 sec: 1.01x faster                                           |
| tornado_http   | 125 ms                                                                    | 119 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 75.7 ms                                                                   | 73.9 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                     |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                                   | 3.05 ms: 1.08x faster                                            |
| regex_dna      | 225 ms                                                                    | 219 ms: 1.03x faster                                             |
| regex_v8       | 24.4 ms                                                                   | 24.3 ms: 1.01x faster                                            |
| regex_compile  | 154 ms                                                                    | 156 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|---------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads          | 28.4 us                                                                   | 25.2 us: 1.13x faster                                            |
| xml_etree_parse     | 161 ms                                                                    | 153 ms: 1.05x faster                                             |
| xml_etree_iterparse | 106 ms                                                                    | 103 ms: 1.03x faster                                             |
| pickle              | 9.92 us                                                                   | 9.80 us: 1.01x faster                                            |
| pickle_dict         | 31.1 us                                                                   | 31.3 us: 1.01x slower                                            |
| json_dumps          | 13.4 ms                                                                   | 13.5 ms: 1.01x slower                                            |
| unpickle            | 13.0 us                                                                   | 13.2 us: 1.01x slower                                            |
| xml_etree_generate  | 79.1 ms                                                                   | 80.2 ms: 1.01x slower                                            |
| unpickle_list       | 4.52 us                                                                   | 4.58 us: 1.01x slower                                            |
| pickle_list         | 3.78 us                                                                   | 3.92 us: 1.04x slower                                            |
| Geometric mean      | (ref)                                                                     | 1.01x faster                                                     |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site | 7.73 ms                                                                   | 7.70 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                     | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 57.8 ms                                                                   | 60.1 ms: 1.04x slower                                            |
| django_template | 39.6 ms                                                                   | 41.4 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                                     | 1.02x slower                                                     |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads              | 28.4 us                                                                   | 25.2 us: 1.13x faster                                            |
| regex_effbot            | 3.31 ms                                                                   | 3.05 ms: 1.08x faster                                            |
| json                    | 5.59 ms                                                                   | 5.20 ms: 1.07x faster                                            |
| coroutines              | 29.5 ms                                                                   | 27.9 ms: 1.06x faster                                            |
| tornado_http            | 125 ms                                                                    | 119 ms: 1.05x faster                                             |
| gc_traversal            | 4.22 ms                                                                   | 4.03 ms: 1.05x faster                                            |
| xml_etree_parse         | 161 ms                                                                    | 153 ms: 1.05x faster                                             |
| scimark_lu              | 114 ms                                                                    | 110 ms: 1.04x faster                                             |
| thrift                  | 942 us                                                                    | 909 us: 1.04x faster                                             |
| chaos                   | 76.2 ms                                                                   | 73.6 ms: 1.04x faster                                            |
| async_tree_memoization  | 639 ms                                                                    | 617 ms: 1.04x faster                                             |
| logging_silent          | 103 ns                                                                    | 99.3 ns: 1.03x faster                                            |
| nqueens                 | 101 ms                                                                    | 97.6 ms: 1.03x faster                                            |
| async_tree_none         | 529 ms                                                                    | 513 ms: 1.03x faster                                             |
| regex_dna               | 225 ms                                                                    | 219 ms: 1.03x faster                                             |
| sympy_expand            | 547 ms                                                                    | 531 ms: 1.03x faster                                             |
| sympy_sum               | 182 ms                                                                    | 177 ms: 1.03x faster                                             |
| xml_etree_iterparse     | 106 ms                                                                    | 103 ms: 1.03x faster                                             |
| float                   | 75.7 ms                                                                   | 73.9 ms: 1.03x faster                                            |
| 2to3                    | 289 ms                                                                    | 284 ms: 1.02x faster                                             |
| sympy_str               | 333 ms                                                                    | 327 ms: 1.02x faster                                             |
| sqlalchemy_imperative   | 19.8 ms                                                                   | 19.6 ms: 1.01x faster                                            |
| async_tree_io           | 1.18 sec                                                                  | 1.17 sec: 1.01x faster                                           |
| pickle                  | 9.92 us                                                                   | 9.80 us: 1.01x faster                                            |
| dulwich_log             | 69.1 ms                                                                   | 68.4 ms: 1.01x faster                                            |
| dask                    | 418 ms                                                                    | 414 ms: 1.01x faster                                             |
| docutils                | 2.86 sec                                                                  | 2.83 sec: 1.01x faster                                           |
| sqlalchemy_declarative  | 156 ms                                                                    | 154 ms: 1.01x faster                                             |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.03 ms: 1.01x faster                                            |
| python_startup          | 10.7 ms                                                                   | 10.7 ms: 1.01x faster                                            |
| crypto_pyaes            | 85.0 ms                                                                   | 84.5 ms: 1.01x faster                                            |
| regex_v8                | 24.4 ms                                                                   | 24.3 ms: 1.01x faster                                            |
| gunicorn                | 936 us                                                                    | 931 us: 1.01x faster                                             |
| python_startup_no_site  | 7.73 ms                                                                   | 7.70 ms: 1.00x faster                                            |
| async_generators        | 318 ms                                                                    | 318 ms: 1.00x faster                                             |
| sympy_integrate         | 25.3 ms                                                                   | 25.2 ms: 1.00x faster                                            |
| pickle_dict             | 31.1 us                                                                   | 31.3 us: 1.01x slower                                            |
| telco                   | 6.70 ms                                                                   | 6.75 ms: 1.01x slower                                            |
| pyflate                 | 438 ms                                                                    | 441 ms: 1.01x slower                                             |
| pprint_safe_repr        | 768 ms                                                                    | 774 ms: 1.01x slower                                             |
| json_dumps              | 13.4 ms                                                                   | 13.5 ms: 1.01x slower                                            |
| pprint_pformat          | 1.60 sec                                                                  | 1.61 sec: 1.01x slower                                           |
| sqlite_synth            | 2.49 us                                                                   | 2.51 us: 1.01x slower                                            |
| sqlglot_normalize       | 122 ms                                                                    | 123 ms: 1.01x slower                                             |
| regex_compile           | 154 ms                                                                    | 156 ms: 1.01x slower                                             |
| meteor_contest          | 129 ms                                                                    | 131 ms: 1.01x slower                                             |
| unpickle                | 13.0 us                                                                   | 13.2 us: 1.01x slower                                            |
| chameleon               | 7.50 ms                                                                   | 7.60 ms: 1.01x slower                                            |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.4 ms: 1.01x slower                                            |
| logging_format          | 7.84 us                                                                   | 7.95 us: 1.01x slower                                            |
| xml_etree_generate      | 79.1 ms                                                                   | 80.2 ms: 1.01x slower                                            |
| unpickle_list           | 4.52 us                                                                   | 4.58 us: 1.01x slower                                            |
| deepcopy                | 384 us                                                                    | 390 us: 1.02x slower                                             |
| spectral_norm           | 95.1 ms                                                                   | 96.8 ms: 1.02x slower                                            |
| deepcopy_memo           | 37.0 us                                                                   | 37.7 us: 1.02x slower                                            |
| create_gc_cycles        | 1.65 ms                                                                   | 1.68 ms: 1.02x slower                                            |
| bench_thread_pool       | 990 us                                                                    | 1.01 ms: 1.02x slower                                            |
| scimark_monte_carlo     | 67.8 ms                                                                   | 69.5 ms: 1.02x slower                                            |
| deepcopy_reduce         | 3.39 us                                                                   | 3.48 us: 1.02x slower                                            |
| scimark_sor             | 109 ms                                                                    | 112 ms: 1.03x slower                                             |
| logging_simple          | 6.95 us                                                                   | 7.16 us: 1.03x slower                                            |
| mdp                     | 2.73 sec                                                                  | 2.81 sec: 1.03x slower                                           |
| scimark_fft             | 276 ms                                                                    | 286 ms: 1.04x slower                                             |
| pickle_list             | 3.78 us                                                                   | 3.92 us: 1.04x slower                                            |
| genshi_xml              | 57.8 ms                                                                   | 60.1 ms: 1.04x slower                                            |
| django_template         | 39.6 ms                                                                   | 41.4 ms: 1.04x slower                                            |
| go                      | 158 ms                                                                    | 166 ms: 1.05x slower                                             |
| deltablue               | 3.99 ms                                                                   | 4.20 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 810 ms: 1.07x slower                                             |
| fannkuch                | 449 ms                                                                    | 496 ms: 1.10x slower                                             |
| comprehensions          | 24.7 us                                                                   | 28.3 us: 1.14x slower                                            |
| sqlglot_transpile       | 1.88 ms                                                                   | 2.32 ms: 1.24x slower                                            |
| sqlglot_parse           | 1.53 ms                                                                   | 1.97 ms: 1.29x slower                                            |
| Geometric mean          | (ref)                                                                     | 1.00x slower                                                     |

Benchmark hidden because not significant (21): mypy2, unpack_sequence, bench_mp_pool, pylint, pathlib, pickle_pure_python, asyncio_tcp, aiohttp, hexiom, generators, unpickle_pure_python, pidigits, richards, flaskblogging, xml_etree_process, genshi_text, raytrace, pycparser, mako, nbody, html5lib
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
