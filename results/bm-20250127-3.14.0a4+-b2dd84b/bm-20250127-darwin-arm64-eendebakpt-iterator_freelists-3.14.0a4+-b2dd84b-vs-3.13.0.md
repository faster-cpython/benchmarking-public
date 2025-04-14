# Results vs. 3.13.0

- fork: eendebakpt
- ref: iterator_freelists
- machine: darwin-arm64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.05x slower                                                     |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                   |
| html5lib       | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                    |
| sphinx         | 602 ms                                                 | 559 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                     |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                     |
| async_tree_io                    | 508 ms                                                 | 360 ms: 1.41x faster                                                     |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                     |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                                     |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.30x faster                                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                     |
| coroutines                       | 20.0 ms                                                | 15.9 ms: 1.26x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| async_generators                 | 294 ms                                                 | 247 ms: 1.19x faster                                                     |
| async_tree_eager                 | 69.9 ms                                                | 62.1 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                     |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.0 ms: 1.21x faster                                                    |
| nbody          | 73.6 ms                                                | 68.1 ms: 1.08x faster                                                    |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 66.2 ms: 1.18x faster                                                    |
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                    |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.31x faster                                                   |
| unpickle_pure_python | 165 us                                                 | 138 us: 1.20x faster                                                     |
| pickle_pure_python   | 215 us                                                 | 195 us: 1.10x faster                                                     |
| xml_etree_generate   | 57.1 ms                                                | 52.3 ms: 1.09x faster                                                    |
| xml_etree_process    | 41.3 ms                                                | 38.0 ms: 1.09x faster                                                    |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 74.2 ms                                                | 71.0 ms: 1.05x faster                                                    |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| json_dumps           | 6.47 ms                                                | 7.40 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                    |
| python_startup_no_site | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.1 ms: 1.29x faster                                                    |
| genshi_xml      | 34.1 ms                                                | 28.0 ms: 1.22x faster                                                    |
| mako            | 7.75 ms                                                | 6.97 ms: 1.11x faster                                                    |
| django_template | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 147 us: 1.61x faster                                                     |
| deepcopy_memo                    | 27.4 us                                                | 17.9 us: 1.53x faster                                                    |
| go                               | 117 ms                                                 | 77.0 ms: 1.52x faster                                                    |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                     |
| generators                       | 31.9 ms                                                | 22.4 ms: 1.43x faster                                                    |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                     |
| async_tree_io                    | 508 ms                                                 | 360 ms: 1.41x faster                                                     |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                     |
| scimark_sor                      | 106 ms                                                 | 77.0 ms: 1.37x faster                                                    |
| deepcopy_reduce                  | 2.09 us                                                | 1.54 us: 1.36x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.31x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.30x faster                                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 13.1 ms: 1.29x faster                                                    |
| html5lib                         | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                    |
| spectral_norm                    | 76.5 ms                                                | 60.4 ms: 1.27x faster                                                    |
| coroutines                       | 20.0 ms                                                | 15.9 ms: 1.26x faster                                                    |
| pyflate                          | 352 ms                                                 | 287 ms: 1.23x faster                                                     |
| genshi_xml                       | 34.1 ms                                                | 28.0 ms: 1.22x faster                                                    |
| float                            | 55.8 ms                                                | 46.0 ms: 1.21x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| unpickle_pure_python             | 165 us                                                 | 138 us: 1.20x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 42.2 ms: 1.20x faster                                                    |
| pprint_pformat                   | 1.10 sec                                               | 924 ms: 1.19x faster                                                     |
| pprint_safe_repr                 | 541 ms                                                 | 455 ms: 1.19x faster                                                     |
| async_generators                 | 294 ms                                                 | 247 ms: 1.19x faster                                                     |
| regex_compile                    | 78.3 ms                                                | 66.2 ms: 1.18x faster                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                    |
| hexiom                           | 4.87 ms                                                | 4.18 ms: 1.17x faster                                                    |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                                     |
| richards                         | 36.2 ms                                                | 31.3 ms: 1.16x faster                                                    |
| deltablue                        | 2.65 ms                                                | 2.29 ms: 1.15x faster                                                    |
| fannkuch                         | 279 ms                                                 | 242 ms: 1.15x faster                                                     |
| bpe_tokeniser                    | 3.26 sec                                               | 2.85 sec: 1.14x faster                                                   |
| pylint                           | 180 ms                                                 | 157 ms: 1.14x faster                                                     |
| logging_simple                   | 3.56 us                                                | 3.15 us: 1.13x faster                                                    |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.64 ms: 1.13x faster                                                    |
| sqlglot_transpile                | 1.04 ms                                                | 920 us: 1.13x faster                                                     |
| async_tree_eager                 | 69.9 ms                                                | 62.1 ms: 1.13x faster                                                    |
| richards_super                   | 39.2 ms                                                | 34.9 ms: 1.12x faster                                                    |
| sqlglot_parse                    | 852 us                                                 | 760 us: 1.12x faster                                                     |
| mako                             | 7.75 ms                                                | 6.97 ms: 1.11x faster                                                    |
| logging_format                   | 3.85 us                                                | 3.47 us: 1.11x faster                                                    |
| chaos                            | 41.1 ms                                                | 37.1 ms: 1.11x faster                                                    |
| pycparser                        | 701 ms                                                 | 634 ms: 1.10x faster                                                     |
| pickle_pure_python               | 215 us                                                 | 195 us: 1.10x faster                                                     |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                     |
| typing_runtime_protocols         | 101 us                                                 | 92.0 us: 1.09x faster                                                    |
| nqueens                          | 61.8 ms                                                | 56.5 ms: 1.09x faster                                                    |
| xml_etree_generate               | 57.1 ms                                                | 52.3 ms: 1.09x faster                                                    |
| thrift                           | 466 us                                                 | 427 us: 1.09x faster                                                     |
| xml_etree_process                | 41.3 ms                                                | 38.0 ms: 1.09x faster                                                    |
| sqlglot_optimize                 | 34.7 ms                                                | 31.9 ms: 1.08x faster                                                    |
| sympy_expand                     | 248 ms                                                 | 229 ms: 1.08x faster                                                     |
| nbody                            | 73.6 ms                                                | 68.1 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                     |
| connected_components             | 319 ms                                                 | 296 ms: 1.08x faster                                                     |
| sphinx                           | 602 ms                                                 | 559 ms: 1.08x faster                                                     |
| bench_thread_pool                | 503 us                                                 | 468 us: 1.08x faster                                                     |
| raytrace                         | 181 ms                                                 | 168 ms: 1.08x faster                                                     |
| k_core                           | 1.61 sec                                               | 1.50 sec: 1.07x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 26.8 ms: 1.07x faster                                                    |
| sympy_str                        | 146 ms                                                 | 136 ms: 1.07x faster                                                     |
| shortest_path                    | 345 ms                                                 | 323 ms: 1.07x faster                                                     |
| bench_mp_pool                    | 64.7 ms                                                | 60.5 ms: 1.07x faster                                                    |
| sqlglot_normalize                | 188 ms                                                 | 176 ms: 1.07x faster                                                     |
| logging_silent                   | 71.0 ns                                                | 66.6 ns: 1.07x faster                                                    |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                     |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                     |
| telco                            | 4.84 ms                                                | 4.56 ms: 1.06x faster                                                    |
| scimark_lu                       | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                    |
| meteor_contest                   | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                    |
| crypto_pyaes                     | 55.3 ms                                                | 52.6 ms: 1.05x faster                                                    |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.39 ms: 1.05x faster                                                    |
| xml_etree_iterparse              | 74.2 ms                                                | 71.0 ms: 1.05x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                     |
| sympy_sum                        | 75.1 ms                                                | 72.6 ms: 1.03x faster                                                    |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                    |
| sqlalchemy_declarative           | 59.0 ms                                                | 57.6 ms: 1.02x faster                                                    |
| pathlib                          | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                    |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                    |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                    |
| comprehensions                   | 12.0 us                                                | 11.8 us: 1.01x faster                                                    |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                   |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                    |
| django_template                  | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                    |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                     |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                    |
| 2to3                             | 179 ms                                                 | 187 ms: 1.05x slower                                                     |
| many_optionals                   | 409 us                                                 | 431 us: 1.06x slower                                                     |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                    |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                    |
| python_startup_no_site           | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                     |
| json_dumps                       | 6.47 ms                                                | 7.40 ms: 1.14x slower                                                    |
| subparsers                       | 9.44 ms                                                | 11.8 ms: 1.25x slower                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                     |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (3): json, asyncio_websockets, dask
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.08x