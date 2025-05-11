# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.104x slower
- HPT reliability: 97.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 193 ms: 1.08x slower                                                  |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| html5lib       | 36.7 ms                                                | 35.1 ms: 1.05x faster                                                 |
| sphinx         | 602 ms                                                 | 638 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 407 ms: 1.25x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 416 ms: 1.20x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 425 ms: 1.19x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 175 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 439 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 77.2 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.36x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.03x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 58.3 ms: 1.05x slower                                                 |
| nbody          | 73.6 ms                                                | 93.3 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.15 ms: 1.22x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                 |
| regex_compile  | 78.3 ms                                                | 87.0 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.5 ms: 1.03x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 61.1 ms: 1.07x slower                                                 |
| json_loads           | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 45.9 ms: 1.11x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 190 us: 1.15x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 251 us: 1.17x slower                                                  |
| json_dumps           | 6.47 ms                                                | 8.19 ms: 1.27x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.5 ms: 1.10x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                 |
| mako            | 7.75 ms                                                | 9.21 ms: 1.19x slower                                                 |
| django_template | 20.5 ms                                                | 26.4 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 870 ms: 1.72x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| deepcopy                         | 236 us                                                 | 188 us: 1.26x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 407 ms: 1.25x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.15 ms: 1.22x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 416 ms: 1.20x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 425 ms: 1.19x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 23.8 us: 1.15x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 175 ms: 1.13x faster                                                  |
| python_startup                   | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 94.5 ms: 1.12x faster                                                 |
| go                               | 117 ms                                                 | 105 ms: 1.11x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.5 ms: 1.10x faster                                                 |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.98 us: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 439 ms: 1.05x faster                                                  |
| html5lib                         | 36.7 ms                                                | 35.1 ms: 1.05x faster                                                 |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| k_core                           | 1.61 sec                                               | 1.57 sec: 1.03x faster                                                |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                 |
| connected_components             | 319 ms                                                 | 313 ms: 1.02x faster                                                  |
| generators                       | 31.9 ms                                                | 31.4 ms: 1.02x faster                                                 |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                  |
| pyflate                          | 352 ms                                                 | 350 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                                |
| json                             | 3.04 ms                                                | 3.12 ms: 1.03x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 78.7 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.5 ms: 1.03x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 208 ms: 1.04x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 77.3 ms: 1.05x slower                                                 |
| float                            | 55.8 ms                                                | 58.3 ms: 1.05x slower                                                 |
| sphinx                           | 602 ms                                                 | 638 ms: 1.06x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 53.8 ms: 1.07x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 61.1 ms: 1.07x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.18 sec: 1.07x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 580 ms: 1.07x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 543 us: 1.08x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 69.9 ms: 1.08x slower                                                 |
| richards                         | 36.2 ms                                                | 39.1 ms: 1.08x slower                                                 |
| 2to3                             | 179 ms                                                 | 193 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.24 ms: 1.09x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| fannkuch                         | 279 ms                                                 | 303 ms: 1.09x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                 |
| pycparser                        | 701 ms                                                 | 766 ms: 1.09x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 271 ms: 1.10x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.90 ms: 1.10x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                 |
| sympy_str                        | 146 ms                                                 | 160 ms: 1.10x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 77.2 ms: 1.10x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 83.0 ms: 1.10x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.4 ms: 1.11x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 45.9 ms: 1.11x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 87.0 ms: 1.11x slower                                                 |
| dask                             | 771 ms                                                 | 864 ms: 1.12x slower                                                  |
| richards_super                   | 39.2 ms                                                | 44.0 ms: 1.12x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 113 us: 1.12x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.48 ms: 1.13x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 86.0 ms: 1.13x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| raytrace                         | 181 ms                                                 | 207 ms: 1.14x slower                                                  |
| chaos                            | 41.1 ms                                                | 47.0 ms: 1.15x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 190 us: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 251 us: 1.17x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.53 us: 1.18x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.21 us: 1.18x slower                                                 |
| mako                             | 7.75 ms                                                | 9.21 ms: 1.19x slower                                                 |
| nqueens                          | 61.8 ms                                                | 75.3 ms: 1.22x slower                                                 |
| comprehensions                   | 12.0 us                                                | 14.6 us: 1.22x slower                                                 |
| many_optionals                   | 409 us                                                 | 510 us: 1.25x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.19 ms: 1.27x slower                                                 |
| nbody                            | 73.6 ms                                                | 93.3 ms: 1.27x slower                                                 |
| django_template                  | 20.5 ms                                                | 26.4 ms: 1.29x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.36x slower                                                  |
| subparsers                       | 9.44 ms                                                | 14.8 ms: 1.57x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.03x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 345 ns: 4.86x slower                                                  |
| coverage                         | 46.2 ms                                                | 334 ms: 7.23x slower                                                  |
| thrift                           | 466 us                                                 | 43.9 ms: 94.20x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (4): pylint, async_tree_eager_cpu_io_mixed, telco, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.104x slower

# HPT report

- Reliability score: 97.88% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x