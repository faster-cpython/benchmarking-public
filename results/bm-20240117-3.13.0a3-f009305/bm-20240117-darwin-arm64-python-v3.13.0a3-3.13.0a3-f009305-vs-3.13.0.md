# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.010x faster
- HPT reliability: 94.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 170 ms: 1.10x faster                                       |
| chameleon      | 5.08 ms                                                | 4.87 ms: 1.04x faster                                      |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 18.7 ms: 1.06x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 68.6 ms: 1.02x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 342 ms: 1.01x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 47.2 ms: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 140 ms: 1.02x slower                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 173 ms: 1.03x slower                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 324 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 521 ms: 1.13x slower                                       |
| async_tree_none                  | 215 ms                                                 | 253 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 531 ms: 1.19x slower                                       |
| async_tree_memoization           | 268 ms                                                 | 329 ms: 1.23x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 670 ms: 1.30x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 260 ms: 1.31x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 644 ms: 1.35x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 672 ms: 1.35x slower                                       |
| async_tree_io                    | 507 ms                                                 | 703 ms: 1.39x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.15x slower                                               |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| float          | 56.0 ms                                                | 56.9 ms: 1.02x slower                                      |
| nbody          | 74.0 ms                                                | 75.6 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 73.8 ms: 1.07x faster                                      |
| regex_dna      | 149 ms                                                 | 157 ms: 1.05x slower                                       |
| regex_effbot   | 2.63 ms                                                | 2.77 ms: 1.05x slower                                      |
| regex_v8       | 17.0 ms                                                | 18.0 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 198 us: 1.08x faster                                       |
| xml_etree_parse      | 107 ms                                                 | 99.6 ms: 1.08x faster                                      |
| unpickle_pure_python | 164 us                                                 | 154 us: 1.07x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 39.9 ms: 1.03x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 71.9 ms: 1.02x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| xml_etree_generate   | 57.0 ms                                                | 56.3 ms: 1.01x faster                                      |
| json_loads           | 17.0 us                                                | 17.1 us: 1.01x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 13.9 ms: 1.36x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 12.3 ms: 1.17x faster                                      |
| Geometric mean         | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| django_template | 22.2 ms                                                | 21.7 ms: 1.02x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.6 ms: 1.02x faster                                      |
| mako            | 7.68 ms                                                | 7.54 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles                 | 1.17 ms                                                | 706 us: 1.66x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 70.9 us: 1.43x faster                                      |
| bench_mp_pool                    | 62.5 ms                                                | 45.1 ms: 1.39x faster                                      |
| python_startup                   | 18.9 ms                                                | 13.9 ms: 1.36x faster                                      |
| gc_traversal                     | 2.91 ms                                                | 2.40 ms: 1.21x faster                                      |
| mypy2                            | 701 ms                                                 | 597 ms: 1.17x faster                                       |
| python_startup_no_site           | 14.5 ms                                                | 12.3 ms: 1.17x faster                                      |
| crypto_pyaes                     | 54.2 ms                                                | 48.3 ms: 1.12x faster                                      |
| generators                       | 31.5 ms                                                | 28.4 ms: 1.11x faster                                      |
| 2to3                             | 187 ms                                                 | 170 ms: 1.10x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.44 ms: 1.10x faster                                      |
| go                               | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 789 us: 1.09x faster                                       |
| pickle_pure_python               | 214 us                                                 | 198 us: 1.08x faster                                       |
| xml_etree_parse                  | 107 ms                                                 | 99.6 ms: 1.08x faster                                      |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| pylint                           | 180 ms                                                 | 169 ms: 1.07x faster                                       |
| unpickle_pure_python             | 164 us                                                 | 154 us: 1.07x faster                                       |
| regex_compile                    | 78.6 ms                                                | 73.8 ms: 1.07x faster                                      |
| deepcopy_memo                    | 27.4 us                                                | 25.7 us: 1.06x faster                                      |
| hexiom                           | 4.86 ms                                                | 4.57 ms: 1.06x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 47.5 ms: 1.06x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 965 us: 1.06x faster                                       |
| coroutines                       | 19.8 ms                                                | 18.7 ms: 1.06x faster                                      |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.7 ms: 1.05x faster                                      |
| deepcopy                         | 237 us                                                 | 225 us: 1.05x faster                                       |
| richards_super                   | 39.1 ms                                                | 37.3 ms: 1.05x faster                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.98 us: 1.04x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.87 ms: 1.04x faster                                      |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                       |
| richards                         | 35.2 ms                                                | 33.8 ms: 1.04x faster                                      |
| fannkuch                         | 284 ms                                                 | 273 ms: 1.04x faster                                       |
| sympy_sum                        | 75.4 ms                                                | 72.5 ms: 1.04x faster                                      |
| chaos                            | 41.2 ms                                                | 39.8 ms: 1.04x faster                                      |
| pyflate                          | 351 ms                                                 | 339 ms: 1.04x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 183 ms: 1.03x faster                                       |
| sympy_expand                     | 246 ms                                                 | 238 ms: 1.03x faster                                       |
| logging_simple                   | 3.60 us                                                | 3.49 us: 1.03x faster                                      |
| pprint_safe_repr                 | 533 ms                                                 | 516 ms: 1.03x faster                                       |
| scimark_lu                       | 76.7 ms                                                | 74.2 ms: 1.03x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.05 sec: 1.03x faster                                     |
| sqlglot_optimize                 | 34.9 ms                                                | 33.9 ms: 1.03x faster                                      |
| xml_etree_process                | 41.0 ms                                                | 39.9 ms: 1.03x faster                                      |
| nqueens                          | 62.5 ms                                                | 60.9 ms: 1.03x faster                                      |
| logging_format                   | 3.89 us                                                | 3.79 us: 1.03x faster                                      |
| django_template                  | 22.2 ms                                                | 21.7 ms: 1.02x faster                                      |
| telco                            | 4.76 ms                                                | 4.65 ms: 1.02x faster                                      |
| xml_etree_iterparse              | 73.6 ms                                                | 71.9 ms: 1.02x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 33.6 ms: 1.02x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 68.6 ms: 1.02x faster                                      |
| mako                             | 7.68 ms                                                | 7.54 ms: 1.02x faster                                      |
| thrift                           | 466 us                                                 | 458 us: 1.02x faster                                       |
| json                             | 3.03 ms                                                | 2.98 ms: 1.02x faster                                      |
| meteor_contest                   | 74.0 ms                                                | 72.7 ms: 1.02x faster                                      |
| tomli_loads                      | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 342 ms: 1.01x faster                                       |
| comprehensions                   | 12.3 us                                                | 12.1 us: 1.01x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 47.2 ms: 1.01x faster                                      |
| spectral_norm                    | 76.3 ms                                                | 75.4 ms: 1.01x faster                                      |
| xml_etree_generate               | 57.0 ms                                                | 56.3 ms: 1.01x faster                                      |
| bench_thread_pool                | 505 us                                                 | 500 us: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                       |
| pycparser                        | 705 ms                                                 | 700 ms: 1.01x faster                                       |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| scimark_sor                      | 105 ms                                                 | 105 ms: 1.00x faster                                       |
| logging_silent                   | 70.1 ns                                                | 69.9 ns: 1.00x faster                                      |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.01x slower                                      |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| float                            | 56.0 ms                                                | 56.9 ms: 1.02x slower                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 140 ms: 1.02x slower                                       |
| scimark_fft                      | 201 ms                                                 | 204 ms: 1.02x slower                                       |
| nbody                            | 74.0 ms                                                | 75.6 ms: 1.02x slower                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 173 ms: 1.03x slower                                       |
| coverage                         | 46.0 ms                                                | 47.2 ms: 1.03x slower                                      |
| dulwich_log                      | 28.5 ms                                                | 29.4 ms: 1.03x slower                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.11 ms: 1.04x slower                                      |
| pathlib                          | 23.4 ms                                                | 24.5 ms: 1.05x slower                                      |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.05x slower                                     |
| regex_dna                        | 149 ms                                                 | 157 ms: 1.05x slower                                       |
| regex_effbot                     | 2.63 ms                                                | 2.77 ms: 1.05x slower                                      |
| regex_v8                         | 17.0 ms                                                | 18.0 ms: 1.06x slower                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 324 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 521 ms: 1.13x slower                                       |
| async_tree_none                  | 215 ms                                                 | 253 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 531 ms: 1.19x slower                                       |
| async_tree_memoization           | 268 ms                                                 | 329 ms: 1.23x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 670 ms: 1.30x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 260 ms: 1.31x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 644 ms: 1.35x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 672 ms: 1.35x slower                                       |
| async_tree_io                    | 507 ms                                                 | 703 ms: 1.39x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (4): html5lib, json_dumps, async_generators, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, dask, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 94.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.88x