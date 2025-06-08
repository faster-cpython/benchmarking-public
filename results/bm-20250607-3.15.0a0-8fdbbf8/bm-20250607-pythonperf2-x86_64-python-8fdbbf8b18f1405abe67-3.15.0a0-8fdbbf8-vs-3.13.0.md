# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.095x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 313 ms: 1.07x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| html5lib       | 73.5 ms                                                      | 71.7 ms: 1.02x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 366 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                        |
| async_tree_io              | 843 ms                                                       | 691 ms: 1.22x faster                                                        |
| async_tree_none            | 376 ms                                                       | 309 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 703 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 298 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 646 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 649 ms: 1.12x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.4 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 80.7 ms: 1.01x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| nbody          | 89.3 ms                                                      | 100 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.28 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.37 sec: 1.04x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 163 ms: 1.08x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 244 us: 1.12x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 72.1 ms: 1.18x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 384 us: 1.19x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.6 us: 1.20x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 105 ms: 1.22x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 13.9 ms: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.39 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 60.0 ms: 1.05x slower                                                       |
| django_template | 36.4 ms                                                      | 41.6 ms: 1.14x slower                                                       |
| mako            | 10.4 ms                                                      | 13.0 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.54 sec: 1.65x faster                                                      |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 366 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                        |
| async_tree_io              | 843 ms                                                       | 691 ms: 1.22x faster                                                        |
| async_tree_none            | 376 ms                                                       | 309 ms: 1.22x faster                                                        |
| deepcopy                   | 392 us                                                       | 322 us: 1.22x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 703 ms: 1.18x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 32.8 us: 1.18x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 298 ms: 1.16x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.28 ms: 1.12x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 63.3 ms: 1.08x faster                                                       |
| generators                 | 33.6 ms                                                      | 31.3 ms: 1.08x faster                                                       |
| pyflate                    | 503 ms                                                       | 477 ms: 1.06x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.37 sec: 1.04x faster                                                      |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 71.7 ms: 1.02x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| float                      | 81.3 ms                                                      | 80.7 ms: 1.01x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.52 ms: 1.00x faster                                                       |
| connected_components       | 432 ms                                                       | 431 ms: 1.00x faster                                                        |
| shortest_path              | 460 ms                                                       | 461 ms: 1.00x slower                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.58 us: 1.01x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| richards                   | 52.9 ms                                                      | 53.5 ms: 1.01x slower                                                       |
| richards_super             | 59.6 ms                                                      | 60.5 ms: 1.02x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.50 ms: 1.02x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| scimark_sor                | 123 ms                                                       | 129 ms: 1.04x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.39 ms: 1.05x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 60.0 ms: 1.05x slower                                                       |
| json                       | 5.69 ms                                                      | 6.03 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 313 ms: 1.07x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 646 ms: 1.07x slower                                                        |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.35 sec: 1.08x slower                                                      |
| xml_etree_parse            | 150 ms                                                       | 163 ms: 1.08x slower                                                        |
| meteor_contest             | 130 ms                                                       | 140 ms: 1.08x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.93 ms: 1.09x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| sympy_sum                  | 155 ms                                                       | 170 ms: 1.10x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.68 ms: 1.10x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.63 sec: 1.11x slower                                                      |
| bench_thread_pool          | 942 us                                                       | 1.05 ms: 1.11x slower                                                       |
| comprehensions             | 17.0 us                                                      | 18.9 us: 1.11x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 649 ms: 1.12x slower                                                        |
| sympy_str                  | 298 ms                                                       | 333 ms: 1.12x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 244 us: 1.12x slower                                                        |
| nbody                      | 89.3 ms                                                      | 100 ms: 1.12x slower                                                        |
| sympy_expand               | 509 ms                                                       | 574 ms: 1.13x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 19.9 ms: 1.13x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 24.4 ms: 1.13x slower                                                       |
| thrift                     | 901 us                                                       | 1.03 ms: 1.14x slower                                                       |
| django_template            | 36.4 ms                                                      | 41.6 ms: 1.14x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 76.6 ms: 1.16x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 3.40 us: 1.17x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 107 ms: 1.18x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 72.1 ms: 1.18x slower                                                       |
| logging_simple             | 6.39 us                                                      | 7.57 us: 1.18x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 384 us: 1.19x slower                                                        |
| chaos                      | 60.2 ms                                                      | 71.6 ms: 1.19x slower                                                       |
| scimark_fft                | 328 ms                                                       | 391 ms: 1.19x slower                                                        |
| raytrace                   | 273 ms                                                       | 327 ms: 1.20x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.6 us: 1.20x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 116 ms: 1.20x slower                                                        |
| coverage                   | 80.0 ms                                                      | 96.1 ms: 1.20x slower                                                       |
| logging_format             | 6.94 us                                                      | 8.39 us: 1.21x slower                                                       |
| many_optionals             | 930 us                                                       | 1.12 ms: 1.21x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 89.0 ms: 1.21x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 105 ms: 1.22x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 121 ms: 1.23x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.12 sec: 1.23x slower                                                      |
| typing_runtime_protocols   | 169 us                                                       | 209 us: 1.24x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.05 sec: 1.24x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 13.9 ms: 1.25x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 5.94 ms: 1.25x slower                                                       |
| mako                       | 10.4 ms                                                      | 13.0 ms: 1.25x slower                                                       |
| fannkuch                   | 363 ms                                                       | 464 ms: 1.28x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.50 ms: 1.36x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 28.2 ms: 1.61x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 671 ns: 6.85x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.21 sec: 235.56x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (4): regex_v8, k_core, djangocms, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.095x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.08x