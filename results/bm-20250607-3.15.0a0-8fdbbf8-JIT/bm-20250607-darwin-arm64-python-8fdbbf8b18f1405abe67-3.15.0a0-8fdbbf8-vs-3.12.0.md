# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.100x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 192 ms: 1.14x slower                                                  |
| docutils       | 1.45 sec                                               | 1.63 sec: 1.12x slower                                                |
| sphinx         | 613 ms                                                 | 658 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 389 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 402 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 398 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 206 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 448 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 452 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.3 ms: 1.08x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 394 ms: 1.05x slower                                                  |
| async_generators                 | 299 ms                                                 | 326 ms: 1.09x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 72.6 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 77.6 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| regex_compile  | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                 |
| regex_dna      | 143 ms                                                 | 147 ms: 1.03x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.7 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 76.9 ms: 1.02x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 150 us: 1.03x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 64.0 ms: 1.16x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.05 ms: 1.30x slower                                                 |
| json_loads           | 17.0 us                                                | 22.9 us: 1.34x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.8 ms: 1.07x slower                                                 |
| mako            | 7.44 ms                                                | 8.15 ms: 1.09x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.5 ms: 1.10x slower                                                 |
| django_template | 19.7 ms                                                | 25.6 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 16.1 ms: 2.00x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 389 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                  |
| mdp                              | 1.49 sec                                               | 891 ms: 1.68x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 402 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 398 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 206 ms: 1.51x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.3 us: 1.35x faster                                                 |
| generators                       | 29.4 ms                                                | 23.1 ms: 1.27x faster                                                 |
| go                               | 98.5 ms                                                | 79.5 ms: 1.24x faster                                                 |
| deepcopy                         | 226 us                                                 | 186 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 448 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 452 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                |
| coroutines                       | 19.7 ms                                                | 18.3 ms: 1.08x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                                 |
| float                            | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.4 us: 1.04x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.98 us: 1.02x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.3 ms: 1.02x faster                                                 |
| pyflate                          | 311 ms                                                 | 310 ms: 1.00x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.9 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 150 us: 1.03x slower                                                  |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                  |
| regex_dna                        | 143 ms                                                 | 147 ms: 1.03x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.1 ms: 1.04x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 89.0 ms: 1.04x slower                                                 |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.69 ms: 1.05x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 80.3 ms: 1.05x slower                                                 |
| connected_components             | 300 ms                                                 | 316 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 394 ms: 1.05x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| hexiom                           | 4.38 ms                                                | 4.68 ms: 1.07x slower                                                 |
| sphinx                           | 613 ms                                                 | 658 ms: 1.07x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.8 ms: 1.07x slower                                                 |
| chaos                            | 41.6 ms                                                | 45.0 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                 |
| async_generators                 | 299 ms                                                 | 326 ms: 1.09x slower                                                  |
| mako                             | 7.44 ms                                                | 8.15 ms: 1.09x slower                                                 |
| dask                             | 779 ms                                                 | 854 ms: 1.10x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.5 ms: 1.10x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 72.6 ms: 1.10x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.63 sec: 1.12x slower                                                |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 543 us: 1.12x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.39 us: 1.12x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.06 us: 1.13x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 86.0 ms: 1.13x slower                                                 |
| 2to3                             | 168 ms                                                 | 192 ms: 1.14x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.76 sec: 1.14x slower                                                |
| nqueens                          | 59.5 ms                                                | 68.3 ms: 1.15x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 75.2 ms: 1.15x slower                                                 |
| nbody                            | 67.6 ms                                                | 77.6 ms: 1.15x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 64.0 ms: 1.16x slower                                                 |
| sympy_str                        | 144 ms                                                 | 168 ms: 1.17x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.7 ms: 1.17x slower                                                 |
| pycparser                        | 673 ms                                                 | 797 ms: 1.18x slower                                                  |
| richards_super                   | 34.6 ms                                                | 41.0 ms: 1.18x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.0 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.3 ms: 1.19x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 87.5 ms: 1.19x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 82.8 ms: 1.20x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.39 ms: 1.21x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.92 us: 1.24x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 291 ms: 1.25x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 248 ms: 1.27x slower                                                  |
| json                             | 3.00 ms                                                | 3.85 ms: 1.28x slower                                                 |
| django_template                  | 19.7 ms                                                | 25.6 ms: 1.30x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.05 ms: 1.30x slower                                                 |
| many_optionals                   | 403 us                                                 | 533 us: 1.32x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.20 ms: 1.33x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 123 us: 1.34x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.9 us: 1.34x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 690 ms: 1.43x slower                                                  |
| fannkuch                         | 250 ms                                                 | 357 ms: 1.43x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.42 sec: 1.44x slower                                                |
| telco                            | 3.92 ms                                                | 5.63 ms: 1.44x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 414 ns: 5.71x slower                                                  |
| coverage                         | 38.5 ms                                                | 306 ms: 7.96x slower                                                  |
| thrift                           | 468 us                                                 | 44.1 ms: 94.37x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (3): pylint, html5lib, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.100x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x