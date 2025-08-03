# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.009x faster
- HPT reliability: 93.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                                                          | 171 ms: 1.01x faster                                                                                                |
| docutils       | 1.45 sec                                                                                                        | 1.46 sec: 1.00x slower                                                                                              |
| html5lib       | 33.1 ms                                                                                                         | 33.6 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                      | 468 ms                                                                                                          | 448 ms: 1.05x faster                                                                                                |
| async_tree_io_tg                 | 383 ms                                                                                                          | 370 ms: 1.04x faster                                                                                                |
| async_tree_eager_memoization_tg  | 171 ms                                                                                                          | 166 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed          | 419 ms                                                                                                          | 415 ms: 1.01x faster                                                                                                |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                                                          | 358 ms: 1.00x slower                                                                                                |
| async_tree_eager                 | 64.9 ms                                                                                                         | 65.4 ms: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 387 ms                                                                                                          | 390 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization     | 139 ms                                                                                                          | 140 ms: 1.01x slower                                                                                                |
| async_tree_none                  | 167 ms                                                                                                          | 170 ms: 1.02x slower                                                                                                |
| coroutines                       | 16.6 ms                                                                                                         | 17.0 ms: 1.03x slower                                                                                               |
| async_tree_memoization           | 196 ms                                                                                                          | 204 ms: 1.04x slower                                                                                                |
| async_tree_none_tg               | 159 ms                                                                                                          | 165 ms: 1.04x slower                                                                                                |
| async_generators                 | 275 ms                                                                                                          | 288 ms: 1.05x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (8): async_tree_eager_tg, async_tree_io, async_tree_eager_io, asyncio_websockets, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                                                                         | 71.7 ms: 1.12x faster                                                                                               |
| float          | 50.1 ms                                                                                                         | 51.6 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                                                                         | 15.3 ms: 1.01x faster                                                                                               |
| regex_dna      | 139 ms                                                                                                          | 138 ms: 1.01x faster                                                                                                |
| regex_effbot   | 2.15 ms                                                                                                         | 2.14 ms: 1.01x faster                                                                                               |
| regex_compile  | 74.0 ms                                                                                                         | 73.6 ms: 1.01x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.51 sec                                                                                                        | 1.24 sec: 1.22x faster                                                                                              |
| unpickle_pure_python | 156 us                                                                                                          | 129 us: 1.21x faster                                                                                                |
| xml_etree_process    | 39.7 ms                                                                                                         | 34.9 ms: 1.14x faster                                                                                               |
| xml_etree_generate   | 56.0 ms                                                                                                         | 49.4 ms: 1.13x faster                                                                                               |
| json_dumps           | 6.63 ms                                                                                                         | 6.28 ms: 1.05x faster                                                                                               |
| xml_etree_parse      | 103 ms                                                                                                          | 99.1 ms: 1.04x faster                                                                                               |
| pickle_pure_python   | 216 us                                                                                                          | 210 us: 1.03x faster                                                                                                |
| xml_etree_iterparse  | 71.8 ms                                                                                                         | 70.8 ms: 1.01x faster                                                                                               |
| unpickle_list        | 3.05 us                                                                                                         | 3.01 us: 1.01x faster                                                                                               |
| unpickle             | 8.95 us                                                                                                         | 9.04 us: 1.01x slower                                                                                               |
| json_loads           | 17.0 us                                                                                                         | 17.4 us: 1.02x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.06x faster                                                                                                        |

Benchmark hidden because not significant (3): pickle_dict, pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.9 ms                                                                                                         | 17.0 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 12.7 ms                                                                                                         | 12.9 ms: 1.02x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.09 ms                                                                                                         | 6.46 ms: 1.25x faster                                                                                               |
| genshi_text     | 15.4 ms                                                                                                         | 15.3 ms: 1.01x faster                                                                                               |
| genshi_xml      | 33.0 ms                                                                                                         | 33.3 ms: 1.01x slower                                                                                               |
| django_template | 22.8 ms                                                                                                         | 23.4 ms: 1.03x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.05x faster                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako                             | 8.09 ms                                                                                                         | 6.46 ms: 1.25x faster                                                                                               |
| tomli_loads                      | 1.51 sec                                                                                                        | 1.24 sec: 1.22x faster                                                                                              |
| unpickle_pure_python             | 156 us                                                                                                          | 129 us: 1.21x faster                                                                                                |
| pprint_pformat                   | 1.08 sec                                                                                                        | 916 ms: 1.18x faster                                                                                                |
| fannkuch                         | 286 ms                                                                                                          | 246 ms: 1.16x faster                                                                                                |
| pprint_safe_repr                 | 529 ms                                                                                                          | 457 ms: 1.16x faster                                                                                                |
| xml_etree_process                | 39.7 ms                                                                                                         | 34.9 ms: 1.14x faster                                                                                               |
| xml_etree_generate               | 56.0 ms                                                                                                         | 49.4 ms: 1.13x faster                                                                                               |
| nbody                            | 80.0 ms                                                                                                         | 71.7 ms: 1.12x faster                                                                                               |
| bpe_tokeniser                    | 3.14 sec                                                                                                        | 2.92 sec: 1.08x faster                                                                                              |
| json_dumps                       | 6.63 ms                                                                                                         | 6.28 ms: 1.05x faster                                                                                               |
| comprehensions                   | 11.9 us                                                                                                         | 11.4 us: 1.05x faster                                                                                               |
| telco                            | 4.60 ms                                                                                                         | 4.40 ms: 1.05x faster                                                                                               |
| asyncio_tcp                      | 468 ms                                                                                                          | 448 ms: 1.05x faster                                                                                                |
| crypto_pyaes                     | 52.1 ms                                                                                                         | 49.9 ms: 1.04x faster                                                                                               |
| pyflate                          | 306 ms                                                                                                          | 293 ms: 1.04x faster                                                                                                |
| sqlglot_v2_parse                 | 816 us                                                                                                          | 783 us: 1.04x faster                                                                                                |
| xml_etree_parse                  | 103 ms                                                                                                          | 99.1 ms: 1.04x faster                                                                                               |
| async_tree_io_tg                 | 383 ms                                                                                                          | 370 ms: 1.04x faster                                                                                                |
| meteor_contest                   | 75.0 ms                                                                                                         | 72.7 ms: 1.03x faster                                                                                               |
| async_tree_eager_memoization_tg  | 171 ms                                                                                                          | 166 ms: 1.03x faster                                                                                                |
| pickle_pure_python               | 216 us                                                                                                          | 210 us: 1.03x faster                                                                                                |
| typing_runtime_protocols         | 96.8 us                                                                                                         | 94.7 us: 1.02x faster                                                                                               |
| regex_v8                         | 15.5 ms                                                                                                         | 15.3 ms: 1.01x faster                                                                                               |
| xml_etree_iterparse              | 71.8 ms                                                                                                         | 70.8 ms: 1.01x faster                                                                                               |
| unpickle_list                    | 3.05 us                                                                                                         | 3.01 us: 1.01x faster                                                                                               |
| 2to3                             | 173 ms                                                                                                          | 171 ms: 1.01x faster                                                                                                |
| sqlglot_v2_transpile             | 990 us                                                                                                          | 981 us: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed          | 419 ms                                                                                                          | 415 ms: 1.01x faster                                                                                                |
| regex_dna                        | 139 ms                                                                                                          | 138 ms: 1.01x faster                                                                                                |
| regex_effbot                     | 2.15 ms                                                                                                         | 2.14 ms: 1.01x faster                                                                                               |
| genshi_text                      | 15.4 ms                                                                                                         | 15.3 ms: 1.01x faster                                                                                               |
| regex_compile                    | 74.0 ms                                                                                                         | 73.6 ms: 1.01x faster                                                                                               |
| scimark_lu                       | 76.4 ms                                                                                                         | 76.0 ms: 1.00x faster                                                                                               |
| sqlglot_v2_normalize             | 69.4 ms                                                                                                         | 69.1 ms: 1.00x faster                                                                                               |
| sqlglot_v2_optimize              | 33.9 ms                                                                                                         | 33.8 ms: 1.00x faster                                                                                               |
| bench_thread_pool                | 505 us                                                                                                          | 504 us: 1.00x faster                                                                                                |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                                                          | 358 ms: 1.00x slower                                                                                                |
| docutils                         | 1.45 sec                                                                                                        | 1.46 sec: 1.00x slower                                                                                              |
| subparsers                       | 25.5 ms                                                                                                         | 25.6 ms: 1.01x slower                                                                                               |
| python_startup                   | 16.9 ms                                                                                                         | 17.0 ms: 1.01x slower                                                                                               |
| nqueens                          | 61.5 ms                                                                                                         | 61.9 ms: 1.01x slower                                                                                               |
| deepcopy                         | 173 us                                                                                                          | 175 us: 1.01x slower                                                                                                |
| bench_mp_pool                    | 69.6 ms                                                                                                         | 70.2 ms: 1.01x slower                                                                                               |
| sympy_expand                     | 247 ms                                                                                                          | 249 ms: 1.01x slower                                                                                                |
| async_tree_eager                 | 64.9 ms                                                                                                         | 65.4 ms: 1.01x slower                                                                                               |
| genshi_xml                       | 33.0 ms                                                                                                         | 33.3 ms: 1.01x slower                                                                                               |
| richards_super                   | 37.7 ms                                                                                                         | 38.0 ms: 1.01x slower                                                                                               |
| unpickle                         | 8.95 us                                                                                                         | 9.04 us: 1.01x slower                                                                                               |
| deepcopy_reduce                  | 1.78 us                                                                                                         | 1.79 us: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 387 ms                                                                                                          | 390 ms: 1.01x slower                                                                                                |
| generators                       | 24.1 ms                                                                                                         | 24.4 ms: 1.01x slower                                                                                               |
| sympy_integrate                  | 10.9 ms                                                                                                         | 11.0 ms: 1.01x slower                                                                                               |
| async_tree_eager_memoization     | 139 ms                                                                                                          | 140 ms: 1.01x slower                                                                                                |
| logging_format                   | 3.64 us                                                                                                         | 3.70 us: 1.01x slower                                                                                               |
| spectral_norm                    | 62.6 ms                                                                                                         | 63.5 ms: 1.01x slower                                                                                               |
| pathlib                          | 24.1 ms                                                                                                         | 24.5 ms: 1.01x slower                                                                                               |
| many_optionals                   | 591 us                                                                                                          | 600 us: 1.02x slower                                                                                                |
| python_startup_no_site           | 12.7 ms                                                                                                         | 12.9 ms: 1.02x slower                                                                                               |
| dulwich_log                      | 25.2 ms                                                                                                         | 25.7 ms: 1.02x slower                                                                                               |
| html5lib                         | 33.1 ms                                                                                                         | 33.6 ms: 1.02x slower                                                                                               |
| async_tree_none                  | 167 ms                                                                                                          | 170 ms: 1.02x slower                                                                                                |
| deepcopy_memo                    | 21.9 us                                                                                                         | 22.3 us: 1.02x slower                                                                                               |
| chaos                            | 38.7 ms                                                                                                         | 39.5 ms: 1.02x slower                                                                                               |
| richards                         | 33.6 ms                                                                                                         | 34.3 ms: 1.02x slower                                                                                               |
| json                             | 2.99 ms                                                                                                         | 3.05 ms: 1.02x slower                                                                                               |
| hexiom                           | 4.58 ms                                                                                                         | 4.67 ms: 1.02x slower                                                                                               |
| scimark_sor                      | 84.3 ms                                                                                                         | 86.2 ms: 1.02x slower                                                                                               |
| scimark_fft                      | 187 ms                                                                                                          | 192 ms: 1.02x slower                                                                                                |
| json_loads                       | 17.0 us                                                                                                         | 17.4 us: 1.02x slower                                                                                               |
| scimark_monte_carlo              | 45.2 ms                                                                                                         | 46.3 ms: 1.02x slower                                                                                               |
| logging_simple                   | 3.34 us                                                                                                         | 3.42 us: 1.03x slower                                                                                               |
| coroutines                       | 16.6 ms                                                                                                         | 17.0 ms: 1.03x slower                                                                                               |
| thrift                           | 447 us                                                                                                          | 459 us: 1.03x slower                                                                                                |
| django_template                  | 22.8 ms                                                                                                         | 23.4 ms: 1.03x slower                                                                                               |
| raytrace                         | 175 ms                                                                                                          | 180 ms: 1.03x slower                                                                                                |
| go                               | 85.7 ms                                                                                                         | 88.2 ms: 1.03x slower                                                                                               |
| float                            | 50.1 ms                                                                                                         | 51.6 ms: 1.03x slower                                                                                               |
| async_tree_memoization           | 196 ms                                                                                                          | 204 ms: 1.04x slower                                                                                                |
| async_tree_none_tg               | 159 ms                                                                                                          | 165 ms: 1.04x slower                                                                                                |
| shortest_path                    | 337 ms                                                                                                          | 350 ms: 1.04x slower                                                                                                |
| k_core                           | 1.53 sec                                                                                                        | 1.59 sec: 1.04x slower                                                                                              |
| coverage                         | 46.1 ms                                                                                                         | 48.2 ms: 1.05x slower                                                                                               |
| async_generators                 | 275 ms                                                                                                          | 288 ms: 1.05x slower                                                                                                |
| connected_components             | 306 ms                                                                                                          | 321 ms: 1.05x slower                                                                                                |
| pycparser                        | 692 ms                                                                                                          | 736 ms: 1.06x slower                                                                                                |
| deltablue                        | 2.39 ms                                                                                                         | 2.54 ms: 1.06x slower                                                                                               |
| unpack_sequence                  | 41.0 ns                                                                                                         | 43.6 ns: 1.07x slower                                                                                               |
| logging_silent                   | 71.5 ns                                                                                                         | 77.0 ns: 1.08x slower                                                                                               |
| scimark_sparse_mat_mult          | 3.12 ms                                                                                                         | 3.39 ms: 1.09x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (21): async_tree_eager_tg, async_tree_io, sphinx, sympy_sum, create_gc_cycles, pylint, sqlite_synth, dask, pickle_dict, sympy_str, async_tree_eager_io, mdp, pickle, pidigits, asyncio_websockets, pickle_list, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_eager_io_tg, gc_traversal, async_tree_cpu_io_mixed_tg

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 93.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x