# Results vs. base

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: linux-aarch64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.002x faster
- HPT reliability: 90.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 458 ms                                                                                                            | 417 ms: 1.10x faster                                                                                                    |
| async_tree_memoization_tg  | 465 ms                                                                                                            | 450 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 374 ms                                                                                                            | 364 ms: 1.03x faster                                                                                                    |
| async_tree_none            | 397 ms                                                                                                            | 386 ms: 1.03x faster                                                                                                    |
| async_tree_memoization     | 467 ms                                                                                                            | 457 ms: 1.02x faster                                                                                                    |
| async_tree_io_tg           | 907 ms                                                                                                            | 893 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 876 ms                                                                                                            | 867 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 668 ms                                                                                                            | 723 ms: 1.08x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                            | 713 ms: 1.10x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 121 ms                                                                                                            | 129 ms: 1.06x slower                                                                                                    |
| pidigits       | 237 ms                                                                                                            | 293 ms: 1.24x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                                                            | 240 ms: 1.05x slower                                                                                                    |
| regex_v8       | 28.1 ms                                                                                                           | 31.8 ms: 1.13x slower                                                                                                   |
| regex_effbot   | 3.70 ms                                                                                                           | 4.58 ms: 1.24x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.83 us                                                                                                           | 5.90 us: 1.16x faster                                                                                                   |
| json_dumps           | 14.4 ms                                                                                                           | 13.2 ms: 1.09x faster                                                                                                   |
| pickle_dict          | 39.3 us                                                                                                           | 36.9 us: 1.06x faster                                                                                                   |
| xml_etree_generate   | 114 ms                                                                                                            | 107 ms: 1.06x faster                                                                                                    |
| unpickle             | 18.7 us                                                                                                           | 17.6 us: 1.06x faster                                                                                                   |
| xml_etree_process    | 79.9 ms                                                                                                           | 76.1 ms: 1.05x faster                                                                                                   |
| unpickle_pure_python | 261 us                                                                                                            | 249 us: 1.04x faster                                                                                                    |
| json_loads           | 35.7 us                                                                                                           | 34.4 us: 1.04x faster                                                                                                   |
| tomli_loads          | 2.45 sec                                                                                                          | 2.37 sec: 1.03x faster                                                                                                  |
| xml_etree_iterparse  | 143 ms                                                                                                            | 149 ms: 1.04x slower                                                                                                    |
| xml_etree_parse      | 182 ms                                                                                                            | 209 ms: 1.15x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (3): pickle_list, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                   |
| python_startup_no_site | 8.67 ms                                                                                                           | 8.82 ms: 1.02x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text    | 26.7 ms                                                                                                           | 26.9 ms: 1.01x slower                                                                                                   |
| mako           | 13.8 ms                                                                                                           | 14.1 ms: 1.02x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.83 us                                                                                                           | 5.90 us: 1.16x faster                                                                                                   |
| scimark_lu                 | 151 ms                                                                                                            | 134 ms: 1.13x faster                                                                                                    |
| async_generators           | 458 ms                                                                                                            | 417 ms: 1.10x faster                                                                                                    |
| coverage                   | 577 ms                                                                                                            | 526 ms: 1.10x faster                                                                                                    |
| spectral_norm              | 131 ms                                                                                                            | 120 ms: 1.09x faster                                                                                                    |
| scimark_fft                | 437 ms                                                                                                            | 402 ms: 1.09x faster                                                                                                    |
| json_dumps                 | 14.4 ms                                                                                                           | 13.2 ms: 1.09x faster                                                                                                   |
| richards_super             | 59.0 ms                                                                                                           | 54.7 ms: 1.08x faster                                                                                                   |
| pathlib                    | 23.5 ms                                                                                                           | 21.8 ms: 1.08x faster                                                                                                   |
| richards                   | 52.4 ms                                                                                                           | 48.8 ms: 1.07x faster                                                                                                   |
| logging_silent             | 636 ns                                                                                                            | 596 ns: 1.07x faster                                                                                                    |
| typing_runtime_protocols   | 206 us                                                                                                            | 193 us: 1.07x faster                                                                                                    |
| deepcopy                   | 339 us                                                                                                            | 318 us: 1.07x faster                                                                                                    |
| pickle_dict                | 39.3 us                                                                                                           | 36.9 us: 1.06x faster                                                                                                   |
| xml_etree_generate         | 114 ms                                                                                                            | 107 ms: 1.06x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.80 ms                                                                                                           | 1.70 ms: 1.06x faster                                                                                                   |
| unpickle                   | 18.7 us                                                                                                           | 17.6 us: 1.06x faster                                                                                                   |
| deepcopy_memo              | 37.7 us                                                                                                           | 35.8 us: 1.05x faster                                                                                                   |
| xml_etree_process          | 79.9 ms                                                                                                           | 76.1 ms: 1.05x faster                                                                                                   |
| scimark_sparse_mat_mult    | 6.98 ms                                                                                                           | 6.66 ms: 1.05x faster                                                                                                   |
| unpickle_pure_python       | 261 us                                                                                                            | 249 us: 1.04x faster                                                                                                    |
| pyflate                    | 537 ms                                                                                                            | 515 ms: 1.04x faster                                                                                                    |
| bench_thread_pool          | 1.37 ms                                                                                                           | 1.32 ms: 1.04x faster                                                                                                   |
| json_loads                 | 35.7 us                                                                                                           | 34.4 us: 1.04x faster                                                                                                   |
| json                       | 6.08 ms                                                                                                           | 5.86 ms: 1.04x faster                                                                                                   |
| sympy_str                  | 269 ms                                                                                                            | 259 ms: 1.04x faster                                                                                                    |
| k_core                     | 2.84 sec                                                                                                          | 2.74 sec: 1.04x faster                                                                                                  |
| logging_simple             | 7.77 us                                                                                                           | 7.50 us: 1.04x faster                                                                                                   |
| deepcopy_reduce            | 3.49 us                                                                                                           | 3.37 us: 1.03x faster                                                                                                   |
| logging_format             | 8.46 us                                                                                                           | 8.18 us: 1.03x faster                                                                                                   |
| bpe_tokeniser              | 5.46 sec                                                                                                          | 5.28 sec: 1.03x faster                                                                                                  |
| tomli_loads                | 2.45 sec                                                                                                          | 2.37 sec: 1.03x faster                                                                                                  |
| async_tree_memoization_tg  | 465 ms                                                                                                            | 450 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 374 ms                                                                                                            | 364 ms: 1.03x faster                                                                                                    |
| scimark_monte_carlo        | 78.9 ms                                                                                                           | 76.6 ms: 1.03x faster                                                                                                   |
| async_tree_none            | 397 ms                                                                                                            | 386 ms: 1.03x faster                                                                                                    |
| async_tree_memoization     | 467 ms                                                                                                            | 457 ms: 1.02x faster                                                                                                    |
| mdp                        | 1.69 sec                                                                                                          | 1.67 sec: 1.02x faster                                                                                                  |
| async_tree_io_tg           | 907 ms                                                                                                            | 893 ms: 1.02x faster                                                                                                    |
| shortest_path              | 583 ms                                                                                                            | 576 ms: 1.01x faster                                                                                                    |
| async_tree_io              | 876 ms                                                                                                            | 867 ms: 1.01x faster                                                                                                    |
| genshi_text                | 26.7 ms                                                                                                           | 26.9 ms: 1.01x slower                                                                                                   |
| python_startup             | 15.1 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                   |
| mako                       | 13.8 ms                                                                                                           | 14.1 ms: 1.02x slower                                                                                                   |
| python_startup_no_site     | 8.67 ms                                                                                                           | 8.82 ms: 1.02x slower                                                                                                   |
| sqlite_synth               | 3.81 us                                                                                                           | 3.90 us: 1.02x slower                                                                                                   |
| subparsers                 | 28.4 ms                                                                                                           | 29.1 ms: 1.03x slower                                                                                                   |
| gc_traversal               | 6.64 ms                                                                                                           | 6.81 ms: 1.03x slower                                                                                                   |
| pprint_safe_repr           | 1.00 sec                                                                                                          | 1.03 sec: 1.03x slower                                                                                                  |
| pprint_pformat             | 2.04 sec                                                                                                          | 2.10 sec: 1.03x slower                                                                                                  |
| create_gc_cycles           | 3.68 ms                                                                                                           | 3.82 ms: 1.04x slower                                                                                                   |
| xml_etree_iterparse        | 143 ms                                                                                                            | 149 ms: 1.04x slower                                                                                                    |
| dulwich_log                | 51.9 ms                                                                                                           | 54.3 ms: 1.05x slower                                                                                                   |
| regex_dna                  | 228 ms                                                                                                            | 240 ms: 1.05x slower                                                                                                    |
| nbody                      | 121 ms                                                                                                            | 129 ms: 1.06x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 668 ms                                                                                                            | 723 ms: 1.08x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                            | 713 ms: 1.10x slower                                                                                                    |
| regex_v8                   | 28.1 ms                                                                                                           | 31.8 ms: 1.13x slower                                                                                                   |
| xml_etree_parse            | 182 ms                                                                                                            | 209 ms: 1.15x slower                                                                                                    |
| pidigits                   | 237 ms                                                                                                            | 293 ms: 1.24x slower                                                                                                    |
| regex_effbot               | 3.70 ms                                                                                                           | 4.58 ms: 1.24x slower                                                                                                   |
| unpack_sequence            | 51.5 ns                                                                                                           | 69.0 ns: 1.34x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (40): comprehensions, pickle_list, pickle_pure_python, raytrace, django_template, sympy_integrate, chaos, sqlglot_v2_normalize, sqlglot_v2_optimize, regex_compile, asyncio_tcp, meteor_contest, scimark_sor, hexiom, sqlglot_v2_parse, 2to3, sympy_expand, pycparser, asyncio_tcp_ssl, thrift, crypto_pyaes, generators, genshi_xml, asyncio_websockets, sympy_sum, connected_components, many_optionals, float, sphinx, docutils, pickle, telco, deltablue, go, pylint, html5lib, nqueens, fannkuch, coroutines, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 90.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x