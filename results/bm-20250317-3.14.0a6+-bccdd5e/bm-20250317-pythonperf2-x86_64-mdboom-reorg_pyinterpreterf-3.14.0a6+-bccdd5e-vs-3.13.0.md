# Results vs. 3.13.0

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: bccdd5e
- commit date: 2025-03-17
- overall geometric mean: 1.033x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.6 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 339 ms: 1.38x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 647 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 416 ms: 1.10x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 108 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                        |
| regex_dna      | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.20 sec: 1.12x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 84.8 ms: 1.02x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 60.2 ms: 1.02x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                         |
| unpickle_pure_python | 217 us                                                       | 226 us: 1.04x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.7 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 56.2 ms: 1.02x faster                                                        |
| django_template | 36.4 ms                                                      | 37.0 ms: 1.02x slower                                                        |
| mako            | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 339 ms: 1.38x faster                                                         |
| deepcopy                   | 392 us                                                       | 295 us: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.7 us: 1.30x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 647 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| go                         | 162 ms                                                       | 133 ms: 1.22x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.01 us: 1.18x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| float                      | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.20 sec: 1.12x faster                                                       |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                        |
| richards                   | 52.9 ms                                                      | 47.8 ms: 1.11x faster                                                        |
| richards_super             | 59.6 ms                                                      | 54.0 ms: 1.10x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.98 ms: 1.10x faster                                                        |
| async_generators           | 457 ms                                                       | 416 ms: 1.10x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 62.7 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 321 ms: 1.08x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| json                       | 5.69 ms                                                      | 5.27 ms: 1.08x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 90.1 ms: 1.08x faster                                                        |
| pyflate                    | 503 ms                                                       | 470 ms: 1.07x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.07x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 69.6 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| thrift                     | 901 us                                                       | 860 us: 1.05x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.86 sec: 1.05x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| scimark_fft                | 328 ms                                                       | 319 ms: 1.03x faster                                                         |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 822 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.68 sec: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 95.7 ns: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 84.8 ms: 1.02x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.2 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.50 sec: 1.02x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.13 sec: 1.02x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.44 ms: 1.02x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 60.2 ms: 1.02x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 56.2 ms: 1.02x faster                                                        |
| shortest_path              | 460 ms                                                       | 453 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.71 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 503 ms: 1.01x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.33 us: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.39 ms: 1.01x faster                                                        |
| sympy_str                  | 298 ms                                                       | 296 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 66.0 ms: 1.00x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 156 ms: 1.01x slower                                                         |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.05 us: 1.02x slower                                                        |
| django_template            | 36.4 ms                                                      | 37.0 ms: 1.02x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 102 ms: 1.03x slower                                                         |
| coverage                   | 80.0 ms                                                      | 82.6 ms: 1.03x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 226 us: 1.04x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.7 us: 1.04x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.29 sec: 1.04x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 96.3 ms: 1.06x slower                                                        |
| chaos                      | 60.2 ms                                                      | 64.3 ms: 1.07x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                        |
| fannkuch                   | 363 ms                                                       | 393 ms: 1.08x slower                                                         |
| raytrace                   | 273 ms                                                       | 297 ms: 1.09x slower                                                         |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 83.6 ms: 1.14x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| nbody                      | 89.3 ms                                                      | 108 ms: 1.21x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.5 ms: 1.34x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.69 sec: 330.61x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (4): sphinx, sqlalchemy_imperative, connected_components, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250317-3.14.0a6+-bccdd5e/bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x