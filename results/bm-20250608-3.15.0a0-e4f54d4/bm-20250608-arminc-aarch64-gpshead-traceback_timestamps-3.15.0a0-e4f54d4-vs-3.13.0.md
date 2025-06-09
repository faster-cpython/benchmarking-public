# Results vs. 3.13.0

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-aarch64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                   |
| html5lib       | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                     |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 650 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.5 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                    |
| regex_dna      | 263 ms                                                   | 232 ms: 1.13x faster                                                     |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                    | 1.18x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, json_dumps, xml_etree_process, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                    |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                    |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                             |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                     |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.5 us: 1.41x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                    |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                     |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.48 us: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 650 ms: 1.21x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                     |
| regex_dna                  | 263 ms                                                   | 232 ms: 1.13x faster                                                     |
| spectral_norm              | 143 ms                                                   | 128 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.37 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.2 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.5 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                     |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.54 sec: 1.09x faster                                                   |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                    |
| scimark_fft                | 463 ms                                                   | 431 ms: 1.07x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.07x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                   |
| hexiom                     | 7.34 ms                                                  | 6.88 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.86 us: 1.06x faster                                                    |
| pyflate                    | 582 ms                                                   | 551 ms: 1.06x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| nqueens                    | 105 ms                                                   | 99.9 ms: 1.05x faster                                                    |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                    |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                    |
| docutils                   | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                   |
| connected_components       | 547 ms                                                   | 566 ms: 1.03x slower                                                     |
| shortest_path              | 565 ms                                                   | 585 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.99 sec                                                 | 2.06 sec: 1.04x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 999 ms: 1.04x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.46 us: 1.04x slower                                                    |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                     |
| logging_simple             | 7.25 us                                                  | 7.68 us: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.13x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.90 ms: 1.16x slower                                                    |
| many_optionals             | 626 us                                                   | 863 us: 1.38x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                                    |
| logging_silent             | 135 ns                                                   | 612 ns: 4.55x slower                                                     |
| coverage                   | 106 ms                                                   | 561 ms: 5.31x slower                                                     |
| thrift                     | 1.01 ms                                                  | 192 ms: 190.11x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (29): sympy_sum, xml_etree_generate, json_dumps, json, sympy_integrate, comprehensions, meteor_contest, genshi_text, sympy_expand, fannkuch, mako, xml_etree_process, richards_super, deltablue, json_loads, asyncio_websockets, chaos, crypto_pyaes, coroutines, typing_runtime_protocols, unpickle_pure_python, pidigits, scimark_sparse_mat_mult, scimark_lu, django_template, genshi_xml, pickle_pure_python, sympy_str, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x