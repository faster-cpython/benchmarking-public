# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: darwin-arm64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 162 ms: 1.15x faster                                         |
| chameleon      | 5.08 ms                                                | 4.37 ms: 1.16x faster                                        |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                       |
| html5lib       | 36.6 ms                                                | 31.9 ms: 1.15x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                         |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                        |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                        |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                         |
| async_generators                 | 295 ms                                                 | 285 ms: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                         |
| async_tree_io                    | 507 ms                                                 | 559 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 497 ms                                                 | 557 ms: 1.12x slower                                         |
| async_tree_eager_io              | 514 ms                                                 | 767 ms: 1.49x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 772 ms: 1.62x slower                                         |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                 |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 60.6 ms: 1.22x faster                                        |
| float          | 56.0 ms                                                | 48.3 ms: 1.16x faster                                        |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.8 ms: 1.14x faster                                        |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                        |
| regex_dna      | 149 ms                                                 | 149 ms: 1.00x faster                                         |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 182 us: 1.18x faster                                         |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.16x faster                                         |
| xml_etree_process    | 41.0 ms                                                | 37.6 ms: 1.09x faster                                        |
| tomli_loads          | 1.57 sec                                               | 1.46 sec: 1.08x faster                                       |
| xml_etree_generate   | 57.0 ms                                                | 53.1 ms: 1.07x faster                                        |
| json_dumps           | 6.52 ms                                                | 6.31 ms: 1.03x faster                                        |
| json_loads           | 17.0 us                                                | 16.7 us: 1.01x faster                                        |
| xml_etree_iterparse  | 73.6 ms                                                | 73.0 ms: 1.01x faster                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 17.2 ms: 1.10x faster                                        |
| python_startup_no_site | 14.5 ms                                                | 13.7 ms: 1.05x faster                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                        |
| genshi_xml      | 34.4 ms                                                | 30.2 ms: 1.14x faster                                        |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                        |
| mako            | 7.68 ms                                                | 7.08 ms: 1.08x faster                                        |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| dask                             | 790 ms                                                 | 234 ms: 3.37x faster                                         |
| mypy2                            | 701 ms                                                 | 479 ms: 1.46x faster                                         |
| generators                       | 31.5 ms                                                | 22.9 ms: 1.37x faster                                        |
| create_gc_cycles                 | 1.17 ms                                                | 898 us: 1.30x faster                                         |
| bench_mp_pool                    | 62.5 ms                                                | 49.0 ms: 1.28x faster                                        |
| deltablue                        | 2.68 ms                                                | 2.16 ms: 1.24x faster                                        |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| nbody                            | 74.0 ms                                                | 60.6 ms: 1.22x faster                                        |
| raytrace                         | 181 ms                                                 | 149 ms: 1.22x faster                                         |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                         |
| chaos                            | 41.2 ms                                                | 34.4 ms: 1.20x faster                                        |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                        |
| deepcopy_memo                    | 27.4 us                                                | 23.0 us: 1.19x faster                                        |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                        |
| nqueens                          | 62.5 ms                                                | 52.9 ms: 1.18x faster                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 42.8 ms: 1.18x faster                                        |
| pickle_pure_python               | 214 us                                                 | 182 us: 1.18x faster                                         |
| hexiom                           | 4.86 ms                                                | 4.16 ms: 1.17x faster                                        |
| chameleon                        | 5.08 ms                                                | 4.37 ms: 1.16x faster                                        |
| float                            | 56.0 ms                                                | 48.3 ms: 1.16x faster                                        |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                         |
| deepcopy                         | 237 us                                                 | 204 us: 1.16x faster                                         |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.16x faster                                         |
| comprehensions                   | 12.3 us                                                | 10.6 us: 1.16x faster                                        |
| logging_silent                   | 70.1 ns                                                | 60.7 ns: 1.15x faster                                        |
| 2to3                             | 187 ms                                                 | 162 ms: 1.15x faster                                         |
| logging_simple                   | 3.60 us                                                | 3.12 us: 1.15x faster                                        |
| logging_format                   | 3.89 us                                                | 3.39 us: 1.15x faster                                        |
| html5lib                         | 36.6 ms                                                | 31.9 ms: 1.15x faster                                        |
| regex_compile                    | 78.6 ms                                                | 68.8 ms: 1.14x faster                                        |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                        |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                         |
| genshi_xml                       | 34.4 ms                                                | 30.2 ms: 1.14x faster                                        |
| pprint_safe_repr                 | 533 ms                                                 | 468 ms: 1.14x faster                                         |
| spectral_norm                    | 76.3 ms                                                | 67.0 ms: 1.14x faster                                        |
| pprint_pformat                   | 1.08 sec                                               | 953 ms: 1.14x faster                                         |
| sqlglot_transpile                | 1.02 ms                                                | 899 us: 1.14x faster                                         |
| deepcopy_reduce                  | 2.07 us                                                | 1.82 us: 1.14x faster                                        |
| scimark_lu                       | 76.7 ms                                                | 67.6 ms: 1.13x faster                                        |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                        |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                        |
| typing_runtime_protocols         | 101 us                                                 | 89.7 us: 1.13x faster                                        |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.12x faster                                         |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                        |
| richards                         | 35.2 ms                                                | 31.5 ms: 1.12x faster                                        |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                        |
| fannkuch                         | 284 ms                                                 | 257 ms: 1.10x faster                                         |
| scimark_sor                      | 105 ms                                                 | 95.5 ms: 1.10x faster                                        |
| python_startup                   | 18.9 ms                                                | 17.2 ms: 1.10x faster                                        |
| pycparser                        | 705 ms                                                 | 641 ms: 1.10x faster                                         |
| bench_thread_pool                | 505 us                                                 | 460 us: 1.10x faster                                         |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                         |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                         |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                         |
| xml_etree_process                | 41.0 ms                                                | 37.6 ms: 1.09x faster                                        |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                        |
| crypto_pyaes                     | 54.2 ms                                                | 49.9 ms: 1.09x faster                                        |
| mako                             | 7.68 ms                                                | 7.08 ms: 1.08x faster                                        |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                         |
| sympy_sum                        | 75.4 ms                                                | 69.8 ms: 1.08x faster                                        |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| tomli_loads                      | 1.57 sec                                               | 1.46 sec: 1.08x faster                                       |
| xml_etree_generate               | 57.0 ms                                                | 53.1 ms: 1.07x faster                                        |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                         |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.81 ms: 1.06x faster                                        |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                       |
| python_startup_no_site           | 14.5 ms                                                | 13.7 ms: 1.05x faster                                        |
| mdp                              | 1.49 sec                                               | 1.42 sec: 1.05x faster                                       |
| dulwich_log                      | 28.5 ms                                                | 27.3 ms: 1.04x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                         |
| async_generators                 | 295 ms                                                 | 285 ms: 1.04x faster                                         |
| json_dumps                       | 6.52 ms                                                | 6.31 ms: 1.03x faster                                        |
| meteor_contest                   | 74.0 ms                                                | 71.6 ms: 1.03x faster                                        |
| coverage                         | 46.0 ms                                                | 44.7 ms: 1.03x faster                                        |
| json                             | 3.03 ms                                                | 2.95 ms: 1.03x faster                                        |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.02x faster                                         |
| telco                            | 4.76 ms                                                | 4.69 ms: 1.02x faster                                        |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.01x faster                                        |
| xml_etree_iterparse              | 73.6 ms                                                | 73.0 ms: 1.01x faster                                        |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                        |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                         |
| regex_dna                        | 149 ms                                                 | 149 ms: 1.00x faster                                         |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                       |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                         |
| pathlib                          | 23.4 ms                                                | 24.6 ms: 1.05x slower                                        |
| async_tree_io                    | 507 ms                                                 | 559 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 497 ms                                                 | 557 ms: 1.12x slower                                         |
| async_tree_eager_io              | 514 ms                                                 | 767 ms: 1.49x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 772 ms: 1.62x slower                                         |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, pylint, async_tree_none_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, tornado_http
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.092x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.45x