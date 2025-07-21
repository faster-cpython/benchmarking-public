# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.089x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 349 ms: 1.12x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.21 sec: 1.08x slower                                                  |
| html5lib       | 65.6 ms                                                  | 70.9 ms: 1.08x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 441 ms: 1.50x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 826 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 842 ms: 1.35x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 632 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 31.6 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 180 ms: 1.52x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.87 ms: 1.32x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 25.7 ms: 1.27x faster                                                   |
| regex_dna      | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| regex_compile  | 134 ms                                                   | 149 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 135 ms: 1.18x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.13x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.82 sec: 1.06x slower                                                  |
| json_dumps           | 14.2 ms                                                  | 15.0 ms: 1.06x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 296 us: 1.12x slower                                                    |
| json_loads           | 32.8 us                                                  | 37.0 us: 1.13x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 441 us: 1.18x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 140 ms: 1.18x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 102 ms: 1.25x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 74.6 ms: 1.21x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 36.7 ms: 1.28x slower                                                   |
| django_template | 39.4 ms                                                  | 51.0 ms: 1.29x slower                                                   |
| mako            | 14.0 ms                                                  | 21.3 ms: 1.53x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.32x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.84 ms: 2.08x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.93 sec: 1.79x faster                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 2.25 ms: 1.51x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 441 ms: 1.50x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 826 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 842 ms: 1.35x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.87 ms: 1.32x faster                                                   |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 632 ms: 1.27x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 25.7 ms: 1.27x faster                                                   |
| deepcopy                   | 479 us                                                   | 390 us: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.44 us: 1.18x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 135 ms: 1.18x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 46.5 us: 1.14x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                    |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| go                         | 164 ms                                                   | 151 ms: 1.09x faster                                                    |
| k_core                     | 2.99 sec                                                 | 3.05 sec: 1.02x slower                                                  |
| logging_silent             | 135 ns                                                   | 140 ns: 1.04x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 7.72 ms: 1.05x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.82 sec: 1.06x slower                                                  |
| json_dumps                 | 14.2 ms                                                  | 15.0 ms: 1.06x slower                                                   |
| json                       | 5.94 ms                                                  | 6.34 ms: 1.07x slower                                                   |
| coroutines                 | 29.4 ms                                                  | 31.6 ms: 1.07x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 70.9 ms: 1.08x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.21 sec: 1.08x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.17 sec: 1.09x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.05 sec: 1.10x slower                                                  |
| pylint                     | 345 ms                                                   | 379 ms: 1.10x slower                                                    |
| nqueens                    | 105 ms                                                   | 116 ms: 1.11x slower                                                    |
| regex_compile              | 134 ms                                                   | 149 ms: 1.11x slower                                                    |
| 2to3                       | 313 ms                                                   | 349 ms: 1.12x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 296 us: 1.12x slower                                                    |
| logging_format             | 8.10 us                                                  | 9.10 us: 1.12x slower                                                   |
| logging_simple             | 7.25 us                                                  | 8.15 us: 1.12x slower                                                   |
| json_loads                 | 32.8 us                                                  | 37.0 us: 1.13x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.56 ms: 1.14x slower                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 6.87 sec: 1.14x slower                                                  |
| deltablue                  | 3.97 ms                                                  | 4.63 ms: 1.17x slower                                                   |
| chaos                      | 70.7 ms                                                  | 82.8 ms: 1.17x slower                                                   |
| comprehensions             | 20.8 us                                                  | 24.4 us: 1.17x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 441 us: 1.18x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 25.4 ms: 1.18x slower                                                   |
| xml_etree_generate         | 118 ms                                                   | 140 ms: 1.18x slower                                                    |
| meteor_contest             | 117 ms                                                   | 139 ms: 1.18x slower                                                    |
| connected_components       | 547 ms                                                   | 649 ms: 1.19x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.20 ms: 1.19x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 74.6 ms: 1.21x slower                                                   |
| sympy_sum                  | 151 ms                                                   | 184 ms: 1.22x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 107 ms: 1.22x slower                                                    |
| shortest_path              | 565 ms                                                   | 690 ms: 1.22x slower                                                    |
| sympy_expand               | 472 ms                                                   | 584 ms: 1.24x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 102 ms: 1.25x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| fannkuch                   | 478 ms                                                   | 598 ms: 1.25x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 247 us: 1.25x slower                                                    |
| raytrace                   | 310 ms                                                   | 393 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 186 ms: 1.27x slower                                                    |
| sympy_str                  | 265 ms                                                   | 339 ms: 1.28x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 36.7 ms: 1.28x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 110 ms: 1.29x slower                                                    |
| django_template            | 39.4 ms                                                  | 51.0 ms: 1.29x slower                                                   |
| richards                   | 54.5 ms                                                  | 70.8 ms: 1.30x slower                                                   |
| richards_super             | 60.8 ms                                                  | 79.8 ms: 1.31x slower                                                   |
| bench_thread_pool          | 1.34 ms                                                  | 1.82 ms: 1.36x slower                                                   |
| coverage                   | 106 ms                                                   | 144 ms: 1.36x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 12.0 ms: 1.36x slower                                                   |
| many_optionals             | 626 us                                                   | 912 us: 1.46x slower                                                    |
| nbody                      | 118 ms                                                   | 180 ms: 1.52x slower                                                    |
| mako                       | 14.0 ms                                                  | 21.3 ms: 1.53x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 34.2 ms: 1.68x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 66.4 ms: 8.24x slower                                                   |
| telco                      | 10.5 ms                                                  | 189 ms: 18.09x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (12): pathlib, scimark_sor, float, pidigits, asyncio_websockets, spectral_norm, pycparser, generators, async_generators, pyflate, scimark_fft, deepcopy_reduce
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.30x