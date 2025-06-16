# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 170 ms: 1.10x faster                                                            |
| docutils       | 1.51 sec                                                              | 1.45 sec: 1.04x faster                                                          |
| html5lib       | 34.2 ms                                                               | 31.7 ms: 1.08x faster                                                           |
| sphinx         | 617 ms                                                                | 580 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 73.3 ms                                                               | 63.6 ms: 1.15x faster                                                           |
| coroutines                       | 19.3 ms                                                               | 16.9 ms: 1.14x faster                                                           |
| async_tree_none                  | 183 ms                                                                | 163 ms: 1.12x faster                                                            |
| async_tree_eager_tg              | 143 ms                                                                | 129 ms: 1.11x faster                                                            |
| async_tree_memoization           | 215 ms                                                                | 195 ms: 1.10x faster                                                            |
| async_tree_io_tg                 | 405 ms                                                                | 367 ms: 1.10x faster                                                            |
| async_tree_none_tg               | 171 ms                                                                | 156 ms: 1.09x faster                                                            |
| async_tree_io                    | 413 ms                                                                | 379 ms: 1.09x faster                                                            |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 168 ms: 1.08x faster                                                            |
| async_tree_memoization_tg        | 208 ms                                                                | 192 ms: 1.08x faster                                                            |
| async_tree_eager_io              | 392 ms                                                                | 363 ms: 1.08x faster                                                            |
| async_tree_eager_memoization     | 151 ms                                                                | 140 ms: 1.08x faster                                                            |
| async_tree_eager_io_tg           | 402 ms                                                                | 373 ms: 1.08x faster                                                            |
| async_generators                 | 274 ms                                                                | 261 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 414 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 357 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 410 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                | 388 ms: 1.03x faster                                                            |
| Geometric mean                   | (ref)                                                                 | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 57.6 ms                                                               | 49.9 ms: 1.15x faster                                                           |
| nbody          | 84.7 ms                                                               | 74.2 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 81.4 ms                                                               | 71.8 ms: 1.13x faster                                                           |
| regex_v8       | 16.3 ms                                                               | 16.2 ms: 1.00x faster                                                           |
| regex_effbot   | 2.37 ms                                                               | 2.37 ms: 1.00x faster                                                           |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 177 us                                                                | 158 us: 1.12x faster                                                            |
| xml_etree_process    | 43.2 ms                                                               | 38.6 ms: 1.12x faster                                                           |
| pickle_pure_python   | 241 us                                                                | 217 us: 1.11x faster                                                            |
| xml_etree_generate   | 58.5 ms                                                               | 53.3 ms: 1.10x faster                                                           |
| tomli_loads          | 1.45 sec                                                              | 1.36 sec: 1.07x faster                                                          |
| xml_etree_parse      | 105 ms                                                                | 100 ms: 1.05x faster                                                            |
| json_dumps           | 6.81 ms                                                               | 6.61 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 74.1 ms                                                               | 72.7 ms: 1.02x faster                                                           |
| json_loads           | 16.6 us                                                               | 16.4 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                                 | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 14.8 ms                                                               | 13.3 ms: 1.11x faster                                                           |
| python_startup         | 19.4 ms                                                               | 17.7 ms: 1.09x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.10x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.8 ms                                                               | 14.6 ms: 1.22x faster                                                           |
| genshi_xml      | 36.5 ms                                                               | 30.9 ms: 1.18x faster                                                           |
| mako            | 9.00 ms                                                               | 7.74 ms: 1.16x faster                                                           |
| django_template | 25.3 ms                                                               | 21.9 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                       | 31.6 ms                                                               | 24.1 ms: 1.31x faster                                                           |
| genshi_text                      | 17.8 ms                                                               | 14.6 ms: 1.22x faster                                                           |
| chaos                            | 48.4 ms                                                               | 39.7 ms: 1.22x faster                                                           |
| sqlglot_v2_parse                 | 993 us                                                                | 822 us: 1.21x faster                                                            |
| sqlglot_v2_transpile             | 1.17 ms                                                               | 990 us: 1.18x faster                                                            |
| genshi_xml                       | 36.5 ms                                                               | 30.9 ms: 1.18x faster                                                           |
| nqueens                          | 71.4 ms                                                               | 60.7 ms: 1.18x faster                                                           |
| raytrace                         | 212 ms                                                                | 180 ms: 1.17x faster                                                            |
| mako                             | 9.00 ms                                                               | 7.74 ms: 1.16x faster                                                           |
| coverage                         | 336 ms                                                                | 290 ms: 1.16x faster                                                            |
| django_template                  | 25.3 ms                                                               | 21.9 ms: 1.16x faster                                                           |
| float                            | 57.6 ms                                                               | 49.9 ms: 1.15x faster                                                           |
| async_tree_eager                 | 73.3 ms                                                               | 63.6 ms: 1.15x faster                                                           |
| fannkuch                         | 310 ms                                                                | 270 ms: 1.15x faster                                                            |
| go                               | 100 ms                                                                | 87.5 ms: 1.15x faster                                                           |
| nbody                            | 84.7 ms                                                               | 74.2 ms: 1.14x faster                                                           |
| scimark_monte_carlo              | 52.9 ms                                                               | 46.4 ms: 1.14x faster                                                           |
| coroutines                       | 19.3 ms                                                               | 16.9 ms: 1.14x faster                                                           |
| regex_compile                    | 81.4 ms                                                               | 71.8 ms: 1.13x faster                                                           |
| sqlglot_v2_normalize             | 76.8 ms                                                               | 67.8 ms: 1.13x faster                                                           |
| deepcopy_reduce                  | 1.90 us                                                               | 1.69 us: 1.13x faster                                                           |
| deepcopy_memo                    | 21.8 us                                                               | 19.4 us: 1.12x faster                                                           |
| deepcopy                         | 175 us                                                                | 157 us: 1.12x faster                                                            |
| unpickle_pure_python             | 177 us                                                                | 158 us: 1.12x faster                                                            |
| xml_etree_process                | 43.2 ms                                                               | 38.6 ms: 1.12x faster                                                           |
| async_tree_none                  | 183 ms                                                                | 163 ms: 1.12x faster                                                            |
| python_startup_no_site           | 14.8 ms                                                               | 13.3 ms: 1.11x faster                                                           |
| async_tree_eager_tg              | 143 ms                                                                | 129 ms: 1.11x faster                                                            |
| logging_simple                   | 4.07 us                                                               | 3.67 us: 1.11x faster                                                           |
| pickle_pure_python               | 241 us                                                                | 217 us: 1.11x faster                                                            |
| pprint_pformat                   | 1.26 sec                                                              | 1.14 sec: 1.11x faster                                                          |
| logging_format                   | 4.39 us                                                               | 3.97 us: 1.11x faster                                                           |
| pprint_safe_repr                 | 619 ms                                                                | 562 ms: 1.10x faster                                                            |
| async_tree_memoization           | 215 ms                                                                | 195 ms: 1.10x faster                                                            |
| sqlglot_v2_optimize              | 36.6 ms                                                               | 33.2 ms: 1.10x faster                                                           |
| async_tree_io_tg                 | 405 ms                                                                | 367 ms: 1.10x faster                                                            |
| 2to3                             | 186 ms                                                                | 170 ms: 1.10x faster                                                            |
| subparsers                       | 14.9 ms                                                               | 13.6 ms: 1.10x faster                                                           |
| xml_etree_generate               | 58.5 ms                                                               | 53.3 ms: 1.10x faster                                                           |
| sympy_expand                     | 262 ms                                                                | 239 ms: 1.10x faster                                                            |
| hexiom                           | 5.10 ms                                                               | 4.66 ms: 1.09x faster                                                           |
| python_startup                   | 19.4 ms                                                               | 17.7 ms: 1.09x faster                                                           |
| pycparser                        | 742 ms                                                                | 679 ms: 1.09x faster                                                            |
| sympy_str                        | 155 ms                                                                | 142 ms: 1.09x faster                                                            |
| async_tree_none_tg               | 171 ms                                                                | 156 ms: 1.09x faster                                                            |
| typing_runtime_protocols         | 110 us                                                                | 100 us: 1.09x faster                                                            |
| async_tree_io                    | 413 ms                                                                | 379 ms: 1.09x faster                                                            |
| mdp                              | 828 ms                                                                | 759 ms: 1.09x faster                                                            |
| sympy_sum                        | 81.4 ms                                                               | 74.8 ms: 1.09x faster                                                           |
| deltablue                        | 2.81 ms                                                               | 2.59 ms: 1.09x faster                                                           |
| crypto_pyaes                     | 61.3 ms                                                               | 56.5 ms: 1.09x faster                                                           |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 168 ms: 1.08x faster                                                            |
| async_tree_memoization_tg        | 208 ms                                                                | 192 ms: 1.08x faster                                                            |
| async_tree_eager_io              | 392 ms                                                                | 363 ms: 1.08x faster                                                            |
| async_tree_eager_memoization     | 151 ms                                                                | 140 ms: 1.08x faster                                                            |
| async_tree_eager_io_tg           | 402 ms                                                                | 373 ms: 1.08x faster                                                            |
| html5lib                         | 34.2 ms                                                               | 31.7 ms: 1.08x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                                              | 3.06 sec: 1.07x faster                                                          |
| dulwich_log                      | 26.8 ms                                                               | 25.0 ms: 1.07x faster                                                           |
| tomli_loads                      | 1.45 sec                                                              | 1.36 sec: 1.07x faster                                                          |
| sphinx                           | 617 ms                                                                | 580 ms: 1.06x faster                                                            |
| logging_silent                   | 343 ns                                                                | 323 ns: 1.06x faster                                                            |
| pyflate                          | 337 ms                                                                | 318 ms: 1.06x faster                                                            |
| comprehensions                   | 13.1 us                                                               | 12.4 us: 1.06x faster                                                           |
| many_optionals                   | 494 us                                                                | 467 us: 1.06x faster                                                            |
| spectral_norm                    | 74.7 ms                                                               | 71.0 ms: 1.05x faster                                                           |
| scimark_fft                      | 206 ms                                                                | 196 ms: 1.05x faster                                                            |
| telco                            | 4.77 ms                                                               | 4.54 ms: 1.05x faster                                                           |
| async_generators                 | 274 ms                                                                | 261 ms: 1.05x faster                                                            |
| pylint                           | 169 ms                                                                | 161 ms: 1.05x faster                                                            |
| xml_etree_parse                  | 105 ms                                                                | 100 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 414 ms: 1.04x faster                                                            |
| docutils                         | 1.51 sec                                                              | 1.45 sec: 1.04x faster                                                          |
| sympy_integrate                  | 11.4 ms                                                               | 11.0 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 357 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 410 ms: 1.03x faster                                                            |
| json_dumps                       | 6.81 ms                                                               | 6.61 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                | 388 ms: 1.03x faster                                                            |
| scimark_sor                      | 91.1 ms                                                               | 88.6 ms: 1.03x faster                                                           |
| scimark_lu                       | 84.3 ms                                                               | 82.0 ms: 1.03x faster                                                           |
| richards                         | 37.5 ms                                                               | 36.5 ms: 1.03x faster                                                           |
| richards_super                   | 41.9 ms                                                               | 40.9 ms: 1.02x faster                                                           |
| meteor_contest                   | 74.3 ms                                                               | 72.8 ms: 1.02x faster                                                           |
| xml_etree_iterparse              | 74.1 ms                                                               | 72.7 ms: 1.02x faster                                                           |
| pathlib                          | 22.9 ms                                                               | 22.4 ms: 1.02x faster                                                           |
| json                             | 2.95 ms                                                               | 2.92 ms: 1.01x faster                                                           |
| json_loads                       | 16.6 us                                                               | 16.4 us: 1.01x faster                                                           |
| thrift                           | 44.1 ms                                                               | 43.6 ms: 1.01x faster                                                           |
| sqlite_synth                     | 1.62 us                                                               | 1.60 us: 1.01x faster                                                           |
| scimark_sparse_mat_mult          | 3.17 ms                                                               | 3.16 ms: 1.00x faster                                                           |
| regex_v8                         | 16.3 ms                                                               | 16.2 ms: 1.00x faster                                                           |
| dask                             | 771 ms                                                                | 769 ms: 1.00x faster                                                            |
| regex_effbot                     | 2.37 ms                                                               | 2.37 ms: 1.00x faster                                                           |
| regex_dna                        | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| shortest_path                    | 327 ms                                                                | 332 ms: 1.01x slower                                                            |
| connected_components             | 303 ms                                                                | 311 ms: 1.03x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.08x faster                                                                    |

Benchmark hidden because not significant (5): create_gc_cycles, pidigits, asyncio_websockets, gc_traversal, k_core

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.01x