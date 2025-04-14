# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.001x faster
- HPT reliability: 62.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.19 sec: 1.08x slower                                                   |
| html5lib       | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 400 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 388 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 689 ms: 1.14x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                             |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.3 ms: 1.08x faster                                                    |
| nbody          | 118 ms                                                   | 130 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.97 ms: 1.28x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 31.5 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 186 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.55 sec: 1.05x faster                                                   |
| pickle_pure_python   | 374 us                                                   | 404 us: 1.08x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 291 us: 1.10x slower                                                     |
| json_loads           | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 64.5 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.38x faster                                                     |
| deepcopy                   | 479 us                                                   | 359 us: 1.33x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.7 us: 1.33x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.97 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 400 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 388 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                                     |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 689 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 186 ms: 1.09x faster                                                     |
| float                      | 95.8 ms                                                  | 88.3 ms: 1.08x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.3 ms: 1.08x faster                                                    |
| scimark_sor                | 164 ms                                                   | 153 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.89 ms: 1.06x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.55 sec: 1.05x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 31.5 ms: 1.03x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.91 sec: 1.02x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 64.5 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.00 ms: 1.05x slower                                                    |
| logging_silent             | 135 ns                                                   | 142 ns: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.58 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 327 ms: 1.06x slower                                                     |
| nqueens                    | 105 ms                                                   | 112 ms: 1.07x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.19 sec: 1.08x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.27 ms: 1.08x slower                                                    |
| sympy_expand               | 472 ms                                                   | 511 ms: 1.08x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 404 us: 1.08x slower                                                     |
| sympy_str                  | 265 ms                                                   | 287 ms: 1.08x slower                                                     |
| meteor_contest             | 117 ms                                                   | 127 ms: 1.09x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.47 sec: 1.10x slower                                                   |
| nbody                      | 118 ms                                                   | 130 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 291 us: 1.10x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 219 us: 1.11x slower                                                     |
| json_loads                 | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.61 ms: 1.12x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 8.41 ms: 1.14x slower                                                    |
| fannkuch                   | 478 ms                                                   | 549 ms: 1.15x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.96 ms: 1.18x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.8 us: 1.19x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 102 ms: 1.20x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.6 ms: 1.31x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.27 sec: 1.32x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.66 sec: 1.34x slower                                                   |
| many_optionals             | 626 us                                                   | 874 us: 1.40x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.23 sec: 275.89x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (42): thrift, pathlib, sqlalchemy_declarative, sqlite_synth, richards, genshi_text, richards_super, coverage, xml_etree_generate, pylint, async_generators, json_dumps, k_core, bench_thread_pool, asyncio_websockets, json, scimark_monte_carlo, xml_etree_process, go, mdp, scimark_lu, logging_format, django_template, pyflate, sphinx, connected_components, regex_compile, sqlalchemy_imperative, sqlglot_normalize, regex_dna, chaos, pidigits, python_startup, shortest_path, coroutines, sympy_sum, mako, logging_simple, 2to3, sqlglot_optimize, sqlglot_transpile, sympy_integrate
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 62.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x