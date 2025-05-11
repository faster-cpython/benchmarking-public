# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 158 ms: 1.13x faster                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.7 ms                                                | 29.5 ms: 1.24x faster                                                 |
| sphinx         | 602 ms                                                 | 560 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 336 ms: 1.52x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.49x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 341 ms: 1.49x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.37x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 57.2 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 406 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                  |
| async_generators                 | 294 ms                                                 | 267 ms: 1.10x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.54x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.1 ms: 1.27x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.9 ms: 1.27x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.21 ms: 1.19x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.31x faster                                                |
| unpickle_pure_python | 165 us                                                 | 130 us: 1.27x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 188 us: 1.14x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 39.3 ms: 1.05x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 55.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| json_loads           | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| json_dumps           | 6.47 ms                                                | 7.34 ms: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.9 ms: 1.31x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 27.1 ms: 1.25x faster                                                 |
| mako            | 7.75 ms                                                | 7.25 ms: 1.07x faster                                                 |
| django_template | 20.5 ms                                                | 19.6 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 706 ms: 2.12x faster                                                  |
| generators                       | 31.9 ms                                                | 18.9 ms: 1.69x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 16.4 us: 1.67x faster                                                 |
| go                               | 117 ms                                                 | 71.1 ms: 1.64x faster                                                 |
| deepcopy                         | 236 us                                                 | 145 us: 1.63x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 336 ms: 1.52x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.49x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 341 ms: 1.49x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.37x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 77.7 ms: 1.36x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.33x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.31x faster                                                |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.9 ms: 1.31x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.05 ms: 1.29x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.77 ms: 1.29x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 130 us: 1.27x faster                                                  |
| pyflate                          | 352 ms                                                 | 277 ms: 1.27x faster                                                  |
| float                            | 55.8 ms                                                | 44.1 ms: 1.27x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 61.9 ms: 1.27x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.1 ms: 1.25x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 40.5 ms: 1.25x faster                                                 |
| html5lib                         | 36.7 ms                                                | 29.5 ms: 1.24x faster                                                 |
| richards                         | 36.2 ms                                                | 29.5 ms: 1.23x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 57.2 ms: 1.22x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 448 ms: 1.21x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.8 ms: 1.21x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 915 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.21 ms: 1.19x faster                                                 |
| richards_super                   | 39.2 ms                                                | 33.2 ms: 1.18x faster                                                 |
| pylint                           | 180 ms                                                 | 152 ms: 1.18x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.6 ms: 1.15x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 188 us: 1.14x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.5 us: 1.14x faster                                                 |
| nqueens                          | 61.8 ms                                                | 54.5 ms: 1.13x faster                                                 |
| 2to3                             | 179 ms                                                 | 158 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 406 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.89 sec: 1.13x faster                                                |
| sympy_expand                     | 248 ms                                                 | 222 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                 |
| pycparser                        | 701 ms                                                 | 630 ms: 1.11x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.8 ms: 1.11x faster                                                 |
| sympy_str                        | 146 ms                                                 | 131 ms: 1.11x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.9 ms: 1.11x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 91.0 us: 1.11x faster                                                 |
| async_generators                 | 294 ms                                                 | 267 ms: 1.10x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| fannkuch                         | 279 ms                                                 | 255 ms: 1.09x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.26 us: 1.09x faster                                                 |
| scimark_lu                       | 75.9 ms                                                | 69.7 ms: 1.09x faster                                                 |
| raytrace                         | 181 ms                                                 | 168 ms: 1.08x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 69.7 ms: 1.08x faster                                                 |
| sphinx                           | 602 ms                                                 | 560 ms: 1.08x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.59 us: 1.07x faster                                                 |
| telco                            | 4.84 ms                                                | 4.51 ms: 1.07x faster                                                 |
| mako                             | 7.75 ms                                                | 7.25 ms: 1.07x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.07x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 473 us: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                |
| shortest_path                    | 345 ms                                                 | 328 ms: 1.05x faster                                                  |
| connected_components             | 319 ms                                                 | 302 ms: 1.05x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 39.3 ms: 1.05x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.6 ms: 1.05x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.6 ms: 1.04x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| pathlib                          | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 55.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 205 ms: 1.03x slower                                                  |
| dask                             | 771 ms                                                 | 802 ms: 1.04x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 68.9 ms: 1.06x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| many_optionals                   | 409 us                                                 | 440 us: 1.08x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.22 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.34 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.37 ms: 1.13x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 7.34 ms: 1.13x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                  |
| subparsers                       | 9.44 ms                                                | 12.6 ms: 1.34x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.54x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 302 ns: 4.26x slower                                                  |
| coverage                         | 46.2 ms                                                | 258 ms: 5.58x slower                                                  |
| thrift                           | 466 us                                                 | 43.1 ms: 92.40x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, nbody, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x