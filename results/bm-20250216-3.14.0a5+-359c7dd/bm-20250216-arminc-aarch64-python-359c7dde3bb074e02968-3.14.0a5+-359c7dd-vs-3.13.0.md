# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                   |
| html5lib       | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 489 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 502 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 942 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 684 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.3 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (3): regex_compile, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.58 sec: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 409 us: 1.10x slower                                                     |
| json_loads          | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                    |
| django_template | 39.4 ms                                                  | 39.0 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 345 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 489 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 502 ms: 1.32x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.0 us: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 942 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 684 ms: 1.17x faster                                                     |
| go                         | 164 ms                                                   | 141 ms: 1.17x faster                                                     |
| spectral_norm              | 143 ms                                                   | 123 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.71 us: 1.14x faster                                                    |
| pylint                     | 345 ms                                                   | 305 ms: 1.13x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| scimark_fft                | 463 ms                                                   | 420 ms: 1.10x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.51 ms: 1.10x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.7 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                                     |
| float                      | 95.8 ms                                                  | 88.3 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.57 sec: 1.08x faster                                                   |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.0 ms: 1.08x faster                                                    |
| thrift                     | 1.01 ms                                                  | 949 us: 1.07x faster                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 61.3 ms: 1.06x faster                                                    |
| coverage                   | 106 ms                                                   | 99.5 ms: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.58 sec: 1.04x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                   |
| django_template            | 39.4 ms                                                  | 39.0 ms: 1.01x faster                                                    |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                    |
| sympy_str                  | 265 ms                                                   | 276 ms: 1.04x slower                                                     |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.57 ms: 1.05x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 409 us: 1.10x slower                                                     |
| json_loads                 | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.03 ms: 1.19x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.1 ms: 1.28x slower                                                    |
| many_optionals             | 626 us                                                   | 841 us: 1.34x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 5.29 sec: 655.48x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (48): sympy_sum, scimark_sor, xml_etree_generate, sqlalchemy_declarative, regex_compile, nqueens, scimark_lu, sqlglot_normalize, scimark_sparse_mat_mult, 2to3, chaos, bench_thread_pool, logging_format, sympy_expand, meteor_contest, scimark_monte_carlo, unpickle_pure_python, sqlite_synth, pprint_pformat, logging_simple, coroutines, asyncio_websockets, crypto_pyaes, mdp, regex_v8, deltablue, genshi_xml, shortest_path, pprint_safe_repr, sympy_integrate, connected_components, mako, python_startup, xml_etree_process, sqlglot_transpile, pyflate, regex_dna, comprehensions, hexiom, typing_runtime_protocols, richards_super, json, nbody, pidigits, sqlglot_parse, logging_silent, fannkuch, json_dumps
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x