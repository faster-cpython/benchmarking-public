# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.014x faster
- HPT reliability: 89.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                                                          | 297 ms: 1.02x slower                                                                                                |
| docutils       | 2.86 sec                                                                                                        | 2.92 sec: 1.02x slower                                                                                              |
| html5lib       | 67.7 ms                                                                                                         | 66.1 ms: 1.03x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                                                                          | 285 ms: 1.02x faster                                                                                                |
| async_tree_memoization     | 349 ms                                                                                                          | 343 ms: 1.02x faster                                                                                                |
| async_tree_none_tg         | 281 ms                                                                                                          | 276 ms: 1.02x faster                                                                                                |
| async_tree_io              | 666 ms                                                                                                          | 655 ms: 1.02x faster                                                                                                |
| asyncio_tcp_ssl            | 1.81 sec                                                                                                        | 1.81 sec: 1.00x slower                                                                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                                                                          | 600 ms: 1.01x slower                                                                                                |
| asyncio_tcp                | 480 ms                                                                                                          | 484 ms: 1.01x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 589 ms                                                                                                          | 595 ms: 1.01x slower                                                                                                |
| async_generators           | 419 ms                                                                                                          | 437 ms: 1.04x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 75.0 ms                                                                                                         | 67.9 ms: 1.10x faster                                                                                               |
| nbody          | 106 ms                                                                                                          | 97.0 ms: 1.09x faster                                                                                               |
| pidigits       | 207 ms                                                                                                          | 203 ms: 1.02x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 203 ms                                                                                                          | 199 ms: 1.02x faster                                                                                                |
| regex_v8       | 24.2 ms                                                                                                         | 25.6 ms: 1.06x slower                                                                                               |
| regex_effbot   | 3.01 ms                                                                                                         | 3.18 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 75.3 ms                                                                                                         | 68.8 ms: 1.09x faster                                                                                               |
| xml_etree_generate   | 110 ms                                                                                                          | 102 ms: 1.08x faster                                                                                                |
| unpickle_pure_python | 256 us                                                                                                          | 240 us: 1.07x faster                                                                                                |
| tomli_loads          | 2.24 sec                                                                                                        | 2.10 sec: 1.06x faster                                                                                              |
| unpickle_list        | 5.96 us                                                                                                         | 5.86 us: 1.02x faster                                                                                               |
| json_dumps           | 13.4 ms                                                                                                         | 13.3 ms: 1.01x faster                                                                                               |
| json_loads           | 33.6 us                                                                                                         | 33.5 us: 1.00x faster                                                                                               |
| pickle_dict          | 37.9 us                                                                                                         | 37.7 us: 1.00x faster                                                                                               |
| pickle_pure_python   | 375 us                                                                                                          | 377 us: 1.01x slower                                                                                                |
| pickle               | 14.9 us                                                                                                         | 15.0 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                         | 13.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 7.35 ms                                                                                                         | 7.39 ms: 1.00x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.8 ms                                                                                                         | 13.2 ms: 1.04x faster                                                                                               |
| django_template | 40.2 ms                                                                                                         | 40.6 ms: 1.01x slower                                                                                               |
| genshi_xml      | 57.2 ms                                                                                                         | 58.4 ms: 1.02x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| richards                   | 54.0 ms                                                                                                         | 39.7 ms: 1.36x faster                                                                                               |
| richards_super             | 61.4 ms                                                                                                         | 46.3 ms: 1.32x faster                                                                                               |
| scimark_fft                | 412 ms                                                                                                          | 351 ms: 1.17x faster                                                                                                |
| deltablue                  | 3.84 ms                                                                                                         | 3.45 ms: 1.12x faster                                                                                               |
| float                      | 75.0 ms                                                                                                         | 67.9 ms: 1.10x faster                                                                                               |
| xml_etree_process          | 75.3 ms                                                                                                         | 68.8 ms: 1.09x faster                                                                                               |
| nbody                      | 106 ms                                                                                                          | 97.0 ms: 1.09x faster                                                                                               |
| xml_etree_generate         | 110 ms                                                                                                          | 102 ms: 1.08x faster                                                                                                |
| scimark_monte_carlo        | 78.2 ms                                                                                                         | 72.7 ms: 1.08x faster                                                                                               |
| spectral_norm              | 118 ms                                                                                                          | 110 ms: 1.07x faster                                                                                                |
| unpickle_pure_python       | 256 us                                                                                                          | 240 us: 1.07x faster                                                                                                |
| tomli_loads                | 2.24 sec                                                                                                        | 2.10 sec: 1.06x faster                                                                                              |
| telco                      | 9.64 ms                                                                                                         | 9.07 ms: 1.06x faster                                                                                               |
| connected_components       | 491 ms                                                                                                          | 470 ms: 1.05x faster                                                                                                |
| shortest_path              | 534 ms                                                                                                          | 511 ms: 1.05x faster                                                                                                |
| mako                       | 13.8 ms                                                                                                         | 13.2 ms: 1.04x faster                                                                                               |
| bpe_tokeniser              | 5.32 sec                                                                                                        | 5.16 sec: 1.03x faster                                                                                              |
| pyflate                    | 469 ms                                                                                                          | 455 ms: 1.03x faster                                                                                                |
| html5lib                   | 67.7 ms                                                                                                         | 66.1 ms: 1.03x faster                                                                                               |
| async_tree_none            | 291 ms                                                                                                          | 285 ms: 1.02x faster                                                                                                |
| pidigits                   | 207 ms                                                                                                          | 203 ms: 1.02x faster                                                                                                |
| scimark_sor                | 137 ms                                                                                                          | 134 ms: 1.02x faster                                                                                                |
| sqlite_synth               | 3.21 us                                                                                                         | 3.14 us: 1.02x faster                                                                                               |
| fannkuch                   | 491 ms                                                                                                          | 482 ms: 1.02x faster                                                                                                |
| unpickle_list              | 5.96 us                                                                                                         | 5.86 us: 1.02x faster                                                                                               |
| regex_dna                  | 203 ms                                                                                                          | 199 ms: 1.02x faster                                                                                                |
| async_tree_memoization     | 349 ms                                                                                                          | 343 ms: 1.02x faster                                                                                                |
| async_tree_none_tg         | 281 ms                                                                                                          | 276 ms: 1.02x faster                                                                                                |
| async_tree_io              | 666 ms                                                                                                          | 655 ms: 1.02x faster                                                                                                |
| json                       | 6.11 ms                                                                                                         | 6.02 ms: 1.01x faster                                                                                               |
| meteor_contest             | 119 ms                                                                                                          | 117 ms: 1.01x faster                                                                                                |
| pathlib                    | 18.2 ms                                                                                                         | 18.1 ms: 1.01x faster                                                                                               |
| sqlglot_v2_optimize        | 62.9 ms                                                                                                         | 62.3 ms: 1.01x faster                                                                                               |
| logging_format             | 8.46 us                                                                                                         | 8.38 us: 1.01x faster                                                                                               |
| json_dumps                 | 13.4 ms                                                                                                         | 13.3 ms: 1.01x faster                                                                                               |
| logging_simple             | 7.51 us                                                                                                         | 7.45 us: 1.01x faster                                                                                               |
| scimark_sparse_mat_mult    | 5.68 ms                                                                                                         | 5.64 ms: 1.01x faster                                                                                               |
| crypto_pyaes               | 86.9 ms                                                                                                         | 86.3 ms: 1.01x faster                                                                                               |
| deepcopy                   | 314 us                                                                                                          | 312 us: 1.01x faster                                                                                                |
| json_loads                 | 33.6 us                                                                                                         | 33.5 us: 1.00x faster                                                                                               |
| gc_traversal               | 5.13 ms                                                                                                         | 5.11 ms: 1.00x faster                                                                                               |
| pickle_dict                | 37.9 us                                                                                                         | 37.7 us: 1.00x faster                                                                                               |
| thrift                     | 149 ms                                                                                                          | 149 ms: 1.00x faster                                                                                                |
| asyncio_tcp_ssl            | 1.81 sec                                                                                                        | 1.81 sec: 1.00x slower                                                                                              |
| mdp                        | 1.48 sec                                                                                                        | 1.48 sec: 1.00x slower                                                                                              |
| python_startup             | 13.1 ms                                                                                                         | 13.2 ms: 1.00x slower                                                                                               |
| chaos                      | 69.9 ms                                                                                                         | 70.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site     | 7.35 ms                                                                                                         | 7.39 ms: 1.00x slower                                                                                               |
| pickle_pure_python         | 375 us                                                                                                          | 377 us: 1.01x slower                                                                                                |
| async_tree_cpu_io_mixed    | 596 ms                                                                                                          | 600 ms: 1.01x slower                                                                                                |
| sympy_sum                  | 167 ms                                                                                                          | 168 ms: 1.01x slower                                                                                                |
| create_gc_cycles           | 2.61 ms                                                                                                         | 2.62 ms: 1.01x slower                                                                                               |
| asyncio_tcp                | 480 ms                                                                                                          | 484 ms: 1.01x slower                                                                                                |
| pickle                     | 14.9 us                                                                                                         | 15.0 us: 1.01x slower                                                                                               |
| scimark_lu                 | 133 ms                                                                                                          | 134 ms: 1.01x slower                                                                                                |
| django_template            | 40.2 ms                                                                                                         | 40.6 ms: 1.01x slower                                                                                               |
| async_tree_cpu_io_mixed_tg | 589 ms                                                                                                          | 595 ms: 1.01x slower                                                                                                |
| deepcopy_reduce            | 3.34 us                                                                                                         | 3.38 us: 1.01x slower                                                                                               |
| bench_thread_pool          | 954 us                                                                                                          | 965 us: 1.01x slower                                                                                                |
| sympy_str                  | 310 ms                                                                                                          | 314 ms: 1.01x slower                                                                                                |
| logging_silent             | 625 ns                                                                                                          | 633 ns: 1.01x slower                                                                                                |
| typing_runtime_protocols   | 197 us                                                                                                          | 200 us: 1.01x slower                                                                                                |
| subparsers                 | 28.0 ms                                                                                                         | 28.4 ms: 1.01x slower                                                                                               |
| sqlglot_v2_transpile       | 1.77 ms                                                                                                         | 1.80 ms: 1.02x slower                                                                                               |
| sqlglot_v2_parse           | 1.42 ms                                                                                                         | 1.44 ms: 1.02x slower                                                                                               |
| generators                 | 32.9 ms                                                                                                         | 33.5 ms: 1.02x slower                                                                                               |
| 2to3                       | 292 ms                                                                                                          | 297 ms: 1.02x slower                                                                                                |
| sympy_integrate            | 21.0 ms                                                                                                         | 21.5 ms: 1.02x slower                                                                                               |
| genshi_xml                 | 57.2 ms                                                                                                         | 58.4 ms: 1.02x slower                                                                                               |
| docutils                   | 2.86 sec                                                                                                        | 2.92 sec: 1.02x slower                                                                                              |
| sympy_expand               | 534 ms                                                                                                          | 548 ms: 1.03x slower                                                                                                |
| many_optionals             | 1.08 ms                                                                                                         | 1.10 ms: 1.03x slower                                                                                               |
| hexiom                     | 6.71 ms                                                                                                         | 6.94 ms: 1.03x slower                                                                                               |
| dulwich_log                | 64.3 ms                                                                                                         | 66.9 ms: 1.04x slower                                                                                               |
| async_generators           | 419 ms                                                                                                          | 437 ms: 1.04x slower                                                                                                |
| pprint_pformat             | 2.05 sec                                                                                                        | 2.15 sec: 1.05x slower                                                                                              |
| regex_v8                   | 24.2 ms                                                                                                         | 25.6 ms: 1.06x slower                                                                                               |
| pprint_safe_repr           | 1.00 sec                                                                                                        | 1.06 sec: 1.06x slower                                                                                              |
| regex_effbot               | 3.01 ms                                                                                                         | 3.18 ms: 1.06x slower                                                                                               |
| comprehensions             | 19.2 us                                                                                                         | 20.4 us: 1.07x slower                                                                                               |
| go                         | 119 ms                                                                                                          | 129 ms: 1.09x slower                                                                                                |
| unpack_sequence            | 52.1 ns                                                                                                         | 70.2 ns: 1.35x slower                                                                                               |
| Geometric mean             | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (20): async_tree_io_tg, async_tree_memoization_tg, k_core, xml_etree_parse, bench_mp_pool, regex_compile, pickle_list, coroutines, coverage, genshi_text, nqueens, asyncio_websockets, deepcopy_memo, unpickle, raytrace, xml_etree_iterparse, pycparser, sqlglot_v2_normalize, sphinx, pylint

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 89.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x