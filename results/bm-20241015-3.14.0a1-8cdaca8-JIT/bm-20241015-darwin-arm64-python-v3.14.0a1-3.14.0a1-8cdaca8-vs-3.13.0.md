# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.037x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 183 ms: 1.02x faster                                       |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                     |
| html5lib       | 36.6 ms                                                | 34.2 ms: 1.07x faster                                      |
| sphinx         | 603 ms                                                 | 664 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 42.6 ms: 1.12x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 63.5 ms: 1.10x faster                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                       |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                       |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 470 ms: 1.05x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                       |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.2 ms: 1.16x faster                                      |
| nbody          | 74.0 ms                                                | 65.3 ms: 1.13x faster                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 74.8 ms: 1.05x faster                                      |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                       |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                      |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.26x faster                                     |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.25x faster                                       |
| pickle_pure_python   | 214 us                                                 | 178 us: 1.20x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 34.8 ms: 1.18x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 50.4 ms: 1.13x faster                                      |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 73.1 ms: 1.01x faster                                      |
| json_dumps           | 6.52 ms                                                | 7.13 ms: 1.09x slower                                      |
| Geometric mean       | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.0 ms: 1.00x slower                                      |
| python_startup_no_site | 14.5 ms                                                | 14.6 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.46 ms: 1.19x faster                                      |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                      |
| django_template | 22.2 ms                                                | 23.0 ms: 1.03x slower                                      |
| genshi_xml      | 34.4 ms                                                | 42.3 ms: 1.23x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.8 us: 1.63x faster                                      |
| deepcopy                         | 237 us                                                 | 154 us: 1.53x faster                                       |
| deepcopy_reduce                  | 2.07 us                                                | 1.53 us: 1.35x faster                                      |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.26x faster                                     |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.25x faster                                       |
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                       |
| scimark_sor                      | 105 ms                                                 | 86.0 ms: 1.23x faster                                      |
| pickle_pure_python               | 214 us                                                 | 178 us: 1.20x faster                                       |
| mako                             | 7.68 ms                                                | 6.46 ms: 1.19x faster                                      |
| scimark_lu                       | 76.7 ms                                                | 64.6 ms: 1.19x faster                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                      |
| xml_etree_process                | 41.0 ms                                                | 34.8 ms: 1.18x faster                                      |
| go                               | 115 ms                                                 | 97.6 ms: 1.18x faster                                      |
| float                            | 56.0 ms                                                | 48.2 ms: 1.16x faster                                      |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                      |
| logging_format                   | 3.89 us                                                | 3.42 us: 1.14x faster                                      |
| nbody                            | 74.0 ms                                                | 65.3 ms: 1.13x faster                                      |
| xml_etree_generate               | 57.0 ms                                                | 50.4 ms: 1.13x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.38 ms: 1.12x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 42.6 ms: 1.12x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 45.5 ms: 1.11x faster                                      |
| pprint_safe_repr                 | 533 ms                                                 | 483 ms: 1.10x faster                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 63.5 ms: 1.10x faster                                      |
| spectral_norm                    | 76.3 ms                                                | 69.3 ms: 1.10x faster                                      |
| thrift                           | 466 us                                                 | 426 us: 1.10x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 990 ms: 1.09x faster                                       |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                       |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                       |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                       |
| html5lib                         | 36.6 ms                                                | 34.2 ms: 1.07x faster                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.06x faster                                     |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.06x faster                                       |
| nqueens                          | 62.5 ms                                                | 58.8 ms: 1.06x faster                                      |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                       |
| fannkuch                         | 284 ms                                                 | 269 ms: 1.06x faster                                       |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| regex_compile                    | 78.6 ms                                                | 74.8 ms: 1.05x faster                                      |
| coverage                         | 46.0 ms                                                | 43.8 ms: 1.05x faster                                      |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                      |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                      |
| pycparser                        | 705 ms                                                 | 678 ms: 1.04x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 97.8 us: 1.03x faster                                      |
| json                             | 3.03 ms                                                | 2.93 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                       |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                       |
| 2to3                             | 187 ms                                                 | 183 ms: 1.02x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                       |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                      |
| bench_mp_pool                    | 62.5 ms                                                | 61.8 ms: 1.01x faster                                      |
| richards_super                   | 39.1 ms                                                | 38.7 ms: 1.01x faster                                      |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                       |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                       |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                      |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                      |
| xml_etree_iterparse              | 73.6 ms                                                | 73.1 ms: 1.01x faster                                      |
| logging_silent                   | 70.1 ns                                                | 69.8 ns: 1.00x faster                                      |
| richards                         | 35.2 ms                                                | 35.0 ms: 1.00x faster                                      |
| crypto_pyaes                     | 54.2 ms                                                | 54.0 ms: 1.00x faster                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| python_startup                   | 18.9 ms                                                | 19.0 ms: 1.00x slower                                      |
| meteor_contest                   | 74.0 ms                                                | 74.4 ms: 1.01x slower                                      |
| chaos                            | 41.2 ms                                                | 41.5 ms: 1.01x slower                                      |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                      |
| python_startup_no_site           | 14.5 ms                                                | 14.6 ms: 1.01x slower                                      |
| dulwich_log                      | 28.5 ms                                                | 28.9 ms: 1.01x slower                                      |
| hexiom                           | 4.86 ms                                                | 4.96 ms: 1.02x slower                                      |
| sqlglot_parse                    | 856 us                                                 | 875 us: 1.02x slower                                       |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.03x slower                                      |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.03x slower                                      |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                       |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.05x slower                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 470 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.14 ms: 1.05x slower                                      |
| sympy_sum                        | 75.4 ms                                                | 79.4 ms: 1.05x slower                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 37.1 ms: 1.06x slower                                      |
| comprehensions                   | 12.3 us                                                | 13.1 us: 1.07x slower                                      |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                       |
| json_dumps                       | 6.52 ms                                                | 7.13 ms: 1.09x slower                                      |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                     |
| sphinx                           | 603 ms                                                 | 664 ms: 1.10x slower                                       |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.11x slower                                      |
| create_gc_cycles                 | 1.17 ms                                                | 1.30 ms: 1.11x slower                                      |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                       |
| pylint                           | 180 ms                                                 | 212 ms: 1.18x slower                                       |
| genshi_xml                       | 34.4 ms                                                | 42.3 ms: 1.23x slower                                      |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (5): tornado_http, async_tree_cpu_io_mixed, sympy_expand, asyncio_websockets, xml_etree_parse
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x