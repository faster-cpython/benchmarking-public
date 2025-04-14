# Results vs. 3.13.0

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: linux-aarch64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 290 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 857 ms: 1.36x faster                                                     |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 363 ms: 1.33x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 878 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 431 ms: 1.16x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 28.3 ms: 1.04x faster                                                    |
| asyncio_websockets         | 674 ms                                                   | 656 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.26x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.4 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                    |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.9 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                   |
| xml_etree_generate   | 118 ms                                                   | 108 ms: 1.09x faster                                                     |
| xml_etree_process    | 82.1 ms                                                  | 77.5 ms: 1.06x faster                                                    |
| unpickle_pure_python | 265 us                                                   | 252 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 59.1 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 455 ms: 1.46x faster                                                     |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.3 us: 1.42x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 857 ms: 1.36x faster                                                     |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 363 ms: 1.33x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 878 ms: 1.30x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.27x faster                                                     |
| spectral_norm              | 143 ms                                                   | 115 ms: 1.25x faster                                                     |
| go                         | 164 ms                                                   | 134 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.45 us: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 431 ms: 1.16x faster                                                     |
| generators                 | 40.3 ms                                                  | 35.1 ms: 1.15x faster                                                    |
| float                      | 95.8 ms                                                  | 84.4 ms: 1.14x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| scimark_fft                | 463 ms                                                   | 410 ms: 1.13x faster                                                     |
| pylint                     | 345 ms                                                   | 306 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.6 ms: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.38 sec: 1.12x faster                                                   |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.40 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.22 sec: 1.11x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 139 ms: 1.10x faster                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.6 ms: 1.10x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                                     |
| thrift                     | 1.01 ms                                                  | 926 us: 1.09x faster                                                     |
| richards                   | 54.5 ms                                                  | 50.2 ms: 1.09x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.13 ms: 1.09x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 139 ms: 1.08x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.47 us: 1.08x faster                                                    |
| sqlglot_optimize           | 65.2 ms                                                  | 60.2 ms: 1.08x faster                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 14.9 ms: 1.08x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                    |
| 2to3                       | 313 ms                                                   | 290 ms: 1.08x faster                                                     |
| chaos                      | 70.7 ms                                                  | 65.6 ms: 1.08x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 895 ms: 1.07x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                   |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.77 us: 1.07x faster                                                    |
| nqueens                    | 105 ms                                                   | 98.2 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.07x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                   |
| richards_super             | 60.8 ms                                                  | 57.1 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.87 sec: 1.06x faster                                                   |
| hexiom                     | 7.34 ms                                                  | 6.93 ms: 1.06x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 77.5 ms: 1.06x faster                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.36 ms: 1.06x faster                                                    |
| coverage                   | 106 ms                                                   | 100 ms: 1.05x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 30.9 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 265 us                                                   | 252 us: 1.05x faster                                                     |
| pyflate                    | 582 ms                                                   | 554 ms: 1.05x faster                                                     |
| deltablue                  | 3.97 ms                                                  | 3.78 ms: 1.05x faster                                                    |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.05x faster                                                     |
| sympy_expand               | 472 ms                                                   | 451 ms: 1.05x faster                                                     |
| mdp                        | 3.45 sec                                                 | 3.29 sec: 1.05x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 59.1 ms: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 255 ms: 1.04x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 28.3 ms: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 190 us: 1.04x faster                                                     |
| asyncio_websockets         | 674 ms                                                   | 656 ms: 1.03x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.49 ms: 1.10x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.0 ms: 1.23x slower                                                    |
| many_optionals             | 626 us                                                   | 813 us: 1.30x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 4.45 sec: 551.11x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (21): sqlglot_transpile, sqlglot_normalize, mako, json_dumps, sympy_integrate, bench_thread_pool, comprehensions, json, connected_components, pidigits, raytrace, python_startup, nbody, fannkuch, shortest_path, django_template, python_startup_no_site, crypto_pyaes, pickle_pure_python, create_gc_cycles, json_loads
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: dulwich_log

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.02x