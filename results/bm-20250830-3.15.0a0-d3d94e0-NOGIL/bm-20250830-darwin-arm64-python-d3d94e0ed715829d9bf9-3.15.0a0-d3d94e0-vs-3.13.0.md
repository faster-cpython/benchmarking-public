# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.028x faster
- HPT reliability: 86.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                |
| html5lib       | 36.7 ms                                                | 32.6 ms: 1.12x faster                                                 |
| sphinx         | 602 ms                                                 | 594 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 168 ms: 1.71x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.67x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 302 ms: 1.66x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 291 ms: 1.64x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 320 ms: 1.59x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.46x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 155 ms: 1.37x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.7 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 380 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 361 ms: 1.04x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 75.7 ms: 1.08x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 150 ms: 1.09x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.44x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 89.5 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.17 ms: 1.21x faster                                                 |
| regex_v8       | 17.0 ms                                                | 14.7 ms: 1.15x faster                                                 |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| regex_compile  | 78.3 ms                                                | 79.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 64.4 ms: 1.15x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| json_dumps           | 6.47 ms                                                | 5.97 ms: 1.08x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| unpickle_pure_python | 165 us                                                 | 164 us: 1.01x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 58.5 ms: 1.03x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 224 us: 1.05x slower                                                  |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.4 ms: 1.08x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.8 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 37.3 ms: 1.10x slower                                                 |
| django_template | 20.5 ms                                                | 24.4 ms: 1.19x slower                                                 |
| mako            | 7.75 ms                                                | 10.7 ms: 1.39x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.18x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.29 ms: 2.28x faster                                                 |
| mdp                              | 1.50 sec                                               | 867 ms: 1.73x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 168 ms: 1.71x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.67x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 302 ms: 1.66x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 291 ms: 1.64x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 320 ms: 1.59x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 773 us: 1.54x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.46x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 155 ms: 1.37x faster                                                  |
| deepcopy                         | 236 us                                                 | 186 us: 1.27x faster                                                  |
| generators                       | 31.9 ms                                                | 25.2 ms: 1.27x faster                                                 |
| go                               | 117 ms                                                 | 93.0 ms: 1.25x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 86.5 ms: 1.22x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.17 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.7 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 380 ms: 1.18x faster                                                  |
| float                            | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 23.4 us: 1.17x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 14.7 ms: 1.15x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 64.4 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.35 us: 1.15x faster                                                 |
| html5lib                         | 36.7 ms                                                | 32.6 ms: 1.12x faster                                                 |
| pyflate                          | 352 ms                                                 | 314 ms: 1.12x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.8 ms: 1.11x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.91 us: 1.09x faster                                                 |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| json_dumps                       | 6.47 ms                                                | 5.97 ms: 1.08x faster                                                 |
| pylint                           | 180 ms                                                 | 167 ms: 1.08x faster                                                  |
| pycparser                        | 701 ms                                                 | 657 ms: 1.07x faster                                                  |
| telco                            | 4.84 ms                                                | 4.57 ms: 1.06x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.51 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.12 sec: 1.04x faster                                                |
| spectral_norm                    | 76.5 ms                                                | 73.3 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| sphinx                           | 602 ms                                                 | 594 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 164 us: 1.01x faster                                                  |
| richards                         | 36.2 ms                                                | 36.4 ms: 1.01x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 79.5 ms: 1.02x slower                                                 |
| shortest_path                    | 345 ms                                                 | 353 ms: 1.02x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 58.5 ms: 1.03x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.13 sec: 1.03x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 555 ms: 1.03x slower                                                  |
| chaos                            | 41.1 ms                                                | 42.3 ms: 1.03x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 206 ms: 1.03x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.67 us: 1.03x slower                                                 |
| dask                             | 771 ms                                                 | 796 ms: 1.03x slower                                                  |
| connected_components             | 319 ms                                                 | 330 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 361 ms: 1.04x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.08 ms: 1.04x slower                                                 |
| 2to3                             | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 224 us: 1.05x slower                                                  |
| richards_super                   | 39.2 ms                                                | 41.1 ms: 1.05x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.05 us: 1.05x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 58.3 ms: 1.05x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| nqueens                          | 61.8 ms                                                | 66.1 ms: 1.07x slower                                                 |
| thrift                           | 466 us                                                 | 499 us: 1.07x slower                                                  |
| raytrace                         | 181 ms                                                 | 194 ms: 1.07x slower                                                  |
| fannkuch                         | 279 ms                                                 | 299 ms: 1.07x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 75.7 ms: 1.08x slower                                                 |
| python_startup                   | 18.8 ms                                                | 20.4 ms: 1.08x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 150 ms: 1.09x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 77.3 ns: 1.09x slower                                                 |
| sympy_str                        | 146 ms                                                 | 159 ms: 1.09x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 271 ms: 1.09x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 37.3 ms: 1.10x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 82.5 ms: 1.10x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 84.8 ms: 1.12x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.4 us: 1.12x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 74.0 ms: 1.14x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 84.6 ms: 1.14x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.8 ms: 1.15x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 119 us: 1.18x slower                                                  |
| django_template                  | 20.5 ms                                                | 24.4 ms: 1.19x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.60 ms: 1.21x slower                                                 |
| nbody                            | 73.6 ms                                                | 89.5 ms: 1.22x slower                                                 |
| coverage                         | 46.2 ms                                                | 63.4 ms: 1.37x slower                                                 |
| mako                             | 7.75 ms                                                | 10.7 ms: 1.39x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 745 us: 1.48x slower                                                  |
| many_optionals                   | 409 us                                                 | 612 us: 1.50x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.44x slower                                                  |
| subparsers                       | 9.44 ms                                                | 26.9 ms: 2.85x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): k_core, scimark_monte_carlo, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 86.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x