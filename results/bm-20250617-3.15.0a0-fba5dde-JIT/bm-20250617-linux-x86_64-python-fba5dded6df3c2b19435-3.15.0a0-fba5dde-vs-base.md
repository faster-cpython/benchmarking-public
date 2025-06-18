# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.008x faster
- HPT reliability: 92.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                                                          | 299 ms: 1.03x slower                                                                                                |
| docutils       | 2.85 sec                                                                                                        | 2.93 sec: 1.03x slower                                                                                              |
| html5lib       | 64.8 ms                                                                                                         | 66.7 ms: 1.03x slower                                                                                               |
| sphinx         | 1.13 sec                                                                                                        | 1.14 sec: 1.02x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 593 ms                                                                                                          | 586 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed    | 602 ms                                                                                                          | 597 ms: 1.01x faster                                                                                                |
| asyncio_tcp_ssl            | 1.81 sec                                                                                                        | 1.82 sec: 1.01x slower                                                                                              |
| async_tree_none_tg         | 276 ms                                                                                                          | 278 ms: 1.01x slower                                                                                                |
| asyncio_tcp                | 488 ms                                                                                                          | 496 ms: 1.02x slower                                                                                                |
| async_tree_memoization_tg  | 346 ms                                                                                                          | 353 ms: 1.02x slower                                                                                                |
| async_tree_io_tg           | 676 ms                                                                                                          | 691 ms: 1.02x slower                                                                                                |
| coroutines                 | 26.8 ms                                                                                                         | 27.6 ms: 1.03x slower                                                                                               |
| async_generators           | 413 ms                                                                                                          | 438 ms: 1.06x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (4): async_tree_io, asyncio_websockets, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 106 ms                                                                                                          | 97.8 ms: 1.09x faster                                                                                               |
| float          | 75.3 ms                                                                                                         | 69.8 ms: 1.08x faster                                                                                               |
| pidigits       | 205 ms                                                                                                          | 207 ms: 1.01x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 197 ms                                                                                                          | 198 ms: 1.01x slower                                                                                                |
| regex_compile  | 144 ms                                                                                                          | 145 ms: 1.01x slower                                                                                                |
| regex_v8       | 24.2 ms                                                                                                         | 24.7 ms: 1.02x slower                                                                                               |
| regex_effbot   | 2.93 ms                                                                                                         | 3.06 ms: 1.04x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 259 us                                                                                                          | 234 us: 1.11x faster                                                                                                |
| xml_etree_process    | 74.4 ms                                                                                                         | 68.6 ms: 1.08x faster                                                                                               |
| xml_etree_generate   | 108 ms                                                                                                          | 101 ms: 1.07x faster                                                                                                |
| tomli_loads          | 2.22 sec                                                                                                        | 2.08 sec: 1.07x faster                                                                                              |
| pickle_list          | 6.06 us                                                                                                         | 5.90 us: 1.03x faster                                                                                               |
| xml_etree_parse      | 162 ms                                                                                                          | 159 ms: 1.02x faster                                                                                                |
| pickle               | 15.1 us                                                                                                         | 14.9 us: 1.02x faster                                                                                               |
| json_loads           | 34.0 us                                                                                                         | 33.5 us: 1.01x faster                                                                                               |
| unpickle             | 19.1 us                                                                                                         | 18.8 us: 1.01x faster                                                                                               |
| pickle_dict          | 38.2 us                                                                                                         | 38.0 us: 1.01x faster                                                                                               |
| pickle_pure_python   | 374 us                                                                                                          | 378 us: 1.01x slower                                                                                                |
| json_dumps           | 13.4 ms                                                                                                         | 13.6 ms: 1.01x slower                                                                                               |
| unpickle_list        | 5.68 us                                                                                                         | 5.93 us: 1.04x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                         | 13.2 ms: 1.00x faster                                                                                               |
| python_startup_no_site | 7.40 ms                                                                                                         | 7.40 ms: 1.00x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.6 ms                                                                                                         | 13.3 ms: 1.02x faster                                                                                               |
| genshi_xml     | 57.2 ms                                                                                                         | 58.7 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| richards                   | 54.3 ms                                                                                                         | 39.1 ms: 1.39x faster                                                                                               |
| richards_super             | 62.2 ms                                                                                                         | 45.9 ms: 1.36x faster                                                                                               |
| scimark_fft                | 403 ms                                                                                                          | 341 ms: 1.18x faster                                                                                                |
| deltablue                  | 3.86 ms                                                                                                         | 3.44 ms: 1.12x faster                                                                                               |
| unpickle_pure_python       | 259 us                                                                                                          | 234 us: 1.11x faster                                                                                                |
| spectral_norm              | 113 ms                                                                                                          | 104 ms: 1.09x faster                                                                                                |
| nbody                      | 106 ms                                                                                                          | 97.8 ms: 1.09x faster                                                                                               |
| xml_etree_process          | 74.4 ms                                                                                                         | 68.6 ms: 1.08x faster                                                                                               |
| float                      | 75.3 ms                                                                                                         | 69.8 ms: 1.08x faster                                                                                               |
| xml_etree_generate         | 108 ms                                                                                                          | 101 ms: 1.07x faster                                                                                                |
| tomli_loads                | 2.22 sec                                                                                                        | 2.08 sec: 1.07x faster                                                                                              |
| sqlite_synth               | 3.18 us                                                                                                         | 3.05 us: 1.04x faster                                                                                               |
| connected_components       | 490 ms                                                                                                          | 470 ms: 1.04x faster                                                                                                |
| scimark_sparse_mat_mult    | 5.61 ms                                                                                                         | 5.38 ms: 1.04x faster                                                                                               |
| bpe_tokeniser              | 5.32 sec                                                                                                        | 5.11 sec: 1.04x faster                                                                                              |
| shortest_path              | 532 ms                                                                                                          | 511 ms: 1.04x faster                                                                                                |
| scimark_monte_carlo        | 76.4 ms                                                                                                         | 73.5 ms: 1.04x faster                                                                                               |
| fannkuch                   | 479 ms                                                                                                          | 465 ms: 1.03x faster                                                                                                |
| pickle_list                | 6.06 us                                                                                                         | 5.90 us: 1.03x faster                                                                                               |
| mako                       | 13.6 ms                                                                                                         | 13.3 ms: 1.02x faster                                                                                               |
| xml_etree_parse            | 162 ms                                                                                                          | 159 ms: 1.02x faster                                                                                                |
| pickle                     | 15.1 us                                                                                                         | 14.9 us: 1.02x faster                                                                                               |
| pyflate                    | 465 ms                                                                                                          | 458 ms: 1.02x faster                                                                                                |
| json_loads                 | 34.0 us                                                                                                         | 33.5 us: 1.01x faster                                                                                               |
| unpickle                   | 19.1 us                                                                                                         | 18.8 us: 1.01x faster                                                                                               |
| pathlib                    | 18.4 ms                                                                                                         | 18.2 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed_tg | 593 ms                                                                                                          | 586 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed    | 602 ms                                                                                                          | 597 ms: 1.01x faster                                                                                                |
| meteor_contest             | 116 ms                                                                                                          | 116 ms: 1.01x faster                                                                                                |
| pickle_dict                | 38.2 us                                                                                                         | 38.0 us: 1.01x faster                                                                                               |
| python_startup             | 13.2 ms                                                                                                         | 13.2 ms: 1.00x faster                                                                                               |
| python_startup_no_site     | 7.40 ms                                                                                                         | 7.40 ms: 1.00x slower                                                                                               |
| raytrace                   | 320 ms                                                                                                          | 321 ms: 1.00x slower                                                                                                |
| create_gc_cycles           | 2.63 ms                                                                                                         | 2.64 ms: 1.00x slower                                                                                               |
| thrift                     | 956 us                                                                                                          | 961 us: 1.00x slower                                                                                                |
| asyncio_tcp_ssl            | 1.81 sec                                                                                                        | 1.82 sec: 1.01x slower                                                                                              |
| regex_dna                  | 197 ms                                                                                                          | 198 ms: 1.01x slower                                                                                                |
| async_tree_none_tg         | 276 ms                                                                                                          | 278 ms: 1.01x slower                                                                                                |
| bench_thread_pool          | 958 us                                                                                                          | 966 us: 1.01x slower                                                                                                |
| deepcopy                   | 315 us                                                                                                          | 318 us: 1.01x slower                                                                                                |
| gc_traversal               | 5.14 ms                                                                                                         | 5.19 ms: 1.01x slower                                                                                               |
| pickle_pure_python         | 374 us                                                                                                          | 378 us: 1.01x slower                                                                                                |
| regex_compile              | 144 ms                                                                                                          | 145 ms: 1.01x slower                                                                                                |
| json_dumps                 | 13.4 ms                                                                                                         | 13.6 ms: 1.01x slower                                                                                               |
| pidigits                   | 205 ms                                                                                                          | 207 ms: 1.01x slower                                                                                                |
| mdp                        | 1.47 sec                                                                                                        | 1.49 sec: 1.01x slower                                                                                              |
| sphinx                     | 1.13 sec                                                                                                        | 1.14 sec: 1.02x slower                                                                                              |
| chaos                      | 68.8 ms                                                                                                         | 69.9 ms: 1.02x slower                                                                                               |
| scimark_sor                | 134 ms                                                                                                          | 136 ms: 1.02x slower                                                                                                |
| pycparser                  | 1.26 sec                                                                                                        | 1.28 sec: 1.02x slower                                                                                              |
| asyncio_tcp                | 488 ms                                                                                                          | 496 ms: 1.02x slower                                                                                                |
| logging_silent             | 623 ns                                                                                                          | 633 ns: 1.02x slower                                                                                                |
| sqlglot_v2_transpile       | 1.76 ms                                                                                                         | 1.80 ms: 1.02x slower                                                                                               |
| logging_format             | 8.43 us                                                                                                         | 8.58 us: 1.02x slower                                                                                               |
| sympy_expand               | 541 ms                                                                                                          | 552 ms: 1.02x slower                                                                                                |
| async_tree_memoization_tg  | 346 ms                                                                                                          | 353 ms: 1.02x slower                                                                                                |
| sympy_sum                  | 166 ms                                                                                                          | 170 ms: 1.02x slower                                                                                                |
| subparsers                 | 28.1 ms                                                                                                         | 28.7 ms: 1.02x slower                                                                                               |
| deepcopy_reduce            | 3.32 us                                                                                                         | 3.39 us: 1.02x slower                                                                                               |
| async_tree_io_tg           | 676 ms                                                                                                          | 691 ms: 1.02x slower                                                                                                |
| regex_v8                   | 24.2 ms                                                                                                         | 24.7 ms: 1.02x slower                                                                                               |
| sqlglot_v2_parse           | 1.41 ms                                                                                                         | 1.44 ms: 1.02x slower                                                                                               |
| 2to3                       | 292 ms                                                                                                          | 299 ms: 1.03x slower                                                                                                |
| docutils                   | 2.85 sec                                                                                                        | 2.93 sec: 1.03x slower                                                                                              |
| genshi_xml                 | 57.2 ms                                                                                                         | 58.7 ms: 1.03x slower                                                                                               |
| logging_simple             | 7.47 us                                                                                                         | 7.66 us: 1.03x slower                                                                                               |
| scimark_lu                 | 133 ms                                                                                                          | 136 ms: 1.03x slower                                                                                                |
| dulwich_log                | 63.8 ms                                                                                                         | 65.5 ms: 1.03x slower                                                                                               |
| deepcopy_memo              | 34.1 us                                                                                                         | 35.1 us: 1.03x slower                                                                                               |
| coroutines                 | 26.8 ms                                                                                                         | 27.6 ms: 1.03x slower                                                                                               |
| html5lib                   | 64.8 ms                                                                                                         | 66.7 ms: 1.03x slower                                                                                               |
| sympy_str                  | 308 ms                                                                                                          | 317 ms: 1.03x slower                                                                                                |
| many_optionals             | 1.08 ms                                                                                                         | 1.11 ms: 1.03x slower                                                                                               |
| sympy_integrate            | 20.9 ms                                                                                                         | 21.6 ms: 1.03x slower                                                                                               |
| typing_runtime_protocols   | 198 us                                                                                                          | 205 us: 1.04x slower                                                                                                |
| comprehensions             | 19.3 us                                                                                                         | 20.0 us: 1.04x slower                                                                                               |
| nqueens                    | 98.2 ms                                                                                                         | 102 ms: 1.04x slower                                                                                                |
| pprint_safe_repr           | 993 ms                                                                                                          | 1.03 sec: 1.04x slower                                                                                              |
| unpickle_list              | 5.68 us                                                                                                         | 5.93 us: 1.04x slower                                                                                               |
| hexiom                     | 6.65 ms                                                                                                         | 6.94 ms: 1.04x slower                                                                                               |
| regex_effbot               | 2.93 ms                                                                                                         | 3.06 ms: 1.04x slower                                                                                               |
| pprint_pformat             | 2.01 sec                                                                                                        | 2.10 sec: 1.05x slower                                                                                              |
| async_generators           | 413 ms                                                                                                          | 438 ms: 1.06x slower                                                                                                |
| generators                 | 33.0 ms                                                                                                         | 35.4 ms: 1.07x slower                                                                                               |
| go                         | 119 ms                                                                                                          | 129 ms: 1.08x slower                                                                                                |
| unpack_sequence            | 53.0 ns                                                                                                         | 76.8 ns: 1.45x slower                                                                                               |
| Geometric mean             | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (17): xml_etree_iterparse, bench_mp_pool, sqlglot_v2_optimize, sqlglot_v2_normalize, async_tree_io, asyncio_websockets, json, k_core, genshi_text, django_template, crypto_pyaes, async_tree_none, async_tree_memoization, telco, coverage, pylint, djangocms

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 92.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x