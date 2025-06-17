# Results vs. 3.13.0

- fork: python
- ref: 3.14
- machine: linux-aarch64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 302 ms: 1.04x faster                                     |
| html5lib       | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                    |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                     |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                     |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                     |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                     |
| Geometric mean             | (ref)                                                    | 1.22x faster                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                    |
| regex_v8       | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                    |
| regex_dna      | 263 ms                                                   | 220 ms: 1.20x faster                                     |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                     |
| Geometric mean | (ref)                                                    | 1.20x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                     |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                   |
| json_loads          | 32.8 us                                                  | 35.7 us: 1.09x slower                                    |
| Geometric mean      | (ref)                                                    | 1.03x faster                                             |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                    |
| Geometric mean         | (ref)                                                    | 1.01x faster                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.2 ms: 1.05x faster                                    |
| genshi_xml     | 61.6 ms                                                  | 59.7 ms: 1.03x faster                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                   |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.8 us: 1.40x faster                                    |
| regex_effbot               | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                    |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                     |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                     |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                     |
| regex_v8                   | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                     |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.20x faster                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                    |
| generators                 | 40.3 ms                                                  | 35.6 ms: 1.13x faster                                    |
| spectral_norm              | 143 ms                                                   | 127 ms: 1.13x faster                                     |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.13x faster                                     |
| float                      | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                    |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.9 ms: 1.11x faster                                    |
| telco                      | 10.5 ms                                                  | 9.43 ms: 1.11x faster                                    |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.44 sec: 1.11x faster                                   |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                     |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                     |
| pyflate                    | 582 ms                                                   | 529 ms: 1.10x faster                                     |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.09x faster                                    |
| richards                   | 54.5 ms                                                  | 50.4 ms: 1.08x faster                                    |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                   |
| meteor_contest             | 117 ms                                                   | 110 ms: 1.07x faster                                     |
| pprint_safe_repr           | 962 ms                                                   | 903 ms: 1.07x faster                                     |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                    |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.05x faster                                     |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.05x faster                                    |
| nqueens                    | 105 ms                                                   | 99.6 ms: 1.05x faster                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                   |
| genshi_text                | 28.6 ms                                                  | 27.2 ms: 1.05x faster                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                   |
| html5lib                   | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                    |
| 2to3                       | 313 ms                                                   | 302 ms: 1.04x faster                                     |
| genshi_xml                 | 61.6 ms                                                  | 59.7 ms: 1.03x faster                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                    |
| logging_format             | 8.10 us                                                  | 8.49 us: 1.05x slower                                    |
| raytrace                   | 310 ms                                                   | 327 ms: 1.06x slower                                     |
| logging_simple             | 7.25 us                                                  | 7.69 us: 1.06x slower                                    |
| json_loads                 | 32.8 us                                                  | 35.7 us: 1.09x slower                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                    |
| gc_traversal               | 5.92 ms                                                  | 6.89 ms: 1.16x slower                                    |
| many_optionals             | 626 us                                                   | 745 us: 1.19x slower                                     |
| subparsers                 | 20.3 ms                                                  | 28.2 ms: 1.39x slower                                    |
| logging_silent             | 135 ns                                                   | 613 ns: 4.55x slower                                     |
| Geometric mean             | (ref)                                                    | 1.05x faster                                             |

Benchmark hidden because not significant (32): hexiom, json_dumps, richards_super, xml_etree_generate, coverage, deltablue, sqlalchemy_declarative, chaos, crypto_pyaes, sympy_expand, asyncio_websockets, docutils, fannkuch, xml_etree_process, python_startup, sqlalchemy_imperative, typing_runtime_protocols, connected_components, sympy_sum, shortest_path, unpickle_pure_python, sympy_str, pidigits, django_template, comprehensions, mako, nbody, json, scimark_sparse_mat_mult, scimark_lu, coroutines, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x