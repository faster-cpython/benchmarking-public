# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a5
- machine: darwin-arm64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.022x faster
- HPT reliability: 79.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 176 ms: 1.04x slower                                       |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                     |
| sphinx         | 613 ms                                                 | 598 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 391 ms: 1.72x faster                                       |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                       |
| async_tree_io                    | 672 ms                                                 | 407 ms: 1.65x faster                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.55x faster                                       |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                       |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                       |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                      |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                       |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                       |
| async_tree_eager                 | 65.8 ms                                                | 69.9 ms: 1.06x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 187 ms: 1.32x slower                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 67.6 ms                                                | 65.0 ms: 1.04x faster                                      |
| float          | 54.1 ms                                                | 52.6 ms: 1.03x faster                                      |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                      |
| regex_compile  | 75.9 ms                                                | 73.5 ms: 1.03x faster                                      |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                       |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 50.6 ms: 1.10x faster                                      |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.09x faster                                       |
| xml_etree_iterparse  | 75.5 ms                                                | 70.7 ms: 1.07x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                       |
| xml_etree_process    | 38.9 ms                                                | 36.7 ms: 1.06x faster                                      |
| tomli_loads          | 1.36 sec                                               | 1.29 sec: 1.05x faster                                     |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                      |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.07x slower                                       |
| json_dumps           | 6.19 ms                                                | 7.53 ms: 1.22x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.8 ms: 1.03x faster                                      |
| python_startup         | 17.8 ms                                                | 17.5 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.49 ms: 1.15x faster                                      |
| genshi_text     | 14.7 ms                                                | 15.8 ms: 1.08x slower                                      |
| genshi_xml      | 30.5 ms                                                | 33.3 ms: 1.09x slower                                      |
| django_template | 19.7 ms                                                | 23.9 ms: 1.21x slower                                      |
| Geometric mean  | (ref)                                                  | 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.5 ms: 2.57x faster                                      |
| async_tree_io_tg                 | 673 ms                                                 | 391 ms: 1.72x faster                                       |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                       |
| async_tree_io                    | 672 ms                                                 | 407 ms: 1.65x faster                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.55x faster                                       |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                       |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                       |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                       |
| deepcopy                         | 226 us                                                 | 168 us: 1.34x faster                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                       |
| deepcopy_memo                    | 26.0 us                                                | 21.2 us: 1.23x faster                                      |
| mako                             | 7.44 ms                                                | 6.49 ms: 1.15x faster                                      |
| spectral_norm                    | 76.5 ms                                                | 66.9 ms: 1.14x faster                                      |
| deepcopy_reduce                  | 2.01 us                                                | 1.77 us: 1.14x faster                                      |
| bpe_tokeniser                    | 3.28 sec                                               | 2.88 sec: 1.14x faster                                     |
| scimark_fft                      | 194 ms                                                 | 172 ms: 1.13x faster                                       |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.12x faster                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.87 ms: 1.10x faster                                      |
| xml_etree_generate               | 55.4 ms                                                | 50.6 ms: 1.10x faster                                      |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                      |
| bench_mp_pool                    | 65.5 ms                                                | 60.3 ms: 1.09x faster                                      |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.09x faster                                       |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.07x faster                                      |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                       |
| xml_etree_iterparse              | 75.5 ms                                                | 70.7 ms: 1.07x faster                                      |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                       |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                      |
| xml_etree_process                | 38.9 ms                                                | 36.7 ms: 1.06x faster                                      |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                       |
| tomli_loads                      | 1.36 sec                                               | 1.29 sec: 1.05x faster                                     |
| go                               | 98.5 ms                                                | 94.2 ms: 1.04x faster                                      |
| nbody                            | 67.6 ms                                                | 65.0 ms: 1.04x faster                                      |
| regex_compile                    | 75.9 ms                                                | 73.5 ms: 1.03x faster                                      |
| python_startup_no_site           | 13.2 ms                                                | 12.8 ms: 1.03x faster                                      |
| generators                       | 29.4 ms                                                | 28.5 ms: 1.03x faster                                      |
| float                            | 54.1 ms                                                | 52.6 ms: 1.03x faster                                      |
| raytrace                         | 204 ms                                                 | 199 ms: 1.03x faster                                       |
| pyflate                          | 311 ms                                                 | 303 ms: 1.03x faster                                       |
| sphinx                           | 613 ms                                                 | 598 ms: 1.02x faster                                       |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                       |
| python_startup                   | 17.8 ms                                                | 17.5 ms: 1.02x faster                                      |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                       |
| thrift                           | 468 us                                                 | 461 us: 1.01x faster                                       |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.7 ms: 1.00x faster                                      |
| connected_components             | 300 ms                                                 | 299 ms: 1.00x faster                                       |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                       |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                       |
| dulwich_log                      | 29.2 ms                                                | 29.6 ms: 1.01x slower                                      |
| sympy_sum                        | 76.2 ms                                                | 78.4 ms: 1.03x slower                                      |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                     |
| logging_silent                   | 72.5 ns                                                | 75.6 ns: 1.04x slower                                      |
| 2to3                             | 168 ms                                                 | 176 ms: 1.04x slower                                       |
| sympy_str                        | 144 ms                                                 | 151 ms: 1.05x slower                                       |
| crypto_pyaes                     | 51.4 ms                                                | 53.9 ms: 1.05x slower                                      |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                      |
| chaos                            | 41.6 ms                                                | 43.8 ms: 1.05x slower                                      |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                      |
| mdp                              | 1.49 sec                                               | 1.58 sec: 1.06x slower                                     |
| pycparser                        | 673 ms                                                 | 713 ms: 1.06x slower                                       |
| async_tree_eager                 | 65.8 ms                                                | 69.9 ms: 1.06x slower                                      |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.07x slower                                       |
| pprint_pformat                   | 986 ms                                                 | 1.06 sec: 1.07x slower                                     |
| sqlglot_optimize                 | 33.2 ms                                                | 35.6 ms: 1.07x slower                                      |
| bench_thread_pool                | 483 us                                                 | 518 us: 1.07x slower                                       |
| pprint_safe_repr                 | 483 ms                                                 | 519 ms: 1.07x slower                                       |
| nqueens                          | 59.5 ms                                                | 64.0 ms: 1.08x slower                                      |
| scimark_sor                      | 85.8 ms                                                | 92.3 ms: 1.08x slower                                      |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.10 ms: 1.08x slower                                      |
| genshi_text                      | 14.7 ms                                                | 15.8 ms: 1.08x slower                                      |
| deltablue                        | 2.57 ms                                                | 2.77 ms: 1.08x slower                                      |
| fannkuch                         | 250 ms                                                 | 272 ms: 1.09x slower                                       |
| meteor_contest                   | 69.1 ms                                                | 75.0 ms: 1.09x slower                                      |
| sqlglot_normalize                | 180 ms                                                 | 196 ms: 1.09x slower                                       |
| genshi_xml                       | 30.5 ms                                                | 33.3 ms: 1.09x slower                                      |
| sqlglot_transpile                | 973 us                                                 | 1.06 ms: 1.09x slower                                      |
| sympy_expand                     | 233 ms                                                 | 256 ms: 1.10x slower                                       |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.10x slower                                      |
| sqlglot_parse                    | 808 us                                                 | 887 us: 1.10x slower                                       |
| typing_runtime_protocols         | 91.5 us                                                | 102 us: 1.11x slower                                       |
| scimark_monte_carlo              | 44.5 ms                                                | 49.4 ms: 1.11x slower                                      |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                      |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                      |
| scimark_lu                       | 73.5 ms                                                | 83.0 ms: 1.13x slower                                      |
| hexiom                           | 4.38 ms                                                | 4.97 ms: 1.14x slower                                      |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.15x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                       |
| many_optionals                   | 403 us                                                 | 470 us: 1.17x slower                                       |
| richards_super                   | 34.6 ms                                                | 41.7 ms: 1.21x slower                                      |
| django_template                  | 19.7 ms                                                | 23.9 ms: 1.21x slower                                      |
| json_dumps                       | 6.19 ms                                                | 7.53 ms: 1.22x slower                                      |
| richards                         | 30.6 ms                                                | 37.7 ms: 1.23x slower                                      |
| coverage                         | 38.5 ms                                                | 47.5 ms: 1.23x slower                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 187 ms: 1.32x slower                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (6): html5lib, shortest_path, logging_simple, sqlite_synth, json, logging_format
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 79.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x