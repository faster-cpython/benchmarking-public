# Results vs. base

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 177 ms                                                                                                            | 166 ms: 1.07x faster                                                                                                  |
| docutils       | 1.49 sec                                                                                                          | 1.44 sec: 1.03x faster                                                                                                |
| html5lib       | 34.0 ms                                                                                                           | 29.8 ms: 1.14x faster                                                                                                 |
| sphinx         | 606 ms                                                                                                            | 575 ms: 1.05x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io                    | 417 ms                                                                                                            | 371 ms: 1.12x faster                                                                                                  |
| coroutines                       | 18.6 ms                                                                                                           | 16.6 ms: 1.12x faster                                                                                                 |
| async_tree_memoization           | 217 ms                                                                                                            | 195 ms: 1.11x faster                                                                                                  |
| async_tree_eager                 | 69.8 ms                                                                                                           | 62.8 ms: 1.11x faster                                                                                                 |
| async_tree_none                  | 179 ms                                                                                                            | 161 ms: 1.11x faster                                                                                                  |
| async_tree_eager_io              | 398 ms                                                                                                            | 359 ms: 1.11x faster                                                                                                  |
| async_tree_io_tg                 | 398 ms                                                                                                            | 360 ms: 1.11x faster                                                                                                  |
| async_tree_none_tg               | 170 ms                                                                                                            | 155 ms: 1.10x faster                                                                                                  |
| async_tree_memoization_tg        | 214 ms                                                                                                            | 196 ms: 1.09x faster                                                                                                  |
| async_tree_eager_io_tg           | 407 ms                                                                                                            | 374 ms: 1.09x faster                                                                                                  |
| async_tree_eager_tg              | 143 ms                                                                                                            | 132 ms: 1.09x faster                                                                                                  |
| async_tree_eager_memoization_tg  | 191 ms                                                                                                            | 176 ms: 1.09x faster                                                                                                  |
| async_tree_eager_memoization     | 152 ms                                                                                                            | 141 ms: 1.08x faster                                                                                                  |
| async_tree_cpu_io_mixed          | 437 ms                                                                                                            | 415 ms: 1.05x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 431 ms                                                                                                            | 420 ms: 1.03x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 403 ms                                                                                                            | 395 ms: 1.02x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                                                            | 360 ms: 1.02x faster                                                                                                  |
| async_generators                 | 266 ms                                                                                                            | 271 ms: 1.02x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                                                           | 64.6 ms: 1.43x faster                                                                                                 |
| float          | 54.3 ms                                                                                                           | 47.4 ms: 1.15x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.18x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 77.8 ms                                                                                                           | 68.9 ms: 1.13x faster                                                                                                 |
| regex_v8       | 16.8 ms                                                                                                           | 16.7 ms: 1.01x faster                                                                                                 |
| regex_dna      | 140 ms                                                                                                            | 140 ms: 1.00x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 169 us                                                                                                            | 134 us: 1.26x faster                                                                                                  |
| tomli_loads          | 1.45 sec                                                                                                          | 1.20 sec: 1.20x faster                                                                                                |
| xml_etree_process    | 42.7 ms                                                                                                           | 35.8 ms: 1.19x faster                                                                                                 |
| pickle_pure_python   | 230 us                                                                                                            | 197 us: 1.17x faster                                                                                                  |
| xml_etree_generate   | 58.2 ms                                                                                                           | 50.8 ms: 1.15x faster                                                                                                 |
| xml_etree_iterparse  | 74.9 ms                                                                                                           | 70.8 ms: 1.06x faster                                                                                                 |
| json_dumps           | 7.57 ms                                                                                                           | 7.23 ms: 1.05x faster                                                                                                 |
| json_loads           | 17.8 us                                                                                                           | 17.6 us: 1.01x faster                                                                                                 |
| xml_etree_parse      | 104 ms                                                                                                            | 102 ms: 1.01x faster                                                                                                  |
| unpickle             | 9.18 us                                                                                                           | 9.22 us: 1.00x slower                                                                                                 |
| pickle_list          | 3.04 us                                                                                                           | 3.07 us: 1.01x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmark hidden because not significant (3): pickle, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.12 ms                                                                                                           | 6.47 ms: 1.26x faster                                                                                                 |
| genshi_text     | 16.4 ms                                                                                                           | 13.9 ms: 1.18x faster                                                                                                 |
| genshi_xml      | 34.0 ms                                                                                                           | 29.2 ms: 1.17x faster                                                                                                 |
| django_template | 24.2 ms                                                                                                           | 21.0 ms: 1.15x faster                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.19x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody                            | 92.1 ms                                                                                                           | 64.6 ms: 1.43x faster                                                                                                 |
| unpickle_pure_python             | 169 us                                                                                                            | 134 us: 1.26x faster                                                                                                  |
| mako                             | 8.12 ms                                                                                                           | 6.47 ms: 1.26x faster                                                                                                 |
| generators                       | 29.0 ms                                                                                                           | 23.3 ms: 1.24x faster                                                                                                 |
| richards                         | 38.6 ms                                                                                                           | 32.1 ms: 1.20x faster                                                                                                 |
| tomli_loads                      | 1.45 sec                                                                                                          | 1.20 sec: 1.20x faster                                                                                                |
| hexiom                           | 5.26 ms                                                                                                           | 4.37 ms: 1.20x faster                                                                                                 |
| xml_etree_process                | 42.7 ms                                                                                                           | 35.8 ms: 1.19x faster                                                                                                 |
| raytrace                         | 212 ms                                                                                                            | 178 ms: 1.19x faster                                                                                                  |
| deltablue                        | 2.80 ms                                                                                                           | 2.37 ms: 1.18x faster                                                                                                 |
| genshi_text                      | 16.4 ms                                                                                                           | 13.9 ms: 1.18x faster                                                                                                 |
| richards_super                   | 42.8 ms                                                                                                           | 36.3 ms: 1.18x faster                                                                                                 |
| go                               | 94.8 ms                                                                                                           | 81.0 ms: 1.17x faster                                                                                                 |
| pickle_pure_python               | 230 us                                                                                                            | 197 us: 1.17x faster                                                                                                  |
| genshi_xml                       | 34.0 ms                                                                                                           | 29.2 ms: 1.17x faster                                                                                                 |
| scimark_sor                      | 92.4 ms                                                                                                           | 79.8 ms: 1.16x faster                                                                                                 |
| deepcopy_memo                    | 21.0 us                                                                                                           | 18.2 us: 1.16x faster                                                                                                 |
| django_template                  | 24.2 ms                                                                                                           | 21.0 ms: 1.15x faster                                                                                                 |
| scimark_monte_carlo              | 50.0 ms                                                                                                           | 43.3 ms: 1.15x faster                                                                                                 |
| float                            | 54.3 ms                                                                                                           | 47.4 ms: 1.15x faster                                                                                                 |
| logging_simple                   | 3.71 us                                                                                                           | 3.23 us: 1.15x faster                                                                                                 |
| xml_etree_generate               | 58.2 ms                                                                                                           | 50.8 ms: 1.15x faster                                                                                                 |
| pyflate                          | 351 ms                                                                                                            | 307 ms: 1.14x faster                                                                                                  |
| html5lib                         | 34.0 ms                                                                                                           | 29.8 ms: 1.14x faster                                                                                                 |
| scimark_lu                       | 83.3 ms                                                                                                           | 73.2 ms: 1.14x faster                                                                                                 |
| comprehensions                   | 13.0 us                                                                                                           | 11.4 us: 1.14x faster                                                                                                 |
| logging_format                   | 4.01 us                                                                                                           | 3.54 us: 1.13x faster                                                                                                 |
| regex_compile                    | 77.8 ms                                                                                                           | 68.9 ms: 1.13x faster                                                                                                 |
| chaos                            | 44.3 ms                                                                                                           | 39.2 ms: 1.13x faster                                                                                                 |
| typing_runtime_protocols         | 104 us                                                                                                            | 92.2 us: 1.12x faster                                                                                                 |
| async_tree_io                    | 417 ms                                                                                                            | 371 ms: 1.12x faster                                                                                                  |
| logging_silent                   | 73.0 ns                                                                                                           | 65.1 ns: 1.12x faster                                                                                                 |
| coroutines                       | 18.6 ms                                                                                                           | 16.6 ms: 1.12x faster                                                                                                 |
| deepcopy_reduce                  | 1.76 us                                                                                                           | 1.57 us: 1.12x faster                                                                                                 |
| deepcopy                         | 168 us                                                                                                            | 151 us: 1.11x faster                                                                                                  |
| nqueens                          | 65.0 ms                                                                                                           | 58.4 ms: 1.11x faster                                                                                                 |
| async_tree_memoization           | 217 ms                                                                                                            | 195 ms: 1.11x faster                                                                                                  |
| async_tree_eager                 | 69.8 ms                                                                                                           | 62.8 ms: 1.11x faster                                                                                                 |
| async_tree_none                  | 179 ms                                                                                                            | 161 ms: 1.11x faster                                                                                                  |
| async_tree_eager_io              | 398 ms                                                                                                            | 359 ms: 1.11x faster                                                                                                  |
| async_tree_io_tg                 | 398 ms                                                                                                            | 360 ms: 1.11x faster                                                                                                  |
| sqlglot_normalize                | 199 ms                                                                                                            | 180 ms: 1.10x faster                                                                                                  |
| async_tree_none_tg               | 170 ms                                                                                                            | 155 ms: 1.10x faster                                                                                                  |
| bpe_tokeniser                    | 3.23 sec                                                                                                          | 2.94 sec: 1.10x faster                                                                                                |
| spectral_norm                    | 77.8 ms                                                                                                           | 71.2 ms: 1.09x faster                                                                                                 |
| sympy_str                        | 153 ms                                                                                                            | 141 ms: 1.09x faster                                                                                                  |
| async_tree_memoization_tg        | 214 ms                                                                                                            | 196 ms: 1.09x faster                                                                                                  |
| async_tree_eager_io_tg           | 407 ms                                                                                                            | 374 ms: 1.09x faster                                                                                                  |
| async_tree_eager_tg              | 143 ms                                                                                                            | 132 ms: 1.09x faster                                                                                                  |
| pprint_pformat                   | 1.06 sec                                                                                                          | 977 ms: 1.09x faster                                                                                                  |
| scimark_fft                      | 197 ms                                                                                                            | 182 ms: 1.09x faster                                                                                                  |
| sqlglot_optimize                 | 36.0 ms                                                                                                           | 33.1 ms: 1.09x faster                                                                                                 |
| async_tree_eager_memoization_tg  | 191 ms                                                                                                            | 176 ms: 1.09x faster                                                                                                  |
| sympy_expand                     | 258 ms                                                                                                            | 239 ms: 1.08x faster                                                                                                  |
| pprint_safe_repr                 | 527 ms                                                                                                            | 488 ms: 1.08x faster                                                                                                  |
| subparsers                       | 13.0 ms                                                                                                           | 12.0 ms: 1.08x faster                                                                                                 |
| sympy_sum                        | 79.4 ms                                                                                                           | 73.7 ms: 1.08x faster                                                                                                 |
| sympy_integrate                  | 12.3 ms                                                                                                           | 11.4 ms: 1.08x faster                                                                                                 |
| async_tree_eager_memoization     | 152 ms                                                                                                            | 141 ms: 1.08x faster                                                                                                  |
| sqlglot_transpile                | 1.11 ms                                                                                                           | 1.03 ms: 1.08x faster                                                                                                 |
| bench_thread_pool                | 525 us                                                                                                            | 490 us: 1.07x faster                                                                                                  |
| 2to3                             | 177 ms                                                                                                            | 166 ms: 1.07x faster                                                                                                  |
| xml_etree_iterparse              | 74.9 ms                                                                                                           | 70.8 ms: 1.06x faster                                                                                                 |
| crypto_pyaes                     | 58.5 ms                                                                                                           | 55.3 ms: 1.06x faster                                                                                                 |
| pylint                           | 171 ms                                                                                                            | 162 ms: 1.06x faster                                                                                                  |
| fannkuch                         | 298 ms                                                                                                            | 282 ms: 1.06x faster                                                                                                  |
| thrift                           | 461 us                                                                                                            | 437 us: 1.06x faster                                                                                                  |
| sqlalchemy_declarative           | 62.0 ms                                                                                                           | 58.7 ms: 1.05x faster                                                                                                 |
| sphinx                           | 606 ms                                                                                                            | 575 ms: 1.05x faster                                                                                                  |
| sqlalchemy_imperative            | 7.02 ms                                                                                                           | 6.67 ms: 1.05x faster                                                                                                 |
| async_tree_cpu_io_mixed          | 437 ms                                                                                                            | 415 ms: 1.05x faster                                                                                                  |
| dulwich_log                      | 29.4 ms                                                                                                           | 28.1 ms: 1.05x faster                                                                                                 |
| connected_components             | 316 ms                                                                                                            | 301 ms: 1.05x faster                                                                                                  |
| telco                            | 4.74 ms                                                                                                           | 4.52 ms: 1.05x faster                                                                                                 |
| json_dumps                       | 7.57 ms                                                                                                           | 7.23 ms: 1.05x faster                                                                                                 |
| pycparser                        | 704 ms                                                                                                            | 674 ms: 1.04x faster                                                                                                  |
| scimark_sparse_mat_mult          | 3.09 ms                                                                                                           | 2.96 ms: 1.04x faster                                                                                                 |
| coverage                         | 47.9 ms                                                                                                           | 46.0 ms: 1.04x faster                                                                                                 |
| sqlglot_parse                    | 896 us                                                                                                            | 861 us: 1.04x faster                                                                                                  |
| meteor_contest                   | 77.6 ms                                                                                                           | 74.8 ms: 1.04x faster                                                                                                 |
| docutils                         | 1.49 sec                                                                                                          | 1.44 sec: 1.03x faster                                                                                                |
| mdp                              | 1.56 sec                                                                                                          | 1.51 sec: 1.03x faster                                                                                                |
| shortest_path                    | 348 ms                                                                                                            | 338 ms: 1.03x faster                                                                                                  |
| many_optionals                   | 467 us                                                                                                            | 453 us: 1.03x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 431 ms                                                                                                            | 420 ms: 1.03x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 403 ms                                                                                                            | 395 ms: 1.02x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                                                            | 360 ms: 1.02x faster                                                                                                  |
| k_core                           | 1.55 sec                                                                                                          | 1.52 sec: 1.02x faster                                                                                                |
| pathlib                          | 23.9 ms                                                                                                           | 23.5 ms: 1.02x faster                                                                                                 |
| json                             | 3.04 ms                                                                                                           | 2.99 ms: 1.02x faster                                                                                                 |
| json_loads                       | 17.8 us                                                                                                           | 17.6 us: 1.01x faster                                                                                                 |
| xml_etree_parse                  | 104 ms                                                                                                            | 102 ms: 1.01x faster                                                                                                  |
| regex_v8                         | 16.8 ms                                                                                                           | 16.7 ms: 1.01x faster                                                                                                 |
| regex_dna                        | 140 ms                                                                                                            | 140 ms: 1.00x slower                                                                                                  |
| sqlite_synth                     | 1.54 us                                                                                                           | 1.55 us: 1.00x slower                                                                                                 |
| unpickle                         | 9.18 us                                                                                                           | 9.22 us: 1.00x slower                                                                                                 |
| pickle_list                      | 3.04 us                                                                                                           | 3.07 us: 1.01x slower                                                                                                 |
| async_generators                 | 266 ms                                                                                                            | 271 ms: 1.02x slower                                                                                                  |
| unpack_sequence                  | 52.4 ns                                                                                                           | 60.0 ns: 1.14x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.08x faster                                                                                                          |

Benchmark hidden because not significant (14): asyncio_tcp_ssl, create_gc_cycles, pickle, dask, bench_mp_pool, gc_traversal, asyncio_websockets, regex_effbot, pidigits, unpickle_list, python_startup_no_site, pickle_dict, python_startup, asyncio_tcp

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.02x