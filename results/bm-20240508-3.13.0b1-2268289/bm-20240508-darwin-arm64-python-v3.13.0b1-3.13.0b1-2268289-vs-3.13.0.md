# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: darwin-arm64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 179 ms: 1.05x faster                                       |
| chameleon      | 5.08 ms                                                | 4.35 ms: 1.17x faster                                      |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.15x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 61.0 ms: 1.15x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                       |
| async_generators                 | 295 ms                                                 | 278 ms: 1.06x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 333 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                       |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.02x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| async_tree_io                    | 507 ms                                                 | 570 ms: 1.12x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 564 ms: 1.14x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 772 ms: 1.50x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 755 ms: 1.58x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.0 ms                                                | 49.0 ms: 1.14x faster                                      |
| nbody          | 74.0 ms                                                | 65.7 ms: 1.13x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.2 ms: 1.15x faster                                      |
| regex_dna      | 149 ms                                                 | 139 ms: 1.07x faster                                       |
| regex_effbot   | 2.63 ms                                                | 2.55 ms: 1.03x faster                                      |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 181 us: 1.18x faster                                       |
| unpickle_pure_python | 164 us                                                 | 141 us: 1.16x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 37.1 ms: 1.11x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 51.8 ms: 1.10x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 97.6 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 67.5 ms: 1.09x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.45 sec: 1.08x faster                                     |
| json_dumps           | 6.52 ms                                                | 6.35 ms: 1.03x faster                                      |
| json_loads           | 17.0 us                                                | 17.3 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 14.3 ms: 1.32x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 11.6 ms: 1.25x faster                                      |
| Geometric mean         | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| django_template | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| genshi_xml      | 34.4 ms                                                | 30.0 ms: 1.15x faster                                      |
| mako            | 7.68 ms                                                | 6.88 ms: 1.12x faster                                      |
| Geometric mean  | (ref)                                                  | 1.16x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                             | 790 ms                                                 | 219 ms: 3.61x faster                                       |
| mypy2                            | 701 ms                                                 | 461 ms: 1.52x faster                                       |
| generators                       | 31.5 ms                                                | 22.7 ms: 1.39x faster                                      |
| bench_mp_pool                    | 62.5 ms                                                | 45.2 ms: 1.38x faster                                      |
| create_gc_cycles                 | 1.17 ms                                                | 884 us: 1.32x faster                                       |
| python_startup                   | 18.9 ms                                                | 14.3 ms: 1.32x faster                                      |
| python_startup_no_site           | 14.5 ms                                                | 11.6 ms: 1.25x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                      |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                      |
| deepcopy_memo                    | 27.4 us                                                | 22.4 us: 1.22x faster                                      |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| raytrace                         | 181 ms                                                 | 150 ms: 1.21x faster                                       |
| hexiom                           | 4.86 ms                                                | 4.09 ms: 1.19x faster                                      |
| nqueens                          | 62.5 ms                                                | 52.8 ms: 1.18x faster                                      |
| pickle_pure_python               | 214 us                                                 | 181 us: 1.18x faster                                       |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                      |
| logging_simple                   | 3.60 us                                                | 3.06 us: 1.18x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                       |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 43.0 ms: 1.17x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.35 ms: 1.17x faster                                      |
| logging_silent                   | 70.1 ns                                                | 60.1 ns: 1.17x faster                                      |
| deepcopy                         | 237 us                                                 | 203 us: 1.16x faster                                       |
| unpickle_pure_python             | 164 us                                                 | 141 us: 1.16x faster                                       |
| logging_format                   | 3.89 us                                                | 3.36 us: 1.16x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                       |
| deepcopy_reduce                  | 2.07 us                                                | 1.79 us: 1.15x faster                                      |
| regex_compile                    | 78.6 ms                                                | 68.2 ms: 1.15x faster                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.15x faster                                      |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 61.0 ms: 1.15x faster                                      |
| chaos                            | 41.2 ms                                                | 35.9 ms: 1.15x faster                                      |
| django_template                  | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 30.0 ms: 1.15x faster                                      |
| float                            | 56.0 ms                                                | 49.0 ms: 1.14x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 947 ms: 1.14x faster                                       |
| pprint_safe_repr                 | 533 ms                                                 | 468 ms: 1.14x faster                                       |
| sqlglot_transpile                | 1.02 ms                                                | 897 us: 1.14x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                       |
| comprehensions                   | 12.3 us                                                | 10.9 us: 1.13x faster                                      |
| fannkuch                         | 284 ms                                                 | 252 ms: 1.13x faster                                       |
| nbody                            | 74.0 ms                                                | 65.7 ms: 1.13x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                      |
| scimark_lu                       | 76.7 ms                                                | 68.3 ms: 1.12x faster                                      |
| pycparser                        | 705 ms                                                 | 630 ms: 1.12x faster                                       |
| spectral_norm                    | 76.3 ms                                                | 68.2 ms: 1.12x faster                                      |
| mako                             | 7.68 ms                                                | 6.88 ms: 1.12x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.2 ms: 1.11x faster                                      |
| xml_etree_process                | 41.0 ms                                                | 37.1 ms: 1.11x faster                                      |
| richards                         | 35.2 ms                                                | 31.9 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 319 ms: 1.10x faster                                       |
| xml_etree_generate               | 57.0 ms                                                | 51.8 ms: 1.10x faster                                      |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.10x faster                                       |
| xml_etree_parse                  | 107 ms                                                 | 97.6 ms: 1.10x faster                                      |
| scimark_sor                      | 105 ms                                                 | 96.3 ms: 1.10x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 92.5 us: 1.09x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                      |
| xml_etree_iterparse              | 73.6 ms                                                | 67.5 ms: 1.09x faster                                      |
| bench_thread_pool                | 505 us                                                 | 464 us: 1.09x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                       |
| tomli_loads                      | 1.57 sec                                               | 1.45 sec: 1.08x faster                                     |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                       |
| crypto_pyaes                     | 54.2 ms                                                | 50.3 ms: 1.08x faster                                      |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                       |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.07x faster                                       |
| sympy_sum                        | 75.4 ms                                                | 70.2 ms: 1.07x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.06x faster                                      |
| async_generators                 | 295 ms                                                 | 278 ms: 1.06x faster                                       |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                       |
| meteor_contest                   | 74.0 ms                                                | 70.6 ms: 1.05x faster                                      |
| 2to3                             | 187 ms                                                 | 179 ms: 1.05x faster                                       |
| telco                            | 4.76 ms                                                | 4.56 ms: 1.04x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 333 ms: 1.04x faster                                       |
| dulwich_log                      | 28.5 ms                                                | 27.3 ms: 1.04x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                       |
| pathlib                          | 23.4 ms                                                | 22.7 ms: 1.03x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.55 ms: 1.03x faster                                      |
| json_dumps                       | 6.52 ms                                                | 6.35 ms: 1.03x faster                                      |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.02x faster                                       |
| json                             | 3.03 ms                                                | 2.99 ms: 1.01x faster                                      |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| mdp                              | 1.49 sec                                               | 1.50 sec: 1.00x slower                                     |
| coverage                         | 46.0 ms                                                | 46.5 ms: 1.01x slower                                      |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| json_loads                       | 17.0 us                                                | 17.3 us: 1.02x slower                                      |
| async_tree_io                    | 507 ms                                                 | 570 ms: 1.12x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 564 ms: 1.14x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 772 ms: 1.50x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 755 ms: 1.58x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                               |

Benchmark hidden because not significant (5): tornado_http, pylint, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.101x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 0.92x