# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.089x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 221 ms: 1.31x slower                                                  |
| docutils       | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                |
| sphinx         | 613 ms                                                 | 651 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 389 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 402 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 174 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 449 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 454 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.1 ms: 1.09x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.05x slower                                                  |
| async_generators                 | 299 ms                                                 | 316 ms: 1.06x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 70.4 ms: 1.07x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 427 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.2 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 77.6 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| regex_compile  | 75.9 ms                                                | 74.3 ms: 1.02x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.3 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 76.7 ms: 1.02x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 156 us: 1.08x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 222 us: 1.13x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 65.1 ms: 1.18x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.07 ms: 1.30x slower                                                 |
| json_loads           | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.2 ms: 1.03x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.6 ms: 1.07x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| mako            | 7.44 ms                                                | 8.23 ms: 1.11x slower                                                 |
| django_template | 19.7 ms                                                | 25.3 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 16.0 ms: 2.01x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 389 ms: 1.73x faster                                                  |
| mdp                              | 1.49 sec                                               | 880 ms: 1.70x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 402 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 174 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.3 us: 1.35x faster                                                 |
| generators                       | 29.4 ms                                                | 23.0 ms: 1.28x faster                                                 |
| go                               | 98.5 ms                                                | 77.4 ms: 1.27x faster                                                 |
| deepcopy                         | 226 us                                                 | 185 us: 1.22x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.9 us: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 449 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 454 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.1 ms: 1.09x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.1 ms: 1.08x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.62 sec: 1.06x faster                                                |
| float                            | 54.1 ms                                                | 51.2 ms: 1.06x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 74.3 ms: 1.02x faster                                                 |
| pyflate                          | 311 ms                                                 | 306 ms: 1.02x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 2.00 us: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.01x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.60 ms: 1.01x slower                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 76.7 ms: 1.02x slower                                                 |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| pathlib                          | 24.7 ms                                                | 25.3 ms: 1.03x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.2 ms: 1.03x slower                                                 |
| raytrace                         | 204 ms                                                 | 210 ms: 1.03x slower                                                  |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                |
| spectral_norm                    | 76.5 ms                                                | 79.2 ms: 1.04x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                 |
| connected_components             | 300 ms                                                 | 312 ms: 1.04x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.05x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 89.9 ms: 1.05x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.60 ms: 1.05x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.7 ms: 1.05x slower                                                 |
| chaos                            | 41.6 ms                                                | 43.8 ms: 1.05x slower                                                 |
| async_generators                 | 299 ms                                                 | 316 ms: 1.06x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                 |
| sphinx                           | 613 ms                                                 | 651 ms: 1.06x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.6 ms: 1.07x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 70.4 ms: 1.07x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 156 us: 1.08x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                |
| gc_traversal                     | 2.95 ms                                                | 3.23 ms: 1.10x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 75.9 ms: 1.10x slower                                                 |
| dask                             | 779 ms                                                 | 857 ms: 1.10x slower                                                  |
| logging_simple                   | 3.60 us                                                | 3.97 us: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 744 ms: 1.10x slower                                                  |
| mako                             | 7.44 ms                                                | 8.23 ms: 1.11x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 535 us: 1.11x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.33 us: 1.11x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.67 sec: 1.12x slower                                                |
| pickle_pure_python               | 197 us                                                 | 222 us: 1.13x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| sympy_str                        | 144 ms                                                 | 163 ms: 1.14x slower                                                  |
| nqueens                          | 59.5 ms                                                | 67.8 ms: 1.14x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 74.8 ms: 1.14x slower                                                 |
| nbody                            | 67.6 ms                                                | 77.6 ms: 1.15x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.3 ms: 1.15x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 85.9 ms: 1.17x slower                                                 |
| richards_super                   | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 60.3 ms: 1.17x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 65.1 ms: 1.18x slower                                                 |
| richards                         | 30.6 ms                                                | 36.0 ms: 1.18x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.21x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 587 ms: 1.22x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.40 ms: 1.22x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 285 ms: 1.22x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.23x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 427 ms: 1.23x slower                                                  |
| fannkuch                         | 250 ms                                                 | 314 ms: 1.26x slower                                                  |
| json                             | 3.00 ms                                                | 3.83 ms: 1.28x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.03 ms: 1.28x slower                                                 |
| django_template                  | 19.7 ms                                                | 25.3 ms: 1.29x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 119 us: 1.30x slower                                                  |
| many_optionals                   | 403 us                                                 | 523 us: 1.30x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 8.07 ms: 1.30x slower                                                 |
| 2to3                             | 168 ms                                                 | 221 ms: 1.31x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 263 ms: 1.35x slower                                                  |
| telco                            | 3.92 ms                                                | 5.55 ms: 1.42x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 420 ns: 5.78x slower                                                  |
| coverage                         | 38.5 ms                                                | 302 ms: 7.84x slower                                                  |
| thrift                           | 468 us                                                 | 44.2 ms: 94.60x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (3): pylint, html5lib, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.10x