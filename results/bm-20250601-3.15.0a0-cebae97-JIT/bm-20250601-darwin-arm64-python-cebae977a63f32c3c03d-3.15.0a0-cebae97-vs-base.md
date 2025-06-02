# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                                                          | 226 ms: 1.03x slower                                                                                                |
| docutils       | 1.59 sec                                                                                                        | 1.67 sec: 1.05x slower                                                                                              |
| sphinx         | 651 ms                                                                                                          | 659 ms: 1.01x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets               | 242 ms                                                                                                          | 243 ms: 1.00x slower                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 427 ms                                                                                                          | 430 ms: 1.01x slower                                                                                                |
| async_tree_none_tg               | 167 ms                                                                                                          | 169 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                                                          | 395 ms: 1.01x slower                                                                                                |
| async_tree_io                    | 402 ms                                                                                                          | 406 ms: 1.01x slower                                                                                                |
| async_tree_memoization           | 205 ms                                                                                                          | 208 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization_tg  | 182 ms                                                                                                          | 184 ms: 1.01x slower                                                                                                |
| async_tree_io_tg                 | 389 ms                                                                                                          | 395 ms: 1.01x slower                                                                                                |
| coroutines                       | 18.1 ms                                                                                                         | 18.4 ms: 1.02x slower                                                                                               |
| async_tree_eager_memoization     | 148 ms                                                                                                          | 151 ms: 1.02x slower                                                                                                |
| async_tree_eager                 | 70.4 ms                                                                                                         | 73.6 ms: 1.05x slower                                                                                               |
| async_generators                 | 316 ms                                                                                                          | 331 ms: 1.05x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (9): asyncio_tcp, async_tree_eager_io, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg, async_tree_eager_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 51.2 ms                                                                                                         | 49.2 ms: 1.04x faster                                                                                               |
| nbody          | 77.6 ms                                                                                                         | 77.9 ms: 1.00x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 74.3 ms                                                                                                         | 68.1 ms: 1.09x faster                                                                                               |
| regex_v8       | 17.3 ms                                                                                                         | 17.4 ms: 1.01x slower                                                                                               |
| regex_effbot   | 2.19 ms                                                                                                         | 2.21 ms: 1.01x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 156 us                                                                                                          | 151 us: 1.04x faster                                                                                                |
| xml_etree_generate   | 65.1 ms                                                                                                         | 63.9 ms: 1.02x faster                                                                                               |
| xml_etree_process    | 43.9 ms                                                                                                         | 43.1 ms: 1.02x faster                                                                                               |
| json_dumps           | 8.07 ms                                                                                                         | 8.02 ms: 1.01x faster                                                                                               |
| pickle_pure_python   | 222 us                                                                                                          | 221 us: 1.00x faster                                                                                                |
| pickle               | 9.79 us                                                                                                         | 9.83 us: 1.00x slower                                                                                               |
| pickle_dict          | 21.5 us                                                                                                         | 21.6 us: 1.01x slower                                                                                               |
| pickle_list          | 3.65 us                                                                                                         | 3.69 us: 1.01x slower                                                                                               |
| xml_etree_iterparse  | 76.7 ms                                                                                                         | 77.5 ms: 1.01x slower                                                                                               |
| unpickle             | 12.0 us                                                                                                         | 12.2 us: 1.02x slower                                                                                               |
| tomli_loads          | 1.40 sec                                                                                                        | 1.44 sec: 1.03x slower                                                                                              |
| Geometric mean       | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                                                                         | 13.2 ms: 1.04x faster                                                                                               |
| python_startup         | 18.2 ms                                                                                                         | 17.8 ms: 1.03x faster                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                                                                         | 15.9 ms: 1.02x slower                                                                                               |
| django_template | 25.3 ms                                                                                                         | 25.8 ms: 1.02x slower                                                                                               |
| genshi_xml      | 33.1 ms                                                                                                         | 33.7 ms: 1.02x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat                   | 1.19 sec                                                                                                        | 1.01 us: 1176152.83x faster                                                                                         |
| pprint_safe_repr                 | 587 ms                                                                                                          | 590 ns: 994618.49x faster                                                                                           |
| regex_compile                    | 74.3 ms                                                                                                         | 68.1 ms: 1.09x faster                                                                                               |
| scimark_fft                      | 263 ms                                                                                                          | 248 ms: 1.06x faster                                                                                                |
| float                            | 51.2 ms                                                                                                         | 49.2 ms: 1.04x faster                                                                                               |
| python_startup_no_site           | 13.7 ms                                                                                                         | 13.2 ms: 1.04x faster                                                                                               |
| unpickle_pure_python             | 156 us                                                                                                          | 151 us: 1.04x faster                                                                                                |
| python_startup                   | 18.2 ms                                                                                                         | 17.8 ms: 1.03x faster                                                                                               |
| logging_silent                   | 420 ns                                                                                                          | 411 ns: 1.02x faster                                                                                                |
| scimark_monte_carlo              | 46.7 ms                                                                                                         | 45.8 ms: 1.02x faster                                                                                               |
| xml_etree_generate               | 65.1 ms                                                                                                         | 63.9 ms: 1.02x faster                                                                                               |
| xml_etree_process                | 43.9 ms                                                                                                         | 43.1 ms: 1.02x faster                                                                                               |
| scimark_sor                      | 89.9 ms                                                                                                         | 89.3 ms: 1.01x faster                                                                                               |
| json_dumps                       | 8.07 ms                                                                                                         | 8.02 ms: 1.01x faster                                                                                               |
| dask                             | 857 ms                                                                                                          | 853 ms: 1.00x faster                                                                                                |
| deepcopy_reduce                  | 2.00 us                                                                                                         | 1.99 us: 1.00x faster                                                                                               |
| pickle_pure_python               | 222 us                                                                                                          | 221 us: 1.00x faster                                                                                                |
| asyncio_websockets               | 242 ms                                                                                                          | 243 ms: 1.00x slower                                                                                                |
| nbody                            | 77.6 ms                                                                                                         | 77.9 ms: 1.00x slower                                                                                               |
| pickle                           | 9.79 us                                                                                                         | 9.83 us: 1.00x slower                                                                                               |
| regex_v8                         | 17.3 ms                                                                                                         | 17.4 ms: 1.01x slower                                                                                               |
| pickle_dict                      | 21.5 us                                                                                                         | 21.6 us: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 427 ms                                                                                                          | 430 ms: 1.01x slower                                                                                                |
| regex_effbot                     | 2.19 ms                                                                                                         | 2.21 ms: 1.01x slower                                                                                               |
| async_tree_none_tg               | 167 ms                                                                                                          | 169 ms: 1.01x slower                                                                                                |
| raytrace                         | 210 ms                                                                                                          | 211 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                                                          | 395 ms: 1.01x slower                                                                                                |
| pickle_list                      | 3.65 us                                                                                                         | 3.69 us: 1.01x slower                                                                                               |
| richards                         | 36.0 ms                                                                                                         | 36.4 ms: 1.01x slower                                                                                               |
| xml_etree_iterparse              | 76.7 ms                                                                                                         | 77.5 ms: 1.01x slower                                                                                               |
| async_tree_io                    | 402 ms                                                                                                          | 406 ms: 1.01x slower                                                                                                |
| logging_format                   | 4.33 us                                                                                                         | 4.38 us: 1.01x slower                                                                                               |
| sympy_sum                        | 85.1 ms                                                                                                         | 86.0 ms: 1.01x slower                                                                                               |
| richards_super                   | 40.5 ms                                                                                                         | 41.0 ms: 1.01x slower                                                                                               |
| mdp                              | 880 ms                                                                                                          | 891 ms: 1.01x slower                                                                                                |
| async_tree_memoization           | 205 ms                                                                                                          | 208 ms: 1.01x slower                                                                                                |
| deepcopy_memo                    | 19.3 us                                                                                                         | 19.5 us: 1.01x slower                                                                                               |
| deepcopy                         | 185 us                                                                                                          | 187 us: 1.01x slower                                                                                                |
| sphinx                           | 651 ms                                                                                                          | 659 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization_tg  | 182 ms                                                                                                          | 184 ms: 1.01x slower                                                                                                |
| nqueens                          | 67.8 ms                                                                                                         | 68.7 ms: 1.01x slower                                                                                               |
| async_tree_io_tg                 | 389 ms                                                                                                          | 395 ms: 1.01x slower                                                                                                |
| genshi_text                      | 15.6 ms                                                                                                         | 15.9 ms: 1.02x slower                                                                                               |
| generators                       | 23.0 ms                                                                                                         | 23.4 ms: 1.02x slower                                                                                               |
| crypto_pyaes                     | 60.3 ms                                                                                                         | 61.2 ms: 1.02x slower                                                                                               |
| scimark_lu                       | 85.9 ms                                                                                                         | 87.3 ms: 1.02x slower                                                                                               |
| coroutines                       | 18.1 ms                                                                                                         | 18.4 ms: 1.02x slower                                                                                               |
| unpickle                         | 12.0 us                                                                                                         | 12.2 us: 1.02x slower                                                                                               |
| dulwich_log                      | 27.1 ms                                                                                                         | 27.5 ms: 1.02x slower                                                                                               |
| sqlglot_v2_normalize             | 78.2 ms                                                                                                         | 79.6 ms: 1.02x slower                                                                                               |
| pyflate                          | 306 ms                                                                                                          | 311 ms: 1.02x slower                                                                                                |
| bench_thread_pool                | 535 us                                                                                                          | 545 us: 1.02x slower                                                                                                |
| logging_simple                   | 3.97 us                                                                                                         | 4.04 us: 1.02x slower                                                                                               |
| django_template                  | 25.3 ms                                                                                                         | 25.8 ms: 1.02x slower                                                                                               |
| genshi_xml                       | 33.1 ms                                                                                                         | 33.7 ms: 1.02x slower                                                                                               |
| coverage                         | 302 ms                                                                                                          | 308 ms: 1.02x slower                                                                                                |
| hexiom                           | 4.60 ms                                                                                                         | 4.69 ms: 1.02x slower                                                                                               |
| sympy_str                        | 163 ms                                                                                                          | 167 ms: 1.02x slower                                                                                                |
| async_tree_eager_memoization     | 148 ms                                                                                                          | 151 ms: 1.02x slower                                                                                                |
| many_optionals                   | 523 us                                                                                                          | 535 us: 1.02x slower                                                                                                |
| spectral_norm                    | 79.2 ms                                                                                                         | 81.0 ms: 1.02x slower                                                                                               |
| sqlite_synth                     | 1.90 us                                                                                                         | 1.94 us: 1.02x slower                                                                                               |
| bpe_tokeniser                    | 3.67 sec                                                                                                        | 3.76 sec: 1.02x slower                                                                                              |
| sympy_expand                     | 285 ms                                                                                                          | 292 ms: 1.02x slower                                                                                                |
| 2to3                             | 221 ms                                                                                                          | 226 ms: 1.03x slower                                                                                                |
| sympy_integrate                  | 11.7 ms                                                                                                         | 12.1 ms: 1.03x slower                                                                                               |
| tomli_loads                      | 1.40 sec                                                                                                        | 1.44 sec: 1.03x slower                                                                                              |
| go                               | 77.4 ms                                                                                                         | 79.7 ms: 1.03x slower                                                                                               |
| deltablue                        | 2.60 ms                                                                                                         | 2.68 ms: 1.03x slower                                                                                               |
| chaos                            | 43.8 ms                                                                                                         | 45.1 ms: 1.03x slower                                                                                               |
| k_core                           | 1.62 sec                                                                                                        | 1.68 sec: 1.03x slower                                                                                              |
| sqlglot_v2_optimize              | 38.2 ms                                                                                                         | 39.5 ms: 1.03x slower                                                                                               |
| typing_runtime_protocols         | 119 us                                                                                                          | 123 us: 1.04x slower                                                                                                |
| shortest_path                    | 341 ms                                                                                                          | 355 ms: 1.04x slower                                                                                                |
| scimark_sparse_mat_mult          | 4.03 ms                                                                                                         | 4.21 ms: 1.04x slower                                                                                               |
| async_tree_eager                 | 70.4 ms                                                                                                         | 73.6 ms: 1.05x slower                                                                                               |
| async_generators                 | 316 ms                                                                                                          | 331 ms: 1.05x slower                                                                                                |
| docutils                         | 1.59 sec                                                                                                        | 1.67 sec: 1.05x slower                                                                                              |
| sqlglot_v2_transpile             | 1.04 ms                                                                                                         | 1.09 ms: 1.05x slower                                                                                               |
| connected_components             | 312 ms                                                                                                          | 328 ms: 1.05x slower                                                                                                |
| sqlglot_v2_parse                 | 846 us                                                                                                          | 893 us: 1.06x slower                                                                                                |
| pycparser                        | 744 ms                                                                                                          | 791 ms: 1.06x slower                                                                                                |
| meteor_contest                   | 75.9 ms                                                                                                         | 81.8 ms: 1.08x slower                                                                                               |
| comprehensions                   | 11.9 us                                                                                                         | 13.5 us: 1.13x slower                                                                                               |
| fannkuch                         | 314 ms                                                                                                          | 358 ms: 1.14x slower                                                                                                |
| unpack_sequence                  | 50.4 ns                                                                                                         | 62.4 ns: 1.24x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.27x faster                                                                                                        |

Benchmark hidden because not significant (25): asyncio_tcp, pathlib, create_gc_cycles, async_tree_eager_io, xml_etree_parse, gc_traversal, subparsers, json_loads, bench_mp_pool, regex_dna, thrift, asyncio_tcp_ssl, async_tree_cpu_io_mixed, mako, pidigits, telco, unpickle_list, json, async_tree_cpu_io_mixed_tg, async_tree_none, html5lib, async_tree_memoization_tg, async_tree_eager_tg, async_tree_eager_io_tg, pylint

- Geometric mean (including insignificant results): 1.300x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x