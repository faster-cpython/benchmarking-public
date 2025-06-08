# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.069x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 233 ms: 1.38x slower                                                  |
| docutils       | 1.45 sec                                               | 1.59 sec: 1.10x slower                                                |
| html5lib       | 33.4 ms                                                | 34.6 ms: 1.04x slower                                                 |
| sphinx         | 613 ms                                                 | 678 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 327 ms: 2.06x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 333 ms: 2.00x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 344 ms: 1.95x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 323 ms: 1.91x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 179 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_generators                 | 299 ms                                                 | 320 ms: 1.07x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 81.8 ms: 1.24x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.1 ms: 1.10x faster                                                 |
| pidigits       | 283 ms                                                 | 281 ms: 1.00x faster                                                  |
| nbody          | 67.6 ms                                                | 95.0 ms: 1.41x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.01x slower                                                  |
| regex_compile  | 75.9 ms                                                | 83.6 ms: 1.10x slower                                                 |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 167 us: 1.15x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.57 sec: 1.15x slower                                                |
| pickle_pure_python   | 197 us                                                 | 237 us: 1.20x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 49.8 ms: 1.28x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 72.1 ms: 1.30x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.41 ms: 1.36x slower                                                 |
| json_loads           | 17.0 us                                                | 24.6 us: 1.44x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 21.0 ms: 1.18x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 16.0 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 18.3 ms: 1.25x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 39.4 ms: 1.29x slower                                                 |
| django_template | 19.7 ms                                                | 28.2 ms: 1.43x slower                                                 |
| mako            | 7.44 ms                                                | 11.0 ms: 1.47x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.36x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.95 ms                                                | 1.42 ms: 2.08x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 327 ms: 2.06x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 333 ms: 2.00x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 344 ms: 1.95x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 323 ms: 1.91x faster                                                  |
| subparsers                       | 32.1 ms                                                | 16.9 ms: 1.90x faster                                                 |
| async_tree_memoization_tg        | 318 ms                                                 | 179 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| mdp                              | 1.49 sec                                               | 989 ms: 1.51x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 861 us: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                  |
| generators                       | 29.4 ms                                                | 23.9 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 22.2 us: 1.17x faster                                                 |
| go                               | 98.5 ms                                                | 84.3 ms: 1.17x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                 |
| float                            | 54.1 ms                                                | 49.1 ms: 1.10x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                 |
| deepcopy                         | 226 us                                                 | 214 us: 1.06x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.64 sec: 1.05x faster                                                |
| dulwich_log                      | 29.2 ms                                                | 28.7 ms: 1.02x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.01x slower                                                  |
| pyflate                          | 311 ms                                                 | 317 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.6 ms: 1.04x slower                                                 |
| shortest_path                    | 331 ms                                                 | 346 ms: 1.05x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.70 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_generators                 | 299 ms                                                 | 320 ms: 1.07x slower                                                  |
| connected_components             | 300 ms                                                 | 322 ms: 1.08x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.67 us: 1.08x slower                                                 |
| comprehensions                   | 14.0 us                                                | 15.3 us: 1.09x slower                                                 |
| pycparser                        | 673 ms                                                 | 736 ms: 1.09x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.59 sec: 1.10x slower                                                |
| regex_compile                    | 75.9 ms                                                | 83.6 ms: 1.10x slower                                                 |
| sphinx                           | 613 ms                                                 | 678 ms: 1.11x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.64 sec: 1.11x slower                                                |
| scimark_sor                      | 85.8 ms                                                | 96.6 ms: 1.13x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 2.29 us: 1.14x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.97 ms: 1.14x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 167 us: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| raytrace                         | 204 ms                                                 | 235 ms: 1.15x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.57 sec: 1.15x slower                                                |
| sympy_integrate                  | 11.1 ms                                                | 12.9 ms: 1.17x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 90.2 ms: 1.18x slower                                                 |
| python_startup                   | 17.8 ms                                                | 21.0 ms: 1.18x slower                                                 |
| chaos                            | 41.6 ms                                                | 49.2 ms: 1.18x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 78.6 ms: 1.20x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 237 us: 1.20x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 83.2 ms: 1.20x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.36 us: 1.21x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 16.0 ms: 1.21x slower                                                 |
| nqueens                          | 59.5 ms                                                | 72.5 ms: 1.22x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.79 us: 1.23x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 93.9 ms: 1.23x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 55.2 ms: 1.24x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 81.8 ms: 1.24x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.3 ms: 1.25x slower                                                 |
| sympy_str                        | 144 ms                                                 | 183 ms: 1.27x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 49.8 ms: 1.28x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 39.4 ms: 1.29x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 72.1 ms: 1.30x slower                                                 |
| richards                         | 30.6 ms                                                | 40.7 ms: 1.33x slower                                                 |
| richards_super                   | 34.6 ms                                                | 46.7 ms: 1.35x slower                                                 |
| thrift                           | 468 us                                                 | 635 us: 1.36x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 8.41 ms: 1.36x slower                                                 |
| json                             | 3.00 ms                                                | 4.08 ms: 1.36x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 100 ms: 1.37x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 70.7 ms: 1.37x slower                                                 |
| many_optionals                   | 403 us                                                 | 557 us: 1.38x slower                                                  |
| 2to3                             | 168 ms                                                 | 233 ms: 1.38x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 324 ms: 1.39x slower                                                  |
| nbody                            | 67.6 ms                                                | 95.0 ms: 1.41x slower                                                 |
| fannkuch                         | 250 ms                                                 | 354 ms: 1.41x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.40 sec: 1.42x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 687 ms: 1.42x slower                                                  |
| django_template                  | 19.7 ms                                                | 28.2 ms: 1.43x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.53 ms: 1.44x slower                                                 |
| json_loads                       | 17.0 us                                                | 24.6 us: 1.44x slower                                                 |
| mako                             | 7.44 ms                                                | 11.0 ms: 1.47x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 287 ms: 1.48x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 140 us: 1.52x slower                                                  |
| telco                            | 3.92 ms                                                | 6.11 ms: 1.56x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 777 us: 1.61x slower                                                  |
| coverage                         | 38.5 ms                                                | 75.7 ms: 1.97x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 444 ns: 6.12x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (2): pathlib, pylint
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.069x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.26x