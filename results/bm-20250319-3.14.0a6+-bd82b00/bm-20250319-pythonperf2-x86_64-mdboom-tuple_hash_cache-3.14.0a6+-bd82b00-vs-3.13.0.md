# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash_cache
- machine: linux-x86_64
- commit hash: bd82b00
- commit date: 2025-03-19
- overall geometric mean: 1.027x faster
- HPT reliability: 97.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                   |
| html5lib       | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 466 ms                                                       | 360 ms: 1.29x faster                                                     |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 831 ms                                                       | 654 ms: 1.27x faster                                                     |
| async_tree_none            | 376 ms                                                       | 300 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 346 ms                                                       | 286 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 529 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 523 ms: 1.11x faster                                                     |
| async_generators           | 457 ms                                                       | 432 ms: 1.06x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                    |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                     |
| nbody          | 89.3 ms                                                      | 104 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.23 ms: 1.14x faster                                                    |
| regex_v8       | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                    |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                     |
| regex_dna      | 247 ms                                                       | 246 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                        | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.17 sec: 1.13x faster                                                   |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                     |
| xml_etree_generate   | 86.5 ms                                                      | 85.1 ms: 1.02x faster                                                    |
| xml_etree_process    | 61.2 ms                                                      | 60.6 ms: 1.01x faster                                                    |
| unpickle_pure_python | 217 us                                                       | 222 us: 1.02x slower                                                     |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                    |
| pickle_pure_python   | 323 us                                                       | 346 us: 1.07x slower                                                     |
| json_loads           | 24.7 us                                                      | 26.6 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.03x slower                                                    |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.18x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                    |
| genshi_xml      | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                                    |
| django_template | 36.4 ms                                                      | 37.9 ms: 1.04x slower                                                    |
| mako            | 10.4 ms                                                      | 11.2 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.36 sec: 1.87x faster                                                   |
| deepcopy                   | 392 us                                                       | 297 us: 1.32x faster                                                     |
| deepcopy_memo              | 38.6 us                                                      | 29.4 us: 1.31x faster                                                    |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 466 ms                                                       | 360 ms: 1.29x faster                                                     |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 831 ms                                                       | 654 ms: 1.27x faster                                                     |
| async_tree_none            | 376 ms                                                       | 300 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 346 ms                                                       | 286 ms: 1.21x faster                                                     |
| go                         | 162 ms                                                       | 135 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                    |
| generators                 | 33.6 ms                                                      | 29.0 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 529 ms: 1.14x faster                                                     |
| regex_effbot               | 3.67 ms                                                      | 3.23 ms: 1.14x faster                                                    |
| float                      | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                    |
| tomli_loads                | 2.46 sec                                                     | 2.17 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 523 ms: 1.11x faster                                                     |
| richards_super             | 59.6 ms                                                      | 53.6 ms: 1.11x faster                                                    |
| richards                   | 52.9 ms                                                      | 47.7 ms: 1.11x faster                                                    |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                     |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                     |
| pyflate                    | 503 ms                                                       | 461 ms: 1.09x faster                                                     |
| regex_v8                   | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                    |
| dulwich_log                | 68.2 ms                                                      | 63.0 ms: 1.08x faster                                                    |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                     |
| telco                      | 8.79 ms                                                      | 8.22 ms: 1.07x faster                                                    |
| spectral_norm              | 97.0 ms                                                      | 90.9 ms: 1.07x faster                                                    |
| genshi_text                | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                    |
| async_generators           | 457 ms                                                       | 432 ms: 1.06x faster                                                     |
| html5lib                   | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                    |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                     |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                    |
| logging_silent             | 97.9 ns                                                      | 95.4 ns: 1.03x faster                                                    |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                     |
| k_core                     | 2.17 sec                                                     | 2.13 sec: 1.02x faster                                                   |
| json                       | 5.69 ms                                                      | 5.59 ms: 1.02x faster                                                    |
| xml_etree_generate         | 86.5 ms                                                      | 85.1 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.72 sec                                                     | 1.69 sec: 1.02x faster                                                   |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                    |
| hexiom                     | 6.55 ms                                                      | 6.48 ms: 1.01x faster                                                    |
| xml_etree_process          | 61.2 ms                                                      | 60.6 ms: 1.01x faster                                                    |
| scimark_fft                | 328 ms                                                       | 325 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 843 ms                                                       | 836 ms: 1.01x faster                                                     |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                                     |
| connected_components       | 432 ms                                                       | 430 ms: 1.01x faster                                                     |
| shortest_path              | 460 ms                                                       | 459 ms: 1.00x faster                                                     |
| regex_dna                  | 247 ms                                                       | 246 ms: 1.00x faster                                                     |
| sympy_expand               | 509 ms                                                       | 512 ms: 1.00x slower                                                     |
| sqlalchemy_declarative     | 148 ms                                                       | 149 ms: 1.01x slower                                                     |
| sympy_str                  | 298 ms                                                       | 301 ms: 1.01x slower                                                     |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                     |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.5 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.84 ms: 1.01x slower                                                    |
| sympy_sum                  | 155 ms                                                       | 157 ms: 1.02x slower                                                     |
| scimark_lu                 | 98.7 ms                                                      | 100 ms: 1.02x slower                                                     |
| genshi_xml                 | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 217 us                                                       | 222 us: 1.02x slower                                                     |
| bench_thread_pool          | 942 us                                                       | 968 us: 1.03x slower                                                     |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.03x slower                                                    |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 68.9 ms: 1.04x slower                                                    |
| django_template            | 36.4 ms                                                      | 37.9 ms: 1.04x slower                                                    |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                    |
| typing_runtime_protocols   | 169 us                                                       | 177 us: 1.04x slower                                                     |
| bpe_tokeniser              | 5.09 sec                                                     | 5.32 sec: 1.05x slower                                                   |
| pycparser                  | 1.24 sec                                                     | 1.30 sec: 1.05x slower                                                   |
| fannkuch                   | 363 ms                                                       | 382 ms: 1.05x slower                                                     |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                    |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.05x slower                                                    |
| logging_format             | 6.94 us                                                      | 7.34 us: 1.06x slower                                                    |
| logging_simple             | 6.39 us                                                      | 6.76 us: 1.06x slower                                                    |
| nqueens                    | 90.7 ms                                                      | 96.1 ms: 1.06x slower                                                    |
| pickle_pure_python         | 323 us                                                       | 346 us: 1.07x slower                                                     |
| json_loads                 | 24.7 us                                                      | 26.6 us: 1.08x slower                                                    |
| mako                       | 10.4 ms                                                      | 11.2 ms: 1.08x slower                                                    |
| raytrace                   | 273 ms                                                       | 298 ms: 1.09x slower                                                     |
| chaos                      | 60.2 ms                                                      | 67.1 ms: 1.11x slower                                                    |
| crypto_pyaes               | 73.3 ms                                                      | 82.4 ms: 1.12x slower                                                    |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                                    |
| nbody                      | 89.3 ms                                                      | 104 ms: 1.17x slower                                                     |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.18x slower                                                    |
| gc_traversal               | 4.74 ms                                                      | 6.39 ms: 1.35x slower                                                    |
| subparsers                 | 17.5 ms                                                      | 24.3 ms: 1.39x slower                                                    |
| bench_mp_pool              | 5.12 ms                                                      | 1.58 sec: 308.31x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                             |

Benchmark hidden because not significant (6): coverage, thrift, asyncio_websockets, deltablue, sympy_integrate, sphinx
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-bd82b00/bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 97.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x