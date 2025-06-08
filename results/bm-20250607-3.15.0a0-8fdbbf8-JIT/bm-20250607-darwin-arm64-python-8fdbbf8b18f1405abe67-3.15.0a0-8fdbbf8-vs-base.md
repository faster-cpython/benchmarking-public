# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                                                                          | 192 ms: 1.13x faster                                                                                                |
| docutils       | 1.59 sec                                                                                                        | 1.63 sec: 1.02x slower                                                                                              |
| sphinx         | 651 ms                                                                                                          | 658 ms: 1.01x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed          | 455 ms                                                                                                          | 452 ms: 1.01x faster                                                                                                |
| async_tree_io_tg                 | 386 ms                                                                                                          | 389 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                                                          | 394 ms: 1.01x slower                                                                                                |
| async_tree_memoization           | 204 ms                                                                                                          | 206 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 426 ms                                                                                                          | 430 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization     | 147 ms                                                                                                          | 150 ms: 1.02x slower                                                                                                |
| async_tree_eager                 | 71.0 ms                                                                                                         | 72.6 ms: 1.02x slower                                                                                               |
| async_generators                 | 314 ms                                                                                                          | 326 ms: 1.04x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (13): asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, asyncio_websockets, coroutines, async_tree_none, async_tree_eager_io, asyncio_tcp_ssl, async_tree_eager_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.19 ms                                                                                                         | 2.22 ms: 1.01x slower                                                                                               |
| regex_dna      | 145 ms                                                                                                          | 147 ms: 1.02x slower                                                                                                |
| regex_v8       | 17.3 ms                                                                                                         | 17.7 ms: 1.02x slower                                                                                               |
| regex_compile  | 74.5 ms                                                                                                         | 76.2 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 158 us                                                                                                          | 150 us: 1.05x faster                                                                                                |
| xml_etree_process    | 43.9 ms                                                                                                         | 43.1 ms: 1.02x faster                                                                                               |
| xml_etree_generate   | 64.9 ms                                                                                                         | 64.0 ms: 1.01x faster                                                                                               |
| xml_etree_parse      | 112 ms                                                                                                          | 111 ms: 1.01x faster                                                                                                |
| json_dumps           | 8.13 ms                                                                                                         | 8.05 ms: 1.01x faster                                                                                               |
| unpickle_list        | 3.58 us                                                                                                         | 3.56 us: 1.01x faster                                                                                               |
| pickle               | 9.85 us                                                                                                         | 9.80 us: 1.01x faster                                                                                               |
| pickle_pure_python   | 221 us                                                                                                          | 221 us: 1.00x faster                                                                                                |
| unpickle             | 11.9 us                                                                                                         | 12.1 us: 1.01x slower                                                                                               |
| tomli_loads          | 1.39 sec                                                                                                        | 1.44 sec: 1.04x slower                                                                                              |
| Geometric mean       | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (4): json_loads, pickle_list, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                                                         | 19.4 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 14.4 ms                                                                                                         | 14.5 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.27 ms                                                                                                         | 8.15 ms: 1.01x faster                                                                                               |
| django_template | 25.7 ms                                                                                                         | 25.6 ms: 1.00x faster                                                                                               |
| genshi_xml      | 33.2 ms                                                                                                         | 33.5 ms: 1.01x slower                                                                                               |
| genshi_text     | 15.6 ms                                                                                                         | 15.8 ms: 1.01x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.00x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3                             | 217 ms                                                                                                          | 192 ms: 1.13x faster                                                                                                |
| scimark_fft                      | 262 ms                                                                                                          | 248 ms: 1.06x faster                                                                                                |
| unpickle_pure_python             | 158 us                                                                                                          | 150 us: 1.05x faster                                                                                                |
| xml_etree_process                | 43.9 ms                                                                                                         | 43.1 ms: 1.02x faster                                                                                               |
| create_gc_cycles                 | 1.42 ms                                                                                                         | 1.39 ms: 1.02x faster                                                                                               |
| logging_silent                   | 421 ns                                                                                                          | 414 ns: 1.02x faster                                                                                                |
| mako                             | 8.27 ms                                                                                                         | 8.15 ms: 1.01x faster                                                                                               |
| xml_etree_generate               | 64.9 ms                                                                                                         | 64.0 ms: 1.01x faster                                                                                               |
| xml_etree_parse                  | 112 ms                                                                                                          | 111 ms: 1.01x faster                                                                                                |
| json_dumps                       | 8.13 ms                                                                                                         | 8.05 ms: 1.01x faster                                                                                               |
| scimark_sor                      | 89.8 ms                                                                                                         | 89.0 ms: 1.01x faster                                                                                               |
| deepcopy_memo                    | 19.4 us                                                                                                         | 19.3 us: 1.01x faster                                                                                               |
| spectral_norm                    | 81.0 ms                                                                                                         | 80.3 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed          | 455 ms                                                                                                          | 452 ms: 1.01x faster                                                                                                |
| deepcopy_reduce                  | 1.99 us                                                                                                         | 1.98 us: 1.01x faster                                                                                               |
| deepcopy                         | 187 us                                                                                                          | 186 us: 1.01x faster                                                                                                |
| scimark_monte_carlo              | 46.3 ms                                                                                                         | 46.1 ms: 1.01x faster                                                                                               |
| unpickle_list                    | 3.58 us                                                                                                         | 3.56 us: 1.01x faster                                                                                               |
| pickle                           | 9.85 us                                                                                                         | 9.80 us: 1.01x faster                                                                                               |
| gc_traversal                     | 3.21 ms                                                                                                         | 3.20 ms: 1.00x faster                                                                                               |
| django_template                  | 25.7 ms                                                                                                         | 25.6 ms: 1.00x faster                                                                                               |
| generators                       | 23.2 ms                                                                                                         | 23.1 ms: 1.00x faster                                                                                               |
| pickle_pure_python               | 221 us                                                                                                          | 221 us: 1.00x faster                                                                                                |
| python_startup                   | 19.3 ms                                                                                                         | 19.4 ms: 1.01x slower                                                                                               |
| nqueens                          | 67.9 ms                                                                                                         | 68.3 ms: 1.01x slower                                                                                               |
| python_startup_no_site           | 14.4 ms                                                                                                         | 14.5 ms: 1.01x slower                                                                                               |
| crypto_pyaes                     | 60.7 ms                                                                                                         | 61.0 ms: 1.01x slower                                                                                               |
| richards                         | 36.1 ms                                                                                                         | 36.3 ms: 1.01x slower                                                                                               |
| richards_super                   | 40.7 ms                                                                                                         | 41.0 ms: 1.01x slower                                                                                               |
| async_tree_io_tg                 | 386 ms                                                                                                          | 389 ms: 1.01x slower                                                                                                |
| bench_thread_pool                | 539 us                                                                                                          | 543 us: 1.01x slower                                                                                                |
| raytrace                         | 210 ms                                                                                                          | 212 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                                                          | 394 ms: 1.01x slower                                                                                                |
| async_tree_memoization           | 204 ms                                                                                                          | 206 ms: 1.01x slower                                                                                                |
| sympy_sum                        | 85.2 ms                                                                                                         | 86.0 ms: 1.01x slower                                                                                               |
| sqlite_synth                     | 1.90 us                                                                                                         | 1.92 us: 1.01x slower                                                                                               |
| genshi_xml                       | 33.2 ms                                                                                                         | 33.5 ms: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 426 ms                                                                                                          | 430 ms: 1.01x slower                                                                                                |
| sphinx                           | 651 ms                                                                                                          | 658 ms: 1.01x slower                                                                                                |
| regex_effbot                     | 2.19 ms                                                                                                         | 2.22 ms: 1.01x slower                                                                                               |
| genshi_text                      | 15.6 ms                                                                                                         | 15.8 ms: 1.01x slower                                                                                               |
| unpickle                         | 11.9 us                                                                                                         | 12.1 us: 1.01x slower                                                                                               |
| typing_runtime_protocols         | 121 us                                                                                                          | 123 us: 1.01x slower                                                                                                |
| chaos                            | 44.4 ms                                                                                                         | 45.0 ms: 1.01x slower                                                                                               |
| telco                            | 5.55 ms                                                                                                         | 5.63 ms: 1.02x slower                                                                                               |
| dulwich_log                      | 27.1 ms                                                                                                         | 27.5 ms: 1.02x slower                                                                                               |
| pyflate                          | 305 ms                                                                                                          | 310 ms: 1.02x slower                                                                                                |
| sympy_str                        | 165 ms                                                                                                          | 168 ms: 1.02x slower                                                                                                |
| regex_dna                        | 145 ms                                                                                                          | 147 ms: 1.02x slower                                                                                                |
| regex_v8                         | 17.3 ms                                                                                                         | 17.7 ms: 1.02x slower                                                                                               |
| async_tree_eager_memoization     | 147 ms                                                                                                          | 150 ms: 1.02x slower                                                                                                |
| sympy_expand                     | 286 ms                                                                                                          | 291 ms: 1.02x slower                                                                                                |
| many_optionals                   | 524 us                                                                                                          | 533 us: 1.02x slower                                                                                                |
| sqlglot_v2_normalize             | 78.4 ms                                                                                                         | 79.9 ms: 1.02x slower                                                                                               |
| docutils                         | 1.59 sec                                                                                                        | 1.63 sec: 1.02x slower                                                                                              |
| async_tree_eager                 | 71.0 ms                                                                                                         | 72.6 ms: 1.02x slower                                                                                               |
| regex_compile                    | 74.5 ms                                                                                                         | 76.2 ms: 1.02x slower                                                                                               |
| logging_format                   | 4.28 us                                                                                                         | 4.39 us: 1.02x slower                                                                                               |
| sympy_integrate                  | 11.8 ms                                                                                                         | 12.1 ms: 1.03x slower                                                                                               |
| sqlglot_v2_optimize              | 38.6 ms                                                                                                         | 39.6 ms: 1.03x slower                                                                                               |
| hexiom                           | 4.56 ms                                                                                                         | 4.68 ms: 1.03x slower                                                                                               |
| go                               | 77.5 ms                                                                                                         | 79.5 ms: 1.03x slower                                                                                               |
| deltablue                        | 2.61 ms                                                                                                         | 2.69 ms: 1.03x slower                                                                                               |
| bpe_tokeniser                    | 3.66 sec                                                                                                        | 3.76 sec: 1.03x slower                                                                                              |
| logging_simple                   | 3.94 us                                                                                                         | 4.06 us: 1.03x slower                                                                                               |
| k_core                           | 1.54 sec                                                                                                        | 1.59 sec: 1.03x slower                                                                                              |
| tomli_loads                      | 1.39 sec                                                                                                        | 1.44 sec: 1.04x slower                                                                                              |
| shortest_path                    | 329 ms                                                                                                          | 341 ms: 1.04x slower                                                                                                |
| async_generators                 | 314 ms                                                                                                          | 326 ms: 1.04x slower                                                                                                |
| sqlglot_v2_transpile             | 1.05 ms                                                                                                         | 1.09 ms: 1.04x slower                                                                                               |
| scimark_sparse_mat_mult          | 4.03 ms                                                                                                         | 4.20 ms: 1.04x slower                                                                                               |
| sqlglot_v2_parse                 | 857 us                                                                                                          | 895 us: 1.05x slower                                                                                                |
| connected_components             | 301 ms                                                                                                          | 316 ms: 1.05x slower                                                                                                |
| pycparser                        | 745 ms                                                                                                          | 797 ms: 1.07x slower                                                                                                |
| meteor_contest                   | 76.3 ms                                                                                                         | 82.8 ms: 1.09x slower                                                                                               |
| comprehensions                   | 12.0 us                                                                                                         | 13.4 us: 1.12x slower                                                                                               |
| fannkuch                         | 310 ms                                                                                                          | 357 ms: 1.15x slower                                                                                                |
| pprint_safe_repr                 | 589 ms                                                                                                          | 690 ms: 1.17x slower                                                                                                |
| pprint_pformat                   | 1.20 sec                                                                                                        | 1.42 sec: 1.18x slower                                                                                              |
| unpack_sequence                  | 50.8 ns                                                                                                         | 62.4 ns: 1.23x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (31): asyncio_tcp, json_loads, pickle_list, html5lib, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, asyncio_websockets, scimark_lu, thrift, pidigits, subparsers, coroutines, pathlib, coverage, async_tree_none, dask, float, mdp, async_tree_eager_io, nbody, pickle_dict, asyncio_tcp_ssl, async_tree_eager_tg, async_tree_none_tg, json, xml_etree_iterparse, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io, pylint

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x