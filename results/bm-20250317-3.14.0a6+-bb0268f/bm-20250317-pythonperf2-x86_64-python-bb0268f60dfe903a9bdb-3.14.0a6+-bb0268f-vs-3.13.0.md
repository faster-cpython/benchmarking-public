# Results vs. 3.13.0

- fork: python
- ref: bb0268f60dfe903a9bdb
- machine: linux-x86_64
- commit hash: bb0268f
- commit date: 2025-03-17
- overall geometric mean: 1.031x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| html5lib       | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                         |
| async_tree_io              | 843 ms                                                       | 644 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.3 ms: 1.14x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 99.3 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.07 ms: 1.20x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                        |
| regex_dna      | 247 ms                                                       | 229 ms: 1.08x faster                                                         |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.18 sec: 1.13x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 143 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 60.7 ms: 1.01x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 228 us: 1.05x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.1 us: 1.06x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 342 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.4 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 56.7 ms: 1.01x faster                                                        |
| django_template | 36.4 ms                                                      | 37.7 ms: 1.04x slower                                                        |
| mako            | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                         |
| deepcopy                   | 392 us                                                       | 289 us: 1.36x faster                                                         |
| async_tree_io              | 843 ms                                                       | 644 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.9 us: 1.29x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                         |
| go                         | 162 ms                                                       | 131 ms: 1.24x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.07 ms: 1.20x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.6 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| float                      | 81.3 ms                                                      | 71.3 ms: 1.14x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.18 sec: 1.13x faster                                                       |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 62.6 ms: 1.09x faster                                                        |
| richards                   | 52.9 ms                                                      | 48.8 ms: 1.08x faster                                                        |
| richards_super             | 59.6 ms                                                      | 55.0 ms: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                         |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                         |
| telco                      | 8.79 ms                                                      | 8.13 ms: 1.08x faster                                                        |
| regex_dna                  | 247 ms                                                       | 229 ms: 1.08x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.4 ms: 1.08x faster                                                        |
| json                       | 5.69 ms                                                      | 5.30 ms: 1.07x faster                                                        |
| pyflate                    | 503 ms                                                       | 474 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.81 sec: 1.06x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 92.0 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.64 sec: 1.05x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 143 ms: 1.05x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 809 ms: 1.04x faster                                                         |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| scimark_fft                | 328 ms                                                       | 318 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 95.7 ns: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                        |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.13 sec: 1.02x faster                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.3 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 504 ms: 1.01x faster                                                         |
| sympy_str                  | 298 ms                                                       | 296 ms: 1.01x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 60.7 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.74 ms: 1.01x faster                                                        |
| connected_components       | 432 ms                                                       | 429 ms: 1.01x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 56.7 ms: 1.01x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.55 sec: 1.00x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 155 ms: 1.00x slower                                                         |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| coverage                   | 80.0 ms                                                      | 81.1 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 67.1 ms: 1.02x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.02x slower                                                         |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| django_template            | 36.4 ms                                                      | 37.7 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 177 us: 1.04x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 94.8 ms: 1.05x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.70 us: 1.05x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 228 us: 1.05x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.1 us: 1.06x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.84 ms: 1.06x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 342 us: 1.06x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.36 us: 1.06x slower                                                        |
| fannkuch                   | 363 ms                                                       | 386 ms: 1.06x slower                                                         |
| comprehensions             | 17.0 us                                                      | 18.1 us: 1.07x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                        |
| raytrace                   | 273 ms                                                       | 293 ms: 1.07x slower                                                         |
| chaos                      | 60.2 ms                                                      | 65.3 ms: 1.08x slower                                                        |
| nbody                      | 89.3 ms                                                      | 99.3 ms: 1.11x slower                                                        |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 82.9 ms: 1.13x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 24.1 ms: 1.38x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.26 sec: 246.77x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (6): sphinx, asyncio_websockets, deltablue, hexiom, sympy_integrate, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250317-3.14.0a6+-bb0268f/bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x