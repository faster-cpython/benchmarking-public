# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.016x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 294 ms: 1.04x faster                                                                                                      |
| html5lib       | 62.9 ms                                                                                                             | 59.3 ms: 1.06x faster                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.13 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 454 ms                                                                                                              | 419 ms: 1.08x faster                                                                                                      |
| async_tree_memoization     | 503 ms                                                                                                              | 480 ms: 1.05x faster                                                                                                      |
| async_tree_memoization_tg  | 493 ms                                                                                                              | 472 ms: 1.04x faster                                                                                                      |
| async_tree_none_tg         | 392 ms                                                                                                              | 376 ms: 1.04x faster                                                                                                      |
| async_tree_none            | 403 ms                                                                                                              | 387 ms: 1.04x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 680 ms                                                                                                              | 739 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 691 ms                                                                                                              | 758 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_io, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 120 ms                                                                                                              | 114 ms: 1.05x faster                                                                                                      |
| pidigits       | 244 ms                                                                                                              | 303 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                                                              | 120 ms: 1.05x faster                                                                                                      |
| regex_dna      | 260 ms                                                                                                              | 250 ms: 1.04x faster                                                                                                      |
| regex_v8       | 32.3 ms                                                                                                             | 34.5 ms: 1.07x slower                                                                                                     |
| regex_effbot   | 4.14 ms                                                                                                             | 4.62 ms: 1.12x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                                                                              | 103 ms: 1.11x faster                                                                                                      |
| xml_etree_process    | 82.5 ms                                                                                                             | 74.6 ms: 1.11x faster                                                                                                     |
| unpickle_pure_python | 266 us                                                                                                              | 252 us: 1.05x faster                                                                                                      |
| tomli_loads          | 2.53 sec                                                                                                            | 2.46 sec: 1.03x faster                                                                                                    |
| xml_etree_parse      | 185 ms                                                                                                              | 209 ms: 1.13x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 64.4 ms                                                                                                             | 58.8 ms: 1.09x faster                                                                                                     |
| genshi_text    | 27.4 ms                                                                                                             | 25.7 ms: 1.07x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| scimark_fft                | 434 ms                                                                                                              | 375 ms: 1.16x faster                                                                                                      |
| logging_silent             | 136 ns                                                                                                              | 118 ns: 1.16x faster                                                                                                      |
| deepcopy_memo              | 40.6 us                                                                                                             | 35.4 us: 1.15x faster                                                                                                     |
| scimark_monte_carlo        | 86.5 ms                                                                                                             | 77.1 ms: 1.12x faster                                                                                                     |
| xml_etree_generate         | 114 ms                                                                                                              | 103 ms: 1.11x faster                                                                                                      |
| xml_etree_process          | 82.5 ms                                                                                                             | 74.6 ms: 1.11x faster                                                                                                     |
| comprehensions             | 21.5 us                                                                                                             | 19.4 us: 1.10x faster                                                                                                     |
| coverage                   | 104 ms                                                                                                              | 94.4 ms: 1.10x faster                                                                                                     |
| deepcopy_reduce            | 3.72 us                                                                                                             | 3.39 us: 1.10x faster                                                                                                     |
| logging_format             | 8.09 us                                                                                                             | 7.37 us: 1.10x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.38 ms                                                                                                             | 5.83 ms: 1.10x faster                                                                                                     |
| genshi_xml                 | 64.4 ms                                                                                                             | 58.8 ms: 1.09x faster                                                                                                     |
| spectral_norm              | 119 ms                                                                                                              | 109 ms: 1.09x faster                                                                                                      |
| async_generators           | 454 ms                                                                                                              | 419 ms: 1.08x faster                                                                                                      |
| richards_super             | 60.3 ms                                                                                                             | 55.7 ms: 1.08x faster                                                                                                     |
| typing_runtime_protocols   | 196 us                                                                                                              | 181 us: 1.08x faster                                                                                                      |
| deepcopy                   | 339 us                                                                                                              | 316 us: 1.07x faster                                                                                                      |
| logging_simple             | 7.29 us                                                                                                             | 6.81 us: 1.07x faster                                                                                                     |
| genshi_text                | 27.4 ms                                                                                                             | 25.7 ms: 1.07x faster                                                                                                     |
| richards                   | 52.8 ms                                                                                                             | 49.6 ms: 1.06x faster                                                                                                     |
| html5lib                   | 62.9 ms                                                                                                             | 59.3 ms: 1.06x faster                                                                                                     |
| unpickle_pure_python       | 266 us                                                                                                              | 252 us: 1.05x faster                                                                                                      |
| regex_compile              | 127 ms                                                                                                              | 120 ms: 1.05x faster                                                                                                      |
| nbody                      | 120 ms                                                                                                              | 114 ms: 1.05x faster                                                                                                      |
| bench_thread_pool          | 1.33 ms                                                                                                             | 1.26 ms: 1.05x faster                                                                                                     |
| go                         | 140 ms                                                                                                              | 133 ms: 1.05x faster                                                                                                      |
| async_tree_memoization     | 503 ms                                                                                                              | 480 ms: 1.05x faster                                                                                                      |
| bpe_tokeniser              | 5.58 sec                                                                                                            | 5.33 sec: 1.05x faster                                                                                                    |
| 2to3                       | 307 ms                                                                                                              | 294 ms: 1.04x faster                                                                                                      |
| async_tree_memoization_tg  | 493 ms                                                                                                              | 472 ms: 1.04x faster                                                                                                      |
| async_tree_none_tg         | 392 ms                                                                                                              | 376 ms: 1.04x faster                                                                                                      |
| async_tree_none            | 403 ms                                                                                                              | 387 ms: 1.04x faster                                                                                                      |
| pprint_pformat             | 1.97 sec                                                                                                            | 1.89 sec: 1.04x faster                                                                                                    |
| regex_dna                  | 260 ms                                                                                                              | 250 ms: 1.04x faster                                                                                                      |
| mdp                        | 3.35 sec                                                                                                            | 3.23 sec: 1.04x faster                                                                                                    |
| pyflate                    | 552 ms                                                                                                              | 532 ms: 1.04x faster                                                                                                      |
| sphinx                     | 1.16 sec                                                                                                            | 1.13 sec: 1.03x faster                                                                                                    |
| tomli_loads                | 2.53 sec                                                                                                            | 2.46 sec: 1.03x faster                                                                                                    |
| regex_v8                   | 32.3 ms                                                                                                             | 34.5 ms: 1.07x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 680 ms                                                                                                              | 739 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 691 ms                                                                                                              | 758 ms: 1.10x slower                                                                                                      |
| regex_effbot               | 4.14 ms                                                                                                             | 4.62 ms: 1.12x slower                                                                                                     |
| xml_etree_parse            | 185 ms                                                                                                              | 209 ms: 1.13x slower                                                                                                      |
| pidigits                   | 244 ms                                                                                                              | 303 ms: 1.24x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (52): sqlglot_transpile, scimark_sor, sqlglot_normalize, xml_etree_iterparse, sqlglot_parse, float, thrift, many_optionals, sympy_sum, raytrace, hexiom, pathlib, sympy_integrate, pickle_pure_python, chaos, async_tree_io_tg, gc_traversal, nqueens, scimark_lu, dulwich_log, async_tree_io, shortest_path, deltablue, k_core, coroutines, pycparser, json_dumps, sympy_expand, pprint_safe_repr, sqlite_synth, sqlglot_optimize, docutils, sqlalchemy_imperative, mako, django_template, json, python_startup, subparsers, connected_components, generators, pylint, asyncio_websockets, telco, fannkuch, meteor_contest, sqlalchemy_declarative, sympy_str, crypto_pyaes, python_startup_no_site, create_gc_cycles, json_loads, bench_mp_pool
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x