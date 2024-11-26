# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: darwin-arm64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.016x faster
- HPT reliability: 66.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 173 ms: 1.08x faster                                       |
| chameleon      | 5.08 ms                                                | 5.13 ms: 1.01x slower                                      |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                     |
| html5lib       | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 19.2 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 48.3 ms: 1.01x slower                                      |
| async_generators                 | 295 ms                                                 | 302 ms: 1.03x slower                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 141 ms: 1.03x slower                                       |
| async_tree_eager                 | 70.1 ms                                                | 72.2 ms: 1.03x slower                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 175 ms: 1.04x slower                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 323 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 531 ms: 1.18x slower                                       |
| async_tree_none                  | 215 ms                                                 | 257 ms: 1.19x slower                                       |
| async_tree_memoization           | 268 ms                                                 | 335 ms: 1.25x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 676 ms: 1.32x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 672 ms: 1.35x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 649 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.17x slower                                               |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 73.7 ms: 1.00x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| float          | 56.0 ms                                                | 57.0 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 75.1 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.02x faster                                      |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.01x slower                                      |
| regex_dna      | 149 ms                                                 | 152 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 201 us: 1.07x faster                                       |
| unpickle_pure_python | 164 us                                                 | 157 us: 1.05x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 40.4 ms: 1.01x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.55 sec: 1.01x faster                                     |
| json_loads           | 17.0 us                                                | 17.1 us: 1.01x slower                                      |
| xml_etree_generate   | 57.0 ms                                                | 58.1 ms: 1.02x slower                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 75.9 ms: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 12.9 ms: 1.47x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 11.3 ms: 1.28x faster                                      |
| Geometric mean         | (ref)                                                  | 1.37x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.9 ms: 1.06x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| mako            | 7.68 ms                                                | 7.57 ms: 1.01x faster                                      |
| django_template | 22.2 ms                                                | 22.2 ms: 1.00x faster                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                             | 790 ms                                                 | 225 ms: 3.51x faster                                       |
| create_gc_cycles                 | 1.17 ms                                                | 710 us: 1.65x faster                                       |
| mypy2                            | 701 ms                                                 | 457 ms: 1.53x faster                                       |
| python_startup                   | 18.9 ms                                                | 12.9 ms: 1.47x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 72.9 us: 1.39x faster                                      |
| bench_mp_pool                    | 62.5 ms                                                | 45.4 ms: 1.38x faster                                      |
| python_startup_no_site           | 14.5 ms                                                | 11.3 ms: 1.28x faster                                      |
| gc_traversal                     | 2.91 ms                                                | 2.42 ms: 1.20x faster                                      |
| crypto_pyaes                     | 54.2 ms                                                | 48.7 ms: 1.11x faster                                      |
| generators                       | 31.5 ms                                                | 28.6 ms: 1.10x faster                                      |
| go                               | 115 ms                                                 | 105 ms: 1.09x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| 2to3                             | 187 ms                                                 | 173 ms: 1.08x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 795 us: 1.08x faster                                       |
| pickle_pure_python               | 214 us                                                 | 201 us: 1.07x faster                                       |
| genshi_text                      | 16.9 ms                                                | 15.9 ms: 1.06x faster                                      |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                       |
| deepcopy_memo                    | 27.4 us                                                | 25.9 us: 1.05x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 972 us: 1.05x faster                                       |
| unpickle_pure_python             | 164 us                                                 | 157 us: 1.05x faster                                       |
| regex_compile                    | 78.6 ms                                                | 75.1 ms: 1.05x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 48.3 ms: 1.04x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                      |
| fannkuch                         | 284 ms                                                 | 274 ms: 1.03x faster                                       |
| scimark_lu                       | 76.7 ms                                                | 74.3 ms: 1.03x faster                                      |
| chaos                            | 41.2 ms                                                | 39.9 ms: 1.03x faster                                      |
| thrift                           | 466 us                                                 | 452 us: 1.03x faster                                       |
| deepcopy                         | 237 us                                                 | 230 us: 1.03x faster                                       |
| html5lib                         | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| logging_simple                   | 3.60 us                                                | 3.50 us: 1.03x faster                                      |
| richards_super                   | 39.1 ms                                                | 38.0 ms: 1.03x faster                                      |
| coroutines                       | 19.8 ms                                                | 19.2 ms: 1.03x faster                                      |
| telco                            | 4.76 ms                                                | 4.63 ms: 1.03x faster                                      |
| pyflate                          | 351 ms                                                 | 342 ms: 1.03x faster                                       |
| json                             | 3.03 ms                                                | 2.95 ms: 1.03x faster                                      |
| logging_format                   | 3.89 us                                                | 3.80 us: 1.03x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.06 sec: 1.02x faster                                     |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.02x faster                                      |
| sqlglot_normalize                | 189 ms                                                 | 185 ms: 1.02x faster                                       |
| pprint_safe_repr                 | 533 ms                                                 | 522 ms: 1.02x faster                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 34.2 ms: 1.02x faster                                      |
| richards                         | 35.2 ms                                                | 34.5 ms: 1.02x faster                                      |
| bench_thread_pool                | 505 us                                                 | 495 us: 1.02x faster                                       |
| genshi_xml                       | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| comprehensions                   | 12.3 us                                                | 12.1 us: 1.02x faster                                      |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                       |
| xml_etree_process                | 41.0 ms                                                | 40.4 ms: 1.01x faster                                      |
| mako                             | 7.68 ms                                                | 7.57 ms: 1.01x faster                                      |
| sympy_expand                     | 246 ms                                                 | 243 ms: 1.01x faster                                       |
| tomli_loads                      | 1.57 sec                                               | 1.55 sec: 1.01x faster                                     |
| pycparser                        | 705 ms                                                 | 700 ms: 1.01x faster                                       |
| hexiom                           | 4.86 ms                                                | 4.83 ms: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                       |
| deepcopy_reduce                  | 2.07 us                                                | 2.06 us: 1.01x faster                                      |
| spectral_norm                    | 76.3 ms                                                | 75.8 ms: 1.01x faster                                      |
| sympy_sum                        | 75.4 ms                                                | 75.0 ms: 1.01x faster                                      |
| meteor_contest                   | 74.0 ms                                                | 73.6 ms: 1.01x faster                                      |
| nbody                            | 74.0 ms                                                | 73.7 ms: 1.00x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| django_template                  | 22.2 ms                                                | 22.2 ms: 1.00x faster                                      |
| scimark_sor                      | 105 ms                                                 | 105 ms: 1.00x faster                                       |
| regex_v8                         | 17.0 ms                                                | 17.1 ms: 1.01x slower                                      |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.01x slower                                      |
| chameleon                        | 5.08 ms                                                | 5.13 ms: 1.01x slower                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 48.3 ms: 1.01x slower                                      |
| regex_dna                        | 149 ms                                                 | 152 ms: 1.02x slower                                       |
| float                            | 56.0 ms                                                | 57.0 ms: 1.02x slower                                      |
| xml_etree_generate               | 57.0 ms                                                | 58.1 ms: 1.02x slower                                      |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                     |
| async_generators                 | 295 ms                                                 | 302 ms: 1.03x slower                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 141 ms: 1.03x slower                                       |
| async_tree_eager                 | 70.1 ms                                                | 72.2 ms: 1.03x slower                                      |
| scimark_fft                      | 201 ms                                                 | 207 ms: 1.03x slower                                       |
| xml_etree_iterparse              | 73.6 ms                                                | 75.9 ms: 1.03x slower                                      |
| dulwich_log                      | 28.5 ms                                                | 29.6 ms: 1.04x slower                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 175 ms: 1.04x slower                                       |
| nqueens                          | 62.5 ms                                                | 65.2 ms: 1.04x slower                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.13 ms: 1.05x slower                                      |
| coverage                         | 46.0 ms                                                | 48.4 ms: 1.05x slower                                      |
| pathlib                          | 23.4 ms                                                | 24.8 ms: 1.06x slower                                      |
| mdp                              | 1.49 sec                                               | 1.64 sec: 1.10x slower                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 323 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 531 ms: 1.18x slower                                       |
| async_tree_none                  | 215 ms                                                 | 257 ms: 1.19x slower                                       |
| async_tree_memoization           | 268 ms                                                 | 335 ms: 1.25x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 676 ms: 1.32x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 672 ms: 1.35x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 649 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (6): tornado_http, pylint, xml_etree_parse, logging_silent, json_dumps, async_tree_eager_cpu_io_mixed
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 66.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.50x