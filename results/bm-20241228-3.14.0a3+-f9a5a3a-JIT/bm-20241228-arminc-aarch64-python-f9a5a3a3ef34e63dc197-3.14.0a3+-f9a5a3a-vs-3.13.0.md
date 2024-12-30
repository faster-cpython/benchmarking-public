# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.029x slower
- HPT reliability: 97.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 324 ms: 1.03x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| html5lib       | 65.6 ms                                                  | 70.2 ms: 1.07x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 488 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 534 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 951 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 400 ms: 1.21x faster                                                     |
| async_tree_none            | 504 ms                                                   | 421 ms: 1.20x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 956 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 693 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 714 ms: 1.11x faster                                                     |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.14x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| regex_dna      | 263 ms                                                   | 252 ms: 1.04x faster                                                     |
| regex_compile  | 134 ms                                                   | 145 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, unpickle_pure_python, json_loads, xml_etree_process, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| django_template | 39.4 ms                                                  | 48.3 ms: 1.23x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 35.8 ms: 1.25x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 87.0 ms: 1.41x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 488 ms: 1.36x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.4 us: 1.28x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 534 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 951 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 400 ms: 1.21x faster                                                     |
| deepcopy                   | 479 us                                                   | 397 us: 1.21x faster                                                     |
| async_tree_none            | 504 ms                                                   | 421 ms: 1.20x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 956 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 693 ms: 1.16x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.0 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 714 ms: 1.11x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| scimark_fft                | 463 ms                                                   | 420 ms: 1.10x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 4.02 us: 1.06x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| scimark_sor                | 164 ms                                                   | 157 ms: 1.05x faster                                                     |
| regex_dna                  | 263 ms                                                   | 252 ms: 1.04x faster                                                     |
| mako                       | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.84 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| djangocms                  | 66.2 us                                                  | 68.3 us: 1.03x slower                                                    |
| 2to3                       | 313 ms                                                   | 324 ms: 1.03x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.59 sec: 1.04x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| fannkuch                   | 478 ms                                                   | 506 ms: 1.06x slower                                                     |
| pyflate                    | 582 ms                                                   | 616 ms: 1.06x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 70.2 ms: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.63 ms: 1.07x slower                                                    |
| logging_format             | 8.10 us                                                  | 8.75 us: 1.08x slower                                                    |
| richards_super             | 60.8 ms                                                  | 65.7 ms: 1.08x slower                                                    |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| regex_compile              | 134 ms                                                   | 145 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 71.1 ms: 1.09x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.33 ms: 1.09x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.6 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.57 ms: 1.10x slower                                                    |
| meteor_contest             | 117 ms                                                   | 128 ms: 1.10x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 144 ms: 1.10x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 23.6 ms: 1.10x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.48 sec: 1.10x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 94.0 ms: 1.11x slower                                                    |
| sympy_expand               | 472 ms                                                   | 525 ms: 1.11x slower                                                     |
| logging_silent             | 135 ns                                                   | 151 ns: 1.12x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.13 us: 1.12x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 171 ms: 1.13x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.86 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 230 us: 1.17x slower                                                     |
| sympy_str                  | 265 ms                                                   | 310 ms: 1.17x slower                                                     |
| raytrace                   | 310 ms                                                   | 367 ms: 1.18x slower                                                     |
| comprehensions             | 20.8 us                                                  | 25.0 us: 1.20x slower                                                    |
| chaos                      | 70.7 ms                                                  | 86.2 ms: 1.22x slower                                                    |
| django_template            | 39.4 ms                                                  | 48.3 ms: 1.23x slower                                                    |
| nqueens                    | 105 ms                                                   | 131 ms: 1.25x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 35.8 ms: 1.25x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.50 ms: 1.29x slower                                                    |
| generators                 | 40.3 ms                                                  | 52.2 ms: 1.30x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 27.3 ms: 1.34x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.67 sec: 1.35x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.32 sec: 1.37x slower                                                   |
| many_optionals             | 626 us                                                   | 860 us: 1.37x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 87.0 ms: 1.41x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 1.56 sec: 193.46x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (30): telco, xml_etree_generate, json, float, sqlalchemy_declarative, scimark_monte_carlo, pylint, k_core, coverage, unpickle_pure_python, asyncio_websockets, regex_v8, coroutines, python_startup, connected_components, nbody, json_loads, thrift, go, pidigits, spectral_norm, xml_etree_process, scimark_sparse_mat_mult, json_dumps, richards, bench_thread_pool, sqlite_synth, scimark_lu, pickle_pure_python, sqlglot_transpile
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 97.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x