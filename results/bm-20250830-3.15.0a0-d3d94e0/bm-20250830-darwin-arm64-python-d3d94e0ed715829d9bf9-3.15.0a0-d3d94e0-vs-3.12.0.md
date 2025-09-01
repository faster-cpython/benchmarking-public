# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.051x faster
- HPT reliability: 93.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                                  |
| docutils       | 1.45 sec                                               | 1.43 sec: 1.01x faster                                                |
| html5lib       | 33.4 ms                                                | 32.5 ms: 1.03x faster                                                 |
| sphinx         | 613 ms                                                 | 573 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 370 ms: 1.80x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 376 ms: 1.79x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 385 ms: 1.75x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 420 ms: 1.25x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.1 ms: 1.10x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 80.0 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| regex_compile  | 75.9 ms                                                | 72.4 ms: 1.05x faster                                                 |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                | 5.67 ms: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.3 ms: 1.04x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 39.5 ms: 1.02x slower                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.41 sec: 1.04x slower                                                |
| unpickle_pure_python | 145 us                                                 | 155 us: 1.07x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 216 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.3 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.02x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 32.6 ms: 1.07x slower                                                 |
| mako            | 7.44 ms                                                | 8.04 ms: 1.08x slower                                                 |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 772 ms: 1.93x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 370 ms: 1.80x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 376 ms: 1.79x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 385 ms: 1.75x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                  |
| deepcopy                         | 226 us                                                 | 171 us: 1.32x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.4 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 420 ms: 1.25x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 21.2 us: 1.23x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                                 |
| generators                       | 29.4 ms                                                | 24.4 ms: 1.20x faster                                                 |
| comprehensions                   | 14.0 us                                                | 11.7 us: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| go                               | 98.5 ms                                                | 84.0 ms: 1.17x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.2 ms: 1.16x faster                                                 |
| raytrace                         | 204 ms                                                 | 177 ms: 1.15x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.14x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.26 us: 1.11x faster                                                 |
| float                            | 54.1 ms                                                | 49.1 ms: 1.10x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.55 us: 1.10x faster                                                 |
| json_dumps                       | 6.19 ms                                                | 5.67 ms: 1.09x faster                                                 |
| chaos                            | 41.6 ms                                                | 38.8 ms: 1.07x faster                                                 |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                  |
| sphinx                           | 613 ms                                                 | 573 ms: 1.07x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.42 ms: 1.06x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 72.4 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.14 sec: 1.05x faster                                                |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.3 ms: 1.04x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 187 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 83.1 ms: 1.03x faster                                                 |
| pyflate                          | 311 ms                                                 | 301 ms: 1.03x faster                                                  |
| html5lib                         | 33.4 ms                                                | 32.5 ms: 1.03x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                 |
| thrift                           | 468 us                                                 | 458 us: 1.02x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.43 sec: 1.01x faster                                                |
| logging_silent                   | 72.5 ns                                                | 71.9 ns: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.12 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 51.6 ms: 1.00x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 73.8 ms: 1.00x slower                                                 |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                                  |
| dask                             | 779 ms                                                 | 786 ms: 1.01x slower                                                  |
| shortest_path                    | 331 ms                                                 | 334 ms: 1.01x slower                                                  |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                 |
| sympy_str                        | 144 ms                                                 | 146 ms: 1.01x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 39.5 ms: 1.02x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.02x slower                                                 |
| pycparser                        | 673 ms                                                 | 687 ms: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| connected_components             | 300 ms                                                 | 306 ms: 1.02x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 493 us: 1.02x slower                                                  |
| nqueens                          | 59.5 ms                                                | 61.0 ms: 1.02x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.53 ms: 1.04x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.41 sec: 1.04x slower                                                |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 246 ms: 1.05x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                 |
| telco                            | 3.92 ms                                                | 4.16 ms: 1.06x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 97.1 us: 1.06x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 73.4 ms: 1.06x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 155 us: 1.07x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 32.6 ms: 1.07x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.16 ms: 1.07x slower                                                 |
| richards_super                   | 34.6 ms                                                | 37.2 ms: 1.07x slower                                                 |
| mako                             | 7.44 ms                                                | 8.04 ms: 1.08x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.3 ms: 1.08x slower                                                 |
| richards                         | 30.6 ms                                                | 33.2 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 71.4 ms: 1.09x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 216 us: 1.10x slower                                                  |
| fannkuch                         | 250 ms                                                 | 276 ms: 1.10x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.12x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 546 ms: 1.13x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.34 ms: 1.17x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| nbody                            | 67.6 ms                                                | 80.0 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.8 ms: 1.24x slower                                                 |
| many_optionals                   | 403 us                                                 | 594 us: 1.48x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): scimark_monte_carlo, asyncio_websockets, async_tree_eager
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 93.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x