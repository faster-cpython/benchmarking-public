# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: darwin-arm64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 168 ms: 1.12x faster                                               |
| html5lib       | 36.6 ms                                                | 30.9 ms: 1.18x faster                                              |
| sphinx         | 603 ms                                                 | 592 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 236 ms: 1.22x faster                                               |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.13x faster                                              |
| async_tree_eager                 | 70.1 ms                                                | 63.4 ms: 1.10x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                               |
| async_tree_eager_tg              | 47.8 ms                                                | 44.6 ms: 1.07x faster                                              |
| async_tree_none                  | 215 ms                                                 | 203 ms: 1.06x faster                                               |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                               |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 341 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                               |
| async_tree_none_tg               | 198 ms                                                 | 203 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 477 ms: 1.06x slower                                               |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                               |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                               |
| async_tree_eager_io              | 514 ms                                                 | 666 ms: 1.30x slower                                               |
| async_tree_eager_io_tg           | 477 ms                                                 | 708 ms: 1.48x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 68.2 ms: 1.09x faster                                              |
| float          | 56.0 ms                                                | 52.5 ms: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.29 ms: 1.15x faster                                              |
| regex_compile  | 78.6 ms                                                | 70.6 ms: 1.11x faster                                              |
| regex_dna      | 149 ms                                                 | 135 ms: 1.10x faster                                               |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 153 us: 1.07x faster                                               |
| tomli_loads          | 1.57 sec                                               | 1.47 sec: 1.07x faster                                             |
| xml_etree_generate   | 57.0 ms                                                | 54.2 ms: 1.05x faster                                              |
| xml_etree_process    | 41.0 ms                                                | 39.5 ms: 1.04x faster                                              |
| pickle_pure_python   | 214 us                                                 | 207 us: 1.04x faster                                               |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                              |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                               |
| xml_etree_iterparse  | 73.6 ms                                                | 76.6 ms: 1.04x slower                                              |
| json_dumps           | 6.52 ms                                                | 7.29 ms: 1.12x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 13.9 ms: 1.04x faster                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                              |
| genshi_xml      | 34.4 ms                                                | 30.8 ms: 1.12x faster                                              |
| mako            | 7.68 ms                                                | 6.92 ms: 1.11x faster                                              |
| django_template | 22.2 ms                                                | 20.9 ms: 1.06x faster                                              |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 154 us: 1.54x faster                                               |
| deepcopy_memo                    | 27.4 us                                                | 18.4 us: 1.49x faster                                              |
| generators                       | 31.5 ms                                                | 22.5 ms: 1.40x faster                                              |
| go                               | 115 ms                                                 | 87.3 ms: 1.32x faster                                              |
| deepcopy_reduce                  | 2.07 us                                                | 1.60 us: 1.30x faster                                              |
| spectral_norm                    | 76.3 ms                                                | 62.1 ms: 1.23x faster                                              |
| async_tree_memoization_tg        | 288 ms                                                 | 236 ms: 1.22x faster                                               |
| html5lib                         | 36.6 ms                                                | 30.9 ms: 1.18x faster                                              |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                              |
| scimark_fft                      | 201 ms                                                 | 173 ms: 1.16x faster                                               |
| regex_effbot                     | 2.63 ms                                                | 2.29 ms: 1.15x faster                                              |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.13x faster                                              |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.67 ms: 1.12x faster                                              |
| 2to3                             | 187 ms                                                 | 168 ms: 1.12x faster                                               |
| genshi_xml                       | 34.4 ms                                                | 30.8 ms: 1.12x faster                                              |
| regex_compile                    | 78.6 ms                                                | 70.6 ms: 1.11x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 45.3 ms: 1.11x faster                                              |
| mako                             | 7.68 ms                                                | 6.92 ms: 1.11x faster                                              |
| logging_simple                   | 3.60 us                                                | 3.26 us: 1.11x faster                                              |
| pprint_safe_repr                 | 533 ms                                                 | 482 ms: 1.11x faster                                               |
| pprint_pformat                   | 1.08 sec                                               | 980 ms: 1.11x faster                                               |
| scimark_sor                      | 105 ms                                                 | 95.4 ms: 1.10x faster                                              |
| async_tree_eager                 | 70.1 ms                                                | 63.4 ms: 1.10x faster                                              |
| regex_dna                        | 149 ms                                                 | 135 ms: 1.10x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                               |
| deltablue                        | 2.68 ms                                                | 2.45 ms: 1.09x faster                                              |
| nqueens                          | 62.5 ms                                                | 57.4 ms: 1.09x faster                                              |
| logging_format                   | 3.89 us                                                | 3.58 us: 1.09x faster                                              |
| hexiom                           | 4.86 ms                                                | 4.47 ms: 1.09x faster                                              |
| nbody                            | 74.0 ms                                                | 68.2 ms: 1.09x faster                                              |
| sqlglot_parse                    | 856 us                                                 | 794 us: 1.08x faster                                               |
| pycparser                        | 705 ms                                                 | 655 ms: 1.08x faster                                               |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.08x faster                                              |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                               |
| async_tree_eager_tg              | 47.8 ms                                                | 44.6 ms: 1.07x faster                                              |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                               |
| unpickle_pure_python             | 164 us                                                 | 153 us: 1.07x faster                                               |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                               |
| bench_thread_pool                | 505 us                                                 | 473 us: 1.07x faster                                               |
| float                            | 56.0 ms                                                | 52.5 ms: 1.07x faster                                              |
| sqlglot_normalize                | 189 ms                                                 | 177 ms: 1.07x faster                                               |
| tomli_loads                      | 1.57 sec                                               | 1.47 sec: 1.07x faster                                             |
| async_tree_none                  | 215 ms                                                 | 203 ms: 1.06x faster                                               |
| django_template                  | 22.2 ms                                                | 20.9 ms: 1.06x faster                                              |
| pathlib                          | 23.4 ms                                                | 22.1 ms: 1.06x faster                                              |
| sqlglot_transpile                | 1.02 ms                                                | 966 us: 1.06x faster                                               |
| fannkuch                         | 284 ms                                                 | 268 ms: 1.06x faster                                               |
| sqlglot_optimize                 | 34.9 ms                                                | 33.2 ms: 1.05x faster                                              |
| telco                            | 4.76 ms                                                | 4.53 ms: 1.05x faster                                              |
| xml_etree_generate               | 57.0 ms                                                | 54.2 ms: 1.05x faster                                              |
| richards_super                   | 39.1 ms                                                | 37.2 ms: 1.05x faster                                              |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                               |
| json                             | 3.03 ms                                                | 2.89 ms: 1.05x faster                                              |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                               |
| sympy_expand                     | 246 ms                                                 | 235 ms: 1.05x faster                                               |
| python_startup_no_site           | 14.5 ms                                                | 13.9 ms: 1.04x faster                                              |
| richards                         | 35.2 ms                                                | 33.7 ms: 1.04x faster                                              |
| scimark_lu                       | 76.7 ms                                                | 73.7 ms: 1.04x faster                                              |
| coverage                         | 46.0 ms                                                | 44.2 ms: 1.04x faster                                              |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                               |
| xml_etree_process                | 41.0 ms                                                | 39.5 ms: 1.04x faster                                              |
| pickle_pure_python               | 214 us                                                 | 207 us: 1.04x faster                                               |
| sympy_sum                        | 75.4 ms                                                | 72.7 ms: 1.04x faster                                              |
| typing_runtime_protocols         | 101 us                                                 | 97.8 us: 1.04x faster                                              |
| logging_silent                   | 70.1 ns                                                | 67.9 ns: 1.03x faster                                              |
| bench_mp_pool                    | 62.5 ms                                                | 60.9 ms: 1.03x faster                                              |
| dulwich_log                      | 28.5 ms                                                | 27.8 ms: 1.03x faster                                              |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.52 ms: 1.03x faster                                              |
| bpe_tokeniser                    | 3.25 sec                                               | 3.18 sec: 1.02x faster                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                               |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                              |
| sphinx                           | 603 ms                                                 | 592 ms: 1.02x faster                                               |
| meteor_contest                   | 74.0 ms                                                | 72.7 ms: 1.02x faster                                              |
| chaos                            | 41.2 ms                                                | 40.5 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 341 ms: 1.02x faster                                               |
| sqlalchemy_declarative           | 58.9 ms                                                | 58.5 ms: 1.01x faster                                              |
| crypto_pyaes                     | 54.2 ms                                                | 54.1 ms: 1.00x faster                                              |
| gc_traversal                     | 2.91 ms                                                | 2.92 ms: 1.00x slower                                              |
| connected_components             | 319 ms                                                 | 321 ms: 1.01x slower                                               |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                             |
| comprehensions                   | 12.3 us                                                | 12.4 us: 1.01x slower                                              |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                               |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.02x slower                                               |
| async_tree_none_tg               | 198 ms                                                 | 203 ms: 1.02x slower                                               |
| xml_etree_iterparse              | 73.6 ms                                                | 76.6 ms: 1.04x slower                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 477 ms: 1.06x slower                                               |
| create_gc_cycles                 | 1.17 ms                                                | 1.30 ms: 1.11x slower                                              |
| json_dumps                       | 6.52 ms                                                | 7.29 ms: 1.12x slower                                              |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                               |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                               |
| async_tree_eager_io              | 514 ms                                                 | 666 ms: 1.30x slower                                               |
| k_core                           | 1.61 sec                                               | 2.27 sec: 1.42x slower                                             |
| async_tree_eager_io_tg           | 477 ms                                                 | 708 ms: 1.48x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (6): pidigits, asyncio_websockets, docutils, shortest_path, python_startup, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.049x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x