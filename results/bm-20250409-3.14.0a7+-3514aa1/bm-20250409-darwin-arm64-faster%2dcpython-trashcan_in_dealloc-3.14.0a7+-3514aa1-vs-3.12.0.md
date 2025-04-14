# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| docutils       | 1.45 sec                                               | 1.43 sec: 1.02x faster                                                          |
| html5lib       | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                           |
| sphinx         | 613 ms                                                 | 578 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.87x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 358 ms: 1.86x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.80x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.63x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.27x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                           |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 63.0 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.24x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.2 ms: 1.15x faster                                                           |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| nbody          | 67.6 ms                                                | 73.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                           |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| xml_etree_generate   | 55.4 ms                                                | 54.4 ms: 1.02x faster                                                           |
| xml_etree_process    | 38.9 ms                                                | 38.5 ms: 1.01x faster                                                           |
| pickle_pure_python   | 197 us                                                 | 205 us: 1.04x slower                                                            |
| unpickle_pure_python | 145 us                                                 | 151 us: 1.04x slower                                                            |
| json_loads           | 17.0 us                                                | 18.4 us: 1.08x slower                                                           |
| json_dumps           | 6.19 ms                                                | 7.57 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.6 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.9 ms: 1.05x faster                                                           |
| genshi_xml      | 30.5 ms                                                | 29.1 ms: 1.05x faster                                                           |
| mako            | 7.44 ms                                                | 7.52 ms: 1.01x slower                                                           |
| django_template | 19.7 ms                                                | 21.2 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.3 ms: 2.62x faster                                                           |
| mdp                              | 1.49 sec                                               | 759 ms: 1.97x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.87x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 358 ms: 1.86x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.80x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.63x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                            |
| deepcopy                         | 226 us                                                 | 153 us: 1.48x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 18.4 us: 1.41x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.27x faster                                                            |
| generators                       | 29.4 ms                                                | 23.5 ms: 1.25x faster                                                           |
| go                               | 98.5 ms                                                | 79.8 ms: 1.23x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.64 us: 1.23x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| comprehensions                   | 14.0 us                                                | 11.7 us: 1.20x faster                                                           |
| dulwich_log                      | 29.2 ms                                                | 24.5 ms: 1.19x faster                                                           |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                           |
| raytrace                         | 204 ms                                                 | 175 ms: 1.17x faster                                                            |
| float                            | 54.1 ms                                                | 47.2 ms: 1.15x faster                                                           |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                            |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                          |
| regex_compile                    | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                           |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                            |
| html5lib                         | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                          |
| logging_simple                   | 3.60 us                                                | 3.25 us: 1.11x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 69.4 ms: 1.10x faster                                                           |
| logging_format                   | 3.90 us                                                | 3.56 us: 1.09x faster                                                           |
| chaos                            | 41.6 ms                                                | 38.1 ms: 1.09x faster                                                           |
| bench_mp_pool                    | 65.5 ms                                                | 60.0 ms: 1.09x faster                                                           |
| deltablue                        | 2.57 ms                                                | 2.36 ms: 1.09x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.03 sec: 1.08x faster                                                          |
| logging_silent                   | 72.5 ns                                                | 67.4 ns: 1.08x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| scimark_sor                      | 85.8 ms                                                | 80.0 ms: 1.07x faster                                                           |
| pyflate                          | 311 ms                                                 | 292 ms: 1.06x faster                                                            |
| sphinx                           | 613 ms                                                 | 578 ms: 1.06x faster                                                            |
| genshi_text                      | 14.7 ms                                                | 13.9 ms: 1.05x faster                                                           |
| scimark_fft                      | 194 ms                                                 | 185 ms: 1.05x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                           |
| genshi_xml                       | 30.5 ms                                                | 29.1 ms: 1.05x faster                                                           |
| 2to3                             | 168 ms                                                 | 161 ms: 1.04x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 63.0 ms: 1.04x faster                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 42.6 ms: 1.04x faster                                                           |
| pprint_pformat                   | 986 ms                                                 | 946 ms: 1.04x faster                                                            |
| pprint_safe_repr                 | 483 ms                                                 | 464 ms: 1.04x faster                                                            |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.5 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                                           |
| pycparser                        | 673 ms                                                 | 653 ms: 1.03x faster                                                            |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                           |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                            |
| xml_etree_generate               | 55.4 ms                                                | 54.4 ms: 1.02x faster                                                           |
| sympy_sum                        | 76.2 ms                                                | 74.9 ms: 1.02x faster                                                           |
| docutils                         | 1.45 sec                                               | 1.43 sec: 1.02x faster                                                          |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| xml_etree_process                | 38.9 ms                                                | 38.5 ms: 1.01x faster                                                           |
| hexiom                           | 4.38 ms                                                | 4.34 ms: 1.01x faster                                                           |
| nqueens                          | 59.5 ms                                                | 59.0 ms: 1.01x faster                                                           |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.57 ms: 1.00x faster                                                           |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                           |
| mako                             | 7.44 ms                                                | 7.52 ms: 1.01x slower                                                           |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                                            |
| sympy_expand                     | 233 ms                                                 | 237 ms: 1.02x slower                                                            |
| bench_thread_pool                | 483 us                                                 | 495 us: 1.02x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 94.3 us: 1.03x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 75.9 ms: 1.03x slower                                                           |
| json                             | 3.00 ms                                                | 3.11 ms: 1.04x slower                                                           |
| python_startup_no_site           | 13.2 ms                                                | 13.6 ms: 1.04x slower                                                           |
| fannkuch                         | 250 ms                                                 | 260 ms: 1.04x slower                                                            |
| pickle_pure_python               | 197 us                                                 | 205 us: 1.04x slower                                                            |
| unpickle_pure_python             | 145 us                                                 | 151 us: 1.04x slower                                                            |
| richards_super                   | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 72.4 ms: 1.05x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 55.2 ms: 1.07x slower                                                           |
| richards                         | 30.6 ms                                                | 32.8 ms: 1.07x slower                                                           |
| django_template                  | 19.7 ms                                                | 21.2 ms: 1.08x slower                                                           |
| nbody                            | 67.6 ms                                                | 73.0 ms: 1.08x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.4 us: 1.08x slower                                                           |
| many_optionals                   | 403 us                                                 | 446 us: 1.11x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                            |
| telco                            | 3.92 ms                                                | 4.60 ms: 1.17x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                            |
| json_dumps                       | 6.19 ms                                                | 7.57 ms: 1.22x slower                                                           |
| coverage                         | 38.5 ms                                                | 47.4 ms: 1.23x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (3): shortest_path, asyncio_websockets, python_startup
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x