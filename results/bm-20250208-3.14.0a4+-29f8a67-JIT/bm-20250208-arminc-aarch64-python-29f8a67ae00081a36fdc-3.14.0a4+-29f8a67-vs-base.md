# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| docutils       | 3.01 sec                                                                                                            | 3.27 sec: 1.09x slower                                                                                                  |
| sphinx         | 1.16 sec                                                                                                            | 1.20 sec: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg | 928 ms                                                                                                              | 955 ms: 1.03x slower                                                                                                    |
| async_tree_io    | 926 ms                                                                                                              | 958 ms: 1.03x slower                                                                                                    |
| asyncio_tcp      | 548 ms                                                                                                              | 569 ms: 1.04x slower                                                                                                    |
| async_generators | 454 ms                                                                                                              | 483 ms: 1.06x slower                                                                                                    |
| Geometric mean   | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, async_tree_none, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 120 ms                                                                                                              | 129 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 260 ms                                                                                                              | 250 ms: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                                                                              | 147 ms: 1.08x faster                                                                                                    |
| unpickle_pure_python | 266 us                                                                                                              | 273 us: 1.03x slower                                                                                                    |
| pickle_dict          | 38.8 us                                                                                                             | 41.0 us: 1.05x slower                                                                                                   |
| pickle_pure_python   | 390 us                                                                                                              | 415 us: 1.06x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.00x slower                                                                                                            |

Benchmark hidden because not significant (10): xml_etree_generate, xml_etree_process, xml_etree_parse, json_dumps, unpickle_list, pickle, tomli_loads, unpickle, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.97 sec                                                                                                            | 2.46 sec: 2.43x faster                                                                                                  |
| xml_etree_iterparse      | 159 ms                                                                                                              | 147 ms: 1.08x faster                                                                                                    |
| regex_dna                | 260 ms                                                                                                              | 250 ms: 1.04x faster                                                                                                    |
| scimark_lu               | 142 ms                                                                                                              | 138 ms: 1.03x faster                                                                                                    |
| k_core                   | 2.85 sec                                                                                                            | 2.92 sec: 1.02x slower                                                                                                  |
| bpe_tokeniser            | 5.58 sec                                                                                                            | 5.73 sec: 1.03x slower                                                                                                  |
| sphinx                   | 1.16 sec                                                                                                            | 1.20 sec: 1.03x slower                                                                                                  |
| unpickle_pure_python     | 266 us                                                                                                              | 273 us: 1.03x slower                                                                                                    |
| async_tree_io_tg         | 928 ms                                                                                                              | 955 ms: 1.03x slower                                                                                                    |
| shortest_path            | 572 ms                                                                                                              | 589 ms: 1.03x slower                                                                                                    |
| async_tree_io            | 926 ms                                                                                                              | 958 ms: 1.03x slower                                                                                                    |
| raytrace                 | 323 ms                                                                                                              | 335 ms: 1.04x slower                                                                                                    |
| asyncio_tcp              | 548 ms                                                                                                              | 569 ms: 1.04x slower                                                                                                    |
| pickle_dict              | 38.8 us                                                                                                             | 41.0 us: 1.05x slower                                                                                                   |
| mdp                      | 3.35 sec                                                                                                            | 3.55 sec: 1.06x slower                                                                                                  |
| pickle_pure_python       | 390 us                                                                                                              | 415 us: 1.06x slower                                                                                                    |
| async_generators         | 454 ms                                                                                                              | 483 ms: 1.06x slower                                                                                                    |
| pyflate                  | 552 ms                                                                                                              | 587 ms: 1.06x slower                                                                                                    |
| sqlalchemy_declarative   | 145 ms                                                                                                              | 155 ms: 1.06x slower                                                                                                    |
| nbody                    | 120 ms                                                                                                              | 129 ms: 1.08x slower                                                                                                    |
| sqlglot_optimize         | 60.8 ms                                                                                                             | 66.0 ms: 1.08x slower                                                                                                   |
| docutils                 | 3.01 sec                                                                                                            | 3.27 sec: 1.09x slower                                                                                                  |
| deltablue                | 3.93 ms                                                                                                             | 4.27 ms: 1.09x slower                                                                                                   |
| sympy_expand             | 462 ms                                                                                                              | 503 ms: 1.09x slower                                                                                                    |
| pylint                   | 304 ms                                                                                                              | 333 ms: 1.10x slower                                                                                                    |
| typing_runtime_protocols | 196 us                                                                                                              | 215 us: 1.10x slower                                                                                                    |
| sympy_sum                | 144 ms                                                                                                              | 158 ms: 1.10x slower                                                                                                    |
| crypto_pyaes             | 86.6 ms                                                                                                             | 95.2 ms: 1.10x slower                                                                                                   |
| sqlglot_parse            | 1.41 ms                                                                                                             | 1.55 ms: 1.10x slower                                                                                                   |
| sympy_str                | 261 ms                                                                                                              | 288 ms: 1.10x slower                                                                                                    |
| meteor_contest           | 114 ms                                                                                                              | 126 ms: 1.10x slower                                                                                                    |
| sqlalchemy_imperative    | 15.4 ms                                                                                                             | 17.1 ms: 1.12x slower                                                                                                   |
| fannkuch                 | 486 ms                                                                                                              | 543 ms: 1.12x slower                                                                                                    |
| pycparser                | 1.28 sec                                                                                                            | 1.44 sec: 1.13x slower                                                                                                  |
| dulwich_log              | 59.9 ms                                                                                                             | 68.4 ms: 1.14x slower                                                                                                   |
| comprehensions           | 21.5 us                                                                                                             | 24.6 us: 1.14x slower                                                                                                   |
| go                       | 140 ms                                                                                                              | 167 ms: 1.20x slower                                                                                                    |
| hexiom                   | 7.46 ms                                                                                                             | 9.10 ms: 1.22x slower                                                                                                   |
| nqueens                  | 101 ms                                                                                                              | 126 ms: 1.25x slower                                                                                                    |
| pprint_pformat           | 1.97 sec                                                                                                            | 2.70 sec: 1.37x slower                                                                                                  |
| pprint_safe_repr         | 953 ms                                                                                                              | 1.31 sec: 1.38x slower                                                                                                  |
| Geometric mean           | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (63): coverage, deepcopy_reduce, gc_traversal, sqlite_synth, thrift, float, xml_etree_generate, scimark_fft, unpack_sequence, xml_etree_process, logging_silent, scimark_monte_carlo, regex_effbot, logging_format, create_gc_cycles, xml_etree_parse, deepcopy_memo, json_dumps, mako, pidigits, regex_v8, unpickle_list, asyncio_tcp_ssl, pickle, scimark_sor, python_startup, python_startup_no_site, async_tree_none, tomli_loads, spectral_norm, asyncio_websockets, coroutines, logging_simple, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, unpickle, async_tree_cpu_io_mixed, generators, genshi_xml, async_tree_none_tg, json, json_loads, django_template, html5lib, chaos, connected_components, richards, sqlglot_normalize, richards_super, pathlib, 2to3, many_optionals, deepcopy, sympy_integrate, regex_compile, pickle_list, sqlglot_transpile, bench_thread_pool, genshi_text, telco, scimark_sparse_mat_mult, subparsers

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x