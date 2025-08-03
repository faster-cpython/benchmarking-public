# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.046x faster
- HPT reliability: 90.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 173 ms: 1.03x slower                                                  |
| sphinx         | 613 ms                                                 | 582 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 382 ms: 1.76x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 383 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 375 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.58x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| async_generators                 | 299 ms                                                 | 275 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.9 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 50.1 ms: 1.08x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 80.0 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.15 ms: 1.13x faster                                                 |
| regex_dna      | 143 ms                                                 | 139 ms: 1.03x faster                                                  |
| regex_compile  | 75.9 ms                                                | 74.0 ms: 1.03x faster                                                 |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 56.0 ms: 1.01x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 39.7 ms: 1.02x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.63 ms: 1.07x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 156 us: 1.07x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 216 us: 1.09x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.51 sec: 1.11x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.9 ms: 1.05x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| mako            | 7.44 ms                                                | 8.09 ms: 1.09x slower                                                 |
| django_template | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 774 ms: 1.93x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 382 ms: 1.76x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 383 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 375 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.58x faster                                                  |
| deepcopy                         | 226 us                                                 | 173 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.5 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 62.6 ms: 1.22x faster                                                 |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 21.9 us: 1.19x faster                                                 |
| comprehensions                   | 14.0 us                                                | 11.9 us: 1.17x faster                                                 |
| raytrace                         | 204 ms                                                 | 175 ms: 1.17x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.2 ms: 1.16x faster                                                 |
| go                               | 98.5 ms                                                | 85.7 ms: 1.15x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.15 ms: 1.13x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                  |
| async_generators                 | 299 ms                                                 | 275 ms: 1.08x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.34 us: 1.08x faster                                                 |
| float                            | 54.1 ms                                                | 50.1 ms: 1.08x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.39 ms: 1.08x faster                                                 |
| chaos                            | 41.6 ms                                                | 38.7 ms: 1.07x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.64 us: 1.07x faster                                                 |
| sphinx                           | 613 ms                                                 | 582 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| python_startup                   | 17.8 ms                                                | 16.9 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| thrift                           | 468 us                                                 | 447 us: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.14 sec: 1.04x faster                                                |
| scimark_fft                      | 194 ms                                                 | 187 ms: 1.04x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 139 ms: 1.03x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 74.0 ms: 1.03x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.1 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 84.3 ms: 1.02x faster                                                 |
| pyflate                          | 311 ms                                                 | 306 ms: 1.02x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 71.5 ns: 1.02x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 64.9 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.12 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 56.0 ms: 1.01x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 52.1 ms: 1.01x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 45.2 ms: 1.02x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                 |
| shortest_path                    | 331 ms                                                 | 337 ms: 1.02x slower                                                  |
| connected_components             | 300 ms                                                 | 306 ms: 1.02x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 39.7 ms: 1.02x slower                                                 |
| sympy_str                        | 144 ms                                                 | 147 ms: 1.02x slower                                                  |
| dask                             | 779 ms                                                 | 797 ms: 1.02x slower                                                  |
| 2to3                             | 168 ms                                                 | 173 ms: 1.03x slower                                                  |
| pycparser                        | 673 ms                                                 | 692 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.5 ms: 1.03x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 76.4 ms: 1.04x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 505 us: 1.05x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.58 ms: 1.05x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 96.8 us: 1.06x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 247 ms: 1.06x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 69.6 ms: 1.06x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.63 ms: 1.07x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 156 us: 1.07x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.17 ms: 1.08x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 75.0 ms: 1.09x slower                                                 |
| mako                             | 7.44 ms                                                | 8.09 ms: 1.09x slower                                                 |
| richards_super                   | 34.6 ms                                                | 37.7 ms: 1.09x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.09x slower                                                |
| pickle_pure_python               | 197 us                                                 | 216 us: 1.09x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 529 ms: 1.10x slower                                                  |
| richards                         | 30.6 ms                                                | 33.6 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.51 sec: 1.11x slower                                                |
| fannkuch                         | 250 ms                                                 | 286 ms: 1.14x slower                                                  |
| django_template                  | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                 |
| telco                            | 3.92 ms                                                | 4.60 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.18x slower                                                 |
| nbody                            | 67.6 ms                                                | 80.0 ms: 1.19x slower                                                 |
| coverage                         | 38.5 ms                                                | 46.1 ms: 1.20x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| many_optionals                   | 403 us                                                 | 591 us: 1.47x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (5): html5lib, json, docutils, asyncio_websockets, json_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 90.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x