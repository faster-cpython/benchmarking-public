# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.089x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 217 ms: 1.29x slower                                                  |
| docutils       | 1.45 sec                                               | 1.59 sec: 1.10x slower                                                |
| sphinx         | 613 ms                                                 | 651 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 386 ms: 1.74x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 399 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 201 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 399 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 449 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 455 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.3 ms: 1.08x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.04x slower                                                  |
| async_generators                 | 299 ms                                                 | 314 ms: 1.05x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 71.0 ms: 1.08x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.26x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 77.4 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| regex_compile  | 75.9 ms                                                | 74.5 ms: 1.02x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.3 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 76.5 ms: 1.01x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.39 sec: 1.02x slower                                                |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 158 us: 1.08x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 64.9 ms: 1.17x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.13 ms: 1.31x slower                                                 |
| json_loads           | 17.0 us                                                | 22.9 us: 1.35x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.2 ms: 1.09x slower                                                 |
| mako            | 7.44 ms                                                | 8.27 ms: 1.11x slower                                                 |
| django_template | 19.7 ms                                                | 25.7 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 16.1 ms: 2.00x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 386 ms: 1.74x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 399 ms: 1.68x faster                                                  |
| mdp                              | 1.49 sec                                               | 889 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 201 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 399 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.4 us: 1.34x faster                                                 |
| go                               | 98.5 ms                                                | 77.5 ms: 1.27x faster                                                 |
| generators                       | 29.4 ms                                                | 23.2 ms: 1.27x faster                                                 |
| deepcopy                         | 226 us                                                 | 187 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 449 ms: 1.17x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 455 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                |
| regex_effbot                     | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.1 ms: 1.08x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.3 ms: 1.08x faster                                                 |
| float                            | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 74.5 ms: 1.02x faster                                                 |
| pyflate                          | 311 ms                                                 | 305 ms: 1.02x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.3 ms: 1.02x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.99 us: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.5 ms: 1.01x slower                                                 |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.61 ms: 1.02x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.39 sec: 1.02x slower                                                |
| raytrace                         | 204 ms                                                 | 210 ms: 1.03x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.56 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.3 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.04x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 89.8 ms: 1.05x slower                                                 |
| async_generators                 | 299 ms                                                 | 314 ms: 1.05x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                 |
| sphinx                           | 613 ms                                                 | 651 ms: 1.06x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                 |
| chaos                            | 41.6 ms                                                | 44.4 ms: 1.07x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 71.0 ms: 1.08x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 158 us: 1.08x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.21 ms: 1.09x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.2 ms: 1.09x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.94 us: 1.09x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| dask                             | 779 ms                                                 | 853 ms: 1.10x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.59 sec: 1.10x slower                                                |
| logging_format                   | 3.90 us                                                | 4.28 us: 1.10x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 76.3 ms: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 745 ms: 1.11x slower                                                  |
| mako                             | 7.44 ms                                                | 8.27 ms: 1.11x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.66 sec: 1.11x slower                                                |
| bench_thread_pool                | 483 us                                                 | 539 us: 1.12x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| nqueens                          | 59.5 ms                                                | 67.9 ms: 1.14x slower                                                 |
| nbody                            | 67.6 ms                                                | 77.4 ms: 1.15x slower                                                 |
| sympy_str                        | 144 ms                                                 | 165 ms: 1.15x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.3 ms: 1.15x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 75.4 ms: 1.15x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 64.9 ms: 1.17x slower                                                 |
| richards_super                   | 34.6 ms                                                | 40.7 ms: 1.18x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 60.7 ms: 1.18x slower                                                 |
| richards                         | 30.6 ms                                                | 36.1 ms: 1.18x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 87.6 ms: 1.19x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.20 sec: 1.21x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 589 ms: 1.22x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.23x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.42 ms: 1.23x slower                                                 |
| fannkuch                         | 250 ms                                                 | 310 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.26x slower                                                  |
| json                             | 3.00 ms                                                | 3.84 ms: 1.28x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.03 ms: 1.28x slower                                                 |
| 2to3                             | 168 ms                                                 | 217 ms: 1.29x slower                                                  |
| many_optionals                   | 403 us                                                 | 524 us: 1.30x slower                                                  |
| django_template                  | 19.7 ms                                                | 25.7 ms: 1.31x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.13 ms: 1.31x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 121 us: 1.32x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.9 us: 1.35x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 262 ms: 1.35x slower                                                  |
| telco                            | 3.92 ms                                                | 5.55 ms: 1.41x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 421 ns: 5.80x slower                                                  |
| coverage                         | 38.5 ms                                                | 306 ms: 7.95x slower                                                  |
| thrift                           | 468 us                                                 | 44.1 ms: 94.38x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (5): pylint, shortest_path, asyncio_websockets, html5lib, connected_components
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x