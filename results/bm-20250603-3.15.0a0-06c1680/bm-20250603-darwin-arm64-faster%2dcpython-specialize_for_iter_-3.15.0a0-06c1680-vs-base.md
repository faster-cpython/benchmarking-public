# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.067x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 211 ms                                                                | 220 ms: 1.04x slower                                                            |
| docutils       | 1.48 sec                                                              | 1.51 sec: 1.02x slower                                                          |
| html5lib       | 31.7 ms                                                               | 34.0 ms: 1.07x slower                                                           |
| sphinx         | 588 ms                                                                | 612 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 391 ms                                                                | 403 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg       | 413 ms                                                                | 426 ms: 1.03x slower                                                            |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                | 373 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed          | 416 ms                                                                | 436 ms: 1.05x slower                                                            |
| async_generators                 | 262 ms                                                                | 275 ms: 1.05x slower                                                            |
| async_tree_eager_io_tg           | 379 ms                                                                | 406 ms: 1.07x slower                                                            |
| async_tree_memoization_tg        | 194 ms                                                                | 209 ms: 1.08x slower                                                            |
| async_tree_eager_memoization_tg  | 171 ms                                                                | 184 ms: 1.08x slower                                                            |
| async_tree_eager_io              | 369 ms                                                                | 398 ms: 1.08x slower                                                            |
| async_tree_eager_memoization     | 141 ms                                                                | 153 ms: 1.09x slower                                                            |
| async_tree_none_tg               | 159 ms                                                                | 172 ms: 1.09x slower                                                            |
| async_tree_io                    | 383 ms                                                                | 417 ms: 1.09x slower                                                            |
| async_tree_io_tg                 | 374 ms                                                                | 408 ms: 1.09x slower                                                            |
| async_tree_memoization           | 197 ms                                                                | 216 ms: 1.09x slower                                                            |
| async_tree_eager_tg              | 130 ms                                                                | 144 ms: 1.11x slower                                                            |
| async_tree_none                  | 165 ms                                                                | 185 ms: 1.12x slower                                                            |
| coroutines                       | 17.1 ms                                                               | 19.3 ms: 1.13x slower                                                           |
| async_tree_eager                 | 64.4 ms                                                               | 73.4 ms: 1.14x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.08x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 75.3 ms                                                               | 85.1 ms: 1.13x slower                                                           |
| float          | 49.9 ms                                                               | 59.3 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| regex_v8       | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| regex_compile  | 72.0 ms                                                               | 81.2 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 103 ms                                                                | 101 ms: 1.01x faster                                                            |
| json_loads           | 16.4 us                                                               | 16.6 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 73.4 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| json_dumps           | 6.55 ms                                                               | 6.84 ms: 1.04x slower                                                           |
| tomli_loads          | 1.36 sec                                                              | 1.44 sec: 1.06x slower                                                          |
| xml_etree_generate   | 53.7 ms                                                               | 58.3 ms: 1.08x slower                                                           |
| pickle_pure_python   | 219 us                                                                | 241 us: 1.10x slower                                                            |
| xml_etree_process    | 39.0 ms                                                               | 43.3 ms: 1.11x slower                                                           |
| unpickle_pure_python | 161 us                                                                | 179 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                               | 14.2 ms: 1.11x faster                                                           |
| python_startup         | 20.3 ms                                                               | 18.7 ms: 1.09x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.10x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.2 ms                                                               | 25.0 ms: 1.13x slower                                                           |
| mako            | 7.81 ms                                                               | 8.98 ms: 1.15x slower                                                           |
| genshi_xml      | 31.3 ms                                                               | 36.2 ms: 1.15x slower                                                           |
| genshi_text     | 14.7 ms                                                               | 17.6 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.16x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site           | 15.8 ms                                                               | 14.2 ms: 1.11x faster                                                           |
| python_startup                   | 20.3 ms                                                               | 18.7 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult          | 3.23 ms                                                               | 3.18 ms: 1.02x faster                                                           |
| connected_components             | 321 ms                                                                | 317 ms: 1.01x faster                                                            |
| xml_etree_parse                  | 103 ms                                                                | 101 ms: 1.01x faster                                                            |
| shortest_path                    | 344 ms                                                                | 342 ms: 1.00x faster                                                            |
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                            |
| regex_effbot                     | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| create_gc_cycles                 | 1.35 ms                                                               | 1.36 ms: 1.01x slower                                                           |
| json_loads                       | 16.4 us                                                               | 16.6 us: 1.01x slower                                                           |
| thrift                           | 43.6 ms                                                               | 44.1 ms: 1.01x slower                                                           |
| regex_v8                         | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| scimark_lu                       | 83.6 ms                                                               | 84.7 ms: 1.01x slower                                                           |
| xml_etree_iterparse              | 73.4 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| sqlite_synth                     | 1.60 us                                                               | 1.62 us: 1.02x slower                                                           |
| meteor_contest                   | 73.6 ms                                                               | 74.9 ms: 1.02x slower                                                           |
| richards_super                   | 41.5 ms                                                               | 42.4 ms: 1.02x slower                                                           |
| logging_silent                   | 339 ns                                                                | 347 ns: 1.02x slower                                                            |
| docutils                         | 1.48 sec                                                              | 1.51 sec: 1.02x slower                                                          |
| scimark_sor                      | 89.0 ms                                                               | 91.2 ms: 1.02x slower                                                           |
| sympy_integrate                  | 11.0 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| dask                             | 827 ms                                                                | 849 ms: 1.03x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 391 ms                                                                | 403 ms: 1.03x slower                                                            |
| json                             | 2.90 ms                                                               | 2.98 ms: 1.03x slower                                                           |
| pylint                           | 164 ms                                                                | 169 ms: 1.03x slower                                                            |
| pathlib                          | 23.3 ms                                                               | 24.0 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg       | 413 ms                                                                | 426 ms: 1.03x slower                                                            |
| richards                         | 36.7 ms                                                               | 37.9 ms: 1.03x slower                                                           |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                | 373 ms: 1.04x slower                                                            |
| sphinx                           | 588 ms                                                                | 612 ms: 1.04x slower                                                            |
| pyflate                          | 325 ms                                                                | 339 ms: 1.04x slower                                                            |
| 2to3                             | 211 ms                                                                | 220 ms: 1.04x slower                                                            |
| json_dumps                       | 6.55 ms                                                               | 6.84 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed          | 416 ms                                                                | 436 ms: 1.05x slower                                                            |
| telco                            | 4.55 ms                                                               | 4.78 ms: 1.05x slower                                                           |
| async_generators                 | 262 ms                                                                | 275 ms: 1.05x slower                                                            |
| bpe_tokeniser                    | 3.09 sec                                                              | 3.26 sec: 1.05x slower                                                          |
| spectral_norm                    | 71.0 ms                                                               | 74.8 ms: 1.05x slower                                                           |
| scimark_fft                      | 196 ms                                                                | 208 ms: 1.06x slower                                                            |
| tomli_loads                      | 1.36 sec                                                              | 1.44 sec: 1.06x slower                                                          |
| dulwich_log                      | 25.0 ms                                                               | 26.6 ms: 1.06x slower                                                           |
| crypto_pyaes                     | 57.2 ms                                                               | 61.0 ms: 1.07x slower                                                           |
| many_optionals                   | 467 us                                                                | 498 us: 1.07x slower                                                            |
| html5lib                         | 31.7 ms                                                               | 34.0 ms: 1.07x slower                                                           |
| async_tree_eager_io_tg           | 379 ms                                                                | 406 ms: 1.07x slower                                                            |
| sympy_sum                        | 75.9 ms                                                               | 81.5 ms: 1.07x slower                                                           |
| async_tree_memoization_tg        | 194 ms                                                                | 209 ms: 1.08x slower                                                            |
| sympy_expand                     | 242 ms                                                                | 260 ms: 1.08x slower                                                            |
| async_tree_eager_memoization_tg  | 171 ms                                                                | 184 ms: 1.08x slower                                                            |
| async_tree_eager_io              | 369 ms                                                                | 398 ms: 1.08x slower                                                            |
| sympy_str                        | 143 ms                                                                | 155 ms: 1.08x slower                                                            |
| xml_etree_generate               | 53.7 ms                                                               | 58.3 ms: 1.08x slower                                                           |
| sqlglot_v2_optimize              | 33.5 ms                                                               | 36.3 ms: 1.08x slower                                                           |
| mdp                              | 764 ms                                                                | 828 ms: 1.08x slower                                                            |
| async_tree_eager_memoization     | 141 ms                                                                | 153 ms: 1.09x slower                                                            |
| async_tree_none_tg               | 159 ms                                                                | 172 ms: 1.09x slower                                                            |
| hexiom                           | 4.67 ms                                                               | 5.09 ms: 1.09x slower                                                           |
| deltablue                        | 2.58 ms                                                               | 2.81 ms: 1.09x slower                                                           |
| async_tree_io                    | 383 ms                                                                | 417 ms: 1.09x slower                                                            |
| pycparser                        | 683 ms                                                                | 745 ms: 1.09x slower                                                            |
| async_tree_io_tg                 | 374 ms                                                                | 408 ms: 1.09x slower                                                            |
| logging_format                   | 4.01 us                                                               | 4.38 us: 1.09x slower                                                           |
| async_tree_memoization           | 197 ms                                                                | 216 ms: 1.09x slower                                                            |
| comprehensions                   | 12.0 us                                                               | 13.2 us: 1.10x slower                                                           |
| logging_simple                   | 3.69 us                                                               | 4.06 us: 1.10x slower                                                           |
| pickle_pure_python               | 219 us                                                                | 241 us: 1.10x slower                                                            |
| subparsers                       | 13.7 ms                                                               | 15.1 ms: 1.10x slower                                                           |
| async_tree_eager_tg              | 130 ms                                                                | 144 ms: 1.11x slower                                                            |
| xml_etree_process                | 39.0 ms                                                               | 43.3 ms: 1.11x slower                                                           |
| unpickle_pure_python             | 161 us                                                                | 179 us: 1.11x slower                                                            |
| sqlglot_v2_normalize             | 68.2 ms                                                               | 76.1 ms: 1.12x slower                                                           |
| deepcopy                         | 157 us                                                                | 175 us: 1.12x slower                                                            |
| async_tree_none                  | 165 ms                                                                | 185 ms: 1.12x slower                                                            |
| pprint_safe_repr                 | 555 ms                                                                | 621 ms: 1.12x slower                                                            |
| pprint_pformat                   | 1.12 sec                                                              | 1.26 sec: 1.12x slower                                                          |
| django_template                  | 22.2 ms                                                               | 25.0 ms: 1.13x slower                                                           |
| deepcopy_reduce                  | 1.69 us                                                               | 1.90 us: 1.13x slower                                                           |
| regex_compile                    | 72.0 ms                                                               | 81.2 ms: 1.13x slower                                                           |
| coroutines                       | 17.1 ms                                                               | 19.3 ms: 1.13x slower                                                           |
| nbody                            | 75.3 ms                                                               | 85.1 ms: 1.13x slower                                                           |
| scimark_monte_carlo              | 46.7 ms                                                               | 53.0 ms: 1.13x slower                                                           |
| typing_runtime_protocols         | 96.5 us                                                               | 110 us: 1.14x slower                                                            |
| async_tree_eager                 | 64.4 ms                                                               | 73.4 ms: 1.14x slower                                                           |
| nqueens                          | 62.1 ms                                                               | 71.1 ms: 1.14x slower                                                           |
| deepcopy_memo                    | 19.2 us                                                               | 22.0 us: 1.15x slower                                                           |
| go                               | 87.6 ms                                                               | 100 ms: 1.15x slower                                                            |
| coverage                         | 292 ms                                                                | 335 ms: 1.15x slower                                                            |
| mako                             | 7.81 ms                                                               | 8.98 ms: 1.15x slower                                                           |
| genshi_xml                       | 31.3 ms                                                               | 36.2 ms: 1.15x slower                                                           |
| fannkuch                         | 267 ms                                                                | 310 ms: 1.16x slower                                                            |
| sqlglot_v2_transpile             | 1.00 ms                                                               | 1.17 ms: 1.17x slower                                                           |
| chaos                            | 40.3 ms                                                               | 47.4 ms: 1.18x slower                                                           |
| raytrace                         | 180 ms                                                                | 212 ms: 1.18x slower                                                            |
| float                            | 49.9 ms                                                               | 59.3 ms: 1.19x slower                                                           |
| genshi_text                      | 14.7 ms                                                               | 17.6 ms: 1.19x slower                                                           |
| sqlglot_v2_parse                 | 827 us                                                                | 994 us: 1.20x slower                                                            |
| generators                       | 24.1 ms                                                               | 31.6 ms: 1.31x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.07x slower                                                                    |

Benchmark hidden because not significant (4): gc_traversal, pidigits, regex_dna, k_core

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.00x