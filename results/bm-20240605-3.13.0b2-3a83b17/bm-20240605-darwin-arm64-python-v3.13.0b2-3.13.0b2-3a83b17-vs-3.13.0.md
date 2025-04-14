# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 161 ms: 1.16x faster                                       |
| chameleon      | 5.08 ms                                                | 4.27 ms: 1.19x faster                                      |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 60.3 ms: 1.16x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.16x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.10x faster                                       |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 331 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                       |
| async_tree_none                  | 215 ms                                                 | 209 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 467 ms: 1.02x slower                                       |
| async_tree_io                    | 507 ms                                                 | 563 ms: 1.11x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 565 ms: 1.14x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 766 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 768 ms: 1.61x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.6 ms: 1.24x faster                                      |
| float          | 56.0 ms                                                | 48.6 ms: 1.15x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.5 ms: 1.15x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_v8       | 17.0 ms                                                | 17.3 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                       |
| unpickle_pure_python | 164 us                                                 | 141 us: 1.17x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 37.1 ms: 1.11x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 52.7 ms: 1.08x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.47 sec: 1.07x faster                                     |
| json_dumps           | 6.52 ms                                                | 6.23 ms: 1.05x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 71.5 ms: 1.03x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 15.2 ms: 1.25x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 12.3 ms: 1.18x faster                                      |
| Geometric mean         | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.21x faster                                      |
| genshi_xml      | 34.4 ms                                                | 29.9 ms: 1.15x faster                                      |
| django_template | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| mako            | 7.68 ms                                                | 6.99 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                             | 790 ms                                                 | 221 ms: 3.57x faster                                       |
| mypy2                            | 701 ms                                                 | 379 ms: 1.85x faster                                       |
| generators                       | 31.5 ms                                                | 22.9 ms: 1.37x faster                                      |
| bench_mp_pool                    | 62.5 ms                                                | 47.2 ms: 1.33x faster                                      |
| create_gc_cycles                 | 1.17 ms                                                | 897 us: 1.30x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.14 ms: 1.25x faster                                      |
| python_startup                   | 18.9 ms                                                | 15.2 ms: 1.25x faster                                      |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                      |
| nbody                            | 74.0 ms                                                | 59.6 ms: 1.24x faster                                      |
| raytrace                         | 181 ms                                                 | 147 ms: 1.23x faster                                       |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.21x faster                                      |
| chaos                            | 41.2 ms                                                | 34.0 ms: 1.21x faster                                      |
| deepcopy_memo                    | 27.4 us                                                | 22.6 us: 1.21x faster                                      |
| comprehensions                   | 12.3 us                                                | 10.2 us: 1.21x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                       |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                       |
| hexiom                           | 4.86 ms                                                | 4.06 ms: 1.20x faster                                      |
| nqueens                          | 62.5 ms                                                | 52.2 ms: 1.20x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.27 ms: 1.19x faster                                      |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 42.5 ms: 1.19x faster                                      |
| logging_simple                   | 3.60 us                                                | 3.04 us: 1.19x faster                                      |
| logging_format                   | 3.89 us                                                | 3.31 us: 1.18x faster                                      |
| python_startup_no_site           | 14.5 ms                                                | 12.3 ms: 1.18x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 732 us: 1.17x faster                                       |
| unpickle_pure_python             | 164 us                                                 | 141 us: 1.17x faster                                       |
| logging_silent                   | 70.1 ns                                                | 60.1 ns: 1.17x faster                                      |
| 2to3                             | 187 ms                                                 | 161 ms: 1.16x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 60.3 ms: 1.16x faster                                      |
| deepcopy                         | 237 us                                                 | 204 us: 1.16x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 87.6 us: 1.16x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.16x faster                                      |
| float                            | 56.0 ms                                                | 48.6 ms: 1.15x faster                                      |
| spectral_norm                    | 76.3 ms                                                | 66.4 ms: 1.15x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 29.9 ms: 1.15x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 891 us: 1.15x faster                                       |
| pprint_safe_repr                 | 533 ms                                                 | 465 ms: 1.15x faster                                       |
| regex_compile                    | 78.6 ms                                                | 68.5 ms: 1.15x faster                                      |
| scimark_lu                       | 76.7 ms                                                | 66.9 ms: 1.15x faster                                      |
| django_template                  | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 947 ms: 1.14x faster                                       |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                       |
| fannkuch                         | 284 ms                                                 | 248 ms: 1.14x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                       |
| deepcopy_reduce                  | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 30.9 ms: 1.13x faster                                      |
| bench_thread_pool                | 505 us                                                 | 447 us: 1.13x faster                                       |
| pycparser                        | 705 ms                                                 | 632 ms: 1.12x faster                                       |
| scimark_sor                      | 105 ms                                                 | 94.9 ms: 1.11x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.2 ms: 1.11x faster                                      |
| scimark_fft                      | 201 ms                                                 | 181 ms: 1.11x faster                                       |
| xml_etree_process                | 41.0 ms                                                | 37.1 ms: 1.11x faster                                      |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                       |
| richards                         | 35.2 ms                                                | 31.8 ms: 1.11x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                       |
| mako                             | 7.68 ms                                                | 6.99 ms: 1.10x faster                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.10x faster                                       |
| crypto_pyaes                     | 54.2 ms                                                | 49.5 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 321 ms: 1.10x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                      |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                       |
| sympy_sum                        | 75.4 ms                                                | 69.2 ms: 1.09x faster                                      |
| xml_etree_generate               | 57.0 ms                                                | 52.7 ms: 1.08x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.77 ms: 1.08x faster                                      |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                       |
| tomli_loads                      | 1.57 sec                                               | 1.47 sec: 1.07x faster                                     |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.06x faster                                     |
| meteor_contest                   | 74.0 ms                                                | 70.3 ms: 1.05x faster                                      |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 331 ms: 1.05x faster                                       |
| json_dumps                       | 6.52 ms                                                | 6.23 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                       |
| telco                            | 4.76 ms                                                | 4.60 ms: 1.04x faster                                      |
| json                             | 3.03 ms                                                | 2.93 ms: 1.03x faster                                      |
| dulwich_log                      | 28.5 ms                                                | 27.6 ms: 1.03x faster                                      |
| async_tree_none                  | 215 ms                                                 | 209 ms: 1.03x faster                                       |
| xml_etree_iterparse              | 73.6 ms                                                | 71.5 ms: 1.03x faster                                      |
| coverage                         | 46.0 ms                                                | 45.0 ms: 1.02x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| xml_etree_parse                  | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| json_loads                       | 17.0 us                                                | 16.8 us: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 467 ms: 1.02x slower                                       |
| regex_v8                         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                      |
| mdp                              | 1.49 sec                                               | 1.53 sec: 1.03x slower                                     |
| async_tree_io                    | 507 ms                                                 | 563 ms: 1.11x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 565 ms: 1.14x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 766 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 768 ms: 1.61x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                               |

Benchmark hidden because not significant (8): tornado_http, pylint, async_tree_memoization, pathlib, async_tree_none_tg, docutils, regex_dna, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.107x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.93x