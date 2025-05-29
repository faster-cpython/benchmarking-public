# Results vs. base

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.026x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                                                            | 250 ms: 1.02x faster                                                                                                    |
| docutils       | 2.59 sec                                                                                                          | 2.57 sec: 1.01x faster                                                                                                  |
| html5lib       | 62.5 ms                                                                                                           | 59.1 ms: 1.06x faster                                                                                                   |
| sphinx         | 1.01 sec                                                                                                          | 985 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 23.5 ms                                                                                                           | 21.8 ms: 1.08x faster                                                                                                   |
| async_tree_io_tg           | 621 ms                                                                                                            | 594 ms: 1.04x faster                                                                                                    |
| async_tree_none_tg         | 251 ms                                                                                                            | 241 ms: 1.04x faster                                                                                                    |
| async_tree_memoization_tg  | 317 ms                                                                                                            | 307 ms: 1.03x faster                                                                                                    |
| async_tree_none            | 257 ms                                                                                                            | 251 ms: 1.03x faster                                                                                                    |
| async_tree_memoization     | 316 ms                                                                                                            | 308 ms: 1.02x faster                                                                                                    |
| asyncio_tcp                | 479 ms                                                                                                            | 471 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 607 ms                                                                                                            | 597 ms: 1.02x faster                                                                                                    |
| async_generators           | 384 ms                                                                                                            | 378 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                                                            | 474 ms: 1.01x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.78 sec                                                                                                          | 1.78 sec: 1.00x faster                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 71.3 ms                                                                                                           | 67.6 ms: 1.06x faster                                                                                                   |
| nbody          | 92.6 ms                                                                                                           | 89.3 ms: 1.04x faster                                                                                                   |
| pidigits       | 186 ms                                                                                                            | 202 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                                                            | 194 ms: 1.17x faster                                                                                                    |
| regex_v8       | 26.2 ms                                                                                                           | 26.1 ms: 1.00x faster                                                                                                   |
| regex_compile  | 125 ms                                                                                                            | 124 ms: 1.00x faster                                                                                                    |
| regex_effbot   | 3.32 ms                                                                                                           | 3.40 ms: 1.02x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.04x faster                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 5.63 us                                                                                                           | 4.46 us: 1.26x faster                                                                                                   |
| unpickle            | 14.6 us                                                                                                           | 14.0 us: 1.04x faster                                                                                                   |
| tomli_loads         | 1.95 sec                                                                                                          | 1.90 sec: 1.03x faster                                                                                                  |
| xml_etree_process   | 59.4 ms                                                                                                           | 58.5 ms: 1.02x faster                                                                                                   |
| pickle_list         | 5.27 us                                                                                                           | 5.19 us: 1.02x faster                                                                                                   |
| pickle_pure_python  | 314 us                                                                                                            | 312 us: 1.00x faster                                                                                                    |
| json_loads          | 30.1 us                                                                                                           | 30.0 us: 1.00x faster                                                                                                   |
| xml_etree_iterparse | 97.2 ms                                                                                                           | 102 ms: 1.05x slower                                                                                                    |
| json_dumps          | 11.4 ms                                                                                                           | 12.1 ms: 1.06x slower                                                                                                   |
| pickle_dict         | 32.4 us                                                                                                           | 35.1 us: 1.08x slower                                                                                                   |
| pickle              | 12.2 us                                                                                                           | 13.6 us: 1.11x slower                                                                                                   |
| xml_etree_parse     | 140 ms                                                                                                            | 162 ms: 1.16x slower                                                                                                    |
| Geometric mean      | (ref)                                                                                                             | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                                                           | 12.7 ms: 1.02x faster                                                                                                   |
| python_startup_no_site | 7.04 ms                                                                                                           | 6.99 ms: 1.01x faster                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 32.2 ms                                                                                                           | 30.3 ms: 1.06x faster                                                                                                   |
| genshi_text     | 22.2 ms                                                                                                           | 20.9 ms: 1.06x faster                                                                                                   |
| genshi_xml      | 49.5 ms                                                                                                           | 47.8 ms: 1.04x faster                                                                                                   |
| mako            | 10.8 ms                                                                                                           | 11.7 ms: 1.08x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.02x faster                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 5.63 us                                                                                                           | 4.46 us: 1.26x faster                                                                                                   |
| spectral_norm              | 96.8 ms                                                                                                           | 82.3 ms: 1.18x faster                                                                                                   |
| regex_dna                  | 227 ms                                                                                                            | 194 ms: 1.17x faster                                                                                                    |
| logging_silent             | 103 ns                                                                                                            | 90.3 ns: 1.15x faster                                                                                                   |
| coverage                   | 90.5 ms                                                                                                           | 79.8 ms: 1.13x faster                                                                                                   |
| scimark_fft                | 333 ms                                                                                                            | 295 ms: 1.13x faster                                                                                                    |
| nqueens                    | 83.0 ms                                                                                                           | 73.9 ms: 1.12x faster                                                                                                   |
| pathlib                    | 16.9 ms                                                                                                           | 15.1 ms: 1.12x faster                                                                                                   |
| scimark_sparse_mat_mult    | 4.58 ms                                                                                                           | 4.11 ms: 1.11x faster                                                                                                   |
| pyflate                    | 465 ms                                                                                                            | 420 ms: 1.11x faster                                                                                                    |
| typing_runtime_protocols   | 159 us                                                                                                            | 146 us: 1.09x faster                                                                                                    |
| scimark_monte_carlo        | 67.2 ms                                                                                                           | 61.8 ms: 1.09x faster                                                                                                   |
| scimark_sor                | 118 ms                                                                                                            | 109 ms: 1.08x faster                                                                                                    |
| coroutines                 | 23.5 ms                                                                                                           | 21.8 ms: 1.08x faster                                                                                                   |
| chaos                      | 58.6 ms                                                                                                           | 54.6 ms: 1.07x faster                                                                                                   |
| telco                      | 7.79 ms                                                                                                           | 7.31 ms: 1.07x faster                                                                                                   |
| richards                   | 43.3 ms                                                                                                           | 40.8 ms: 1.06x faster                                                                                                   |
| django_template            | 32.2 ms                                                                                                           | 30.3 ms: 1.06x faster                                                                                                   |
| genshi_text                | 22.2 ms                                                                                                           | 20.9 ms: 1.06x faster                                                                                                   |
| deepcopy_reduce            | 2.64 us                                                                                                           | 2.50 us: 1.06x faster                                                                                                   |
| html5lib                   | 62.5 ms                                                                                                           | 59.1 ms: 1.06x faster                                                                                                   |
| float                      | 71.3 ms                                                                                                           | 67.6 ms: 1.06x faster                                                                                                   |
| deltablue                  | 3.14 ms                                                                                                           | 2.98 ms: 1.05x faster                                                                                                   |
| bench_thread_pool          | 863 us                                                                                                            | 821 us: 1.05x faster                                                                                                    |
| comprehensions             | 16.3 us                                                                                                           | 15.5 us: 1.05x faster                                                                                                   |
| deepcopy                   | 259 us                                                                                                            | 247 us: 1.05x faster                                                                                                    |
| sqlite_synth               | 2.78 us                                                                                                           | 2.65 us: 1.05x faster                                                                                                   |
| async_tree_io_tg           | 621 ms                                                                                                            | 594 ms: 1.04x faster                                                                                                    |
| sympy_sum                  | 148 ms                                                                                                            | 142 ms: 1.04x faster                                                                                                    |
| raytrace                   | 270 ms                                                                                                            | 259 ms: 1.04x faster                                                                                                    |
| richards_super             | 49.7 ms                                                                                                           | 47.6 ms: 1.04x faster                                                                                                   |
| unpickle                   | 14.6 us                                                                                                           | 14.0 us: 1.04x faster                                                                                                   |
| dulwich_log                | 64.7 ms                                                                                                           | 62.2 ms: 1.04x faster                                                                                                   |
| sympy_integrate            | 19.7 ms                                                                                                           | 18.9 ms: 1.04x faster                                                                                                   |
| thrift                     | 771 us                                                                                                            | 742 us: 1.04x faster                                                                                                    |
| async_tree_none_tg         | 251 ms                                                                                                            | 241 ms: 1.04x faster                                                                                                    |
| bpe_tokeniser              | 4.52 sec                                                                                                          | 4.35 sec: 1.04x faster                                                                                                  |
| scimark_lu                 | 115 ms                                                                                                            | 110 ms: 1.04x faster                                                                                                    |
| nbody                      | 92.6 ms                                                                                                           | 89.3 ms: 1.04x faster                                                                                                   |
| genshi_xml                 | 49.5 ms                                                                                                           | 47.8 ms: 1.04x faster                                                                                                   |
| sqlglot_parse              | 1.25 ms                                                                                                           | 1.21 ms: 1.04x faster                                                                                                   |
| sqlglot_transpile          | 1.56 ms                                                                                                           | 1.51 ms: 1.03x faster                                                                                                   |
| sympy_str                  | 267 ms                                                                                                            | 258 ms: 1.03x faster                                                                                                    |
| async_tree_memoization_tg  | 317 ms                                                                                                            | 307 ms: 1.03x faster                                                                                                    |
| tomli_loads                | 1.95 sec                                                                                                          | 1.90 sec: 1.03x faster                                                                                                  |
| sympy_expand               | 454 ms                                                                                                            | 441 ms: 1.03x faster                                                                                                    |
| logging_format             | 6.10 us                                                                                                           | 5.94 us: 1.03x faster                                                                                                   |
| async_tree_none            | 257 ms                                                                                                            | 251 ms: 1.03x faster                                                                                                    |
| unpack_sequence            | 51.3 ns                                                                                                           | 50.1 ns: 1.02x faster                                                                                                   |
| hexiom                     | 6.09 ms                                                                                                           | 5.94 ms: 1.02x faster                                                                                                   |
| async_tree_memoization     | 316 ms                                                                                                            | 308 ms: 1.02x faster                                                                                                    |
| sqlalchemy_declarative     | 128 ms                                                                                                            | 125 ms: 1.02x faster                                                                                                    |
| subparsers                 | 20.4 ms                                                                                                           | 19.9 ms: 1.02x faster                                                                                                   |
| sqlglot_normalize          | 105 ms                                                                                                            | 103 ms: 1.02x faster                                                                                                    |
| bench_mp_pool              | 81.7 ms                                                                                                           | 80.0 ms: 1.02x faster                                                                                                   |
| 2to3                       | 255 ms                                                                                                            | 250 ms: 1.02x faster                                                                                                    |
| sphinx                     | 1.01 sec                                                                                                          | 985 ms: 1.02x faster                                                                                                    |
| logging_simple             | 5.48 us                                                                                                           | 5.37 us: 1.02x faster                                                                                                   |
| fannkuch                   | 403 ms                                                                                                            | 395 ms: 1.02x faster                                                                                                    |
| go                         | 115 ms                                                                                                            | 113 ms: 1.02x faster                                                                                                    |
| asyncio_tcp                | 479 ms                                                                                                            | 471 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 607 ms                                                                                                            | 597 ms: 1.02x faster                                                                                                    |
| xml_etree_process          | 59.4 ms                                                                                                           | 58.5 ms: 1.02x faster                                                                                                   |
| pickle_list                | 5.27 us                                                                                                           | 5.19 us: 1.02x faster                                                                                                   |
| python_startup             | 12.9 ms                                                                                                           | 12.7 ms: 1.02x faster                                                                                                   |
| async_generators           | 384 ms                                                                                                            | 378 ms: 1.01x faster                                                                                                    |
| sqlglot_optimize           | 52.5 ms                                                                                                           | 51.8 ms: 1.01x faster                                                                                                   |
| sqlalchemy_imperative      | 16.3 ms                                                                                                           | 16.1 ms: 1.01x faster                                                                                                   |
| many_optionals             | 928 us                                                                                                            | 917 us: 1.01x faster                                                                                                    |
| deepcopy_memo              | 30.0 us                                                                                                           | 29.7 us: 1.01x faster                                                                                                   |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                                                            | 474 ms: 1.01x faster                                                                                                    |
| shortest_path              | 484 ms                                                                                                            | 480 ms: 1.01x faster                                                                                                    |
| docutils                   | 2.59 sec                                                                                                          | 2.57 sec: 1.01x faster                                                                                                  |
| python_startup_no_site     | 7.04 ms                                                                                                           | 6.99 ms: 1.01x faster                                                                                                   |
| regex_v8                   | 26.2 ms                                                                                                           | 26.1 ms: 1.00x faster                                                                                                   |
| pickle_pure_python         | 314 us                                                                                                            | 312 us: 1.00x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.78 sec                                                                                                          | 1.78 sec: 1.00x faster                                                                                                  |
| json_loads                 | 30.1 us                                                                                                           | 30.0 us: 1.00x faster                                                                                                   |
| regex_compile              | 125 ms                                                                                                            | 124 ms: 1.00x faster                                                                                                    |
| regex_effbot               | 3.32 ms                                                                                                           | 3.40 ms: 1.02x slower                                                                                                   |
| meteor_contest             | 108 ms                                                                                                            | 111 ms: 1.03x slower                                                                                                    |
| create_gc_cycles           | 2.43 ms                                                                                                           | 2.50 ms: 1.03x slower                                                                                                   |
| pprint_pformat             | 1.45 sec                                                                                                          | 1.50 sec: 1.03x slower                                                                                                  |
| pprint_safe_repr           | 711 ms                                                                                                            | 737 ms: 1.04x slower                                                                                                    |
| xml_etree_iterparse        | 97.2 ms                                                                                                           | 102 ms: 1.05x slower                                                                                                    |
| gc_traversal               | 4.74 ms                                                                                                           | 5.01 ms: 1.06x slower                                                                                                   |
| json_dumps                 | 11.4 ms                                                                                                           | 12.1 ms: 1.06x slower                                                                                                   |
| mako                       | 10.8 ms                                                                                                           | 11.7 ms: 1.08x slower                                                                                                   |
| pickle_dict                | 32.4 us                                                                                                           | 35.1 us: 1.08x slower                                                                                                   |
| pidigits                   | 186 ms                                                                                                            | 202 ms: 1.08x slower                                                                                                    |
| mdp                        | 2.53 sec                                                                                                          | 2.77 sec: 1.09x slower                                                                                                  |
| pickle                     | 12.2 us                                                                                                           | 13.6 us: 1.11x slower                                                                                                   |
| xml_etree_parse            | 140 ms                                                                                                            | 162 ms: 1.16x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (11): pylint, pycparser, k_core, async_tree_cpu_io_mixed, xml_etree_generate, unpickle_pure_python, asyncio_websockets, generators, crypto_pyaes, connected_components, json

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x