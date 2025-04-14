# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.024x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                                                            | 247 ms: 1.02x faster                                                                                                    |
| docutils       | 2.58 sec                                                                                                          | 2.56 sec: 1.01x faster                                                                                                  |
| html5lib       | 59.8 ms                                                                                                           | 60.3 ms: 1.01x slower                                                                                                   |
| sphinx         | 996 ms                                                                                                            | 978 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                                                           | 21.8 ms: 1.06x faster                                                                                                   |
| async_tree_none_tg         | 256 ms                                                                                                            | 244 ms: 1.05x faster                                                                                                    |
| async_tree_none            | 266 ms                                                                                                            | 254 ms: 1.05x faster                                                                                                    |
| async_tree_memoization     | 324 ms                                                                                                            | 310 ms: 1.04x faster                                                                                                    |
| async_tree_memoization_tg  | 317 ms                                                                                                            | 310 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 614 ms                                                                                                            | 605 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                                                            | 514 ms: 1.07x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 486 ms                                                                                                            | 528 ms: 1.09x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (3): async_tree_io_tg, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                                                                           | 81.8 ms: 1.14x faster                                                                                                   |
| float          | 70.0 ms                                                                                                           | 65.4 ms: 1.07x faster                                                                                                   |
| pidigits       | 186 ms                                                                                                            | 212 ms: 1.14x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                                                            | 197 ms: 1.07x faster                                                                                                    |
| regex_effbot   | 3.30 ms                                                                                                           | 3.20 ms: 1.03x faster                                                                                                   |
| regex_v8       | 25.7 ms                                                                                                           | 25.2 ms: 1.02x faster                                                                                                   |
| regex_compile  | 125 ms                                                                                                            | 123 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pickle_pure_python   | 315 us                                                                                                            | 302 us: 1.04x faster                                                                                                    |
| tomli_loads          | 1.97 sec                                                                                                          | 1.90 sec: 1.04x faster                                                                                                  |
| unpickle_pure_python | 217 us                                                                                                            | 213 us: 1.01x faster                                                                                                    |
| xml_etree_process    | 57.9 ms                                                                                                           | 57.5 ms: 1.01x faster                                                                                                   |
| xml_etree_generate   | 82.6 ms                                                                                                           | 84.6 ms: 1.02x slower                                                                                                   |
| xml_etree_iterparse  | 96.1 ms                                                                                                           | 99.7 ms: 1.04x slower                                                                                                   |
| json_loads           | 28.9 us                                                                                                           | 30.2 us: 1.05x slower                                                                                                   |
| json_dumps           | 11.6 ms                                                                                                           | 12.2 ms: 1.05x slower                                                                                                   |
| xml_etree_parse      | 138 ms                                                                                                            | 156 ms: 1.13x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                                                           | 12.6 ms: 1.01x faster                                                                                                   |
| python_startup_no_site | 7.02 ms                                                                                                           | 6.96 ms: 1.01x faster                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 31.7 ms                                                                                                           | 30.3 ms: 1.05x faster                                                                                                   |
| genshi_text     | 21.1 ms                                                                                                           | 20.5 ms: 1.03x faster                                                                                                   |
| mako            | 11.0 ms                                                                                                           | 11.5 ms: 1.04x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.79 ms                                                                                                           | 4.02 ms: 1.19x faster                                                                                                   |
| scimark_fft                | 344 ms                                                                                                            | 292 ms: 1.18x faster                                                                                                    |
| scimark_monte_carlo        | 68.0 ms                                                                                                           | 59.4 ms: 1.14x faster                                                                                                   |
| nbody                      | 92.9 ms                                                                                                           | 81.8 ms: 1.14x faster                                                                                                   |
| spectral_norm              | 95.6 ms                                                                                                           | 84.5 ms: 1.13x faster                                                                                                   |
| logging_silent             | 103 ns                                                                                                            | 91.1 ns: 1.13x faster                                                                                                   |
| coverage                   | 89.9 ms                                                                                                           | 79.6 ms: 1.13x faster                                                                                                   |
| pathlib                    | 16.2 ms                                                                                                           | 14.6 ms: 1.11x faster                                                                                                   |
| nqueens                    | 81.6 ms                                                                                                           | 74.3 ms: 1.10x faster                                                                                                   |
| telco                      | 7.84 ms                                                                                                           | 7.21 ms: 1.09x faster                                                                                                   |
| scimark_sor                | 119 ms                                                                                                            | 110 ms: 1.08x faster                                                                                                    |
| comprehensions             | 16.3 us                                                                                                           | 15.1 us: 1.08x faster                                                                                                   |
| float                      | 70.0 ms                                                                                                           | 65.4 ms: 1.07x faster                                                                                                   |
| regex_dna                  | 210 ms                                                                                                            | 197 ms: 1.07x faster                                                                                                    |
| chaos                      | 57.8 ms                                                                                                           | 54.4 ms: 1.06x faster                                                                                                   |
| coroutines                 | 23.2 ms                                                                                                           | 21.8 ms: 1.06x faster                                                                                                   |
| pyflate                    | 428 ms                                                                                                            | 405 ms: 1.06x faster                                                                                                    |
| deepcopy_memo              | 30.2 us                                                                                                           | 28.6 us: 1.06x faster                                                                                                   |
| richards                   | 43.5 ms                                                                                                           | 41.2 ms: 1.06x faster                                                                                                   |
| typing_runtime_protocols   | 158 us                                                                                                            | 150 us: 1.05x faster                                                                                                    |
| sqlglot_parse              | 1.24 ms                                                                                                           | 1.18 ms: 1.05x faster                                                                                                   |
| deepcopy_reduce            | 2.70 us                                                                                                           | 2.56 us: 1.05x faster                                                                                                   |
| async_tree_none_tg         | 256 ms                                                                                                            | 244 ms: 1.05x faster                                                                                                    |
| raytrace                   | 270 ms                                                                                                            | 257 ms: 1.05x faster                                                                                                    |
| pycparser                  | 1.17 sec                                                                                                          | 1.11 sec: 1.05x faster                                                                                                  |
| scimark_lu                 | 115 ms                                                                                                            | 110 ms: 1.05x faster                                                                                                    |
| async_tree_none            | 266 ms                                                                                                            | 254 ms: 1.05x faster                                                                                                    |
| django_template            | 31.7 ms                                                                                                           | 30.3 ms: 1.05x faster                                                                                                   |
| richards_super             | 49.8 ms                                                                                                           | 47.6 ms: 1.05x faster                                                                                                   |
| deepcopy                   | 256 us                                                                                                            | 245 us: 1.04x faster                                                                                                    |
| async_tree_memoization     | 324 ms                                                                                                            | 310 ms: 1.04x faster                                                                                                    |
| pickle_pure_python         | 315 us                                                                                                            | 302 us: 1.04x faster                                                                                                    |
| sqlglot_transpile          | 1.54 ms                                                                                                           | 1.48 ms: 1.04x faster                                                                                                   |
| bench_thread_pool          | 859 us                                                                                                            | 826 us: 1.04x faster                                                                                                    |
| tomli_loads                | 1.97 sec                                                                                                          | 1.90 sec: 1.04x faster                                                                                                  |
| dulwich_log                | 64.3 ms                                                                                                           | 62.0 ms: 1.04x faster                                                                                                   |
| hexiom                     | 6.13 ms                                                                                                           | 5.91 ms: 1.04x faster                                                                                                   |
| deltablue                  | 3.14 ms                                                                                                           | 3.03 ms: 1.04x faster                                                                                                   |
| sympy_integrate            | 19.6 ms                                                                                                           | 18.9 ms: 1.03x faster                                                                                                   |
| sqlite_synth               | 2.76 us                                                                                                           | 2.67 us: 1.03x faster                                                                                                   |
| bpe_tokeniser              | 4.42 sec                                                                                                          | 4.28 sec: 1.03x faster                                                                                                  |
| sympy_expand               | 448 ms                                                                                                            | 435 ms: 1.03x faster                                                                                                    |
| regex_effbot               | 3.30 ms                                                                                                           | 3.20 ms: 1.03x faster                                                                                                   |
| logging_format             | 6.01 us                                                                                                           | 5.84 us: 1.03x faster                                                                                                   |
| fannkuch                   | 397 ms                                                                                                            | 386 ms: 1.03x faster                                                                                                    |
| thrift                     | 764 us                                                                                                            | 742 us: 1.03x faster                                                                                                    |
| genshi_text                | 21.1 ms                                                                                                           | 20.5 ms: 1.03x faster                                                                                                   |
| sympy_str                  | 265 ms                                                                                                            | 258 ms: 1.03x faster                                                                                                    |
| sqlalchemy_declarative     | 127 ms                                                                                                            | 124 ms: 1.03x faster                                                                                                    |
| sympy_sum                  | 146 ms                                                                                                            | 142 ms: 1.02x faster                                                                                                    |
| logging_simple             | 5.42 us                                                                                                           | 5.30 us: 1.02x faster                                                                                                   |
| sqlalchemy_imperative      | 16.2 ms                                                                                                           | 15.9 ms: 1.02x faster                                                                                                   |
| async_tree_memoization_tg  | 317 ms                                                                                                            | 310 ms: 1.02x faster                                                                                                    |
| regex_v8                   | 25.7 ms                                                                                                           | 25.2 ms: 1.02x faster                                                                                                   |
| sphinx                     | 996 ms                                                                                                            | 978 ms: 1.02x faster                                                                                                    |
| 2to3                       | 251 ms                                                                                                            | 247 ms: 1.02x faster                                                                                                    |
| go                         | 115 ms                                                                                                            | 113 ms: 1.02x faster                                                                                                    |
| bench_mp_pool              | 81.1 ms                                                                                                           | 79.7 ms: 1.02x faster                                                                                                   |
| async_tree_io              | 614 ms                                                                                                            | 605 ms: 1.01x faster                                                                                                    |
| subparsers                 | 20.2 ms                                                                                                           | 19.9 ms: 1.01x faster                                                                                                   |
| unpickle_pure_python       | 217 us                                                                                                            | 213 us: 1.01x faster                                                                                                    |
| crypto_pyaes               | 69.5 ms                                                                                                           | 68.5 ms: 1.01x faster                                                                                                   |
| python_startup             | 12.8 ms                                                                                                           | 12.6 ms: 1.01x faster                                                                                                   |
| regex_compile              | 125 ms                                                                                                            | 123 ms: 1.01x faster                                                                                                    |
| many_optionals             | 926 us                                                                                                            | 918 us: 1.01x faster                                                                                                    |
| python_startup_no_site     | 7.02 ms                                                                                                           | 6.96 ms: 1.01x faster                                                                                                   |
| docutils                   | 2.58 sec                                                                                                          | 2.56 sec: 1.01x faster                                                                                                  |
| xml_etree_process          | 57.9 ms                                                                                                           | 57.5 ms: 1.01x faster                                                                                                   |
| html5lib                   | 59.8 ms                                                                                                           | 60.3 ms: 1.01x slower                                                                                                   |
| shortest_path              | 475 ms                                                                                                            | 483 ms: 1.02x slower                                                                                                    |
| meteor_contest             | 104 ms                                                                                                            | 107 ms: 1.02x slower                                                                                                    |
| create_gc_cycles           | 2.46 ms                                                                                                           | 2.52 ms: 1.02x slower                                                                                                   |
| xml_etree_generate         | 82.6 ms                                                                                                           | 84.6 ms: 1.02x slower                                                                                                   |
| pprint_safe_repr           | 713 ms                                                                                                            | 732 ms: 1.03x slower                                                                                                    |
| gc_traversal               | 4.79 ms                                                                                                           | 4.91 ms: 1.03x slower                                                                                                   |
| pprint_pformat             | 1.45 sec                                                                                                          | 1.49 sec: 1.03x slower                                                                                                  |
| connected_components       | 437 ms                                                                                                            | 450 ms: 1.03x slower                                                                                                    |
| xml_etree_iterparse        | 96.1 ms                                                                                                           | 99.7 ms: 1.04x slower                                                                                                   |
| mako                       | 11.0 ms                                                                                                           | 11.5 ms: 1.04x slower                                                                                                   |
| json_loads                 | 28.9 us                                                                                                           | 30.2 us: 1.05x slower                                                                                                   |
| json                       | 5.14 ms                                                                                                           | 5.39 ms: 1.05x slower                                                                                                   |
| json_dumps                 | 11.6 ms                                                                                                           | 12.2 ms: 1.05x slower                                                                                                   |
| mdp                        | 2.47 sec                                                                                                          | 2.60 sec: 1.05x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                                                            | 514 ms: 1.07x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 486 ms                                                                                                            | 528 ms: 1.09x slower                                                                                                    |
| xml_etree_parse            | 138 ms                                                                                                            | 156 ms: 1.13x slower                                                                                                    |
| pidigits                   | 186 ms                                                                                                            | 212 ms: 1.14x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (9): pylint, async_tree_io_tg, genshi_xml, sqlglot_normalize, async_generators, k_core, generators, sqlglot_optimize, asyncio_websockets
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x