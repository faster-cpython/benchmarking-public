# Results vs. base

- fork: python
- ref: 4f18916c5c28321f363e
- machine: linux-aarch64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.015x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                                                              | 288 ms: 1.03x faster                                                                                                      |
| docutils       | 2.94 sec                                                                                                            | 2.89 sec: 1.02x faster                                                                                                    |
| html5lib       | 61.2 ms                                                                                                             | 58.2 ms: 1.05x faster                                                                                                     |
| sphinx         | 1.15 sec                                                                                                            | 1.10 sec: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 30.3 ms                                                                                                             | 27.8 ms: 1.09x faster                                                                                                     |
| async_tree_none            | 392 ms                                                                                                              | 365 ms: 1.07x faster                                                                                                      |
| async_generators           | 445 ms                                                                                                              | 416 ms: 1.07x faster                                                                                                      |
| async_tree_memoization     | 468 ms                                                                                                              | 441 ms: 1.06x faster                                                                                                      |
| async_tree_none_tg         | 371 ms                                                                                                              | 353 ms: 1.05x faster                                                                                                      |
| async_tree_memoization_tg  | 463 ms                                                                                                              | 443 ms: 1.04x faster                                                                                                      |
| async_tree_io              | 899 ms                                                                                                              | 865 ms: 1.04x faster                                                                                                      |
| async_tree_io_tg           | 884 ms                                                                                                              | 853 ms: 1.04x faster                                                                                                      |
| asyncio_tcp                | 531 ms                                                                                                              | 546 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 665 ms                                                                                                              | 713 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 649 ms                                                                                                              | 697 ms: 1.07x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                                                                              | 290 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                              |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 241 ms                                                                                                              | 234 ms: 1.03x faster                                                                                                      |
| regex_effbot   | 3.85 ms                                                                                                             | 4.02 ms: 1.05x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.59 us                                                                                                             | 5.57 us: 1.18x faster                                                                                                     |
| xml_etree_process    | 82.6 ms                                                                                                             | 75.1 ms: 1.10x faster                                                                                                     |
| unpickle_pure_python | 266 us                                                                                                              | 246 us: 1.08x faster                                                                                                      |
| pickle_dict          | 39.4 us                                                                                                             | 36.4 us: 1.08x faster                                                                                                     |
| xml_etree_generate   | 112 ms                                                                                                              | 104 ms: 1.07x faster                                                                                                      |
| pickle               | 15.9 us                                                                                                             | 15.0 us: 1.06x faster                                                                                                     |
| unpickle             | 17.4 us                                                                                                             | 16.5 us: 1.06x faster                                                                                                     |
| pickle_list          | 5.58 us                                                                                                             | 5.40 us: 1.03x faster                                                                                                     |
| tomli_loads          | 2.40 sec                                                                                                            | 2.36 sec: 1.02x faster                                                                                                    |
| json_loads           | 34.1 us                                                                                                             | 33.4 us: 1.02x faster                                                                                                     |
| xml_etree_iterparse  | 141 ms                                                                                                              | 150 ms: 1.07x slower                                                                                                      |
| xml_etree_parse      | 180 ms                                                                                                              | 203 ms: 1.12x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 62.1 ms                                                                                                             | 58.0 ms: 1.07x faster                                                                                                     |
| genshi_text    | 27.5 ms                                                                                                             | 25.8 ms: 1.07x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250426-3.14.0a7+-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json | results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.59 us                                                                                                             | 5.57 us: 1.18x faster                                                                                                     |
| logging_silent             | 133 ns                                                                                                              | 116 ns: 1.15x faster                                                                                                      |
| xml_etree_process          | 82.6 ms                                                                                                             | 75.1 ms: 1.10x faster                                                                                                     |
| scimark_lu                 | 154 ms                                                                                                              | 142 ms: 1.09x faster                                                                                                      |
| coroutines                 | 30.3 ms                                                                                                             | 27.8 ms: 1.09x faster                                                                                                     |
| unpickle_pure_python       | 266 us                                                                                                              | 246 us: 1.08x faster                                                                                                      |
| sqlglot_v2_parse           | 1.44 ms                                                                                                             | 1.33 ms: 1.08x faster                                                                                                     |
| pickle_dict                | 39.4 us                                                                                                             | 36.4 us: 1.08x faster                                                                                                     |
| pathlib                    | 22.8 ms                                                                                                             | 21.1 ms: 1.08x faster                                                                                                     |
| xml_etree_generate         | 112 ms                                                                                                              | 104 ms: 1.07x faster                                                                                                      |
| deepcopy_memo              | 37.4 us                                                                                                             | 34.8 us: 1.07x faster                                                                                                     |
| async_tree_none            | 392 ms                                                                                                              | 365 ms: 1.07x faster                                                                                                      |
| dulwich_log                | 54.6 ms                                                                                                             | 50.9 ms: 1.07x faster                                                                                                     |
| genshi_xml                 | 62.1 ms                                                                                                             | 58.0 ms: 1.07x faster                                                                                                     |
| deepcopy                   | 328 us                                                                                                              | 306 us: 1.07x faster                                                                                                      |
| async_generators           | 445 ms                                                                                                              | 416 ms: 1.07x faster                                                                                                      |
| genshi_text                | 27.5 ms                                                                                                             | 25.8 ms: 1.07x faster                                                                                                     |
| sqlglot_v2_normalize       | 127 ms                                                                                                              | 120 ms: 1.06x faster                                                                                                      |
| sympy_str                  | 273 ms                                                                                                              | 256 ms: 1.06x faster                                                                                                      |
| sqlglot_v2_optimize        | 61.3 ms                                                                                                             | 57.7 ms: 1.06x faster                                                                                                     |
| sympy_sum                  | 145 ms                                                                                                              | 137 ms: 1.06x faster                                                                                                      |
| async_tree_memoization     | 468 ms                                                                                                              | 441 ms: 1.06x faster                                                                                                      |
| telco                      | 9.38 ms                                                                                                             | 8.83 ms: 1.06x faster                                                                                                     |
| richards                   | 52.3 ms                                                                                                             | 49.3 ms: 1.06x faster                                                                                                     |
| pickle                     | 15.9 us                                                                                                             | 15.0 us: 1.06x faster                                                                                                     |
| unpickle                   | 17.4 us                                                                                                             | 16.5 us: 1.06x faster                                                                                                     |
| sympy_integrate            | 20.5 ms                                                                                                             | 19.4 ms: 1.06x faster                                                                                                     |
| deltablue                  | 3.92 ms                                                                                                             | 3.72 ms: 1.05x faster                                                                                                     |
| html5lib                   | 61.2 ms                                                                                                             | 58.2 ms: 1.05x faster                                                                                                     |
| async_tree_none_tg         | 371 ms                                                                                                              | 353 ms: 1.05x faster                                                                                                      |
| coverage                   | 102 ms                                                                                                              | 97.5 ms: 1.05x faster                                                                                                     |
| scimark_fft                | 420 ms                                                                                                              | 401 ms: 1.05x faster                                                                                                      |
| async_tree_memoization_tg  | 463 ms                                                                                                              | 443 ms: 1.04x faster                                                                                                      |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                             | 1.67 ms: 1.04x faster                                                                                                     |
| sphinx                     | 1.15 sec                                                                                                            | 1.10 sec: 1.04x faster                                                                                                    |
| async_tree_io              | 899 ms                                                                                                              | 865 ms: 1.04x faster                                                                                                      |
| typing_runtime_protocols   | 194 us                                                                                                              | 187 us: 1.04x faster                                                                                                      |
| async_tree_io_tg           | 884 ms                                                                                                              | 853 ms: 1.04x faster                                                                                                      |
| bpe_tokeniser              | 5.36 sec                                                                                                            | 5.19 sec: 1.03x faster                                                                                                    |
| pickle_list                | 5.58 us                                                                                                             | 5.40 us: 1.03x faster                                                                                                     |
| logging_format             | 7.71 us                                                                                                             | 7.47 us: 1.03x faster                                                                                                     |
| regex_dna                  | 241 ms                                                                                                              | 234 ms: 1.03x faster                                                                                                      |
| sympy_expand               | 464 ms                                                                                                              | 450 ms: 1.03x faster                                                                                                      |
| k_core                     | 2.84 sec                                                                                                            | 2.75 sec: 1.03x faster                                                                                                    |
| 2to3                       | 297 ms                                                                                                              | 288 ms: 1.03x faster                                                                                                      |
| mdp                        | 1.62 sec                                                                                                            | 1.59 sec: 1.02x faster                                                                                                    |
| pycparser                  | 1.24 sec                                                                                                            | 1.21 sec: 1.02x faster                                                                                                    |
| tomli_loads                | 2.40 sec                                                                                                            | 2.36 sec: 1.02x faster                                                                                                    |
| json_loads                 | 34.1 us                                                                                                             | 33.4 us: 1.02x faster                                                                                                     |
| docutils                   | 2.94 sec                                                                                                            | 2.89 sec: 1.02x faster                                                                                                    |
| logging_simple             | 6.94 us                                                                                                             | 6.85 us: 1.01x faster                                                                                                     |
| connected_components       | 567 ms                                                                                                              | 560 ms: 1.01x faster                                                                                                      |
| subparsers                 | 25.7 ms                                                                                                             | 25.5 ms: 1.01x faster                                                                                                     |
| pprint_pformat             | 1.82 sec                                                                                                            | 1.85 sec: 1.01x slower                                                                                                    |
| asyncio_tcp                | 531 ms                                                                                                              | 546 ms: 1.03x slower                                                                                                      |
| nqueens                    | 96.3 ms                                                                                                             | 101 ms: 1.04x slower                                                                                                      |
| regex_effbot               | 3.85 ms                                                                                                             | 4.02 ms: 1.05x slower                                                                                                     |
| meteor_contest             | 112 ms                                                                                                              | 118 ms: 1.05x slower                                                                                                      |
| create_gc_cycles           | 3.62 ms                                                                                                             | 3.84 ms: 1.06x slower                                                                                                     |
| xml_etree_iterparse        | 141 ms                                                                                                              | 150 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 665 ms                                                                                                              | 713 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 649 ms                                                                                                              | 697 ms: 1.07x slower                                                                                                      |
| fannkuch                   | 458 ms                                                                                                              | 493 ms: 1.08x slower                                                                                                      |
| xml_etree_parse            | 180 ms                                                                                                              | 203 ms: 1.12x slower                                                                                                      |
| pidigits                   | 234 ms                                                                                                              | 290 ms: 1.24x slower                                                                                                      |
| unpack_sequence            | 51.6 ns                                                                                                             | 75.8 ns: 1.47x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (37): comprehensions, spectral_norm, scimark_sor, hexiom, many_optionals, regex_compile, pylint, deepcopy_reduce, django_template, generators, richards_super, sqlite_synth, bench_thread_pool, raytrace, pickle_pure_python, go, chaos, mako, asyncio_tcp_ssl, float, python_startup, scimark_sparse_mat_mult, asyncio_websockets, json, json_dumps, pyflate, regex_v8, pprint_safe_repr, sqlalchemy_declarative, scimark_monte_carlo, python_startup_no_site, shortest_path, crypto_pyaes, gc_traversal, sqlalchemy_imperative, nbody, bench_mp_pool

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x