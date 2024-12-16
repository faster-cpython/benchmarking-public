# Results vs. 3.13.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-aarch64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.019x slower
- HPT reliability: 91.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                                   |
| html5lib       | 65.6 ms                                                  | 70.9 ms: 1.08x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 488 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 509 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 909 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 398 ms: 1.22x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 945 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 699 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 532 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.16x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 92.3 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                    |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.51 sec: 1.06x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 415 us: 1.11x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.07 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 32.4 ms: 1.13x slower                                                    |
| django_template | 39.4 ms                                                  | 48.0 ms: 1.22x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 80.3 ms: 1.30x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.15x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 488 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 509 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 909 ms: 1.28x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.6 us: 1.27x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 398 ms: 1.22x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 945 ms: 1.21x faster                                                     |
| deepcopy                   | 479 us                                                   | 399 us: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 699 ms: 1.13x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 419 ms: 1.10x faster                                                     |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.51 sec: 1.06x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.9 ms: 1.06x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 23.1 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.74 sec: 1.05x faster                                                   |
| float                      | 95.8 ms                                                  | 92.3 ms: 1.04x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.07 ms: 1.03x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.56 sec: 1.03x slower                                                   |
| pyflate                    | 582 ms                                                   | 609 ms: 1.05x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| fannkuch                   | 478 ms                                                   | 506 ms: 1.06x slower                                                     |
| meteor_contest             | 117 ms                                                   | 124 ms: 1.06x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.06x slower                                                   |
| richards_super             | 60.8 ms                                                  | 64.6 ms: 1.06x slower                                                    |
| async_generators           | 500 ms                                                   | 532 ms: 1.06x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 139 ms: 1.06x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.67 us: 1.07x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.27 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.66 ms: 1.08x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                                   |
| sympy_expand               | 472 ms                                                   | 511 ms: 1.08x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 70.9 ms: 1.08x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 23.3 ms: 1.09x slower                                                    |
| richards                   | 54.5 ms                                                  | 59.3 ms: 1.09x slower                                                    |
| logging_silent             | 135 ns                                                   | 147 ns: 1.09x slower                                                     |
| logging_simple             | 7.25 us                                                  | 7.96 us: 1.10x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 93.9 ms: 1.11x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 415 us: 1.11x slower                                                     |
| sympy_str                  | 265 ms                                                   | 299 ms: 1.13x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 32.4 ms: 1.13x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.63 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 226 us: 1.15x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.94 ms: 1.17x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.7 us: 1.18x slower                                                    |
| raytrace                   | 310 ms                                                   | 370 ms: 1.19x slower                                                     |
| chaos                      | 70.7 ms                                                  | 85.9 ms: 1.21x slower                                                    |
| django_template            | 39.4 ms                                                  | 48.0 ms: 1.22x slower                                                    |
| nqueens                    | 105 ms                                                   | 130 ms: 1.24x slower                                                     |
| generators                 | 40.3 ms                                                  | 50.7 ms: 1.26x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.31 ms: 1.27x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 80.3 ms: 1.30x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.8 ms: 1.32x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.62 sec: 1.32x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.27 sec: 1.32x slower                                                   |
| many_optionals             | 626 us                                                   | 832 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.66 sec: 205.71x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (35): xml_etree_generate, telco, spectral_norm, mako, coroutines, deepcopy_reduce, json, pylint, regex_v8, json_loads, xml_etree_process, sqlalchemy_declarative, nbody, scimark_sparse_mat_mult, asyncio_websockets, scimark_sor, thrift, unpickle_pure_python, connected_components, djangocms, sqlite_synth, sqlalchemy_imperative, pidigits, python_startup, coverage, 2to3, shortest_path, bench_thread_pool, sqlglot_transpile, go, sympy_sum, sqlglot_optimize, json_dumps, regex_compile, scimark_lu
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.019x slower

# HPT report

- Reliability score: 91.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x