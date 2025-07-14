# Results vs. base

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.019x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 300 ms                                                                                                            | 313 ms: 1.04x slower                                                                                                  |
| docutils       | 2.93 sec                                                                                                          | 3.14 sec: 1.07x slower                                                                                                |
| html5lib       | 61.5 ms                                                                                                           | 64.0 ms: 1.04x slower                                                                                                 |
| sphinx         | 1.12 sec                                                                                                          | 1.16 sec: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.05x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                            | 665 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg  | 470 ms                                                                                                            | 480 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg         | 376 ms                                                                                                            | 386 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                            | 676 ms: 1.03x slower                                                                                                  |
| async_tree_io              | 872 ms                                                                                                            | 898 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.23 sec: 1.03x slower                                                                                                |
| asyncio_tcp                | 543 ms                                                                                                            | 563 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 473 ms                                                                                                            | 491 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 374 ms                                                                                                            | 389 ms: 1.04x slower                                                                                                  |
| async_generators           | 460 ms                                                                                                            | 479 ms: 1.04x slower                                                                                                  |
| async_tree_io_tg           | 883 ms                                                                                                            | 920 ms: 1.04x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 85.3 ms                                                                                                           | 82.8 ms: 1.03x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.45 sec                                                                                                          | 2.30 sec: 1.07x faster                                                                                                |
| json_dumps          | 14.2 ms                                                                                                           | 13.5 ms: 1.05x faster                                                                                                 |
| pickle_list         | 5.86 us                                                                                                           | 5.60 us: 1.05x faster                                                                                                 |
| xml_etree_generate  | 111 ms                                                                                                            | 106 ms: 1.05x faster                                                                                                  |
| xml_etree_process   | 78.8 ms                                                                                                           | 76.0 ms: 1.04x faster                                                                                                 |
| xml_etree_parse     | 181 ms                                                                                                            | 183 ms: 1.01x slower                                                                                                  |
| xml_etree_iterparse | 142 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (7): unpickle_pure_python, unpickle_list, pickle_dict, unpickle, json_loads, pickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.59 ms                                                                                                           | 8.69 ms: 1.01x slower                                                                                                 |
| python_startup         | 15.0 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.6 ms                                                                                                           | 12.9 ms: 1.06x faster                                                                                                 |
| genshi_xml     | 59.7 ms                                                                                                           | 63.6 ms: 1.07x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 2.81 sec                                                                                                          | 1.25 sec: 2.25x faster                                                                                                |
| richards_super             | 61.5 ms                                                                                                           | 51.7 ms: 1.19x faster                                                                                                 |
| richards                   | 52.2 ms                                                                                                           | 44.8 ms: 1.17x faster                                                                                                 |
| create_gc_cycles           | 4.13 ms                                                                                                           | 3.77 ms: 1.09x faster                                                                                                 |
| tomli_loads                | 2.45 sec                                                                                                          | 2.30 sec: 1.07x faster                                                                                                |
| mako                       | 13.6 ms                                                                                                           | 12.9 ms: 1.06x faster                                                                                                 |
| gc_traversal               | 7.17 ms                                                                                                           | 6.82 ms: 1.05x faster                                                                                                 |
| json_dumps                 | 14.2 ms                                                                                                           | 13.5 ms: 1.05x faster                                                                                                 |
| pickle_list                | 5.86 us                                                                                                           | 5.60 us: 1.05x faster                                                                                                 |
| xml_etree_generate         | 111 ms                                                                                                            | 106 ms: 1.05x faster                                                                                                  |
| scimark_fft                | 427 ms                                                                                                            | 410 ms: 1.04x faster                                                                                                  |
| sqlite_synth               | 3.80 us                                                                                                           | 3.66 us: 1.04x faster                                                                                                 |
| xml_etree_process          | 78.8 ms                                                                                                           | 76.0 ms: 1.04x faster                                                                                                 |
| float                      | 85.3 ms                                                                                                           | 82.8 ms: 1.03x faster                                                                                                 |
| connected_components       | 574 ms                                                                                                            | 562 ms: 1.02x faster                                                                                                  |
| bpe_tokeniser              | 5.52 sec                                                                                                          | 5.41 sec: 1.02x faster                                                                                                |
| deepcopy                   | 321 us                                                                                                            | 324 us: 1.01x slower                                                                                                  |
| logging_format             | 7.65 us                                                                                                           | 7.72 us: 1.01x slower                                                                                                 |
| xml_etree_parse            | 181 ms                                                                                                            | 183 ms: 1.01x slower                                                                                                  |
| bench_thread_pool          | 1.36 ms                                                                                                           | 1.38 ms: 1.01x slower                                                                                                 |
| python_startup_no_site     | 8.59 ms                                                                                                           | 8.69 ms: 1.01x slower                                                                                                 |
| python_startup             | 15.0 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| xml_etree_iterparse        | 142 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| thrift                     | 946 us                                                                                                            | 958 us: 1.01x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.90 ms                                                                                                           | 7.00 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_normalize       | 125 ms                                                                                                            | 127 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                            | 665 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg  | 470 ms                                                                                                            | 480 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg         | 376 ms                                                                                                            | 386 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                            | 676 ms: 1.03x slower                                                                                                  |
| sqlglot_v2_optimize        | 60.7 ms                                                                                                           | 62.5 ms: 1.03x slower                                                                                                 |
| async_tree_io              | 872 ms                                                                                                            | 898 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.23 sec: 1.03x slower                                                                                                |
| raytrace                   | 326 ms                                                                                                            | 336 ms: 1.03x slower                                                                                                  |
| scimark_lu                 | 146 ms                                                                                                            | 151 ms: 1.03x slower                                                                                                  |
| asyncio_tcp                | 543 ms                                                                                                            | 563 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 473 ms                                                                                                            | 491 ms: 1.04x slower                                                                                                  |
| sphinx                     | 1.12 sec                                                                                                          | 1.16 sec: 1.04x slower                                                                                                |
| async_tree_none            | 374 ms                                                                                                            | 389 ms: 1.04x slower                                                                                                  |
| html5lib                   | 61.5 ms                                                                                                           | 64.0 ms: 1.04x slower                                                                                                 |
| nqueens                    | 97.1 ms                                                                                                           | 101 ms: 1.04x slower                                                                                                  |
| async_generators           | 460 ms                                                                                                            | 479 ms: 1.04x slower                                                                                                  |
| async_tree_io_tg           | 883 ms                                                                                                            | 920 ms: 1.04x slower                                                                                                  |
| 2to3                       | 300 ms                                                                                                            | 313 ms: 1.04x slower                                                                                                  |
| subparsers                 | 27.8 ms                                                                                                           | 29.2 ms: 1.05x slower                                                                                                 |
| pyflate                    | 522 ms                                                                                                            | 550 ms: 1.05x slower                                                                                                  |
| meteor_contest             | 108 ms                                                                                                            | 114 ms: 1.06x slower                                                                                                  |
| crypto_pyaes               | 84.6 ms                                                                                                           | 89.5 ms: 1.06x slower                                                                                                 |
| genshi_xml                 | 59.7 ms                                                                                                           | 63.6 ms: 1.07x slower                                                                                                 |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                           | 1.88 ms: 1.07x slower                                                                                                 |
| docutils                   | 2.93 sec                                                                                                          | 3.14 sec: 1.07x slower                                                                                                |
| sympy_expand               | 460 ms                                                                                                            | 495 ms: 1.07x slower                                                                                                  |
| comprehensions             | 20.0 us                                                                                                           | 21.7 us: 1.08x slower                                                                                                 |
| pycparser                  | 1.26 sec                                                                                                          | 1.37 sec: 1.09x slower                                                                                                |
| sympy_sum                  | 141 ms                                                                                                            | 153 ms: 1.09x slower                                                                                                  |
| typing_runtime_protocols   | 193 us                                                                                                            | 213 us: 1.10x slower                                                                                                  |
| hexiom                     | 6.79 ms                                                                                                           | 7.48 ms: 1.10x slower                                                                                                 |
| sqlglot_v2_parse           | 1.43 ms                                                                                                           | 1.57 ms: 1.10x slower                                                                                                 |
| many_optionals             | 745 us                                                                                                            | 824 us: 1.10x slower                                                                                                  |
| go                         | 127 ms                                                                                                            | 155 ms: 1.23x slower                                                                                                  |
| pprint_pformat             | 1.82 sec                                                                                                          | 2.35 sec: 1.30x slower                                                                                                |
| unpack_sequence            | 52.2 ns                                                                                                           | 70.0 ns: 1.34x slower                                                                                                 |
| pprint_safe_repr           | 884 ms                                                                                                            | 1.20 sec: 1.36x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (40): regex_v8, django_template, unpickle_pure_python, unpickle_list, logging_simple, coroutines, scimark_sor, deltablue, pickle_dict, k_core, unpickle, pathlib, asyncio_websockets, telco, fannkuch, shortest_path, mdp, coverage, djangocms, json, pidigits, regex_dna, generators, json_loads, regex_effbot, dulwich_log, pylint, sympy_str, deepcopy_reduce, genshi_text, regex_compile, spectral_norm, pickle, scimark_monte_carlo, logging_silent, pickle_pure_python, chaos, sympy_integrate, deepcopy_memo, nbody

- Geometric mean (including insignificant results): 1.019x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x