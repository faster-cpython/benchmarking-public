# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.251x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                                                          | 185 ms: 1.09x slower                                                                                                |
| docutils       | 1.46 sec                                                                                                        | 1.52 sec: 1.04x slower                                                                                              |
| html5lib       | 31.6 ms                                                                                                         | 34.0 ms: 1.08x slower                                                                                               |
| sphinx         | 585 ms                                                                                                          | 618 ms: 1.06x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg       | 411 ms                                                                                                          | 422 ms: 1.03x slower                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 389 ms                                                                                                          | 400 ms: 1.03x slower                                                                                                |
| asyncio_websockets               | 242 ms                                                                                                          | 249 ms: 1.03x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                                                          | 368 ms: 1.03x slower                                                                                                |
| async_tree_cpu_io_mixed          | 414 ms                                                                                                          | 428 ms: 1.03x slower                                                                                                |
| async_tree_io_tg                 | 375 ms                                                                                                          | 396 ms: 1.06x slower                                                                                                |
| async_tree_eager_io_tg           | 374 ms                                                                                                          | 396 ms: 1.06x slower                                                                                                |
| async_tree_eager_io              | 365 ms                                                                                                          | 387 ms: 1.06x slower                                                                                                |
| async_tree_memoization           | 195 ms                                                                                                          | 208 ms: 1.07x slower                                                                                                |
| async_tree_none_tg               | 157 ms                                                                                                          | 168 ms: 1.07x slower                                                                                                |
| async_tree_io                    | 380 ms                                                                                                          | 406 ms: 1.07x slower                                                                                                |
| async_tree_eager_memoization_tg  | 168 ms                                                                                                          | 180 ms: 1.07x slower                                                                                                |
| async_tree_memoization_tg        | 192 ms                                                                                                          | 206 ms: 1.07x slower                                                                                                |
| async_tree_eager_memoization     | 140 ms                                                                                                          | 151 ms: 1.07x slower                                                                                                |
| async_tree_none                  | 164 ms                                                                                                          | 178 ms: 1.08x slower                                                                                                |
| async_tree_eager_tg              | 129 ms                                                                                                          | 140 ms: 1.09x slower                                                                                                |
| async_tree_eager                 | 63.9 ms                                                                                                         | 71.5 ms: 1.12x slower                                                                                               |
| async_generators                 | 263 ms                                                                                                          | 294 ms: 1.12x slower                                                                                                |
| coroutines                       | 17.0 ms                                                                                                         | 19.4 ms: 1.14x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 49.5 ms                                                                                                         | 48.3 ms: 1.02x faster                                                                                               |
| nbody          | 75.1 ms                                                                                                         | 76.2 ms: 1.01x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.37 ms                                                                                                         | 2.34 ms: 1.01x faster                                                                                               |
| regex_dna      | 143 ms                                                                                                          | 143 ms: 1.00x faster                                                                                                |
| regex_v8       | 16.1 ms                                                                                                         | 16.2 ms: 1.00x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 161 us                                                                                                          | 138 us: 1.17x faster                                                                                                |
| xml_etree_generate   | 53.6 ms                                                                                                         | 51.4 ms: 1.04x faster                                                                                               |
| xml_etree_process    | 38.9 ms                                                                                                         | 37.4 ms: 1.04x faster                                                                                               |
| pickle_pure_python   | 219 us                                                                                                          | 227 us: 1.03x slower                                                                                                |
| json_dumps           | 6.61 ms                                                                                                         | 6.86 ms: 1.04x slower                                                                                               |
| json_loads           | 16.4 us                                                                                                         | 17.1 us: 1.04x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 18.1 ms                                                                                                         | 18.3 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 13.5 ms                                                                                                         | 13.8 ms: 1.02x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.81 ms                                                                                                         | 6.95 ms: 1.12x faster                                                                                               |
| django_template | 22.0 ms                                                                                                         | 25.3 ms: 1.15x slower                                                                                               |
| genshi_xml      | 31.2 ms                                                                                                         | 36.9 ms: 1.18x slower                                                                                               |
| genshi_text     | 14.7 ms                                                                                                         | 17.7 ms: 1.20x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.10x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat                   | 1.13 sec                                                                                                        | 1.12 us: 1010333.45x faster                                                                                         |
| pprint_safe_repr                 | 558 ms                                                                                                          | 647 ns: 863267.83x faster                                                                                           |
| unpickle_pure_python             | 161 us                                                                                                          | 138 us: 1.17x faster                                                                                                |
| mako                             | 7.81 ms                                                                                                         | 6.95 ms: 1.12x faster                                                                                               |
| xml_etree_generate               | 53.6 ms                                                                                                         | 51.4 ms: 1.04x faster                                                                                               |
| xml_etree_process                | 38.9 ms                                                                                                         | 37.4 ms: 1.04x faster                                                                                               |
| float                            | 49.5 ms                                                                                                         | 48.3 ms: 1.02x faster                                                                                               |
| regex_effbot                     | 2.37 ms                                                                                                         | 2.34 ms: 1.01x faster                                                                                               |
| regex_dna                        | 143 ms                                                                                                          | 143 ms: 1.00x faster                                                                                                |
| bpe_tokeniser                    | 3.09 sec                                                                                                        | 3.09 sec: 1.00x slower                                                                                              |
| dask                             | 766 ms                                                                                                          | 768 ms: 1.00x slower                                                                                                |
| regex_v8                         | 16.1 ms                                                                                                         | 16.2 ms: 1.00x slower                                                                                               |
| pyflate                          | 319 ms                                                                                                          | 320 ms: 1.00x slower                                                                                                |
| create_gc_cycles                 | 1.35 ms                                                                                                         | 1.36 ms: 1.00x slower                                                                                               |
| sqlite_synth                     | 1.59 us                                                                                                         | 1.60 us: 1.01x slower                                                                                               |
| python_startup                   | 18.1 ms                                                                                                         | 18.3 ms: 1.01x slower                                                                                               |
| scimark_lu                       | 83.3 ms                                                                                                         | 84.5 ms: 1.01x slower                                                                                               |
| crypto_pyaes                     | 57.1 ms                                                                                                         | 57.9 ms: 1.01x slower                                                                                               |
| nbody                            | 75.1 ms                                                                                                         | 76.2 ms: 1.01x slower                                                                                               |
| telco                            | 4.50 ms                                                                                                         | 4.58 ms: 1.02x slower                                                                                               |
| json                             | 2.87 ms                                                                                                         | 2.93 ms: 1.02x slower                                                                                               |
| pathlib                          | 24.1 ms                                                                                                         | 24.5 ms: 1.02x slower                                                                                               |
| shortest_path                    | 329 ms                                                                                                          | 335 ms: 1.02x slower                                                                                                |
| python_startup_no_site           | 13.5 ms                                                                                                         | 13.8 ms: 1.02x slower                                                                                               |
| async_tree_cpu_io_mixed_tg       | 411 ms                                                                                                          | 422 ms: 1.03x slower                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 389 ms                                                                                                          | 400 ms: 1.03x slower                                                                                                |
| coverage                         | 48.1 ms                                                                                                         | 49.4 ms: 1.03x slower                                                                                               |
| scimark_sor                      | 88.4 ms                                                                                                         | 90.9 ms: 1.03x slower                                                                                               |
| asyncio_websockets               | 242 ms                                                                                                          | 249 ms: 1.03x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                                                          | 368 ms: 1.03x slower                                                                                                |
| async_tree_cpu_io_mixed          | 414 ms                                                                                                          | 428 ms: 1.03x slower                                                                                                |
| pickle_pure_python               | 219 us                                                                                                          | 227 us: 1.03x slower                                                                                                |
| sympy_integrate                  | 11.1 ms                                                                                                         | 11.5 ms: 1.04x slower                                                                                               |
| k_core                           | 1.47 sec                                                                                                        | 1.52 sec: 1.04x slower                                                                                              |
| logging_silent                   | 331 ns                                                                                                          | 344 ns: 1.04x slower                                                                                                |
| json_dumps                       | 6.61 ms                                                                                                         | 6.86 ms: 1.04x slower                                                                                               |
| richards_super                   | 40.2 ms                                                                                                         | 41.9 ms: 1.04x slower                                                                                               |
| json_loads                       | 16.4 us                                                                                                         | 17.1 us: 1.04x slower                                                                                               |
| docutils                         | 1.46 sec                                                                                                        | 1.52 sec: 1.04x slower                                                                                              |
| richards                         | 35.8 ms                                                                                                         | 37.5 ms: 1.04x slower                                                                                               |
| meteor_contest                   | 73.7 ms                                                                                                         | 77.2 ms: 1.05x slower                                                                                               |
| pylint                           | 162 ms                                                                                                          | 170 ms: 1.05x slower                                                                                                |
| scimark_fft                      | 196 ms                                                                                                          | 206 ms: 1.05x slower                                                                                                |
| spectral_norm                    | 70.9 ms                                                                                                         | 74.7 ms: 1.05x slower                                                                                               |
| sphinx                           | 585 ms                                                                                                          | 618 ms: 1.06x slower                                                                                                |
| async_tree_io_tg                 | 375 ms                                                                                                          | 396 ms: 1.06x slower                                                                                                |
| async_tree_eager_io_tg           | 374 ms                                                                                                          | 396 ms: 1.06x slower                                                                                                |
| async_tree_eager_io              | 365 ms                                                                                                          | 387 ms: 1.06x slower                                                                                                |
| thrift                           | 444 us                                                                                                          | 472 us: 1.06x slower                                                                                                |
| sqlglot_v2_parse                 | 832 us                                                                                                          | 886 us: 1.06x slower                                                                                                |
| async_tree_memoization           | 195 ms                                                                                                          | 208 ms: 1.07x slower                                                                                                |
| async_tree_none_tg               | 157 ms                                                                                                          | 168 ms: 1.07x slower                                                                                                |
| async_tree_io                    | 380 ms                                                                                                          | 406 ms: 1.07x slower                                                                                                |
| async_tree_eager_memoization_tg  | 168 ms                                                                                                          | 180 ms: 1.07x slower                                                                                                |
| async_tree_memoization_tg        | 192 ms                                                                                                          | 206 ms: 1.07x slower                                                                                                |
| sympy_sum                        | 75.6 ms                                                                                                         | 81.0 ms: 1.07x slower                                                                                               |
| mdp                              | 761 ms                                                                                                          | 816 ms: 1.07x slower                                                                                                |
| async_tree_eager_memoization     | 140 ms                                                                                                          | 151 ms: 1.07x slower                                                                                                |
| sqlglot_v2_transpile             | 1.01 ms                                                                                                         | 1.08 ms: 1.07x slower                                                                                               |
| html5lib                         | 31.6 ms                                                                                                         | 34.0 ms: 1.08x slower                                                                                               |
| typing_runtime_protocols         | 96.7 us                                                                                                         | 104 us: 1.08x slower                                                                                                |
| async_tree_none                  | 164 ms                                                                                                          | 178 ms: 1.08x slower                                                                                                |
| dulwich_log                      | 24.9 ms                                                                                                         | 26.9 ms: 1.08x slower                                                                                               |
| many_optionals                   | 466 us                                                                                                          | 506 us: 1.09x slower                                                                                                |
| async_tree_eager_tg              | 129 ms                                                                                                          | 140 ms: 1.09x slower                                                                                                |
| sympy_str                        | 143 ms                                                                                                          | 156 ms: 1.09x slower                                                                                                |
| hexiom                           | 4.69 ms                                                                                                         | 5.11 ms: 1.09x slower                                                                                               |
| 2to3                             | 170 ms                                                                                                          | 185 ms: 1.09x slower                                                                                                |
| subparsers                       | 13.7 ms                                                                                                         | 14.9 ms: 1.09x slower                                                                                               |
| sqlglot_v2_optimize              | 33.5 ms                                                                                                         | 36.6 ms: 1.09x slower                                                                                               |
| comprehensions                   | 12.0 us                                                                                                         | 13.1 us: 1.09x slower                                                                                               |
| scimark_sparse_mat_mult          | 3.23 ms                                                                                                         | 3.54 ms: 1.10x slower                                                                                               |
| sympy_expand                     | 241 ms                                                                                                          | 266 ms: 1.10x slower                                                                                                |
| logging_format                   | 3.97 us                                                                                                         | 4.39 us: 1.10x slower                                                                                               |
| pycparser                        | 682 ms                                                                                                          | 754 ms: 1.11x slower                                                                                                |
| sqlglot_v2_normalize             | 68.2 ms                                                                                                         | 76.0 ms: 1.12x slower                                                                                               |
| deepcopy                         | 156 us                                                                                                          | 174 us: 1.12x slower                                                                                                |
| async_tree_eager                 | 63.9 ms                                                                                                         | 71.5 ms: 1.12x slower                                                                                               |
| nqueens                          | 61.9 ms                                                                                                         | 69.3 ms: 1.12x slower                                                                                               |
| async_generators                 | 263 ms                                                                                                          | 294 ms: 1.12x slower                                                                                                |
| logging_simple                   | 3.66 us                                                                                                         | 4.11 us: 1.12x slower                                                                                               |
| deltablue                        | 2.58 ms                                                                                                         | 2.90 ms: 1.13x slower                                                                                               |
| deepcopy_reduce                  | 1.68 us                                                                                                         | 1.89 us: 1.13x slower                                                                                               |
| coroutines                       | 17.0 ms                                                                                                         | 19.4 ms: 1.14x slower                                                                                               |
| scimark_monte_carlo              | 46.6 ms                                                                                                         | 53.3 ms: 1.14x slower                                                                                               |
| fannkuch                         | 267 ms                                                                                                          | 306 ms: 1.15x slower                                                                                                |
| go                               | 87.5 ms                                                                                                         | 100 ms: 1.15x slower                                                                                                |
| django_template                  | 22.0 ms                                                                                                         | 25.3 ms: 1.15x slower                                                                                               |
| deepcopy_memo                    | 19.3 us                                                                                                         | 22.3 us: 1.16x slower                                                                                               |
| raytrace                         | 180 ms                                                                                                          | 211 ms: 1.17x slower                                                                                                |
| genshi_xml                       | 31.2 ms                                                                                                         | 36.9 ms: 1.18x slower                                                                                               |
| chaos                            | 40.2 ms                                                                                                         | 47.9 ms: 1.19x slower                                                                                               |
| genshi_text                      | 14.7 ms                                                                                                         | 17.7 ms: 1.20x slower                                                                                               |
| generators                       | 24.0 ms                                                                                                         | 31.6 ms: 1.31x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.24x faster                                                                                                        |

Benchmark hidden because not significant (7): xml_etree_parse, gc_traversal, tomli_loads, connected_components, pidigits, regex_compile, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.251x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x