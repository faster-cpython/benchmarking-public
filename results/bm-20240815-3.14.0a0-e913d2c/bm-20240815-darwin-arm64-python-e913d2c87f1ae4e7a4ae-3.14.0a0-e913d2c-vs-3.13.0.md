# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: darwin-arm64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                |
| html5lib       | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 229 ms: 1.25x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 63.0 ms: 1.11x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                  |
| async_generators                 | 295 ms                                                 | 282 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                  |
| async_tree_io                    | 507 ms                                                 | 550 ms: 1.09x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 543 ms: 1.09x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 643 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.5 ms: 1.24x faster                                                 |
| float          | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 69.2 ms: 1.14x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 187 us: 1.15x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 145 us: 1.13x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 38.6 ms: 1.06x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 54.0 ms: 1.06x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                |
| json_loads           | 17.0 us                                                | 17.2 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 74.8 ms: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.4 ms: 1.15x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.4 ms: 1.08x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.6 ms: 1.12x faster                                                 |
| django_template | 22.2 ms                                                | 20.2 ms: 1.10x faster                                                 |
| mako            | 7.68 ms                                                | 7.20 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 148 us: 1.60x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 17.4 us: 1.57x faster                                                 |
| generators                       | 31.5 ms                                                | 20.7 ms: 1.52x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 896 us: 1.30x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.8 ms: 1.28x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 229 ms: 1.25x faster                                                  |
| nbody                            | 74.0 ms                                                | 59.5 ms: 1.24x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.24x faster                                                 |
| raytrace                         | 181 ms                                                 | 149 ms: 1.21x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.14 ms: 1.18x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.48 ms: 1.17x faster                                                 |
| go                               | 115 ms                                                 | 98.1 ms: 1.17x faster                                                 |
| nqueens                          | 62.5 ms                                                | 53.4 ms: 1.17x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                                 |
| chaos                            | 41.2 ms                                                | 35.5 ms: 1.16x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.5 ms: 1.16x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.4 ms: 1.15x faster                                                 |
| float                            | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 187 us: 1.15x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.39 us: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 746 us: 1.15x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 69.2 ms: 1.14x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 62.0 ns: 1.13x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 145 us: 1.13x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 67.9 ms: 1.13x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 93.6 ms: 1.13x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 448 us: 1.13x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.6 ms: 1.12x faster                                                 |
| comprehensions                   | 12.3 us                                                | 10.9 us: 1.12x faster                                                 |
| richards_super                   | 39.1 ms                                                | 34.9 ms: 1.12x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 913 us: 1.12x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 68.1 ms: 1.12x faster                                                 |
| richards                         | 35.2 ms                                                | 31.7 ms: 1.11x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 63.0 ms: 1.11x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 481 ms: 1.11x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 980 ms: 1.11x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                  |
| pycparser                        | 705 ms                                                 | 640 ms: 1.10x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.2 ms: 1.10x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 173 ms: 1.09x faster                                                  |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 32.2 ms: 1.08x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.4 ms: 1.08x faster                                                 |
| fannkuch                         | 284 ms                                                 | 262 ms: 1.08x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 432 us: 1.08x faster                                                  |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 50.6 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.6 ms: 1.07x faster                                                 |
| mako                             | 7.68 ms                                                | 7.20 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 38.6 ms: 1.06x faster                                                 |
| dulwich_log                      | 28.5 ms                                                | 27.0 ms: 1.06x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 54.0 ms: 1.06x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 233 ms: 1.05x faster                                                  |
| sympy_sum                        | 75.4 ms                                                | 71.5 ms: 1.05x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 96.2 us: 1.05x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                |
| async_generators                 | 295 ms                                                 | 282 ms: 1.05x faster                                                  |
| telco                            | 4.76 ms                                                | 4.59 ms: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.13 sec: 1.04x faster                                                |
| mdp                              | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| json                             | 3.03 ms                                                | 2.96 ms: 1.02x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                  |
| coverage                         | 46.0 ms                                                | 45.2 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| 2to3                             | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.2 us: 1.01x slower                                                 |
| xml_etree_iterparse              | 73.6 ms                                                | 74.8 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                |
| async_tree_io                    | 507 ms                                                 | 550 ms: 1.09x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 543 ms: 1.09x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 643 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, json_dumps, pathlib, pylint, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.084x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.64x