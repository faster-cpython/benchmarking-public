# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.043x slower
- HPT reliability: 89.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 313 ms: 1.07x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 291 ms: 1.60x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 524 ms: 1.59x faster                                                         |
| async_tree_io              | 843 ms                                                       | 555 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 229 ms: 1.51x faster                                                         |
| async_tree_none            | 376 ms                                                       | 261 ms: 1.44x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 318 ms: 1.43x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 462 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 491 ms: 1.23x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 370 ms: 1.05x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                        |
| async_generators           | 457 ms                                                       | 474 ms: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.5 ms: 1.14x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                         |
| nbody          | 89.3 ms                                                      | 124 ms: 1.39x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| regex_dna      | 247 ms                                                       | 219 ms: 1.13x faster                                                         |
| regex_effbot   | 3.67 ms                                                      | 3.36 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.16 sec: 1.14x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 237 us: 1.09x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 360 us: 1.11x slower                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 97.3 ms: 1.12x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 69.3 ms: 1.13x slower                                                        |
| json_loads           | 24.7 us                                                      | 28.0 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 29.9 ms: 1.14x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 66.0 ms: 1.16x slower                                                        |
| django_template | 36.4 ms                                                      | 43.7 ms: 1.20x slower                                                        |
| mako            | 10.4 ms                                                      | 17.3 ms: 1.66x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.27x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.20 ms: 2.15x faster                                                        |
| mdp                        | 2.54 sec                                                     | 1.45 sec: 1.75x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 291 ms: 1.60x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 524 ms: 1.59x faster                                                         |
| async_tree_io              | 843 ms                                                       | 555 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 229 ms: 1.51x faster                                                         |
| async_tree_none            | 376 ms                                                       | 261 ms: 1.44x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 318 ms: 1.43x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                        |
| deepcopy                   | 392 us                                                       | 294 us: 1.33x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.3 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 462 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 491 ms: 1.23x faster                                                         |
| go                         | 162 ms                                                       | 139 ms: 1.17x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 88.4 ms: 1.16x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.4 ms: 1.14x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.16 sec: 1.14x faster                                                       |
| float                      | 81.3 ms                                                      | 71.5 ms: 1.14x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.56 us: 1.13x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.8 ms: 1.13x faster                                                        |
| regex_dna                  | 247 ms                                                       | 219 ms: 1.13x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 61.7 ms: 1.11x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.36 ms: 1.09x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.32 us: 1.07x faster                                                        |
| pyflate                    | 503 ms                                                       | 472 ms: 1.07x faster                                                         |
| scimark_sor                | 123 ms                                                       | 117 ms: 1.06x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 370 ms: 1.05x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                        |
| pylint                     | 347 ms                                                       | 335 ms: 1.04x faster                                                         |
| scimark_fft                | 328 ms                                                       | 317 ms: 1.03x faster                                                         |
| json                       | 5.69 ms                                                      | 5.52 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.04 sec: 1.01x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 97.1 ns: 1.01x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.51 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                         |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                        |
| async_generators           | 457 ms                                                       | 474 ms: 1.04x slower                                                         |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.04x slower                                                         |
| richards                   | 52.9 ms                                                      | 55.4 ms: 1.05x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 887 ms: 1.05x slower                                                         |
| deltablue                  | 3.42 ms                                                      | 3.61 ms: 1.06x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 24.9 ms: 1.06x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.1 us: 1.06x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.83 sec: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 313 ms: 1.07x slower                                                         |
| richards_super             | 59.6 ms                                                      | 63.8 ms: 1.07x slower                                                        |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                         |
| k_core                     | 2.17 sec                                                     | 2.33 sec: 1.08x slower                                                       |
| sympy_expand               | 509 ms                                                       | 550 ms: 1.08x slower                                                         |
| logging_simple             | 6.39 us                                                      | 6.90 us: 1.08x slower                                                        |
| sympy_str                  | 298 ms                                                       | 323 ms: 1.08x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 237 us: 1.09x slower                                                         |
| sympy_sum                  | 155 ms                                                       | 169 ms: 1.09x slower                                                         |
| thrift                     | 901 us                                                       | 993 us: 1.10x slower                                                         |
| chaos                      | 60.2 ms                                                      | 66.7 ms: 1.11x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 360 us: 1.11x slower                                                         |
| shortest_path              | 460 ms                                                       | 514 ms: 1.12x slower                                                         |
| connected_components       | 432 ms                                                       | 484 ms: 1.12x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.78 us: 1.12x slower                                                        |
| meteor_contest             | 130 ms                                                       | 146 ms: 1.12x slower                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 97.3 ms: 1.12x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 69.3 ms: 1.13x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.0 us: 1.14x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 29.9 ms: 1.14x slower                                                        |
| raytrace                   | 273 ms                                                       | 315 ms: 1.16x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 66.0 ms: 1.16x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 116 ms: 1.18x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 107 ms: 1.18x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 203 us: 1.20x slower                                                         |
| python_startup             | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                        |
| django_template            | 36.4 ms                                                      | 43.7 ms: 1.20x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.76 ms: 1.21x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 81.2 ms: 1.23x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 6.33 ms: 1.24x slower                                                        |
| fannkuch                   | 363 ms                                                       | 460 ms: 1.27x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 93.4 ms: 1.27x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                        |
| nbody                      | 89.3 ms                                                      | 124 ms: 1.39x slower                                                         |
| many_optionals             | 930 us                                                       | 1.30 ms: 1.39x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.34 ms: 1.42x slower                                                        |
| coverage                   | 80.0 ms                                                      | 119 ms: 1.49x slower                                                         |
| mako                       | 10.4 ms                                                      | 17.3 ms: 1.66x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 50.1 ms: 2.87x slower                                                        |
| telco                      | 8.79 ms                                                      | 168 ms: 19.14x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 89.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.33x