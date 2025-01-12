# Results vs. base

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.059x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                              | 319 ms: 1.05x slower                                                                                                    |
| docutils       | 3.02 sec                                                                                                            | 3.24 sec: 1.07x slower                                                                                                  |
| html5lib       | 63.8 ms                                                                                                             | 68.9 ms: 1.08x slower                                                                                                   |
| sphinx         | 1.18 sec                                                                                                            | 1.27 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 679 ms                                                                                                              | 700 ms: 1.03x slower                                                                                                    |
| async_tree_io           | 889 ms                                                                                                              | 921 ms: 1.04x slower                                                                                                    |
| async_tree_io_tg        | 883 ms                                                                                                              | 918 ms: 1.04x slower                                                                                                    |
| async_tree_none         | 389 ms                                                                                                              | 406 ms: 1.04x slower                                                                                                    |
| async_tree_memoization  | 495 ms                                                                                                              | 518 ms: 1.05x slower                                                                                                    |
| async_generators        | 496 ms                                                                                                              | 521 ms: 1.05x slower                                                                                                    |
| asyncio_tcp             | 569 ms                                                                                                              | 603 ms: 1.06x slower                                                                                                    |
| async_tree_none_tg      | 367 ms                                                                                                              | 390 ms: 1.06x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (5): asyncio_websockets, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 123 ms                                                                                                              | 114 ms: 1.07x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                                                              | 266 ms: 1.06x slower                                                                                                    |
| regex_compile  | 125 ms                                                                                                              | 141 ms: 1.13x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads        | 2.60 sec                                                                                                            | 2.53 sec: 1.03x faster                                                                                                  |
| pickle_pure_python | 385 us                                                                                                              | 403 us: 1.05x slower                                                                                                    |
| Geometric mean     | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (12): pickle_list, json_loads, xml_etree_process, xml_etree_generate, json_dumps, pickle_dict, unpickle, xml_etree_parse, xml_etree_iterparse, unpickle_list, unpickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 14.2 ms                                                                                                             | 13.3 ms: 1.07x faster                                                                                                   |
| django_template | 41.2 ms                                                                                                             | 47.0 ms: 1.14x slower                                                                                                   |
| genshi_text     | 28.5 ms                                                                                                             | 33.1 ms: 1.16x slower                                                                                                   |
| genshi_xml      | 64.4 ms                                                                                                             | 83.7 ms: 1.30x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.13x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 4.18 sec                                                                                                            | 1.33 sec: 3.15x faster                                                                                                  |
| nbody                    | 123 ms                                                                                                              | 114 ms: 1.07x faster                                                                                                    |
| mako                     | 14.2 ms                                                                                                             | 13.3 ms: 1.07x faster                                                                                                   |
| tomli_loads              | 2.60 sec                                                                                                            | 2.53 sec: 1.03x faster                                                                                                  |
| async_tree_cpu_io_mixed  | 679 ms                                                                                                              | 700 ms: 1.03x slower                                                                                                    |
| async_tree_io            | 889 ms                                                                                                              | 921 ms: 1.04x slower                                                                                                    |
| mdp                      | 3.42 sec                                                                                                            | 3.55 sec: 1.04x slower                                                                                                  |
| async_tree_io_tg         | 883 ms                                                                                                              | 918 ms: 1.04x slower                                                                                                    |
| async_tree_none          | 389 ms                                                                                                              | 406 ms: 1.04x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.24 ms                                                                                                             | 6.52 ms: 1.04x slower                                                                                                   |
| pickle_pure_python       | 385 us                                                                                                              | 403 us: 1.05x slower                                                                                                    |
| async_tree_memoization   | 495 ms                                                                                                              | 518 ms: 1.05x slower                                                                                                    |
| 2to3                     | 303 ms                                                                                                              | 319 ms: 1.05x slower                                                                                                    |
| async_generators         | 496 ms                                                                                                              | 521 ms: 1.05x slower                                                                                                    |
| sqlglot_normalize        | 132 ms                                                                                                              | 139 ms: 1.06x slower                                                                                                    |
| pylint                   | 324 ms                                                                                                              | 343 ms: 1.06x slower                                                                                                    |
| asyncio_tcp              | 569 ms                                                                                                              | 603 ms: 1.06x slower                                                                                                    |
| richards                 | 52.1 ms                                                                                                             | 55.3 ms: 1.06x slower                                                                                                   |
| async_tree_none_tg       | 367 ms                                                                                                              | 390 ms: 1.06x slower                                                                                                    |
| regex_dna                | 250 ms                                                                                                              | 266 ms: 1.06x slower                                                                                                    |
| sqlglot_parse            | 1.47 ms                                                                                                             | 1.57 ms: 1.07x slower                                                                                                   |
| deepcopy_reduce          | 3.74 us                                                                                                             | 4.00 us: 1.07x slower                                                                                                   |
| docutils                 | 3.02 sec                                                                                                            | 3.24 sec: 1.07x slower                                                                                                  |
| sphinx                   | 1.18 sec                                                                                                            | 1.27 sec: 1.07x slower                                                                                                  |
| scimark_sor              | 152 ms                                                                                                              | 164 ms: 1.08x slower                                                                                                    |
| sympy_expand             | 482 ms                                                                                                              | 518 ms: 1.08x slower                                                                                                    |
| logging_silent           | 139 ns                                                                                                              | 150 ns: 1.08x slower                                                                                                    |
| logging_format           | 8.00 us                                                                                                             | 8.63 us: 1.08x slower                                                                                                   |
| html5lib                 | 63.8 ms                                                                                                             | 68.9 ms: 1.08x slower                                                                                                   |
| sympy_integrate          | 21.6 ms                                                                                                             | 23.4 ms: 1.08x slower                                                                                                   |
| logging_simple           | 7.44 us                                                                                                             | 8.04 us: 1.08x slower                                                                                                   |
| fannkuch                 | 478 ms                                                                                                              | 517 ms: 1.08x slower                                                                                                    |
| sympy_sum                | 148 ms                                                                                                              | 160 ms: 1.09x slower                                                                                                    |
| meteor_contest           | 115 ms                                                                                                              | 125 ms: 1.09x slower                                                                                                    |
| pyflate                  | 569 ms                                                                                                              | 619 ms: 1.09x slower                                                                                                    |
| sqlglot_transpile        | 1.83 ms                                                                                                             | 2.00 ms: 1.09x slower                                                                                                   |
| scimark_lu               | 140 ms                                                                                                              | 154 ms: 1.09x slower                                                                                                    |
| sqlglot_optimize         | 62.9 ms                                                                                                             | 68.9 ms: 1.10x slower                                                                                                   |
| typing_runtime_protocols | 201 us                                                                                                              | 220 us: 1.10x slower                                                                                                    |
| sqlalchemy_declarative   | 146 ms                                                                                                              | 161 ms: 1.10x slower                                                                                                    |
| deltablue                | 3.98 ms                                                                                                             | 4.42 ms: 1.11x slower                                                                                                   |
| dulwich_log              | 62.6 ms                                                                                                             | 70.2 ms: 1.12x slower                                                                                                   |
| raytrace                 | 324 ms                                                                                                              | 366 ms: 1.13x slower                                                                                                    |
| sqlalchemy_imperative    | 15.4 ms                                                                                                             | 17.4 ms: 1.13x slower                                                                                                   |
| regex_compile            | 125 ms                                                                                                              | 141 ms: 1.13x slower                                                                                                    |
| sympy_str                | 268 ms                                                                                                              | 305 ms: 1.14x slower                                                                                                    |
| spectral_norm            | 129 ms                                                                                                              | 147 ms: 1.14x slower                                                                                                    |
| django_template          | 41.2 ms                                                                                                             | 47.0 ms: 1.14x slower                                                                                                   |
| crypto_pyaes             | 83.1 ms                                                                                                             | 95.1 ms: 1.14x slower                                                                                                   |
| pycparser                | 1.28 sec                                                                                                            | 1.46 sec: 1.15x slower                                                                                                  |
| deepcopy                 | 350 us                                                                                                              | 402 us: 1.15x slower                                                                                                    |
| comprehensions           | 21.7 us                                                                                                             | 24.9 us: 1.15x slower                                                                                                   |
| genshi_text              | 28.5 ms                                                                                                             | 33.1 ms: 1.16x slower                                                                                                   |
| go                       | 144 ms                                                                                                              | 168 ms: 1.16x slower                                                                                                    |
| chaos                    | 73.6 ms                                                                                                             | 87.0 ms: 1.18x slower                                                                                                   |
| many_optionals           | 694 us                                                                                                              | 851 us: 1.23x slower                                                                                                    |
| hexiom                   | 7.70 ms                                                                                                             | 9.47 ms: 1.23x slower                                                                                                   |
| unpack_sequence          | 58.4 ns                                                                                                             | 72.5 ns: 1.24x slower                                                                                                   |
| nqueens                  | 103 ms                                                                                                              | 129 ms: 1.25x slower                                                                                                    |
| pprint_safe_repr         | 963 ms                                                                                                              | 1.23 sec: 1.28x slower                                                                                                  |
| pprint_pformat           | 1.98 sec                                                                                                            | 2.57 sec: 1.30x slower                                                                                                  |
| genshi_xml               | 64.4 ms                                                                                                             | 83.7 ms: 1.30x slower                                                                                                   |
| generators               | 36.6 ms                                                                                                             | 50.8 ms: 1.39x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (41): pickle_list, json_loads, xml_etree_process, deepcopy_memo, telco, pidigits, scimark_monte_carlo, scimark_fft, xml_etree_generate, json_dumps, pickle_dict, unpickle, subparsers, xml_etree_parse, regex_effbot, python_startup, asyncio_websockets, xml_etree_iterparse, unpickle_list, unpickle_pure_python, bench_thread_pool, regex_v8, bpe_tokeniser, json, connected_components, python_startup_no_site, asyncio_tcp_ssl, shortest_path, pickle, async_tree_cpu_io_mixed_tg, k_core, sqlite_synth, create_gc_cycles, gc_traversal, async_tree_memoization_tg, richards_super, thrift, pathlib, coverage, float, coroutines

- Geometric mean (including insignificant results): 1.059x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.02x