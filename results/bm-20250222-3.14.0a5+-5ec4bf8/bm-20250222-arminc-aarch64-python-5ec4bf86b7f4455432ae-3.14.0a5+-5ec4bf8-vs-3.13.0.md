# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.033x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 488 ms: 1.36x faster                                                     |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 929 ms: 1.25x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 459 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.4 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.13 ms: 1.24x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 31.6 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 397 us: 1.06x slower                                                     |
| json_loads          | 32.8 us                                                  | 35.9 us: 1.09x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.5 ms: 1.04x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 64.9 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 488 ms: 1.36x faster                                                     |
| deepcopy                   | 479 us                                                   | 361 us: 1.33x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.6 us: 1.30x faster                                                    |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 929 ms: 1.25x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.13 ms: 1.24x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                                     |
| go                         | 164 ms                                                   | 142 ms: 1.16x faster                                                     |
| spectral_norm              | 143 ms                                                   | 126 ms: 1.14x faster                                                     |
| pylint                     | 345 ms                                                   | 304 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.83 us: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 87.4 ms: 1.10x faster                                                    |
| async_generators           | 500 ms                                                   | 459 ms: 1.09x faster                                                     |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.08x faster                                                     |
| generators                 | 40.3 ms                                                  | 37.6 ms: 1.07x faster                                                    |
| coverage                   | 106 ms                                                   | 98.7 ms: 1.07x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.81 ms: 1.07x faster                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.2 ms: 1.06x faster                                                    |
| scimark_sor                | 164 ms                                                   | 155 ms: 1.06x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.32 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.77 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 27.5 ms: 1.04x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.30 sec: 1.04x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 31.6 ms: 1.03x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.92 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 64.9 ms: 1.05x slower                                                    |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 397 us: 1.06x slower                                                     |
| json_loads                 | 32.8 us                                                  | 35.9 us: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.33 ms: 1.24x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.3 ms: 1.29x slower                                                    |
| many_optionals             | 626 us                                                   | 853 us: 1.36x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 7.33 sec: 908.21x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (48): regex_compile, thrift, scimark_lu, pyflate, coroutines, richards_super, sqlglot_transpile, sqlglot_normalize, sympy_sum, richards, scimark_monte_carlo, json_dumps, sphinx, html5lib, chaos, nqueens, bench_thread_pool, logging_format, connected_components, xml_etree_generate, asyncio_websockets, mdp, regex_dna, django_template, pidigits, sqlglot_parse, logging_silent, sympy_expand, 2to3, xml_etree_process, mako, sqlglot_optimize, deltablue, pprint_safe_repr, shortest_path, hexiom, sympy_integrate, pprint_pformat, json, crypto_pyaes, python_startup, meteor_contest, sqlite_synth, logging_simple, comprehensions, fannkuch, nbody, unpickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x