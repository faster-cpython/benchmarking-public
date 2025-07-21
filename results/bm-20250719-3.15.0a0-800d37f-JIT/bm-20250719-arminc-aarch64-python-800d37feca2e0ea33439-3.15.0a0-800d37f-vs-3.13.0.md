# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.012x faster
- HPT reliability: 96.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.08 sec: 1.04x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                    |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                    |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.0 ms: 1.17x faster                                                   |
| nbody          | 118 ms                                                   | 130 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| regex_dna      | 263 ms                                                   | 220 ms: 1.19x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.2 ms: 1.05x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 410 us: 1.10x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                   |
| genshi_text     | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                   |
| genshi_xml      | 61.6 ms                                                  | 64.0 ms: 1.04x slower                                                   |
| django_template | 39.4 ms                                                  | 41.3 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.71 sec: 2.02x faster                                                  |
| deepcopy                   | 479 us                                                   | 332 us: 1.44x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.8 us: 1.36x faster                                                   |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.25x faster                                                    |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.24x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                    |
| richards                   | 54.5 ms                                                  | 45.5 ms: 1.20x faster                                                   |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.19x faster                                                    |
| float                      | 95.8 ms                                                  | 82.0 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.68 us: 1.15x faster                                                   |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                                  |
| richards_super             | 60.8 ms                                                  | 53.2 ms: 1.14x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.4 ms: 1.14x faster                                                   |
| scimark_fft                | 463 ms                                                   | 408 ms: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.48 sec: 1.10x faster                                                  |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| mako                       | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                   |
| go                         | 164 ms                                                   | 154 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 78.2 ms: 1.05x faster                                                   |
| pyflate                    | 582 ms                                                   | 555 ms: 1.05x faster                                                    |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| python_startup_no_site     | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.92 sec: 1.02x faster                                                  |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| sympy_expand               | 472 ms                                                   | 489 ms: 1.04x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 64.0 ms: 1.04x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.08 sec: 1.04x slower                                                  |
| connected_components       | 547 ms                                                   | 573 ms: 1.05x slower                                                    |
| shortest_path              | 565 ms                                                   | 593 ms: 1.05x slower                                                    |
| django_template            | 39.4 ms                                                  | 41.3 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.02 ms: 1.05x slower                                                   |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 210 us: 1.06x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.3 us: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                    |
| nbody                      | 118 ms                                                   | 130 ms: 1.10x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 410 us: 1.10x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.75 ms: 1.11x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 94.7 ms: 1.12x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.28 sec: 1.15x slower                                                  |
| gc_traversal               | 5.92 ms                                                  | 6.87 ms: 1.16x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.12 sec: 1.17x slower                                                  |
| many_optionals             | 626 us                                                   | 812 us: 1.30x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 29.2 ms: 1.44x slower                                                   |
| telco                      | 10.5 ms                                                  | 166 ms: 15.84x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 2.68 sec: 332.43x slower                                                |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                            |

Benchmark hidden because not significant (27): pylint, fannkuch, thrift, meteor_contest, nqueens, scimark_monte_carlo, logging_format, chaos, deltablue, json, unpickle_pure_python, json_dumps, asyncio_websockets, logging_simple, logging_silent, coverage, 2to3, pidigits, sympy_integrate, html5lib, pycparser, json_loads, coroutines, bench_thread_pool, hexiom, sympy_sum, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 96.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x