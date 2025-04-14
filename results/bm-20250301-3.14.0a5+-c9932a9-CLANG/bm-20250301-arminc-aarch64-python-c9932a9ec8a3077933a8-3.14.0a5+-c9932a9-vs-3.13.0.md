# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: linux-aarch64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| html5lib       | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                     |
| async_tree_none            | 504 ms                                                   | 371 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                     |
| async_generators           | 500 ms                                                   | 417 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 727 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 749 ms: 1.05x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.32 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 118 ms                                                   | 106 ms: 1.11x faster                                                     |
| tomli_loads        | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| xml_etree_process  | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                    |
| Geometric mean     | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, json_loads, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.29 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.8 ms: 1.06x faster                                                    |
| django_template | 39.4 ms                                                  | 37.7 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 313 us: 1.53x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.0 us: 1.43x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                     |
| async_tree_none            | 504 ms                                                   | 371 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| spectral_norm              | 143 ms                                                   | 112 ms: 1.28x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.35 us: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                     |
| go                         | 164 ms                                                   | 135 ms: 1.22x faster                                                     |
| async_generators           | 500 ms                                                   | 417 ms: 1.20x faster                                                     |
| scimark_fft                | 463 ms                                                   | 388 ms: 1.19x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.32 ms: 1.18x faster                                                    |
| pylint                     | 345 ms                                                   | 297 ms: 1.16x faster                                                     |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.13 ms: 1.15x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.3 ms: 1.14x faster                                                    |
| logging_silent             | 135 ns                                                   | 119 ns: 1.13x faster                                                     |
| richards                   | 54.5 ms                                                  | 48.9 ms: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 106 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.46 sec: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 727 ms: 1.10x faster                                                     |
| thrift                     | 1.01 ms                                                  | 921 us: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.07 ms: 1.10x faster                                                    |
| coverage                   | 106 ms                                                   | 96.4 ms: 1.10x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 138 ms: 1.09x faster                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 537 ms: 1.08x faster                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 1.70 ms: 1.08x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.4 ms: 1.08x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                    |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.1 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.06x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.24 sec: 1.06x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.06x faster                                                   |
| nqueens                    | 105 ms                                                   | 99.1 ms: 1.06x faster                                                    |
| comprehensions             | 20.8 us                                                  | 19.7 us: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 749 ms: 1.05x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                   |
| django_template            | 39.4 ms                                                  | 37.7 ms: 1.05x faster                                                    |
| richards_super             | 60.8 ms                                                  | 58.5 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 937 ms: 1.03x faster                                                     |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.29 ms: 1.06x slower                                                    |
| regex_v8                   | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.69 ms: 1.09x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.72 ms: 1.13x slower                                                    |
| pidigits                   | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.8 ms: 1.32x slower                                                    |
| many_optionals             | 626 us                                                   | 861 us: 1.37x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 3.26 sec: 404.29x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (38): scimark_lu, sqlalchemy_declarative, logging_format, float, logging_simple, sqlglot_optimize, chaos, bench_thread_pool, sqlglot_normalize, typing_runtime_protocols, sympy_expand, 2to3, xml_etree_iterparse, sqlglot_parse, coroutines, nbody, pprint_pformat, regex_dna, deltablue, genshi_xml, mako, sqlite_synth, connected_components, unpickle_pure_python, asyncio_websockets, raytrace, hexiom, crypto_pyaes, json, shortest_path, sympy_str, json_loads, python_startup, fannkuch, json_dumps, xml_etree_parse, meteor_contest, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.05x