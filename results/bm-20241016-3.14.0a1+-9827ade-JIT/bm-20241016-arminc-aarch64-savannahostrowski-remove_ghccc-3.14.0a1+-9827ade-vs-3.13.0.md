# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.070x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 373 ms: 1.23x slower                                                        |
| docutils       | 2.89 sec                                                 | 3.66 sec: 1.27x slower                                                      |
| html5lib       | 66.4 ms                                                  | 71.4 ms: 1.08x slower                                                       |
| sphinx         | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                      |
| tornado_http   | 128 ms                                                   | 150 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                    | 1.19x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                        |
| async_tree_none            | 497 ms                                                   | 458 ms: 1.08x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 605 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                                        |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                      |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 108 ms: 1.06x faster                                                        |
| float          | 93.3 ms                                                  | 91.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 245 ms: 1.03x faster                                                        |
| regex_compile  | 127 ms                                                   | 165 ms: 1.30x slower                                                        |
| Geometric mean | (ref)                                                    | 1.06x slower                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.04x faster                                                        |
| xml_etree_process    | 80.5 ms                                                  | 78.0 ms: 1.03x faster                                                       |
| tomli_loads          | 2.54 sec                                                 | 2.49 sec: 1.02x faster                                                      |
| unpickle_pure_python | 251 us                                                   | 264 us: 1.05x slower                                                        |
| json_dumps           | 13.6 ms                                                  | 14.3 ms: 1.06x slower                                                       |
| pickle_pure_python   | 357 us                                                   | 377 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 14.8 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.73 ms                                                  | 8.83 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.8 ms: 1.05x faster                                                       |
| genshi_text     | 27.7 ms                                                  | 32.2 ms: 1.16x slower                                                       |
| django_template | 41.6 ms                                                  | 49.0 ms: 1.18x slower                                                       |
| genshi_xml      | 60.3 ms                                                  | 78.6 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 38.1 us: 1.32x faster                                                       |
| deepcopy                   | 447 us                                                   | 366 us: 1.22x faster                                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                        |
| async_tree_none            | 497 ms                                                   | 458 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.78 us: 1.08x faster                                                       |
| async_tree_memoization     | 651 ms                                                   | 605 ms: 1.08x faster                                                        |
| nbody                      | 114 ms                                                   | 108 ms: 1.06x faster                                                        |
| scimark_fft                | 447 ms                                                   | 424 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                        |
| mako                       | 13.4 ms                                                  | 12.8 ms: 1.05x faster                                                       |
| json                       | 5.73 ms                                                  | 5.48 ms: 1.04x faster                                                       |
| xml_etree_generate         | 113 ms                                                   | 109 ms: 1.04x faster                                                        |
| python_startup             | 15.4 ms                                                  | 14.8 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                                        |
| regex_dna                  | 253 ms                                                   | 245 ms: 1.03x faster                                                        |
| xml_etree_process          | 80.5 ms                                                  | 78.0 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.87 sec                                                 | 5.69 sec: 1.03x faster                                                      |
| tomli_loads                | 2.54 sec                                                 | 2.49 sec: 1.02x faster                                                      |
| telco                      | 9.74 ms                                                  | 9.57 ms: 1.02x faster                                                       |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                        |
| float                      | 93.3 ms                                                  | 91.9 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.73 ms                                                  | 8.83 ms: 1.01x slower                                                       |
| spectral_norm              | 143 ms                                                   | 146 ms: 1.02x slower                                                        |
| logging_format             | 7.82 us                                                  | 8.04 us: 1.03x slower                                                       |
| scimark_monte_carlo        | 83.6 ms                                                  | 86.4 ms: 1.03x slower                                                       |
| mdp                        | 3.34 sec                                                 | 3.46 sec: 1.04x slower                                                      |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                        |
| logging_simple             | 7.07 us                                                  | 7.35 us: 1.04x slower                                                       |
| pyflate                    | 556 ms                                                   | 581 ms: 1.04x slower                                                        |
| unpickle_pure_python       | 251 us                                                   | 264 us: 1.05x slower                                                        |
| meteor_contest             | 114 ms                                                   | 120 ms: 1.05x slower                                                        |
| json_dumps                 | 13.6 ms                                                  | 14.3 ms: 1.06x slower                                                       |
| pickle_pure_python         | 357 us                                                   | 377 us: 1.06x slower                                                        |
| scimark_lu                 | 139 ms                                                   | 148 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.94 ms: 1.07x slower                                                       |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                      |
| html5lib                   | 66.4 ms                                                  | 71.4 ms: 1.08x slower                                                       |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                                       |
| deltablue                  | 3.82 ms                                                  | 4.15 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 193 us                                                   | 210 us: 1.09x slower                                                        |
| gc_traversal               | 5.77 ms                                                  | 6.34 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                      |
| create_gc_cycles           | 3.35 ms                                                  | 3.73 ms: 1.11x slower                                                       |
| go                         | 160 ms                                                   | 179 ms: 1.12x slower                                                        |
| richards_super             | 60.1 ms                                                  | 67.9 ms: 1.13x slower                                                       |
| richards                   | 53.6 ms                                                  | 60.9 ms: 1.13x slower                                                       |
| pycparser                  | 1.27 sec                                                 | 1.45 sec: 1.14x slower                                                      |
| comprehensions             | 20.4 us                                                  | 23.3 us: 1.14x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                  | 1.59 ms: 1.15x slower                                                       |
| chaos                      | 68.0 ms                                                  | 78.8 ms: 1.16x slower                                                       |
| genshi_text                | 27.7 ms                                                  | 32.2 ms: 1.16x slower                                                       |
| raytrace                   | 300 ms                                                   | 350 ms: 1.17x slower                                                        |
| tornado_http               | 128 ms                                                   | 150 ms: 1.17x slower                                                        |
| nqueens                    | 100 ms                                                   | 117 ms: 1.17x slower                                                        |
| django_template            | 41.6 ms                                                  | 49.0 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 127 ms                                                   | 151 ms: 1.19x slower                                                        |
| sqlglot_transpile          | 1.73 ms                                                  | 2.10 ms: 1.21x slower                                                       |
| 2to3                       | 304 ms                                                   | 373 ms: 1.23x slower                                                        |
| sphinx                     | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                      |
| pprint_safe_repr           | 926 ms                                                   | 1.17 sec: 1.26x slower                                                      |
| docutils                   | 2.89 sec                                                 | 3.66 sec: 1.27x slower                                                      |
| sympy_expand               | 457 ms                                                   | 580 ms: 1.27x slower                                                        |
| sqlglot_optimize           | 62.2 ms                                                  | 79.3 ms: 1.27x slower                                                       |
| pprint_pformat             | 1.90 sec                                                 | 2.42 sec: 1.28x slower                                                      |
| generators                 | 37.6 ms                                                  | 48.3 ms: 1.28x slower                                                       |
| regex_compile              | 127 ms                                                   | 165 ms: 1.30x slower                                                        |
| genshi_xml                 | 60.3 ms                                                  | 78.6 ms: 1.30x slower                                                       |
| sympy_str                  | 264 ms                                                   | 347 ms: 1.31x slower                                                        |
| hexiom                     | 7.11 ms                                                  | 9.54 ms: 1.34x slower                                                       |
| sympy_integrate            | 20.8 ms                                                  | 29.1 ms: 1.40x slower                                                       |
| pylint                     | 342 ms                                                   | 486 ms: 1.42x slower                                                        |
| sympy_sum                  | 144 ms                                                   | 211 ms: 1.47x slower                                                        |
| bench_mp_pool              | 7.68 ms                                                  | 2.16 sec: 281.27x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                                |

Benchmark hidden because not significant (15): xml_etree_parse, async_tree_cpu_io_mixed, crypto_pyaes, json_loads, coverage, pathlib, scimark_sor, regex_v8, regex_effbot, xml_etree_iterparse, asyncio_websockets, fannkuch, pidigits, thrift, coroutines
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower
# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.07x