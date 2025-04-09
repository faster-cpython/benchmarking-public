# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 161 ms: 1.05x faster                                                            |
| docutils       | 1.45 sec                                               | 1.42 sec: 1.02x faster                                                          |
| html5lib       | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                           |
| sphinx         | 613 ms                                                 | 578 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                            |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                           |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 63.0 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                            |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.83x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                           |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| nbody          | 67.6 ms                                                | 71.6 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.9 ms: 1.12x faster                                                           |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                           |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| xml_etree_generate   | 55.4 ms                                                | 54.8 ms: 1.01x faster                                                           |
| xml_etree_process    | 38.9 ms                                                | 38.5 ms: 1.01x faster                                                           |
| unpickle_pure_python | 145 us                                                 | 149 us: 1.03x slower                                                            |
| pickle_pure_python   | 197 us                                                 | 206 us: 1.05x slower                                                            |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| json_dumps           | 6.19 ms                                                | 7.65 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.4 ms: 1.08x faster                                                           |
| python_startup_no_site | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 28.8 ms: 1.06x faster                                                           |
| genshi_text     | 14.7 ms                                                | 13.9 ms: 1.06x faster                                                           |
| mako            | 7.44 ms                                                | 7.49 ms: 1.01x slower                                                           |
| django_template | 19.7 ms                                                | 21.1 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.3 ms: 2.61x faster                                                           |
| mdp                              | 1.49 sec                                               | 765 ms: 1.95x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                            |
| deepcopy                         | 226 us                                                 | 155 us: 1.46x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 18.4 us: 1.41x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                            |
| generators                       | 29.4 ms                                                | 23.5 ms: 1.25x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.63 us: 1.24x faster                                                           |
| go                               | 98.5 ms                                                | 80.1 ms: 1.23x faster                                                           |
| comprehensions                   | 14.0 us                                                | 11.5 us: 1.21x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                            |
| dulwich_log                      | 29.2 ms                                                | 24.5 ms: 1.19x faster                                                           |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                           |
| raytrace                         | 204 ms                                                 | 174 ms: 1.17x faster                                                            |
| float                            | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.12x faster                                                          |
| html5lib                         | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                           |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                            |
| regex_compile                    | 75.9 ms                                                | 67.9 ms: 1.12x faster                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 69.0 ms: 1.11x faster                                                           |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                            |
| logging_simple                   | 3.60 us                                                | 3.26 us: 1.10x faster                                                           |
| bench_mp_pool                    | 65.5 ms                                                | 59.4 ms: 1.10x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                           |
| chaos                            | 41.6 ms                                                | 38.2 ms: 1.09x faster                                                           |
| logging_format                   | 3.90 us                                                | 3.58 us: 1.09x faster                                                           |
| deltablue                        | 2.57 ms                                                | 2.36 ms: 1.09x faster                                                           |
| python_startup                   | 17.8 ms                                                | 16.4 ms: 1.08x faster                                                           |
| logging_silent                   | 72.5 ns                                                | 67.2 ns: 1.08x faster                                                           |
| scimark_sor                      | 85.8 ms                                                | 79.6 ms: 1.08x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.05 sec: 1.08x faster                                                          |
| python_startup_no_site           | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                           |
| pyflate                          | 311 ms                                                 | 290 ms: 1.07x faster                                                            |
| sphinx                           | 613 ms                                                 | 578 ms: 1.06x faster                                                            |
| genshi_xml                       | 30.5 ms                                                | 28.8 ms: 1.06x faster                                                           |
| scimark_fft                      | 194 ms                                                 | 184 ms: 1.06x faster                                                            |
| genshi_text                      | 14.7 ms                                                | 13.9 ms: 1.06x faster                                                           |
| xml_etree_iterparse              | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                           |
| 2to3                             | 168 ms                                                 | 161 ms: 1.05x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 63.0 ms: 1.04x faster                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 42.6 ms: 1.04x faster                                                           |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.4 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| pycparser                        | 673 ms                                                 | 655 ms: 1.03x faster                                                            |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                           |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                           |
| docutils                         | 1.45 sec                                               | 1.42 sec: 1.02x faster                                                          |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                            |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| xml_etree_generate               | 55.4 ms                                                | 54.8 ms: 1.01x faster                                                           |
| hexiom                           | 4.38 ms                                                | 4.33 ms: 1.01x faster                                                           |
| xml_etree_process                | 38.9 ms                                                | 38.5 ms: 1.01x faster                                                           |
| sympy_sum                        | 76.2 ms                                                | 75.6 ms: 1.01x faster                                                           |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                            |
| pprint_safe_repr                 | 483 ms                                                 | 482 ms: 1.00x faster                                                            |
| nqueens                          | 59.5 ms                                                | 59.4 ms: 1.00x faster                                                           |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.14 ms: 1.00x faster                                                           |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                            |
| mako                             | 7.44 ms                                                | 7.49 ms: 1.01x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                           |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                                            |
| sympy_expand                     | 233 ms                                                 | 238 ms: 1.02x slower                                                            |
| scimark_lu                       | 73.5 ms                                                | 74.9 ms: 1.02x slower                                                           |
| bench_thread_pool                | 483 us                                                 | 494 us: 1.02x slower                                                            |
| json                             | 3.00 ms                                                | 3.08 ms: 1.03x slower                                                           |
| unpickle_pure_python             | 145 us                                                 | 149 us: 1.03x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 94.2 us: 1.03x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                           |
| richards_super                   | 34.6 ms                                                | 36.2 ms: 1.04x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 72.2 ms: 1.05x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 206 us: 1.05x slower                                                            |
| fannkuch                         | 250 ms                                                 | 263 ms: 1.05x slower                                                            |
| nbody                            | 67.6 ms                                                | 71.6 ms: 1.06x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| richards                         | 30.6 ms                                                | 32.7 ms: 1.07x slower                                                           |
| django_template                  | 19.7 ms                                                | 21.1 ms: 1.07x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 55.4 ms: 1.08x slower                                                           |
| many_optionals                   | 403 us                                                 | 447 us: 1.11x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                            |
| telco                            | 3.92 ms                                                | 4.62 ms: 1.18x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                            |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.21x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 7.65 ms: 1.24x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.83x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (3): sqlalchemy_imperative, shortest_path, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.088x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x