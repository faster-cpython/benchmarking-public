# Results vs. base

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: darwin-arm64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 170 ms: 1.10x faster                                                         |
| docutils       | 1.51 sec                                                              | 1.44 sec: 1.05x faster                                                       |
| html5lib       | 34.2 ms                                                               | 31.7 ms: 1.08x faster                                                        |
| sphinx         | 614 ms                                                                | 584 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager                 | 72.9 ms                                                               | 64.1 ms: 1.14x faster                                                        |
| coroutines                       | 19.3 ms                                                               | 17.1 ms: 1.13x faster                                                        |
| async_tree_none                  | 182 ms                                                                | 165 ms: 1.11x faster                                                         |
| async_tree_eager_tg              | 143 ms                                                                | 129 ms: 1.11x faster                                                         |
| async_tree_memoization           | 215 ms                                                                | 196 ms: 1.10x faster                                                         |
| async_tree_none_tg               | 171 ms                                                                | 157 ms: 1.09x faster                                                         |
| async_tree_io                    | 413 ms                                                                | 380 ms: 1.09x faster                                                         |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 168 ms: 1.08x faster                                                         |
| async_tree_io_tg                 | 405 ms                                                                | 375 ms: 1.08x faster                                                         |
| async_tree_eager_io              | 392 ms                                                                | 364 ms: 1.08x faster                                                         |
| async_tree_memoization_tg        | 207 ms                                                                | 192 ms: 1.08x faster                                                         |
| async_tree_eager_memoization     | 151 ms                                                                | 140 ms: 1.08x faster                                                         |
| async_tree_eager_io_tg           | 402 ms                                                                | 374 ms: 1.07x faster                                                         |
| async_generators                 | 274 ms                                                                | 262 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed          | 433 ms                                                                | 418 ms: 1.04x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 357 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 423 ms                                                                | 411 ms: 1.03x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 389 ms: 1.03x faster                                                         |
| Geometric mean                   | (ref)                                                                 | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 57.5 ms                                                               | 49.6 ms: 1.16x faster                                                        |
| nbody          | 84.6 ms                                                               | 73.8 ms: 1.15x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 81.1 ms                                                               | 71.8 ms: 1.13x faster                                                        |
| regex_v8       | 16.3 ms                                                               | 16.1 ms: 1.02x faster                                                        |
| regex_effbot   | 2.37 ms                                                               | 2.35 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 178 us                                                                | 160 us: 1.11x faster                                                         |
| xml_etree_process    | 43.1 ms                                                               | 38.9 ms: 1.11x faster                                                        |
| pickle_pure_python   | 241 us                                                                | 218 us: 1.11x faster                                                         |
| xml_etree_generate   | 58.1 ms                                                               | 53.7 ms: 1.08x faster                                                        |
| tomli_loads          | 1.44 sec                                                              | 1.36 sec: 1.06x faster                                                       |
| json_dumps           | 6.79 ms                                                               | 6.54 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 74.0 ms                                                               | 72.7 ms: 1.02x faster                                                        |
| xml_etree_parse      | 104 ms                                                                | 103 ms: 1.01x faster                                                         |
| json_loads           | 16.5 us                                                               | 16.5 us: 1.00x faster                                                        |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 12.0 ms                                                               | 11.6 ms: 1.03x faster                                                        |
| python_startup         | 16.4 ms                                                               | 15.9 ms: 1.03x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.03x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 14.6 ms: 1.22x faster                                                        |
| mako            | 9.03 ms                                                               | 7.72 ms: 1.17x faster                                                        |
| genshi_xml      | 36.4 ms                                                               | 31.2 ms: 1.17x faster                                                        |
| django_template | 25.2 ms                                                               | 22.0 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.17x faster                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators                       | 31.5 ms                                                               | 24.1 ms: 1.31x faster                                                        |
| genshi_text                      | 17.7 ms                                                               | 14.6 ms: 1.22x faster                                                        |
| chaos                            | 48.4 ms                                                               | 40.1 ms: 1.21x faster                                                        |
| sqlglot_v2_parse                 | 992 us                                                                | 829 us: 1.20x faster                                                         |
| sqlglot_v2_transpile             | 1.18 ms                                                               | 1000 us: 1.18x faster                                                        |
| raytrace                         | 212 ms                                                                | 180 ms: 1.17x faster                                                         |
| mako                             | 9.03 ms                                                               | 7.72 ms: 1.17x faster                                                        |
| genshi_xml                       | 36.4 ms                                                               | 31.2 ms: 1.17x faster                                                        |
| fannkuch                         | 310 ms                                                                | 266 ms: 1.16x faster                                                         |
| nqueens                          | 71.4 ms                                                               | 61.5 ms: 1.16x faster                                                        |
| coverage                         | 337 ms                                                                | 290 ms: 1.16x faster                                                         |
| float                            | 57.5 ms                                                               | 49.6 ms: 1.16x faster                                                        |
| scimark_monte_carlo              | 53.0 ms                                                               | 46.2 ms: 1.15x faster                                                        |
| go                               | 100 ms                                                                | 87.6 ms: 1.15x faster                                                        |
| nbody                            | 84.6 ms                                                               | 73.8 ms: 1.15x faster                                                        |
| django_template                  | 25.2 ms                                                               | 22.0 ms: 1.15x faster                                                        |
| typing_runtime_protocols         | 110 us                                                                | 95.9 us: 1.14x faster                                                        |
| async_tree_eager                 | 72.9 ms                                                               | 64.1 ms: 1.14x faster                                                        |
| deepcopy_memo                    | 21.8 us                                                               | 19.2 us: 1.14x faster                                                        |
| coroutines                       | 19.3 ms                                                               | 17.1 ms: 1.13x faster                                                        |
| deepcopy_reduce                  | 1.90 us                                                               | 1.69 us: 1.13x faster                                                        |
| regex_compile                    | 81.1 ms                                                               | 71.8 ms: 1.13x faster                                                        |
| deepcopy                         | 176 us                                                                | 156 us: 1.13x faster                                                         |
| sqlglot_v2_normalize             | 76.3 ms                                                               | 68.1 ms: 1.12x faster                                                        |
| pprint_pformat                   | 1.26 sec                                                              | 1.13 sec: 1.12x faster                                                       |
| pprint_safe_repr                 | 621 ms                                                                | 558 ms: 1.11x faster                                                         |
| unpickle_pure_python             | 178 us                                                                | 160 us: 1.11x faster                                                         |
| xml_etree_process                | 43.1 ms                                                               | 38.9 ms: 1.11x faster                                                        |
| async_tree_none                  | 182 ms                                                                | 165 ms: 1.11x faster                                                         |
| async_tree_eager_tg              | 143 ms                                                                | 129 ms: 1.11x faster                                                         |
| pickle_pure_python               | 241 us                                                                | 218 us: 1.11x faster                                                         |
| logging_simple                   | 4.06 us                                                               | 3.68 us: 1.10x faster                                                        |
| async_tree_memoization           | 215 ms                                                                | 196 ms: 1.10x faster                                                         |
| 2to3                             | 186 ms                                                                | 170 ms: 1.10x faster                                                         |
| pycparser                        | 743 ms                                                                | 678 ms: 1.10x faster                                                         |
| comprehensions                   | 13.1 us                                                               | 12.0 us: 1.10x faster                                                        |
| sqlglot_v2_optimize              | 36.4 ms                                                               | 33.3 ms: 1.09x faster                                                        |
| logging_format                   | 4.37 us                                                               | 4.00 us: 1.09x faster                                                        |
| deltablue                        | 2.81 ms                                                               | 2.58 ms: 1.09x faster                                                        |
| hexiom                           | 5.10 ms                                                               | 4.68 ms: 1.09x faster                                                        |
| async_tree_none_tg               | 171 ms                                                                | 157 ms: 1.09x faster                                                         |
| mdp                              | 828 ms                                                                | 761 ms: 1.09x faster                                                         |
| sympy_expand                     | 261 ms                                                                | 240 ms: 1.09x faster                                                         |
| async_tree_io                    | 413 ms                                                                | 380 ms: 1.09x faster                                                         |
| subparsers                       | 14.8 ms                                                               | 13.7 ms: 1.08x faster                                                        |
| xml_etree_generate               | 58.1 ms                                                               | 53.7 ms: 1.08x faster                                                        |
| async_tree_eager_memoization_tg  | 182 ms                                                                | 168 ms: 1.08x faster                                                         |
| async_tree_io_tg                 | 405 ms                                                                | 375 ms: 1.08x faster                                                         |
| crypto_pyaes                     | 61.7 ms                                                               | 57.2 ms: 1.08x faster                                                        |
| async_tree_eager_io              | 392 ms                                                                | 364 ms: 1.08x faster                                                         |
| sympy_str                        | 154 ms                                                                | 143 ms: 1.08x faster                                                         |
| async_tree_memoization_tg        | 207 ms                                                                | 192 ms: 1.08x faster                                                         |
| html5lib                         | 34.2 ms                                                               | 31.7 ms: 1.08x faster                                                        |
| async_tree_eager_memoization     | 151 ms                                                                | 140 ms: 1.08x faster                                                         |
| sympy_sum                        | 81.2 ms                                                               | 75.5 ms: 1.07x faster                                                        |
| async_tree_eager_io_tg           | 402 ms                                                                | 374 ms: 1.07x faster                                                         |
| dulwich_log                      | 26.8 ms                                                               | 25.0 ms: 1.07x faster                                                        |
| bpe_tokeniser                    | 3.28 sec                                                              | 3.08 sec: 1.06x faster                                                       |
| pyflate                          | 337 ms                                                                | 317 ms: 1.06x faster                                                         |
| many_optionals                   | 493 us                                                                | 466 us: 1.06x faster                                                         |
| telco                            | 4.77 ms                                                               | 4.51 ms: 1.06x faster                                                        |
| tomli_loads                      | 1.44 sec                                                              | 1.36 sec: 1.06x faster                                                       |
| spectral_norm                    | 74.7 ms                                                               | 70.7 ms: 1.06x faster                                                        |
| scimark_fft                      | 206 ms                                                                | 195 ms: 1.05x faster                                                         |
| richards_super                   | 41.8 ms                                                               | 39.7 ms: 1.05x faster                                                        |
| sphinx                           | 614 ms                                                                | 584 ms: 1.05x faster                                                         |
| docutils                         | 1.51 sec                                                              | 1.44 sec: 1.05x faster                                                       |
| async_generators                 | 274 ms                                                                | 262 ms: 1.04x faster                                                         |
| pylint                           | 168 ms                                                                | 161 ms: 1.04x faster                                                         |
| richards                         | 37.4 ms                                                               | 35.8 ms: 1.04x faster                                                        |
| json_dumps                       | 6.79 ms                                                               | 6.54 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed          | 433 ms                                                                | 418 ms: 1.04x faster                                                         |
| python_startup_no_site           | 12.0 ms                                                               | 11.6 ms: 1.03x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                | 357 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 423 ms                                                                | 411 ms: 1.03x faster                                                         |
| sympy_integrate                  | 11.4 ms                                                               | 11.0 ms: 1.03x faster                                                        |
| python_startup                   | 16.4 ms                                                               | 15.9 ms: 1.03x faster                                                        |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 389 ms: 1.03x faster                                                         |
| scimark_sor                      | 90.9 ms                                                               | 88.7 ms: 1.03x faster                                                        |
| logging_silent                   | 336 ns                                                                | 328 ns: 1.02x faster                                                         |
| meteor_contest                   | 75.0 ms                                                               | 73.7 ms: 1.02x faster                                                        |
| xml_etree_iterparse              | 74.0 ms                                                               | 72.7 ms: 1.02x faster                                                        |
| pathlib                          | 24.3 ms                                                               | 23.9 ms: 1.02x faster                                                        |
| regex_v8                         | 16.3 ms                                                               | 16.1 ms: 1.02x faster                                                        |
| sqlite_synth                     | 1.62 us                                                               | 1.60 us: 1.01x faster                                                        |
| scimark_lu                       | 84.4 ms                                                               | 83.5 ms: 1.01x faster                                                        |
| regex_effbot                     | 2.37 ms                                                               | 2.35 ms: 1.01x faster                                                        |
| thrift                           | 43.9 ms                                                               | 43.5 ms: 1.01x faster                                                        |
| xml_etree_parse                  | 104 ms                                                                | 103 ms: 1.01x faster                                                         |
| json_loads                       | 16.5 us                                                               | 16.5 us: 1.00x faster                                                        |
| dask                             | 771 ms                                                                | 769 ms: 1.00x faster                                                         |
| create_gc_cycles                 | 1.35 ms                                                               | 1.36 ms: 1.00x slower                                                        |
| shortest_path                    | 327 ms                                                                | 329 ms: 1.01x slower                                                         |
| connected_components             | 302 ms                                                                | 307 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult          | 3.17 ms                                                               | 3.23 ms: 1.02x slower                                                        |
| Geometric mean                   | (ref)                                                                 | 1.08x faster                                                                 |

Benchmark hidden because not significant (6): asyncio_websockets, regex_dna, pidigits, gc_traversal, json, k_core

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.00x