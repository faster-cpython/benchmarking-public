# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-aarch64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 288 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 59.5 ms: 1.10x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 456 ms: 1.45x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                     |
| async_generators           | 500 ms                                                   | 409 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 706 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 27.9 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.1 ms: 1.14x faster                                                    |
| nbody          | 118 ms                                                   | 124 ms: 1.05x slower                                                     |
| pidigits       | 238 ms                                                   | 294 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.24 ms: 1.20x faster                                                    |
| regex_dna      | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                   |
| xml_etree_generate   | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| xml_etree_process    | 82.1 ms                                                  | 74.0 ms: 1.11x faster                                                    |
| unpickle_pure_python | 265 us                                                   | 249 us: 1.06x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 151 ms: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (4): pickle_pure_python, json_dumps, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 25.5 ms: 1.12x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 57.8 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.61 sec: 2.14x faster                                                   |
| deepcopy                   | 479 us                                                   | 311 us: 1.54x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.4 us: 1.50x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 456 ms: 1.45x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.25 us: 1.31x faster                                                    |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                     |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                     |
| async_generators           | 500 ms                                                   | 409 ms: 1.22x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.24 ms: 1.20x faster                                                    |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.20x faster                                                     |
| logging_silent             | 135 ns                                                   | 113 ns: 1.19x faster                                                     |
| scimark_fft                | 463 ms                                                   | 397 ms: 1.16x faster                                                     |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                   |
| pylint                     | 345 ms                                                   | 301 ms: 1.15x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.25 sec: 1.15x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| float                      | 95.8 ms                                                  | 84.1 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.4 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 706 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.6 ms: 1.13x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 25.5 ms: 1.12x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.6 ms: 1.12x faster                                                    |
| richards_super             | 60.8 ms                                                  | 54.3 ms: 1.12x faster                                                    |
| pyflate                    | 582 ms                                                   | 520 ms: 1.12x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.20 sec: 1.12x faster                                                   |
| coverage                   | 106 ms                                                   | 95.0 ms: 1.11x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 74.0 ms: 1.11x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.44 ms: 1.11x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.5 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.7 ms: 1.10x faster                                                    |
| regex_dna                  | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.44 us: 1.09x faster                                                    |
| 2to3                       | 313 ms                                                   | 288 ms: 1.08x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.76 us: 1.08x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.77 sec: 1.08x faster                                                   |
| chaos                      | 70.7 ms                                                  | 65.8 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.0 ms: 1.07x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.07x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 184 us: 1.07x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.86 sec: 1.07x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 902 ms: 1.07x faster                                                     |
| genshi_xml                 | 61.6 ms                                                  | 57.8 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 265 us                                                   | 249 us: 1.06x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.82 us: 1.06x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.75 ms: 1.06x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 27.9 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 151 ms: 1.05x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.99 ms: 1.05x faster                                                    |
| comprehensions             | 20.8 us                                                  | 19.8 us: 1.05x faster                                                    |
| sympy_expand               | 472 ms                                                   | 453 ms: 1.04x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.53 ms: 1.04x slower                                                    |
| nbody                      | 118 ms                                                   | 124 ms: 1.05x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.52 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 294 ms: 1.23x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.9 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 825 us: 1.32x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.23 sec: 276.22x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (22): sqlalchemy_declarative, nqueens, scimark_lu, scimark_sparse_mat_mult, django_template, json, meteor_contest, sympy_str, sqlalchemy_imperative, mako, pickle_pure_python, bench_thread_pool, asyncio_websockets, json_dumps, crypto_pyaes, connected_components, raytrace, python_startup, json_loads, shortest_path, fannkuch, xml_etree_parse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x