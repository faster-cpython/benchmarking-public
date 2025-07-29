# Results vs. base

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: 0887346
- commit date: 2025-07-28
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 202 ms                                                                | 172 ms: 1.17x faster                                               |
| docutils       | 1.82 sec                                                              | 1.46 sec: 1.25x faster                                             |
| html5lib       | 38.5 ms                                                               | 33.5 ms: 1.15x faster                                              |
| sphinx         | 686 ms                                                                | 578 ms: 1.19x faster                                               |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg                 | 434 ms                                                                | 367 ms: 1.18x faster                                               |
| async_tree_eager_io_tg           | 432 ms                                                                | 372 ms: 1.16x faster                                               |
| async_tree_eager_memoization_tg  | 198 ms                                                                | 171 ms: 1.15x faster                                               |
| async_tree_eager_io              | 419 ms                                                                | 364 ms: 1.15x faster                                               |
| async_tree_io                    | 432 ms                                                                | 378 ms: 1.14x faster                                               |
| async_tree_memoization           | 224 ms                                                                | 196 ms: 1.14x faster                                               |
| async_tree_eager_tg              | 148 ms                                                                | 130 ms: 1.14x faster                                               |
| async_tree_none_tg               | 180 ms                                                                | 159 ms: 1.13x faster                                               |
| async_tree_memoization_tg        | 219 ms                                                                | 193 ms: 1.13x faster                                               |
| async_tree_none                  | 187 ms                                                                | 166 ms: 1.13x faster                                               |
| asyncio_websockets               | 273 ms                                                                | 242 ms: 1.13x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 436 ms                                                                | 388 ms: 1.12x faster                                               |
| async_tree_cpu_io_mixed          | 466 ms                                                                | 419 ms: 1.11x faster                                               |
| async_tree_eager                 | 71.1 ms                                                               | 64.2 ms: 1.11x faster                                              |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                | 357 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg       | 457 ms                                                                | 414 ms: 1.10x faster                                               |
| coroutines                       | 18.1 ms                                                               | 16.5 ms: 1.09x faster                                              |
| async_generators                 | 311 ms                                                                | 285 ms: 1.09x faster                                               |
| async_tree_eager_memoization     | 151 ms                                                                | 139 ms: 1.09x faster                                               |
| Geometric mean                   | (ref)                                                                 | 1.13x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.9 ms                                                               | 51.4 ms: 1.11x faster                                              |
| nbody          | 78.4 ms                                                               | 71.6 ms: 1.09x faster                                              |
| pidigits       | 310 ms                                                                | 284 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 83.1 ms                                                               | 72.9 ms: 1.14x faster                                              |
| regex_v8       | 17.1 ms                                                               | 15.3 ms: 1.12x faster                                              |
| regex_dna      | 153 ms                                                                | 138 ms: 1.11x faster                                               |
| regex_effbot   | 2.38 ms                                                               | 2.16 ms: 1.10x faster                                              |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 82.5 ms                                                               | 70.9 ms: 1.16x faster                                              |
| xml_etree_generate   | 56.0 ms                                                               | 49.4 ms: 1.13x faster                                              |
| xml_etree_process    | 39.1 ms                                                               | 34.5 ms: 1.13x faster                                              |
| xml_etree_parse      | 110 ms                                                                | 97.5 ms: 1.13x faster                                              |
| pickle_pure_python   | 234 us                                                                | 208 us: 1.13x faster                                               |
| json_loads           | 19.3 us                                                               | 17.4 us: 1.11x faster                                              |
| json_dumps           | 7.33 ms                                                               | 6.62 ms: 1.11x faster                                              |
| unpickle_pure_python | 143 us                                                                | 129 us: 1.11x faster                                               |
| tomli_loads          | 1.37 sec                                                              | 1.24 sec: 1.10x faster                                             |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                               | 11.7 ms: 1.17x faster                                              |
| python_startup         | 18.5 ms                                                               | 16.1 ms: 1.15x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.16x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 37.7 ms                                                               | 33.6 ms: 1.12x faster                                              |
| django_template | 26.0 ms                                                               | 23.2 ms: 1.12x faster                                              |
| genshi_text     | 17.1 ms                                                               | 15.4 ms: 1.11x faster                                              |
| mako            | 7.16 ms                                                               | 6.47 ms: 1.11x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.11x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| create_gc_cycles                 | 2.12 ms                                                               | 1.36 ms: 1.56x faster                                              |
| gc_traversal                     | 4.61 ms                                                               | 3.19 ms: 1.45x faster                                              |
| k_core                           | 2.18 sec                                                              | 1.59 sec: 1.37x faster                                             |
| shortest_path                    | 454 ms                                                                | 350 ms: 1.30x faster                                               |
| connected_components             | 417 ms                                                                | 322 ms: 1.30x faster                                               |
| docutils                         | 1.82 sec                                                              | 1.46 sec: 1.25x faster                                             |
| sympy_integrate                  | 13.4 ms                                                               | 10.9 ms: 1.23x faster                                              |
| pylint                           | 195 ms                                                                | 161 ms: 1.21x faster                                               |
| pycparser                        | 846 ms                                                                | 701 ms: 1.21x faster                                               |
| mdp                              | 932 ms                                                                | 776 ms: 1.20x faster                                               |
| pyflate                          | 340 ms                                                                | 285 ms: 1.19x faster                                               |
| sphinx                           | 686 ms                                                                | 578 ms: 1.19x faster                                               |
| many_optionals                   | 709 us                                                                | 598 us: 1.19x faster                                               |
| async_tree_io_tg                 | 434 ms                                                                | 367 ms: 1.18x faster                                               |
| sympy_sum                        | 91.0 ms                                                               | 76.9 ms: 1.18x faster                                              |
| dulwich_log                      | 30.0 ms                                                               | 25.4 ms: 1.18x faster                                              |
| sympy_str                        | 173 ms                                                                | 147 ms: 1.18x faster                                               |
| sqlglot_v2_transpile             | 1.13 ms                                                               | 958 us: 1.18x faster                                               |
| 2to3                             | 202 ms                                                                | 172 ms: 1.17x faster                                               |
| python_startup_no_site           | 13.6 ms                                                               | 11.7 ms: 1.17x faster                                              |
| xml_etree_iterparse              | 82.5 ms                                                               | 70.9 ms: 1.16x faster                                              |
| async_tree_eager_io_tg           | 432 ms                                                                | 372 ms: 1.16x faster                                               |
| sympy_expand                     | 287 ms                                                                | 249 ms: 1.16x faster                                               |
| async_tree_eager_memoization_tg  | 198 ms                                                                | 171 ms: 1.15x faster                                               |
| async_tree_eager_io              | 419 ms                                                                | 364 ms: 1.15x faster                                               |
| sqlglot_v2_optimize              | 38.5 ms                                                               | 33.5 ms: 1.15x faster                                              |
| html5lib                         | 38.5 ms                                                               | 33.5 ms: 1.15x faster                                              |
| python_startup                   | 18.5 ms                                                               | 16.1 ms: 1.15x faster                                              |
| subparsers                       | 29.2 ms                                                               | 25.4 ms: 1.15x faster                                              |
| async_tree_io                    | 432 ms                                                                | 378 ms: 1.14x faster                                               |
| sqlglot_v2_parse                 | 900 us                                                                | 788 us: 1.14x faster                                               |
| async_tree_memoization           | 224 ms                                                                | 196 ms: 1.14x faster                                               |
| regex_compile                    | 83.1 ms                                                               | 72.9 ms: 1.14x faster                                              |
| async_tree_eager_tg              | 148 ms                                                                | 130 ms: 1.14x faster                                               |
| meteor_contest                   | 84.3 ms                                                               | 74.3 ms: 1.14x faster                                              |
| xml_etree_generate               | 56.0 ms                                                               | 49.4 ms: 1.13x faster                                              |
| xml_etree_process                | 39.1 ms                                                               | 34.5 ms: 1.13x faster                                              |
| pprint_pformat                   | 1.03 sec                                                              | 910 ms: 1.13x faster                                               |
| async_tree_none_tg               | 180 ms                                                                | 159 ms: 1.13x faster                                               |
| json                             | 3.44 ms                                                               | 3.04 ms: 1.13x faster                                              |
| bpe_tokeniser                    | 3.31 sec                                                              | 2.92 sec: 1.13x faster                                             |
| deltablue                        | 2.79 ms                                                               | 2.47 ms: 1.13x faster                                              |
| async_tree_memoization_tg        | 219 ms                                                                | 193 ms: 1.13x faster                                               |
| xml_etree_parse                  | 110 ms                                                                | 97.5 ms: 1.13x faster                                              |
| sqlglot_v2_normalize             | 77.3 ms                                                               | 68.5 ms: 1.13x faster                                              |
| async_tree_none                  | 187 ms                                                                | 166 ms: 1.13x faster                                               |
| hexiom                           | 5.18 ms                                                               | 4.60 ms: 1.13x faster                                              |
| asyncio_websockets               | 273 ms                                                                | 242 ms: 1.13x faster                                               |
| pickle_pure_python               | 234 us                                                                | 208 us: 1.13x faster                                               |
| pprint_safe_repr                 | 505 ms                                                                | 449 ms: 1.12x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 436 ms                                                                | 388 ms: 1.12x faster                                               |
| typing_runtime_protocols         | 105 us                                                                | 93.5 us: 1.12x faster                                              |
| genshi_xml                       | 37.7 ms                                                               | 33.6 ms: 1.12x faster                                              |
| regex_v8                         | 17.1 ms                                                               | 15.3 ms: 1.12x faster                                              |
| django_template                  | 26.0 ms                                                               | 23.2 ms: 1.12x faster                                              |
| crypto_pyaes                     | 55.7 ms                                                               | 49.7 ms: 1.12x faster                                              |
| go                               | 97.9 ms                                                               | 87.5 ms: 1.12x faster                                              |
| thrift                           | 513 us                                                                | 458 us: 1.12x faster                                               |
| chaos                            | 43.7 ms                                                               | 39.1 ms: 1.12x faster                                              |
| raytrace                         | 193 ms                                                                | 173 ms: 1.12x faster                                               |
| logging_simple                   | 3.77 us                                                               | 3.38 us: 1.12x faster                                              |
| deepcopy_memo                    | 24.5 us                                                               | 21.9 us: 1.12x faster                                              |
| telco                            | 4.92 ms                                                               | 4.41 ms: 1.12x faster                                              |
| deepcopy_reduce                  | 2.00 us                                                               | 1.80 us: 1.11x faster                                              |
| async_tree_cpu_io_mixed          | 466 ms                                                                | 419 ms: 1.11x faster                                               |
| logging_format                   | 4.09 us                                                               | 3.68 us: 1.11x faster                                              |
| deepcopy                         | 194 us                                                                | 174 us: 1.11x faster                                               |
| regex_dna                        | 153 ms                                                                | 138 ms: 1.11x faster                                               |
| json_loads                       | 19.3 us                                                               | 17.4 us: 1.11x faster                                              |
| genshi_text                      | 17.1 ms                                                               | 15.4 ms: 1.11x faster                                              |
| float                            | 56.9 ms                                                               | 51.4 ms: 1.11x faster                                              |
| json_dumps                       | 7.33 ms                                                               | 6.62 ms: 1.11x faster                                              |
| async_tree_eager                 | 71.1 ms                                                               | 64.2 ms: 1.11x faster                                              |
| unpickle_pure_python             | 143 us                                                                | 129 us: 1.11x faster                                               |
| mako                             | 7.16 ms                                                               | 6.47 ms: 1.11x faster                                              |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                | 357 ms: 1.11x faster                                               |
| richards_super                   | 41.4 ms                                                               | 37.6 ms: 1.10x faster                                              |
| async_tree_cpu_io_mixed_tg       | 457 ms                                                                | 414 ms: 1.10x faster                                               |
| tomli_loads                      | 1.37 sec                                                              | 1.24 sec: 1.10x faster                                             |
| spectral_norm                    | 69.2 ms                                                               | 62.9 ms: 1.10x faster                                              |
| regex_effbot                     | 2.38 ms                                                               | 2.16 ms: 1.10x faster                                              |
| sqlite_synth                     | 1.74 us                                                               | 1.59 us: 1.10x faster                                              |
| richards                         | 37.1 ms                                                               | 33.8 ms: 1.10x faster                                              |
| comprehensions                   | 12.4 us                                                               | 11.4 us: 1.10x faster                                              |
| nqueens                          | 68.0 ms                                                               | 62.0 ms: 1.10x faster                                              |
| coroutines                       | 18.1 ms                                                               | 16.5 ms: 1.09x faster                                              |
| scimark_sparse_mat_mult          | 3.70 ms                                                               | 3.38 ms: 1.09x faster                                              |
| nbody                            | 78.4 ms                                                               | 71.6 ms: 1.09x faster                                              |
| fannkuch                         | 276 ms                                                                | 252 ms: 1.09x faster                                               |
| generators                       | 26.9 ms                                                               | 24.6 ms: 1.09x faster                                              |
| pidigits                         | 310 ms                                                                | 284 ms: 1.09x faster                                               |
| scimark_monte_carlo              | 49.9 ms                                                               | 45.7 ms: 1.09x faster                                              |
| scimark_fft                      | 209 ms                                                                | 191 ms: 1.09x faster                                               |
| async_generators                 | 311 ms                                                                | 285 ms: 1.09x faster                                               |
| coverage                         | 52.1 ms                                                               | 47.9 ms: 1.09x faster                                              |
| async_tree_eager_memoization     | 151 ms                                                                | 139 ms: 1.09x faster                                               |
| scimark_sor                      | 92.6 ms                                                               | 85.3 ms: 1.09x faster                                              |
| scimark_lu                       | 82.9 ms                                                               | 77.0 ms: 1.08x faster                                              |
| pathlib                          | 25.1 ms                                                               | 23.4 ms: 1.07x faster                                              |
| logging_silent                   | 81.7 ns                                                               | 77.1 ns: 1.06x faster                                              |
| dask                             | 785 ms                                                                | 796 ms: 1.01x slower                                               |
| Geometric mean                   | (ref)                                                                 | 1.14x faster                                                       |

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 0.96x