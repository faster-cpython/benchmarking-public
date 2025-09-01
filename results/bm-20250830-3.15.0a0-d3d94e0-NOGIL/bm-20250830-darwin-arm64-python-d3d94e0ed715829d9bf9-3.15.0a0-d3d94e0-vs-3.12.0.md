# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.026x faster
- HPT reliability: 55.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| docutils       | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                |
| html5lib       | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                 |
| sphinx         | 613 ms                                                 | 594 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 302 ms: 2.23x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.18x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 291 ms: 2.12x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 320 ms: 2.10x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 168 ms: 1.89x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 136 ms: 1.88x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 155 ms: 1.70x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 380 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                 |
| async_generators                 | 299 ms                                                 | 286 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 361 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 150 ms: 1.06x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 75.7 ms: 1.15x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.46x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 89.5 ms: 1.33x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.17 ms: 1.12x faster                                                 |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 14.7 ms: 1.02x faster                                                 |
| regex_compile  | 75.9 ms                                                | 79.5 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 64.4 ms: 1.17x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| json_dumps           | 6.19 ms                                                | 5.97 ms: 1.04x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 58.5 ms: 1.06x slower                                                 |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 164 us: 1.13x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.54 sec: 1.14x slower                                                |
| pickle_pure_python   | 197 us                                                 | 224 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.4 ms: 1.15x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.3 ms: 1.22x slower                                                 |
| genshi_text     | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                 |
| django_template | 19.7 ms                                                | 24.4 ms: 1.24x slower                                                 |
| mako            | 7.44 ms                                                | 10.7 ms: 1.44x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.28x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.95 ms                                                | 1.29 ms: 2.29x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 302 ms: 2.23x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.18x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 291 ms: 2.12x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 320 ms: 2.10x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 168 ms: 1.89x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 136 ms: 1.88x faster                                                  |
| mdp                              | 1.49 sec                                               | 867 ms: 1.72x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 155 ms: 1.70x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 773 us: 1.49x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 380 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                                  |
| deepcopy                         | 226 us                                                 | 186 us: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| subparsers                       | 32.1 ms                                                | 26.9 ms: 1.19x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 64.4 ms: 1.17x faster                                                 |
| generators                       | 29.4 ms                                                | 25.2 ms: 1.16x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.35 us: 1.14x faster                                                 |
| float                            | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.8 ms: 1.13x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.17 ms: 1.12x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 23.4 us: 1.11x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| pylint                           | 182 ms                                                 | 167 ms: 1.09x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                |
| go                               | 98.5 ms                                                | 93.0 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.12 sec: 1.05x faster                                                |
| deepcopy_reduce                  | 2.01 us                                                | 1.91 us: 1.05x faster                                                 |
| raytrace                         | 204 ms                                                 | 194 ms: 1.05x faster                                                  |
| async_generators                 | 299 ms                                                 | 286 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 73.3 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.4 us: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| json_dumps                       | 6.19 ms                                                | 5.97 ms: 1.04x faster                                                 |
| sphinx                           | 613 ms                                                 | 594 ms: 1.03x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                |
| pycparser                        | 673 ms                                                 | 657 ms: 1.02x faster                                                  |
| regex_v8                         | 15.1 ms                                                | 14.7 ms: 1.02x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.51 ms: 1.02x faster                                                 |
| html5lib                         | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 86.5 ms: 1.01x slower                                                 |
| pyflate                          | 311 ms                                                 | 314 ms: 1.01x slower                                                  |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                 |
| chaos                            | 41.6 ms                                                | 42.3 ms: 1.02x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.67 us: 1.02x slower                                                 |
| dask                             | 779 ms                                                 | 796 ms: 1.02x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.05 us: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 361 ms: 1.04x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 79.5 ms: 1.05x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 58.5 ms: 1.06x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 150 ms: 1.06x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 77.3 ns: 1.07x slower                                                 |
| thrift                           | 468 us                                                 | 499 us: 1.07x slower                                                  |
| shortest_path                    | 331 ms                                                 | 353 ms: 1.07x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 82.5 ms: 1.08x slower                                                 |
| connected_components             | 300 ms                                                 | 330 ms: 1.10x slower                                                  |
| sympy_str                        | 144 ms                                                 | 159 ms: 1.10x slower                                                  |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| nqueens                          | 59.5 ms                                                | 66.1 ms: 1.11x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 164 us: 1.13x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 74.0 ms: 1.13x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 50.3 ms: 1.13x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 58.3 ms: 1.13x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.54 sec: 1.14x slower                                                |
| pickle_pure_python               | 197 us                                                 | 224 us: 1.14x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.60 ms: 1.14x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.13 sec: 1.15x slower                                                |
| python_startup                   | 17.8 ms                                                | 20.4 ms: 1.15x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 555 ms: 1.15x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 75.7 ms: 1.15x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 84.8 ms: 1.15x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.08 ms: 1.16x slower                                                 |
| telco                            | 3.92 ms                                                | 4.57 ms: 1.17x slower                                                 |
| richards_super                   | 34.6 ms                                                | 41.1 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.4 ms: 1.19x slower                                                 |
| fannkuch                         | 250 ms                                                 | 299 ms: 1.20x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 37.3 ms: 1.22x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 84.6 ms: 1.22x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                 |
| django_template                  | 19.7 ms                                                | 24.4 ms: 1.24x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 119 us: 1.30x slower                                                  |
| nbody                            | 67.6 ms                                                | 89.5 ms: 1.33x slower                                                 |
| mako                             | 7.44 ms                                                | 10.7 ms: 1.44x slower                                                 |
| many_optionals                   | 403 us                                                 | 612 us: 1.52x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 745 us: 1.54x slower                                                  |
| coverage                         | 38.5 ms                                                | 63.4 ms: 1.65x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.46x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 55.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.28x