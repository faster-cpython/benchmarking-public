# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: darwin-arm64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.149x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                                 | 185 ms: 1.04x slower                                                   |
| docutils       | 1.50 sec                                                               | 1.40 sec: 1.07x faster                                                 |
| html5lib       | 33.1 ms                                                                | 28.2 ms: 1.17x faster                                                  |
| sphinx         | 610 ms                                                                 | 577 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                       | 18.6 ms                                                                | 14.4 ms: 1.30x faster                                                  |
| async_tree_eager                 | 69.8 ms                                                                | 55.4 ms: 1.26x faster                                                  |
| async_tree_memoization           | 221 ms                                                                 | 180 ms: 1.23x faster                                                   |
| async_tree_none                  | 178 ms                                                                 | 145 ms: 1.23x faster                                                   |
| async_tree_none_tg               | 172 ms                                                                 | 140 ms: 1.22x faster                                                   |
| async_tree_eager_tg              | 143 ms                                                                 | 120 ms: 1.20x faster                                                   |
| async_tree_io_tg                 | 401 ms                                                                 | 342 ms: 1.18x faster                                                   |
| async_tree_io                    | 413 ms                                                                 | 353 ms: 1.17x faster                                                   |
| async_tree_eager_memoization_tg  | 191 ms                                                                 | 164 ms: 1.16x faster                                                   |
| async_tree_memoization_tg        | 212 ms                                                                 | 183 ms: 1.16x faster                                                   |
| async_tree_eager_io              | 399 ms                                                                 | 345 ms: 1.16x faster                                                   |
| async_tree_eager_memoization     | 150 ms                                                                 | 132 ms: 1.14x faster                                                   |
| async_tree_eager_io_tg           | 407 ms                                                                 | 359 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 436 ms                                                                 | 397 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 430 ms                                                                 | 398 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 365 ms                                                                 | 344 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 403 ms                                                                 | 381 ms: 1.06x faster                                                   |
| async_generators                 | 268 ms                                                                 | 253 ms: 1.06x faster                                                   |
| Geometric mean                   | (ref)                                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                | 66.9 ms: 1.38x faster                                                  |
| float          | 54.5 ms                                                                | 42.8 ms: 1.27x faster                                                  |
| pidigits       | 284 ms                                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.21x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.5 ms                                                                | 64.0 ms: 1.21x faster                                                  |
| regex_dna      | 141 ms                                                                 | 127 ms: 1.11x faster                                                   |
| regex_effbot   | 2.29 ms                                                                | 2.22 ms: 1.03x faster                                                  |
| regex_v8       | 16.9 ms                                                                | 17.5 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 169 us                                                                 | 134 us: 1.26x faster                                                   |
| pickle_pure_python   | 229 us                                                                 | 185 us: 1.24x faster                                                   |
| tomli_loads          | 1.44 sec                                                               | 1.19 sec: 1.21x faster                                                 |
| xml_etree_process    | 42.8 ms                                                                | 35.8 ms: 1.20x faster                                                  |
| xml_etree_generate   | 58.1 ms                                                                | 50.6 ms: 1.15x faster                                                  |
| xml_etree_parse      | 103 ms                                                                 | 93.7 ms: 1.10x faster                                                  |
| json_dumps           | 7.54 ms                                                                | 7.05 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.7 ms                                                                | 71.2 ms: 1.05x faster                                                  |
| json_loads           | 17.7 us                                                                | 17.3 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                                | 13.4 ms: 1.03x faster                                                  |
| python_startup         | 18.6 ms                                                                | 18.6 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.3 ms                                                                | 13.3 ms: 1.23x faster                                                  |
| genshi_xml      | 33.7 ms                                                                | 27.8 ms: 1.21x faster                                                  |
| mako            | 8.41 ms                                                                | 6.97 ms: 1.21x faster                                                  |
| django_template | 24.1 ms                                                                | 20.4 ms: 1.18x faster                                                  |
| Geometric mean  | (ref)                                                                  | 1.21x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20250226-darwin-arm64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| hexiom                           | 5.28 ms                                                                | 3.73 ms: 1.42x faster                                                  |
| generators                       | 28.9 ms                                                                | 20.7 ms: 1.40x faster                                                  |
| nbody                            | 92.1 ms                                                                | 66.9 ms: 1.38x faster                                                  |
| richards                         | 39.9 ms                                                                | 29.3 ms: 1.36x faster                                                  |
| deltablue                        | 2.76 ms                                                                | 2.04 ms: 1.35x faster                                                  |
| go                               | 94.8 ms                                                                | 70.3 ms: 1.35x faster                                                  |
| raytrace                         | 212 ms                                                                 | 159 ms: 1.33x faster                                                   |
| comprehensions                   | 13.1 us                                                                | 9.99 us: 1.31x faster                                                  |
| richards_super                   | 42.9 ms                                                                | 32.7 ms: 1.31x faster                                                  |
| coroutines                       | 18.6 ms                                                                | 14.4 ms: 1.30x faster                                                  |
| scimark_sor                      | 92.7 ms                                                                | 71.8 ms: 1.29x faster                                                  |
| scimark_monte_carlo              | 49.9 ms                                                                | 38.8 ms: 1.29x faster                                                  |
| float                            | 54.5 ms                                                                | 42.8 ms: 1.27x faster                                                  |
| chaos                            | 44.0 ms                                                                | 34.8 ms: 1.26x faster                                                  |
| deepcopy_memo                    | 21.0 us                                                                | 16.7 us: 1.26x faster                                                  |
| async_tree_eager                 | 69.8 ms                                                                | 55.4 ms: 1.26x faster                                                  |
| unpickle_pure_python             | 169 us                                                                 | 134 us: 1.26x faster                                                   |
| pprint_pformat                   | 1.10 sec                                                               | 875 ms: 1.25x faster                                                   |
| pprint_safe_repr                 | 540 ms                                                                 | 434 ms: 1.25x faster                                                   |
| pickle_pure_python               | 229 us                                                                 | 185 us: 1.24x faster                                                   |
| fannkuch                         | 290 ms                                                                 | 235 ms: 1.24x faster                                                   |
| logging_silent                   | 72.9 ns                                                                | 59.2 ns: 1.23x faster                                                  |
| meteor_contest                   | 78.3 ms                                                                | 63.5 ms: 1.23x faster                                                  |
| genshi_text                      | 16.3 ms                                                                | 13.3 ms: 1.23x faster                                                  |
| async_tree_memoization           | 221 ms                                                                 | 180 ms: 1.23x faster                                                   |
| async_tree_none                  | 178 ms                                                                 | 145 ms: 1.23x faster                                                   |
| sqlglot_parse                    | 887 us                                                                 | 723 us: 1.23x faster                                                   |
| async_tree_none_tg               | 172 ms                                                                 | 140 ms: 1.22x faster                                                   |
| genshi_xml                       | 33.7 ms                                                                | 27.8 ms: 1.21x faster                                                  |
| tomli_loads                      | 1.44 sec                                                               | 1.19 sec: 1.21x faster                                                 |
| sqlglot_transpile                | 1.07 ms                                                                | 882 us: 1.21x faster                                                   |
| regex_compile                    | 77.5 ms                                                                | 64.0 ms: 1.21x faster                                                  |
| mako                             | 8.41 ms                                                                | 6.97 ms: 1.21x faster                                                  |
| spectral_norm                    | 77.8 ms                                                                | 64.5 ms: 1.21x faster                                                  |
| typing_runtime_protocols         | 101 us                                                                 | 83.6 us: 1.20x faster                                                  |
| logging_simple                   | 3.75 us                                                                | 3.12 us: 1.20x faster                                                  |
| async_tree_eager_tg              | 143 ms                                                                 | 120 ms: 1.20x faster                                                   |
| xml_etree_process                | 42.8 ms                                                                | 35.8 ms: 1.20x faster                                                  |
| logging_format                   | 4.06 us                                                                | 3.42 us: 1.19x faster                                                  |
| pyflate                          | 352 ms                                                                 | 297 ms: 1.18x faster                                                   |
| deepcopy                         | 169 us                                                                 | 143 us: 1.18x faster                                                   |
| scimark_fft                      | 198 ms                                                                 | 167 ms: 1.18x faster                                                   |
| django_template                  | 24.1 ms                                                                | 20.4 ms: 1.18x faster                                                  |
| async_tree_io_tg                 | 401 ms                                                                 | 342 ms: 1.18x faster                                                   |
| html5lib                         | 33.1 ms                                                                | 28.2 ms: 1.17x faster                                                  |
| async_tree_io                    | 413 ms                                                                 | 353 ms: 1.17x faster                                                   |
| crypto_pyaes                     | 58.7 ms                                                                | 50.5 ms: 1.16x faster                                                  |
| async_tree_eager_memoization_tg  | 191 ms                                                                 | 164 ms: 1.16x faster                                                   |
| async_tree_memoization_tg        | 212 ms                                                                 | 183 ms: 1.16x faster                                                   |
| deepcopy_reduce                  | 1.76 us                                                                | 1.52 us: 1.16x faster                                                  |
| async_tree_eager_io              | 399 ms                                                                 | 345 ms: 1.16x faster                                                   |
| nqueens                          | 64.7 ms                                                                | 56.1 ms: 1.15x faster                                                  |
| xml_etree_generate               | 58.1 ms                                                                | 50.6 ms: 1.15x faster                                                  |
| sympy_str                        | 153 ms                                                                 | 135 ms: 1.14x faster                                                   |
| sqlalchemy_imperative            | 7.09 ms                                                                | 6.23 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 150 ms                                                                 | 132 ms: 1.14x faster                                                   |
| async_tree_eager_io_tg           | 407 ms                                                                 | 359 ms: 1.14x faster                                                   |
| sympy_expand                     | 255 ms                                                                 | 225 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult          | 3.09 ms                                                                | 2.73 ms: 1.13x faster                                                  |
| sqlalchemy_declarative           | 62.5 ms                                                                | 55.3 ms: 1.13x faster                                                  |
| sympy_integrate                  | 12.2 ms                                                                | 10.9 ms: 1.13x faster                                                  |
| bench_thread_pool                | 524 us                                                                 | 469 us: 1.12x faster                                                   |
| regex_dna                        | 141 ms                                                                 | 127 ms: 1.11x faster                                                   |
| dulwich_log                      | 29.9 ms                                                                | 27.1 ms: 1.11x faster                                                  |
| xml_etree_parse                  | 103 ms                                                                 | 93.7 ms: 1.10x faster                                                  |
| pycparser                        | 705 ms                                                                 | 639 ms: 1.10x faster                                                   |
| many_optionals                   | 468 us                                                                 | 425 us: 1.10x faster                                                   |
| async_tree_cpu_io_mixed          | 436 ms                                                                 | 397 ms: 1.10x faster                                                   |
| thrift                           | 463 us                                                                 | 424 us: 1.09x faster                                                   |
| sqlglot_normalize                | 196 ms                                                                 | 180 ms: 1.09x faster                                                   |
| sympy_sum                        | 79.6 ms                                                                | 73.0 ms: 1.09x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                                               | 2.98 sec: 1.09x faster                                                 |
| pylint                           | 169 ms                                                                 | 156 ms: 1.09x faster                                                   |
| sqlglot_optimize                 | 35.6 ms                                                                | 32.9 ms: 1.08x faster                                                  |
| mdp                              | 1.56 sec                                                               | 1.44 sec: 1.08x faster                                                 |
| subparsers                       | 12.9 ms                                                                | 11.9 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 430 ms                                                                 | 398 ms: 1.08x faster                                                   |
| telco                            | 4.73 ms                                                                | 4.41 ms: 1.07x faster                                                  |
| connected_components             | 316 ms                                                                 | 294 ms: 1.07x faster                                                   |
| scimark_lu                       | 83.4 ms                                                                | 77.9 ms: 1.07x faster                                                  |
| docutils                         | 1.50 sec                                                               | 1.40 sec: 1.07x faster                                                 |
| json_dumps                       | 7.54 ms                                                                | 7.05 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 365 ms                                                                 | 344 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 403 ms                                                                 | 381 ms: 1.06x faster                                                   |
| async_generators                 | 268 ms                                                                 | 253 ms: 1.06x faster                                                   |
| sphinx                           | 610 ms                                                                 | 577 ms: 1.06x faster                                                   |
| shortest_path                    | 339 ms                                                                 | 322 ms: 1.05x faster                                                   |
| xml_etree_iterparse              | 74.7 ms                                                                | 71.2 ms: 1.05x faster                                                  |
| sqlite_synth                     | 1.54 us                                                                | 1.48 us: 1.04x faster                                                  |
| coverage                         | 48.0 ms                                                                | 46.6 ms: 1.03x faster                                                  |
| python_startup_no_site           | 13.8 ms                                                                | 13.4 ms: 1.03x faster                                                  |
| k_core                           | 1.54 sec                                                               | 1.49 sec: 1.03x faster                                                 |
| regex_effbot                     | 2.29 ms                                                                | 2.22 ms: 1.03x faster                                                  |
| pathlib                          | 23.7 ms                                                                | 23.0 ms: 1.03x faster                                                  |
| bench_mp_pool                    | 61.8 ms                                                                | 60.4 ms: 1.02x faster                                                  |
| json_loads                       | 17.7 us                                                                | 17.3 us: 1.02x faster                                                  |
| json                             | 3.02 ms                                                                | 2.97 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                                 | 281 ms: 1.01x faster                                                   |
| python_startup                   | 18.6 ms                                                                | 18.6 ms: 1.00x faster                                                  |
| dask                             | 769 ms                                                                 | 767 ms: 1.00x faster                                                   |
| regex_v8                         | 16.9 ms                                                                | 17.5 ms: 1.04x slower                                                  |
| 2to3                             | 178 ms                                                                 | 185 ms: 1.04x slower                                                   |
| Geometric mean                   | (ref)                                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (3): create_gc_cycles, gc_traversal, asyncio_websockets

- Geometric mean (including insignificant results): 1.149x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 0.98x