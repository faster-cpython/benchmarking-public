# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                         |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 409 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                        |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 96.9 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                        |
| regex_compile  | 143 ms                                                       | 133 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.89 sec: 1.31x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                        |
| python_startup_no_site | 8.96 ms                                                      | 8.82 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                        |
| mako            | 10.4 ms                                                      | 9.82 ms: 1.06x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                        |
| django_template | 36.4 ms                                                      | 34.6 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 25.1 us: 1.54x faster                                                        |
| deepcopy                   | 392 us                                                       | 259 us: 1.51x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                         |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                         |
| go                         | 162 ms                                                       | 118 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 1.89 sec: 1.31x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                         |
| pyflate                    | 503 ms                                                       | 400 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                         |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.19x faster                                                         |
| richards                   | 52.9 ms                                                      | 44.7 ms: 1.18x faster                                                        |
| scimark_fft                | 328 ms                                                       | 278 ms: 1.18x faster                                                         |
| float                      | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.48 sec: 1.16x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 730 ms: 1.15x faster                                                         |
| richards_super             | 59.6 ms                                                      | 51.8 ms: 1.15x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.3 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 60.0 ms: 1.14x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 5.87 ms: 1.12x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 87.2 ms: 1.11x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.76 us: 1.11x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                        |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.6 ms: 1.10x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.16 ms: 1.08x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.42 us: 1.08x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                       |
| thrift                     | 901 us                                                       | 834 us: 1.08x faster                                                         |
| regex_compile              | 143 ms                                                       | 133 ms: 1.08x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 92.3 ns: 1.06x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.4 ms: 1.06x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.82 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 410 ms: 1.05x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.6 ms: 1.05x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.77 us: 1.05x faster                                                        |
| json                       | 5.69 ms                                                      | 5.44 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 441 ms: 1.04x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                         |
| coverage                   | 80.0 ms                                                      | 77.8 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.03x faster                                                         |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                         |
| chaos                      | 60.2 ms                                                      | 59.2 ms: 1.02x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.82 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 168 us: 1.01x faster                                                         |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.85 ms: 1.02x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 92.4 ms: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| raytrace                   | 273 ms                                                       | 281 ms: 1.03x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 76.1 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 409 ms: 1.05x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| nbody                      | 89.3 ms                                                      | 96.9 ms: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.24 ms: 1.33x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.49 ms: 1.37x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 45.1 ms: 2.58x slower                                                        |
| telco                      | 8.79 ms                                                      | 157 ms: 17.82x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 2.74 sec: 534.70x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): bench_thread_pool, djangocms, fannkuch
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x