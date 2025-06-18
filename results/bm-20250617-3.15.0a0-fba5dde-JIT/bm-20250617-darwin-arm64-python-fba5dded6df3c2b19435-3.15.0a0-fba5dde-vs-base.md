# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.017x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                                                          | 191 ms: 1.02x slower                                                                                                |
| docutils       | 1.64 sec                                                                                                        | 1.63 sec: 1.01x faster                                                                                              |
| html5lib       | 33.3 ms                                                                                                         | 33.7 ms: 1.01x slower                                                                                               |
| sphinx         | 647 ms                                                                                                          | 659 ms: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed         | 450 ms                                                                                                          | 452 ms: 1.00x slower                                                                                                |
| async_tree_eager_cpu_io_mixed   | 389 ms                                                                                                          | 393 ms: 1.01x slower                                                                                                |
| async_tree_none_tg              | 167 ms                                                                                                          | 168 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization_tg | 180 ms                                                                                                          | 182 ms: 1.01x slower                                                                                                |
| async_tree_io                   | 400 ms                                                                                                          | 405 ms: 1.01x slower                                                                                                |
| async_tree_none                 | 173 ms                                                                                                          | 175 ms: 1.01x slower                                                                                                |
| async_tree_memoization          | 204 ms                                                                                                          | 207 ms: 1.01x slower                                                                                                |
| coroutines                      | 18.1 ms                                                                                                         | 18.4 ms: 1.02x slower                                                                                               |
| async_tree_eager_memoization    | 148 ms                                                                                                          | 151 ms: 1.02x slower                                                                                                |
| async_tree_io_tg                | 387 ms                                                                                                          | 397 ms: 1.03x slower                                                                                                |
| async_tree_eager                | 70.5 ms                                                                                                         | 73.8 ms: 1.05x slower                                                                                               |
| async_generators                | 310 ms                                                                                                          | 329 ms: 1.06x slower                                                                                                |
| Geometric mean                  | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (9): asyncio_tcp, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_io_tg, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 83.1 ms                                                                                                         | 80.0 ms: 1.04x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                                                          | 145 ms: 1.00x slower                                                                                                |
| regex_effbot   | 2.19 ms                                                                                                         | 2.22 ms: 1.01x slower                                                                                               |
| regex_compile  | 74.2 ms                                                                                                         | 76.4 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 155 us                                                                                                          | 150 us: 1.03x faster                                                                                                |
| xml_etree_generate   | 65.2 ms                                                                                                         | 64.3 ms: 1.01x faster                                                                                               |
| xml_etree_process    | 43.9 ms                                                                                                         | 43.4 ms: 1.01x faster                                                                                               |
| unpickle_list        | 3.53 us                                                                                                         | 3.51 us: 1.00x faster                                                                                               |
| pickle_dict          | 22.6 us                                                                                                         | 22.7 us: 1.00x slower                                                                                               |
| xml_etree_iterparse  | 76.0 ms                                                                                                         | 77.1 ms: 1.01x slower                                                                                               |
| tomli_loads          | 1.39 sec                                                                                                        | 1.41 sec: 1.02x slower                                                                                              |
| Geometric mean       | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (7): unpickle, xml_etree_parse, pickle_pure_python, pickle, pickle_list, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.3 ms                                                                                                         | 13.9 ms: 1.10x faster                                                                                               |
| python_startup         | 20.2 ms                                                                                                         | 18.7 ms: 1.08x faster                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.09x faster                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.21 ms                                                                                                         | 8.17 ms: 1.00x faster                                                                                               |
| django_template | 25.5 ms                                                                                                         | 25.8 ms: 1.01x slower                                                                                               |
| genshi_text     | 15.7 ms                                                                                                         | 15.9 ms: 1.01x slower                                                                                               |
| genshi_xml      | 33.1 ms                                                                                                         | 33.8 ms: 1.02x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.01x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site          | 15.3 ms                                                                                                         | 13.9 ms: 1.10x faster                                                                                               |
| scimark_fft                     | 267 ms                                                                                                          | 245 ms: 1.09x faster                                                                                                |
| python_startup                  | 20.2 ms                                                                                                         | 18.7 ms: 1.08x faster                                                                                               |
| nbody                           | 83.1 ms                                                                                                         | 80.0 ms: 1.04x faster                                                                                               |
| unpickle_pure_python            | 155 us                                                                                                          | 150 us: 1.03x faster                                                                                                |
| pathlib                         | 24.3 ms                                                                                                         | 23.8 ms: 1.02x faster                                                                                               |
| xml_etree_generate              | 65.2 ms                                                                                                         | 64.3 ms: 1.01x faster                                                                                               |
| xml_etree_process               | 43.9 ms                                                                                                         | 43.4 ms: 1.01x faster                                                                                               |
| docutils                        | 1.64 sec                                                                                                        | 1.63 sec: 1.01x faster                                                                                              |
| mako                            | 8.21 ms                                                                                                         | 8.17 ms: 1.00x faster                                                                                               |
| unpickle_list                   | 3.53 us                                                                                                         | 3.51 us: 1.00x faster                                                                                               |
| regex_dna                       | 145 ms                                                                                                          | 145 ms: 1.00x slower                                                                                                |
| pickle_dict                     | 22.6 us                                                                                                         | 22.7 us: 1.00x slower                                                                                               |
| create_gc_cycles                | 1.39 ms                                                                                                         | 1.40 ms: 1.00x slower                                                                                               |
| async_tree_cpu_io_mixed         | 450 ms                                                                                                          | 452 ms: 1.00x slower                                                                                                |
| sqlite_synth                    | 1.89 us                                                                                                         | 1.90 us: 1.01x slower                                                                                               |
| crypto_pyaes                    | 60.1 ms                                                                                                         | 60.4 ms: 1.01x slower                                                                                               |
| thrift                          | 571 us                                                                                                          | 575 us: 1.01x slower                                                                                                |
| shortest_path                   | 340 ms                                                                                                          | 342 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed   | 389 ms                                                                                                          | 393 ms: 1.01x slower                                                                                                |
| async_tree_none_tg              | 167 ms                                                                                                          | 168 ms: 1.01x slower                                                                                                |
| logging_silent                  | 413 ns                                                                                                          | 417 ns: 1.01x slower                                                                                                |
| django_template                 | 25.5 ms                                                                                                         | 25.8 ms: 1.01x slower                                                                                               |
| raytrace                        | 211 ms                                                                                                          | 214 ms: 1.01x slower                                                                                                |
| html5lib                        | 33.3 ms                                                                                                         | 33.7 ms: 1.01x slower                                                                                               |
| async_tree_eager_memoization_tg | 180 ms                                                                                                          | 182 ms: 1.01x slower                                                                                                |
| connected_components            | 312 ms                                                                                                          | 315 ms: 1.01x slower                                                                                                |
| chaos                           | 44.1 ms                                                                                                         | 44.7 ms: 1.01x slower                                                                                               |
| regex_effbot                    | 2.19 ms                                                                                                         | 2.22 ms: 1.01x slower                                                                                               |
| async_tree_io                   | 400 ms                                                                                                          | 405 ms: 1.01x slower                                                                                                |
| async_tree_none                 | 173 ms                                                                                                          | 175 ms: 1.01x slower                                                                                                |
| dulwich_log                     | 27.0 ms                                                                                                         | 27.3 ms: 1.01x slower                                                                                               |
| genshi_text                     | 15.7 ms                                                                                                         | 15.9 ms: 1.01x slower                                                                                               |
| nqueens                         | 67.5 ms                                                                                                         | 68.3 ms: 1.01x slower                                                                                               |
| richards_super                  | 40.4 ms                                                                                                         | 41.0 ms: 1.01x slower                                                                                               |
| mdp                             | 883 ms                                                                                                          | 895 ms: 1.01x slower                                                                                                |
| async_tree_memoization          | 204 ms                                                                                                          | 207 ms: 1.01x slower                                                                                                |
| xml_etree_iterparse             | 76.0 ms                                                                                                         | 77.1 ms: 1.01x slower                                                                                               |
| deepcopy_memo                   | 19.3 us                                                                                                         | 19.6 us: 1.01x slower                                                                                               |
| bench_thread_pool               | 538 us                                                                                                          | 546 us: 1.02x slower                                                                                                |
| coroutines                      | 18.1 ms                                                                                                         | 18.4 ms: 1.02x slower                                                                                               |
| bpe_tokeniser                   | 3.65 sec                                                                                                        | 3.71 sec: 1.02x slower                                                                                              |
| richards                        | 35.9 ms                                                                                                         | 36.5 ms: 1.02x slower                                                                                               |
| sphinx                          | 647 ms                                                                                                          | 659 ms: 1.02x slower                                                                                                |
| tomli_loads                     | 1.39 sec                                                                                                        | 1.41 sec: 1.02x slower                                                                                              |
| coverage                        | 59.8 ms                                                                                                         | 60.8 ms: 1.02x slower                                                                                               |
| subparsers                      | 15.9 ms                                                                                                         | 16.2 ms: 1.02x slower                                                                                               |
| sympy_sum                       | 85.1 ms                                                                                                         | 86.7 ms: 1.02x slower                                                                                               |
| sqlglot_v2_normalize            | 79.3 ms                                                                                                         | 80.9 ms: 1.02x slower                                                                                               |
| genshi_xml                      | 33.1 ms                                                                                                         | 33.8 ms: 1.02x slower                                                                                               |
| async_tree_eager_memoization    | 148 ms                                                                                                          | 151 ms: 1.02x slower                                                                                                |
| 2to3                            | 187 ms                                                                                                          | 191 ms: 1.02x slower                                                                                                |
| deepcopy                        | 186 us                                                                                                          | 190 us: 1.02x slower                                                                                                |
| scimark_lu                      | 86.6 ms                                                                                                         | 88.6 ms: 1.02x slower                                                                                               |
| spectral_norm                   | 79.9 ms                                                                                                         | 81.9 ms: 1.02x slower                                                                                               |
| pylint                          | 176 ms                                                                                                          | 181 ms: 1.02x slower                                                                                                |
| telco                           | 5.50 ms                                                                                                         | 5.63 ms: 1.02x slower                                                                                               |
| logging_format                  | 4.29 us                                                                                                         | 4.39 us: 1.02x slower                                                                                               |
| generators                      | 22.8 ms                                                                                                         | 23.4 ms: 1.03x slower                                                                                               |
| async_tree_io_tg                | 387 ms                                                                                                          | 397 ms: 1.03x slower                                                                                                |
| deepcopy_reduce                 | 1.98 us                                                                                                         | 2.04 us: 1.03x slower                                                                                               |
| logging_simple                  | 3.96 us                                                                                                         | 4.07 us: 1.03x slower                                                                                               |
| regex_compile                   | 74.2 ms                                                                                                         | 76.4 ms: 1.03x slower                                                                                               |
| sympy_str                       | 164 ms                                                                                                          | 169 ms: 1.03x slower                                                                                                |
| many_optionals                  | 520 us                                                                                                          | 536 us: 1.03x slower                                                                                                |
| scimark_sparse_mat_mult         | 4.19 ms                                                                                                         | 4.32 ms: 1.03x slower                                                                                               |
| deltablue                       | 2.61 ms                                                                                                         | 2.70 ms: 1.03x slower                                                                                               |
| go                              | 77.2 ms                                                                                                         | 79.8 ms: 1.03x slower                                                                                               |
| sympy_integrate                 | 11.8 ms                                                                                                         | 12.2 ms: 1.03x slower                                                                                               |
| sympy_expand                    | 286 ms                                                                                                          | 296 ms: 1.03x slower                                                                                                |
| k_core                          | 1.54 sec                                                                                                        | 1.59 sec: 1.04x slower                                                                                              |
| sqlglot_v2_optimize             | 38.8 ms                                                                                                         | 40.2 ms: 1.04x slower                                                                                               |
| typing_runtime_protocols        | 120 us                                                                                                          | 125 us: 1.04x slower                                                                                                |
| async_tree_eager                | 70.5 ms                                                                                                         | 73.8 ms: 1.05x slower                                                                                               |
| sqlglot_v2_transpile            | 1.04 ms                                                                                                         | 1.10 ms: 1.06x slower                                                                                               |
| async_generators                | 310 ms                                                                                                          | 329 ms: 1.06x slower                                                                                                |
| sqlglot_v2_parse                | 848 us                                                                                                          | 905 us: 1.07x slower                                                                                                |
| pycparser                       | 741 ms                                                                                                          | 792 ms: 1.07x slower                                                                                                |
| meteor_contest                  | 75.8 ms                                                                                                         | 81.4 ms: 1.07x slower                                                                                               |
| hexiom                          | 4.58 ms                                                                                                         | 4.96 ms: 1.08x slower                                                                                               |
| fannkuch                        | 311 ms                                                                                                          | 349 ms: 1.12x slower                                                                                                |
| comprehensions                  | 12.0 us                                                                                                         | 13.6 us: 1.14x slower                                                                                               |
| pprint_pformat                  | 1.19 sec                                                                                                        | 1.40 sec: 1.18x slower                                                                                              |
| pprint_safe_repr                | 586 ms                                                                                                          | 693 ms: 1.18x slower                                                                                                |
| unpack_sequence                 | 50.2 ns                                                                                                         | 62.4 ns: 1.24x slower                                                                                               |
| Geometric mean                  | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (26): asyncio_tcp, bench_mp_pool, scimark_sor, unpickle, pidigits, xml_etree_parse, dask, pickle_pure_python, pickle, asyncio_websockets, regex_v8, pickle_list, pyflate, gc_traversal, scimark_monte_carlo, json_dumps, json_loads, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, float, json, async_tree_eager_tg, async_tree_eager_io_tg, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_eager_io

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x