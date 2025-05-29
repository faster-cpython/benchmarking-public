# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: darwin-arm64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| docutils       | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                |
| html5lib       | 33.4 ms                                                | 30.8 ms: 1.08x faster                                                 |
| sphinx         | 613 ms                                                 | 551 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 335 ms: 1.99x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.96x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 342 ms: 1.96x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.76x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 178 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 401 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.28x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 57.2 ms: 1.15x faster                                                 |
| async_generators                 | 299 ms                                                 | 263 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 383 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.12x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.55x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.31x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.0 ms: 1.23x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 73.0 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.4 ms: 1.24x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                                  |
| regex_v8       | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                |
| xml_etree_generate   | 55.4 ms                                                | 49.2 ms: 1.13x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.9 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 70.5 ms: 1.07x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 188 us: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_dumps           | 6.19 ms                                                | 6.08 ms: 1.02x faster                                                 |
| json_loads           | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.8 ms: 1.15x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 27.1 ms: 1.13x faster                                                 |
| mako            | 7.44 ms                                                | 7.20 ms: 1.03x faster                                                 |
| django_template | 19.7 ms                                                | 19.5 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.0 ms: 2.47x faster                                                 |
| mdp                              | 1.49 sec                                               | 700 ms: 2.13x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 335 ms: 1.99x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.96x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 342 ms: 1.96x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.76x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 178 ms: 1.74x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.5 us: 1.57x faster                                                 |
| deepcopy                         | 226 us                                                 | 145 us: 1.56x faster                                                  |
| generators                       | 29.4 ms                                                | 18.9 ms: 1.55x faster                                                 |
| go                               | 98.5 ms                                                | 71.5 ms: 1.38x faster                                                 |
| comprehensions                   | 14.0 us                                                | 10.4 us: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 401 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.28x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.28x faster                                                 |
| raytrace                         | 204 ms                                                 | 160 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.07 ms: 1.24x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 61.4 ms: 1.24x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 23.7 ms: 1.23x faster                                                 |
| float                            | 54.1 ms                                                | 44.0 ms: 1.23x faster                                                 |
| pylint                           | 182 ms                                                 | 151 ms: 1.21x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.75 ms: 1.17x faster                                                 |
| chaos                            | 41.6 ms                                                | 35.9 ms: 1.16x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 57.2 ms: 1.15x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                |
| genshi_text                      | 14.7 ms                                                | 12.8 ms: 1.15x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.14x faster                                                |
| async_generators                 | 299 ms                                                 | 263 ms: 1.13x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 75.9 ms: 1.13x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 49.2 ms: 1.13x faster                                                 |
| pyflate                          | 311 ms                                                 | 276 ms: 1.13x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 27.1 ms: 1.13x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.92 sec: 1.13x faster                                                |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.4 ms: 1.12x faster                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 39.9 ms: 1.12x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.9 ms: 1.11x faster                                                 |
| sphinx                           | 613 ms                                                 | 551 ms: 1.11x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.26 us: 1.11x faster                                                 |
| sympy_str                        | 144 ms                                                 | 130 ms: 1.11x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.1 ms: 1.10x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.58 us: 1.09x faster                                                 |
| pycparser                        | 673 ms                                                 | 621 ms: 1.08x faster                                                  |
| html5lib                         | 33.4 ms                                                | 30.8 ms: 1.08x faster                                                 |
| nqueens                          | 59.5 ms                                                | 55.2 ms: 1.08x faster                                                 |
| 2to3                             | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.5 ms: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                |
| sympy_expand                     | 233 ms                                                 | 221 ms: 1.06x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 69.7 ms: 1.05x faster                                                 |
| richards_super                   | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                 |
| pickle_pure_python               | 197 us                                                 | 188 us: 1.05x faster                                                  |
| richards                         | 30.6 ms                                                | 29.2 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| mako                             | 7.44 ms                                                | 7.20 ms: 1.03x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.8 ms: 1.03x faster                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 88.9 us: 1.03x faster                                                 |
| bench_thread_pool                | 483 us                                                 | 472 us: 1.02x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.2 ms: 1.02x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 969 ms: 1.02x faster                                                  |
| json_dumps                       | 6.19 ms                                                | 6.08 ms: 1.02x faster                                                 |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.5 ms: 1.01x faster                                                 |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 479 ms: 1.01x faster                                                  |
| connected_components             | 300 ms                                                 | 301 ms: 1.00x slower                                                  |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| json                             | 3.00 ms                                                | 3.06 ms: 1.02x slower                                                 |
| dask                             | 779 ms                                                 | 798 ms: 1.02x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.8 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.24 ms: 1.03x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 201 ms: 1.03x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 69.6 ms: 1.06x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| nbody                            | 67.6 ms                                                | 73.0 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| many_optionals                   | 403 us                                                 | 439 us: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 383 ms: 1.10x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.12x slower                                                  |
| telco                            | 3.92 ms                                                | 4.45 ms: 1.14x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.34 ms: 1.16x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.55x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 292 ns: 4.03x slower                                                  |
| coverage                         | 38.5 ms                                                | 235 ms: 6.11x slower                                                  |
| thrift                           | 468 us                                                 | 43.1 ms: 92.17x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, fannkuch, sqlite_synth
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x