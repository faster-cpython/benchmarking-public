# Results vs. 3.13.0

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: 6d7efa0
- commit date: 2025-07-29
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                               |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                             |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                              |
| sphinx         | 602 ms                                                 | 578 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 369 ms: 1.36x faster                                               |
| async_tree_io                    | 508 ms                                                 | 381 ms: 1.33x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                               |
| async_tree_none                  | 212 ms                                                 | 166 ms: 1.27x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                               |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                               |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                               |
| async_tree_eager                 | 69.9 ms                                                | 64.6 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                               |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                               |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                               |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.1 ms: 1.09x faster                                              |
| nbody          | 73.6 ms                                                | 71.9 ms: 1.02x faster                                              |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.15 ms: 1.23x faster                                              |
| regex_v8       | 17.0 ms                                                | 15.2 ms: 1.12x faster                                              |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                               |
| regex_compile  | 78.3 ms                                                | 73.0 ms: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                               |
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                             |
| xml_etree_process    | 41.3 ms                                                | 34.7 ms: 1.19x faster                                              |
| xml_etree_generate   | 57.1 ms                                                | 49.5 ms: 1.15x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 74.2 ms                                                | 70.9 ms: 1.05x faster                                              |
| pickle_pure_python   | 215 us                                                 | 206 us: 1.04x faster                                               |
| json_dumps           | 6.47 ms                                                | 6.61 ms: 1.02x slower                                              |
| json_loads           | 17.0 us                                                | 17.5 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.5 ms: 1.14x faster                                              |
| python_startup_no_site | 13.7 ms                                                | 12.2 ms: 1.13x faster                                              |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.51 ms: 1.19x faster                                              |
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.08x faster                                              |
| genshi_xml      | 34.1 ms                                                | 33.6 ms: 1.01x faster                                              |
| django_template | 20.5 ms                                                | 23.2 ms: 1.13x slower                                              |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 775 ms: 1.93x faster                                               |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                               |
| deepcopy                         | 236 us                                                 | 173 us: 1.36x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 369 ms: 1.36x faster                                               |
| go                               | 117 ms                                                 | 87.2 ms: 1.34x faster                                              |
| async_tree_io                    | 508 ms                                                 | 381 ms: 1.33x faster                                               |
| generators                       | 31.9 ms                                                | 24.6 ms: 1.30x faster                                              |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                               |
| async_tree_none                  | 212 ms                                                 | 166 ms: 1.27x faster                                               |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                             |
| scimark_sor                      | 106 ms                                                 | 84.7 ms: 1.25x faster                                              |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                               |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.25x faster                                              |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.15 ms: 1.23x faster                                              |
| pyflate                          | 352 ms                                                 | 287 ms: 1.22x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                               |
| pprint_safe_repr                 | 541 ms                                                 | 449 ms: 1.20x faster                                               |
| spectral_norm                    | 76.5 ms                                                | 63.8 ms: 1.20x faster                                              |
| pprint_pformat                   | 1.10 sec                                               | 920 ms: 1.20x faster                                               |
| mako                             | 7.75 ms                                                | 6.51 ms: 1.19x faster                                              |
| xml_etree_process                | 41.3 ms                                                | 34.7 ms: 1.19x faster                                              |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                              |
| xml_etree_generate               | 57.1 ms                                                | 49.5 ms: 1.15x faster                                              |
| python_startup                   | 18.8 ms                                                | 16.5 ms: 1.14x faster                                              |
| dulwich_log                      | 28.7 ms                                                | 25.5 ms: 1.13x faster                                              |
| python_startup_no_site           | 13.7 ms                                                | 12.2 ms: 1.13x faster                                              |
| fannkuch                         | 279 ms                                                 | 248 ms: 1.12x faster                                               |
| bpe_tokeniser                    | 3.26 sec                                               | 2.91 sec: 1.12x faster                                             |
| regex_v8                         | 17.0 ms                                                | 15.2 ms: 1.12x faster                                              |
| crypto_pyaes                     | 55.3 ms                                                | 49.8 ms: 1.11x faster                                              |
| xml_etree_parse                  | 108 ms                                                 | 97.6 ms: 1.11x faster                                              |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                              |
| pylint                           | 180 ms                                                 | 164 ms: 1.10x faster                                               |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                               |
| telco                            | 4.84 ms                                                | 4.43 ms: 1.09x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 46.2 ms: 1.09x faster                                              |
| float                            | 55.8 ms                                                | 51.1 ms: 1.09x faster                                              |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.08x faster                                              |
| async_tree_eager                 | 69.9 ms                                                | 64.6 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                               |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                               |
| regex_compile                    | 78.3 ms                                                | 73.0 ms: 1.07x faster                                              |
| typing_runtime_protocols         | 101 us                                                 | 94.8 us: 1.06x faster                                              |
| hexiom                           | 4.87 ms                                                | 4.58 ms: 1.06x faster                                              |
| comprehensions                   | 12.0 us                                                | 11.3 us: 1.06x faster                                              |
| chaos                            | 41.1 ms                                                | 38.9 ms: 1.06x faster                                              |
| logging_simple                   | 3.56 us                                                | 3.37 us: 1.05x faster                                              |
| richards                         | 36.2 ms                                                | 34.3 ms: 1.05x faster                                              |
| logging_format                   | 3.85 us                                                | 3.66 us: 1.05x faster                                              |
| deltablue                        | 2.65 ms                                                | 2.52 ms: 1.05x faster                                              |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                               |
| xml_etree_iterparse              | 74.2 ms                                                | 70.9 ms: 1.05x faster                                              |
| scimark_fft                      | 200 ms                                                 | 191 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                               |
| sphinx                           | 602 ms                                                 | 578 ms: 1.04x faster                                               |
| pickle_pure_python               | 215 us                                                 | 206 us: 1.04x faster                                               |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                               |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.03x faster                                              |
| nbody                            | 73.6 ms                                                | 71.9 ms: 1.02x faster                                              |
| richards_super                   | 39.2 ms                                                | 38.4 ms: 1.02x faster                                              |
| thrift                           | 466 us                                                 | 457 us: 1.02x faster                                               |
| raytrace                         | 181 ms                                                 | 178 ms: 1.02x faster                                               |
| genshi_xml                       | 34.1 ms                                                | 33.6 ms: 1.01x faster                                              |
| scimark_lu                       | 75.9 ms                                                | 75.5 ms: 1.00x faster                                              |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                               |
| sympy_expand                     | 248 ms                                                 | 249 ms: 1.01x slower                                               |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                             |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                              |
| connected_components             | 319 ms                                                 | 322 ms: 1.01x slower                                               |
| shortest_path                    | 345 ms                                                 | 349 ms: 1.01x slower                                               |
| sympy_str                        | 146 ms                                                 | 147 ms: 1.01x slower                                               |
| pycparser                        | 701 ms                                                 | 710 ms: 1.01x slower                                               |
| json_dumps                       | 6.47 ms                                                | 6.61 ms: 1.02x slower                                              |
| json_loads                       | 17.0 us                                                | 17.5 us: 1.03x slower                                              |
| sympy_sum                        | 75.1 ms                                                | 77.1 ms: 1.03x slower                                              |
| coverage                         | 46.2 ms                                                | 47.6 ms: 1.03x slower                                              |
| dask                             | 771 ms                                                 | 802 ms: 1.04x slower                                               |
| logging_silent                   | 71.0 ns                                                | 75.0 ns: 1.06x slower                                              |
| gc_traversal                     | 2.94 ms                                                | 3.25 ms: 1.11x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                               |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.37 ms: 1.13x slower                                              |
| django_template                  | 20.5 ms                                                | 23.2 ms: 1.13x slower                                              |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                              |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                               |
| many_optionals                   | 409 us                                                 | 593 us: 1.45x slower                                               |
| subparsers                       | 9.44 ms                                                | 25.2 ms: 2.67x slower                                              |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (6): k_core, json, nqueens, asyncio_websockets, meteor_contest, pathlib
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250729-3.15.0a0-6d7efa0-JIT/bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x