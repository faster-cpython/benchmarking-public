# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.056x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils       | 1.45 sec                                               | 1.46 sec: 1.00x slower                                                |
| sphinx         | 613 ms                                                 | 579 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.54x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                  |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.6 ms: 1.05x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_compile  | 75.9 ms                                                | 73.6 ms: 1.03x faster                                                 |
| regex_v8       | 15.1 ms                                                | 15.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 49.4 ms: 1.12x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.9 ms: 1.11x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                 |
| json_dumps           | 6.19 ms                                                | 6.28 ms: 1.02x slower                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.0 ms: 1.04x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 12.9 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                 |
| genshi_text     | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.3 ms: 1.09x slower                                                 |
| django_template | 19.7 ms                                                | 23.4 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 774 ms: 1.93x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.54x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| deepcopy                         | 226 us                                                 | 175 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.6 ms: 1.25x faster                                                 |
| comprehensions                   | 14.0 us                                                | 11.4 us: 1.23x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 63.5 ms: 1.20x faster                                                 |
| generators                       | 29.4 ms                                                | 24.4 ms: 1.20x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 22.3 us: 1.17x faster                                                 |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| mako                             | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.7 ms: 1.14x faster                                                 |
| raytrace                         | 204 ms                                                 | 180 ms: 1.14x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.92 sec: 1.13x faster                                                |
| deepcopy_reduce                  | 2.01 us                                                | 1.79 us: 1.12x faster                                                 |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.4 ms: 1.12x faster                                                 |
| go                               | 98.5 ms                                                | 88.2 ms: 1.12x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.9 ms: 1.11x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                |
| pprint_pformat                   | 986 ms                                                 | 916 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                 |
| pyflate                          | 311 ms                                                 | 293 ms: 1.06x faster                                                  |
| sphinx                           | 613 ms                                                 | 579 ms: 1.06x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 457 ms: 1.06x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.70 us: 1.06x faster                                                 |
| chaos                            | 41.6 ms                                                | 39.5 ms: 1.05x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.42 us: 1.05x faster                                                 |
| float                            | 54.1 ms                                                | 51.6 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.0 ms: 1.04x faster                                                 |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                                  |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 73.6 ms: 1.03x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.9 ms: 1.03x faster                                                 |
| python_startup_no_site           | 13.2 ms                                                | 12.9 ms: 1.02x faster                                                 |
| thrift                           | 468 us                                                 | 459 us: 1.02x faster                                                  |
| fannkuch                         | 250 ms                                                 | 246 ms: 1.02x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 192 ms: 1.02x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.54 ms: 1.01x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.5 ms: 1.01x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.46 sec: 1.00x slower                                                |
| scimark_sor                      | 85.8 ms                                                | 86.2 ms: 1.01x slower                                                 |
| json                             | 3.00 ms                                                | 3.05 ms: 1.01x slower                                                 |
| 2to3                             | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 77.4 ms: 1.01x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.3 ms: 1.02x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.28 ms: 1.02x slower                                                 |
| sympy_str                        | 144 ms                                                 | 147 ms: 1.02x slower                                                  |
| dask                             | 779 ms                                                 | 797 ms: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 94.7 us: 1.03x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 76.0 ms: 1.04x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.9 ms: 1.04x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.3 ms: 1.04x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 504 us: 1.04x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 72.7 ms: 1.05x slower                                                 |
| shortest_path                    | 331 ms                                                 | 350 ms: 1.06x slower                                                  |
| nbody                            | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 77.0 ns: 1.06x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.06x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 249 ms: 1.07x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.67 ms: 1.07x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 70.2 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 321 ms: 1.07x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.18 ms: 1.08x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.39 ms: 1.08x slower                                                 |
| pycparser                        | 673 ms                                                 | 736 ms: 1.09x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.3 ms: 1.09x slower                                                 |
| richards_super                   | 34.6 ms                                                | 38.0 ms: 1.10x slower                                                 |
| richards                         | 30.6 ms                                                | 34.3 ms: 1.12x slower                                                 |
| telco                            | 3.92 ms                                                | 4.40 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.17x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.4 ms: 1.19x slower                                                 |
| coverage                         | 38.5 ms                                                | 48.2 ms: 1.25x slower                                                 |
| many_optionals                   | 403 us                                                 | 600 us: 1.49x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, html5lib
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.58% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x