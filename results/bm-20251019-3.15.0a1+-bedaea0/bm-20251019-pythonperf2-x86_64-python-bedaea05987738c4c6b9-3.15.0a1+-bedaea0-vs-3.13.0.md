# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 277 ms: 1.06x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.83 sec: 1.00x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                         |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                         |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 423 ms: 1.08x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 410 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.0 ms: 1.20x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 96.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 218 ms: 1.13x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                         |
| regex_effbot   | 3.67 ms                                                      | 3.41 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.97 sec: 1.25x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| unpickle_pure_python | 217 us                                                       | 203 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 83.6 ms: 1.04x faster                                                        |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                        |
| python_startup_no_site | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.2 ms: 1.05x faster                                                        |
| django_template | 36.4 ms                                                      | 35.1 ms: 1.04x faster                                                        |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.25 sec: 2.03x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 24.8 us: 1.56x faster                                                        |
| deepcopy                   | 392 us                                                       | 257 us: 1.52x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                         |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                         |
| go                         | 162 ms                                                       | 116 ms: 1.40x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                         |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                         |
| pyflate                    | 503 ms                                                       | 399 ms: 1.26x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 1.97 sec: 1.25x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.85 us: 1.24x faster                                                        |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                         |
| richards                   | 52.9 ms                                                      | 44.1 ms: 1.20x faster                                                        |
| float                      | 81.3 ms                                                      | 68.0 ms: 1.20x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.4 ms: 1.18x faster                                                        |
| richards_super             | 59.6 ms                                                      | 50.4 ms: 1.18x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.0 ms: 1.17x faster                                                        |
| scimark_fft                | 328 ms                                                       | 281 ms: 1.17x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 59.0 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 5.72 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 58.2 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| regex_dna                  | 247 ms                                                       | 218 ms: 1.13x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 86.9 ms: 1.12x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.74 us: 1.11x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 758 ms: 1.11x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.55 sec: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                         |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                         |
| logging_format             | 6.94 us                                                      | 6.37 us: 1.09x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.14 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.70 sec: 1.08x faster                                                       |
| thrift                     | 901 us                                                       | 834 us: 1.08x faster                                                         |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                         |
| async_generators           | 457 ms                                                       | 423 ms: 1.08x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.41 ms: 1.08x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 203 us: 1.07x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.0 ms: 1.07x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 92.7 ms: 1.06x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.0 us: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.51 ms: 1.06x faster                                                        |
| 2to3                       | 293 ms                                                       | 277 ms: 1.06x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 92.7 ns: 1.06x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.2 ms: 1.05x faster                                                        |
| sympy_str                  | 298 ms                                                       | 284 ms: 1.05x faster                                                         |
| sympy_expand               | 509 ms                                                       | 485 ms: 1.05x faster                                                         |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 148 ms: 1.04x faster                                                         |
| chaos                      | 60.2 ms                                                      | 57.8 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.1 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 83.6 ms: 1.04x faster                                                        |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                        |
| connected_components       | 432 ms                                                       | 420 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| bench_thread_pool          | 942 us                                                       | 920 us: 1.02x faster                                                         |
| shortest_path              | 460 ms                                                       | 451 ms: 1.02x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| typing_runtime_protocols   | 169 us                                                       | 166 us: 1.02x faster                                                         |
| fannkuch                   | 363 ms                                                       | 358 ms: 1.02x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                                        |
| docutils                   | 2.83 sec                                                     | 2.83 sec: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 75.9 ms: 1.04x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 94.0 ms: 1.04x slower                                                        |
| coverage                   | 80.0 ms                                                      | 83.2 ms: 1.04x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 410 ms: 1.06x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| nbody                      | 89.3 ms                                                      | 96.5 ms: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.52 ms: 1.38x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 44.6 ms: 2.55x slower                                                        |
| telco                      | 8.79 ms                                                      | 155 ms: 17.61x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 2.36 sec: 461.12x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): djangocms, pickle_pure_python, raytrace
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x