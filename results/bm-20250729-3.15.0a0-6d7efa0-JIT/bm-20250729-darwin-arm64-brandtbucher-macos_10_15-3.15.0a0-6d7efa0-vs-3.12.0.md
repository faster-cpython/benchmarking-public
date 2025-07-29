# Results vs. 3.12.0

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: 6d7efa0
- commit date: 2025-07-29
- overall geometric mean: 1.063x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                               |
| docutils       | 1.45 sec                                               | 1.46 sec: 1.00x slower                                             |
| sphinx         | 613 ms                                                 | 578 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 369 ms: 1.82x faster                                               |
| async_tree_io                    | 672 ms                                                 | 381 ms: 1.76x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.60x faster                                               |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.59x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                               |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                               |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 64.6 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.1 ms: 1.06x faster                                              |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| nbody          | 67.6 ms                                                | 71.9 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.15 ms: 1.14x faster                                              |
| regex_compile  | 75.9 ms                                                | 73.0 ms: 1.04x faster                                              |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                               |
| regex_v8       | 15.1 ms                                                | 15.2 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 128 us: 1.13x faster                                               |
| xml_etree_generate   | 55.4 ms                                                | 49.5 ms: 1.12x faster                                              |
| xml_etree_process    | 38.9 ms                                                | 34.7 ms: 1.12x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.11x faster                                              |
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                             |
| xml_etree_iterparse  | 75.5 ms                                                | 70.9 ms: 1.06x faster                                              |
| json_loads           | 17.0 us                                                | 17.5 us: 1.03x slower                                              |
| pickle_pure_python   | 197 us                                                 | 206 us: 1.05x slower                                               |
| json_dumps           | 6.19 ms                                                | 6.61 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.2 ms: 1.08x faster                                              |
| python_startup         | 17.8 ms                                                | 16.5 ms: 1.08x faster                                              |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.51 ms: 1.14x faster                                              |
| genshi_text     | 14.7 ms                                                | 15.6 ms: 1.06x slower                                              |
| genshi_xml      | 30.5 ms                                                | 33.6 ms: 1.10x slower                                              |
| django_template | 19.7 ms                                                | 23.2 ms: 1.18x slower                                              |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 775 ms: 1.93x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 369 ms: 1.82x faster                                               |
| async_tree_io                    | 672 ms                                                 | 381 ms: 1.76x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.60x faster                                               |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.59x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                               |
| deepcopy                         | 226 us                                                 | 173 us: 1.30x faster                                               |
| subparsers                       | 32.1 ms                                                | 25.2 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                               |
| comprehensions                   | 14.0 us                                                | 11.3 us: 1.24x faster                                              |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                               |
| spectral_norm                    | 76.5 ms                                                | 63.8 ms: 1.20x faster                                              |
| generators                       | 29.4 ms                                                | 24.6 ms: 1.19x faster                                              |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                              |
| dulwich_log                      | 29.2 ms                                                | 25.5 ms: 1.15x faster                                              |
| raytrace                         | 204 ms                                                 | 178 ms: 1.15x faster                                               |
| mako                             | 7.44 ms                                                | 6.51 ms: 1.14x faster                                              |
| regex_effbot                     | 2.44 ms                                                | 2.15 ms: 1.14x faster                                              |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.13x faster                                               |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                              |
| go                               | 98.5 ms                                                | 87.2 ms: 1.13x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 2.91 sec: 1.13x faster                                             |
| xml_etree_generate               | 55.4 ms                                                | 49.5 ms: 1.12x faster                                              |
| xml_etree_process                | 38.9 ms                                                | 34.7 ms: 1.12x faster                                              |
| pylint                           | 182 ms                                                 | 164 ms: 1.11x faster                                               |
| xml_etree_parse                  | 108 ms                                                 | 97.6 ms: 1.11x faster                                              |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                             |
| pyflate                          | 311 ms                                                 | 287 ms: 1.08x faster                                               |
| python_startup_no_site           | 13.2 ms                                                | 12.2 ms: 1.08x faster                                              |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                             |
| pprint_safe_repr                 | 483 ms                                                 | 449 ms: 1.08x faster                                               |
| python_startup                   | 17.8 ms                                                | 16.5 ms: 1.08x faster                                              |
| pprint_pformat                   | 986 ms                                                 | 920 ms: 1.07x faster                                               |
| chaos                            | 41.6 ms                                                | 38.9 ms: 1.07x faster                                              |
| logging_simple                   | 3.60 us                                                | 3.37 us: 1.07x faster                                              |
| logging_format                   | 3.90 us                                                | 3.66 us: 1.07x faster                                              |
| xml_etree_iterparse              | 75.5 ms                                                | 70.9 ms: 1.06x faster                                              |
| sphinx                           | 613 ms                                                 | 578 ms: 1.06x faster                                               |
| float                            | 54.1 ms                                                | 51.1 ms: 1.06x faster                                              |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.06x faster                                              |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                               |
| regex_compile                    | 75.9 ms                                                | 73.0 ms: 1.04x faster                                              |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                               |
| crypto_pyaes                     | 51.4 ms                                                | 49.8 ms: 1.03x faster                                              |
| thrift                           | 468 us                                                 | 457 us: 1.02x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 64.6 ms: 1.02x faster                                              |
| deltablue                        | 2.57 ms                                                | 2.52 ms: 1.02x faster                                              |
| scimark_fft                      | 194 ms                                                 | 191 ms: 1.02x faster                                               |
| scimark_sor                      | 85.8 ms                                                | 84.7 ms: 1.01x faster                                              |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.01x faster                                              |
| fannkuch                         | 250 ms                                                 | 248 ms: 1.01x faster                                               |
| docutils                         | 1.45 sec                                               | 1.46 sec: 1.00x slower                                             |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| json                             | 3.00 ms                                                | 3.03 ms: 1.01x slower                                              |
| regex_v8                         | 15.1 ms                                                | 15.2 ms: 1.01x slower                                              |
| sympy_sum                        | 76.2 ms                                                | 77.1 ms: 1.01x slower                                              |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                               |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.02x slower                                              |
| sympy_str                        | 144 ms                                                 | 147 ms: 1.02x slower                                               |
| json_loads                       | 17.0 us                                                | 17.5 us: 1.03x slower                                              |
| scimark_lu                       | 73.5 ms                                                | 75.5 ms: 1.03x slower                                              |
| dask                             | 779 ms                                                 | 802 ms: 1.03x slower                                               |
| logging_silent                   | 72.5 ns                                                | 75.0 ns: 1.03x slower                                              |
| typing_runtime_protocols         | 91.5 us                                                | 94.8 us: 1.04x slower                                              |
| nqueens                          | 59.5 ms                                                | 61.7 ms: 1.04x slower                                              |
| scimark_monte_carlo              | 44.5 ms                                                | 46.2 ms: 1.04x slower                                              |
| pickle_pure_python               | 197 us                                                 | 206 us: 1.05x slower                                               |
| hexiom                           | 4.38 ms                                                | 4.58 ms: 1.05x slower                                              |
| pycparser                        | 673 ms                                                 | 710 ms: 1.06x slower                                               |
| shortest_path                    | 331 ms                                                 | 349 ms: 1.06x slower                                               |
| genshi_text                      | 14.7 ms                                                | 15.6 ms: 1.06x slower                                              |
| nbody                            | 67.6 ms                                                | 71.9 ms: 1.06x slower                                              |
| sympy_expand                     | 233 ms                                                 | 249 ms: 1.07x slower                                               |
| json_dumps                       | 6.19 ms                                                | 6.61 ms: 1.07x slower                                              |
| meteor_contest                   | 69.1 ms                                                | 74.1 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.37 ms: 1.07x slower                                              |
| connected_components             | 300 ms                                                 | 322 ms: 1.07x slower                                               |
| genshi_xml                       | 30.5 ms                                                | 33.6 ms: 1.10x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.25 ms: 1.10x slower                                              |
| richards_super                   | 34.6 ms                                                | 38.4 ms: 1.11x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                               |
| richards                         | 30.6 ms                                                | 34.3 ms: 1.12x slower                                              |
| telco                            | 3.92 ms                                                | 4.43 ms: 1.13x slower                                              |
| django_template                  | 19.7 ms                                                | 23.2 ms: 1.18x slower                                              |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                               |
| coverage                         | 38.5 ms                                                | 47.6 ms: 1.24x slower                                              |
| many_optionals                   | 403 us                                                 | 593 us: 1.47x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (2): html5lib, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250729-3.15.0a0-6d7efa0-JIT/bm-20250729-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-6d7efa0.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x