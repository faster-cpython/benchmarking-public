# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.105x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 193 ms: 1.15x slower                                                  |
| docutils       | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| html5lib       | 33.4 ms                                                | 35.1 ms: 1.05x slower                                                 |
| sphinx         | 613 ms                                                 | 638 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 407 ms: 1.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 416 ms: 1.62x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 175 ms: 1.46x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 439 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 77.2 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.32x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.06x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 58.3 ms: 1.08x slower                                                 |
| nbody          | 67.6 ms                                                | 93.3 ms: 1.38x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.15 ms: 1.14x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                 |
| regex_compile  | 75.9 ms                                                | 87.0 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 76.5 ms: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 61.1 ms: 1.10x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 251 us: 1.28x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 190 us: 1.30x slower                                                  |
| json_dumps           | 6.19 ms                                                | 8.19 ms: 1.32x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 12.5 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                 |
| mako            | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                 |
| genshi_text     | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                 |
| django_template | 19.7 ms                                                | 26.4 ms: 1.34x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.27x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.8 ms: 2.17x faster                                                 |
| mdp                              | 1.49 sec                                               | 870 ms: 1.72x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 407 ms: 1.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 416 ms: 1.62x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 175 ms: 1.46x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                  |
| deepcopy                         | 226 us                                                 | 188 us: 1.20x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 439 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.15 ms: 1.14x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| deepcopy_memo                    | 26.0 us                                                | 23.8 us: 1.09x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.4 ms: 1.07x faster                                                 |
| python_startup                   | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                 |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.5 ms: 1.05x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.98 us: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.5 ms: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                                |
| raytrace                         | 204 ms                                                 | 207 ms: 1.02x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 78.7 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.24 ms: 1.03x slower                                                 |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| json                             | 3.00 ms                                                | 3.12 ms: 1.04x slower                                                 |
| sphinx                           | 613 ms                                                 | 638 ms: 1.04x slower                                                  |
| connected_components             | 300 ms                                                 | 313 ms: 1.04x slower                                                  |
| comprehensions                   | 14.0 us                                                | 14.6 us: 1.05x slower                                                 |
| html5lib                         | 33.4 ms                                                | 35.1 ms: 1.05x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 69.9 ms: 1.07x slower                                                 |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 208 ms: 1.07x slower                                                  |
| generators                       | 29.4 ms                                                | 31.4 ms: 1.07x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| float                            | 54.1 ms                                                | 58.3 ms: 1.08x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| sympy_sum                        | 76.2 ms                                                | 83.0 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.21 ms: 1.09x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 94.5 ms: 1.10x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 61.1 ms: 1.10x slower                                                 |
| dask                             | 779 ms                                                 | 864 ms: 1.11x slower                                                  |
| sympy_str                        | 144 ms                                                 | 160 ms: 1.12x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 77.3 ms: 1.12x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| bench_thread_pool                | 483 us                                                 | 543 us: 1.13x slower                                                  |
| pyflate                          | 311 ms                                                 | 350 ms: 1.13x slower                                                  |
| chaos                            | 41.6 ms                                                | 47.0 ms: 1.13x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.90 ms: 1.13x slower                                                 |
| pycparser                        | 673 ms                                                 | 766 ms: 1.14x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 87.0 ms: 1.15x slower                                                 |
| 2to3                             | 168 ms                                                 | 193 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.53 us: 1.16x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.21 us: 1.17x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 86.0 ms: 1.17x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 77.2 ms: 1.17x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.4 ms: 1.19x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.18 sec: 1.20x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 580 ms: 1.20x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 53.8 ms: 1.21x slower                                                 |
| fannkuch                         | 250 ms                                                 | 303 ms: 1.21x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                 |
| telco                            | 3.92 ms                                                | 4.83 ms: 1.23x slower                                                 |
| mako                             | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 113 us: 1.24x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.48 ms: 1.25x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                 |
| nqueens                          | 59.5 ms                                                | 75.3 ms: 1.27x slower                                                 |
| many_optionals                   | 403 us                                                 | 510 us: 1.27x slower                                                  |
| richards_super                   | 34.6 ms                                                | 44.0 ms: 1.27x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 251 us: 1.28x slower                                                  |
| richards                         | 30.6 ms                                                | 39.1 ms: 1.28x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 190 us: 1.30x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.32x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 8.19 ms: 1.32x slower                                                 |
| django_template                  | 19.7 ms                                                | 26.4 ms: 1.34x slower                                                 |
| nbody                            | 67.6 ms                                                | 93.3 ms: 1.38x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.06x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 345 ns: 4.76x slower                                                  |
| coverage                         | 38.5 ms                                                | 334 ms: 8.68x slower                                                  |
| thrift                           | 468 us                                                 | 43.9 ms: 93.87x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (3): pylint, coroutines, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.105x slower

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.12x