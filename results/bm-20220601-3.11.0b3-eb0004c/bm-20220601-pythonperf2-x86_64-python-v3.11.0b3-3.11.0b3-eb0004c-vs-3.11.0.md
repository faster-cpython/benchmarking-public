
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.00x faster \*
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                             |
| docutils       | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                           |
| html5lib       | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                            |
| tornado_http   | 122 ms                                                       | 119 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 93.0 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.05 ms: 1.15x faster                                            |
| regex_dna      | 227 ms                                                       | 219 ms: 1.04x faster                                             |
| regex_compile  | 158 ms                                                       | 156 ms: 1.01x faster                                             |
| regex_v8       | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 25.2 us: 1.14x faster                                            |
| xml_etree_parse      | 158 ms                                                       | 153 ms: 1.03x faster                                             |
| unpickle             | 13.4 us                                                      | 13.2 us: 1.02x faster                                            |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                             |
| xml_etree_process    | 56.5 ms                                                      | 55.9 ms: 1.01x faster                                            |
| unpickle_pure_python | 241 us                                                       | 238 us: 1.01x faster                                             |
| xml_etree_generate   | 80.5 ms                                                      | 80.2 ms: 1.00x faster                                            |
| json_dumps           | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                            |
| unpickle_list        | 4.53 us                                                      | 4.58 us: 1.01x slower                                            |
| pickle_dict          | 30.8 us                                                      | 31.3 us: 1.02x slower                                            |
| pickle               | 9.64 us                                                      | 9.80 us: 1.02x slower                                            |
| pickle_list          | 3.83 us                                                      | 3.92 us: 1.03x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site | 7.76 ms                                                      | 7.70 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 60.1 ms: 1.03x slower                                            |
| django_template | 40.2 ms                                                      | 41.4 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot            | 3.50 ms                                                      | 3.05 ms: 1.15x faster                                            |
| json_loads              | 28.7 us                                                      | 25.2 us: 1.14x faster                                            |
| chaos                   | 80.9 ms                                                      | 73.6 ms: 1.10x faster                                            |
| json                    | 5.65 ms                                                      | 5.20 ms: 1.09x faster                                            |
| nqueens                 | 103 ms                                                       | 97.6 ms: 1.05x faster                                            |
| gunicorn                | 973 us                                                       | 931 us: 1.04x faster                                             |
| sympy_expand            | 555 ms                                                       | 531 ms: 1.04x faster                                             |
| sympy_sum               | 185 ms                                                       | 177 ms: 1.04x faster                                             |
| raytrace                | 317 ms                                                       | 304 ms: 1.04x faster                                             |
| scimark_lu              | 115 ms                                                       | 110 ms: 1.04x faster                                             |
| regex_dna               | 227 ms                                                       | 219 ms: 1.04x faster                                             |
| sympy_str               | 337 ms                                                       | 327 ms: 1.03x faster                                             |
| deepcopy_memo           | 38.8 us                                                      | 37.7 us: 1.03x faster                                            |
| aiohttp                 | 985 us                                                       | 958 us: 1.03x faster                                             |
| xml_etree_parse         | 158 ms                                                       | 153 ms: 1.03x faster                                             |
| html5lib                | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                            |
| sqlalchemy_imperative   | 20.1 ms                                                      | 19.6 ms: 1.03x faster                                            |
| tornado_http            | 122 ms                                                       | 119 ms: 1.02x faster                                             |
| deepcopy                | 399 us                                                       | 390 us: 1.02x faster                                             |
| sqlglot_normalize       | 126 ms                                                       | 123 ms: 1.02x faster                                             |
| sympy_integrate         | 25.8 ms                                                      | 25.2 ms: 1.02x faster                                            |
| async_tree_memoization  | 630 ms                                                       | 617 ms: 1.02x faster                                             |
| logging_format          | 8.11 us                                                      | 7.95 us: 1.02x faster                                            |
| hexiom                  | 7.13 ms                                                      | 7.00 ms: 1.02x faster                                            |
| thrift                  | 925 us                                                       | 909 us: 1.02x faster                                             |
| pyflate                 | 449 ms                                                       | 441 ms: 1.02x faster                                             |
| unpickle                | 13.4 us                                                      | 13.2 us: 1.02x faster                                            |
| telco                   | 6.86 ms                                                      | 6.75 ms: 1.02x faster                                            |
| flaskblogging           | 3.88 ms                                                      | 3.82 ms: 1.02x faster                                            |
| logging_silent          | 101 ns                                                       | 99.3 ns: 1.02x faster                                            |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                             |
| pycparser               | 1.32 sec                                                     | 1.31 sec: 1.01x faster                                           |
| pprint_safe_repr        | 784 ms                                                       | 774 ms: 1.01x faster                                             |
| async_tree_none         | 519 ms                                                       | 513 ms: 1.01x faster                                             |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                             |
| regex_compile           | 158 ms                                                       | 156 ms: 1.01x faster                                             |
| deepcopy_reduce         | 3.51 us                                                      | 3.48 us: 1.01x faster                                            |
| pprint_pformat          | 1.63 sec                                                     | 1.61 sec: 1.01x faster                                           |
| xml_etree_process       | 56.5 ms                                                      | 55.9 ms: 1.01x faster                                            |
| unpickle_pure_python    | 241 us                                                       | 238 us: 1.01x faster                                             |
| docutils                | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                           |
| python_startup          | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site  | 7.76 ms                                                      | 7.70 ms: 1.01x faster                                            |
| sqlglot_optimize        | 59.8 ms                                                      | 59.4 ms: 1.01x faster                                            |
| async_tree_io           | 1.17 sec                                                     | 1.17 sec: 1.01x faster                                           |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.03 ms: 1.01x faster                                            |
| xml_etree_generate      | 80.5 ms                                                      | 80.2 ms: 1.00x faster                                            |
| meteor_contest          | 131 ms                                                       | 131 ms: 1.00x slower                                             |
| scimark_fft             | 285 ms                                                       | 286 ms: 1.00x slower                                             |
| pathlib                 | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                            |
| json_dumps              | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                            |
| async_generators        | 316 ms                                                       | 318 ms: 1.01x slower                                             |
| scimark_sor             | 111 ms                                                       | 112 ms: 1.01x slower                                             |
| dask                    | 410 ms                                                       | 414 ms: 1.01x slower                                             |
| go                      | 164 ms                                                       | 166 ms: 1.01x slower                                             |
| unpickle_list           | 4.53 us                                                      | 4.58 us: 1.01x slower                                            |
| coroutines              | 27.6 ms                                                      | 27.9 ms: 1.01x slower                                            |
| crypto_pyaes            | 83.4 ms                                                      | 84.5 ms: 1.01x slower                                            |
| regex_v8                | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                            |
| pickle_dict             | 30.8 us                                                      | 31.3 us: 1.02x slower                                            |
| pickle                  | 9.64 us                                                      | 9.80 us: 1.02x slower                                            |
| richards                | 48.3 ms                                                      | 49.2 ms: 1.02x slower                                            |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.5 ms: 1.02x slower                                            |
| mdp                     | 2.75 sec                                                     | 2.81 sec: 1.03x slower                                           |
| pickle_list             | 3.83 us                                                      | 3.92 us: 1.03x slower                                            |
| nbody                   | 90.7 ms                                                      | 93.0 ms: 1.03x slower                                            |
| genshi_xml              | 58.5 ms                                                      | 60.1 ms: 1.03x slower                                            |
| django_template         | 40.2 ms                                                      | 41.4 ms: 1.03x slower                                            |
| spectral_norm           | 93.3 ms                                                      | 96.8 ms: 1.04x slower                                            |
| create_gc_cycles        | 1.61 ms                                                      | 1.68 ms: 1.04x slower                                            |
| gc_traversal            | 3.85 ms                                                      | 4.03 ms: 1.05x slower                                            |
| deltablue               | 4.00 ms                                                      | 4.20 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed | 749 ms                                                       | 810 ms: 1.08x slower                                             |
| comprehensions          | 24.6 us                                                      | 28.3 us: 1.15x slower                                            |
| fannkuch                | 429 ms                                                       | 496 ms: 1.16x slower                                             |
| sqlglot_transpile       | 1.92 ms                                                      | 2.32 ms: 1.21x slower                                            |
| sqlglot_parse           | 1.53 ms                                                      | 1.97 ms: 1.29x slower                                            |
| Geometric mean          | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (17): mypy2, bench_mp_pool, chameleon, unpack_sequence, float, logging_simple, mako, asyncio_tcp, generators, pickle_pure_python, dulwich_log, pylint, sqlalchemy_declarative, pidigits, bench_thread_pool, sqlite_synth, genshi_text
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
