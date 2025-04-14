# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.012x slower
- HPT reliability: 98.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 177 ms: 1.05x slower                                                   |
| docutils       | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                 |
| html5lib       | 33.4 ms                                                | 34.0 ms: 1.02x slower                                                  |
| sphinx         | 613 ms                                                 | 606 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 398 ms: 1.69x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 398 ms: 1.68x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 417 ms: 1.61x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 407 ms: 1.52x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 214 ms: 1.49x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 217 ms: 1.43x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                   |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.6 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 69.8 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 191 ms: 1.35x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.06x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 92.1 ms: 1.36x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_compile  | 75.9 ms                                                | 77.8 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.8 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 74.9 ms: 1.01x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 58.2 ms: 1.05x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 42.7 ms: 1.10x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 169 us: 1.16x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 230 us: 1.17x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.57 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| python_startup         | 17.8 ms                                                | 18.2 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.12 ms: 1.09x slower                                                  |
| genshi_xml      | 30.5 ms                                                | 34.0 ms: 1.12x slower                                                  |
| genshi_text     | 14.7 ms                                                | 16.4 ms: 1.12x slower                                                  |
| django_template | 19.7 ms                                                | 24.2 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.0 ms: 2.48x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 398 ms: 1.69x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 398 ms: 1.68x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 417 ms: 1.61x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 407 ms: 1.52x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 214 ms: 1.49x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 217 ms: 1.43x faster                                                   |
| deepcopy                         | 226 us                                                 | 168 us: 1.34x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 21.0 us: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.14x faster                                                  |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 60.8 ms: 1.08x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| pylint                           | 182 ms                                                 | 171 ms: 1.06x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.6 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| go                               | 98.5 ms                                                | 94.8 ms: 1.04x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                                  |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.23 sec: 1.02x faster                                                 |
| thrift                           | 468 us                                                 | 461 us: 1.01x faster                                                   |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                   |
| generators                       | 29.4 ms                                                | 29.0 ms: 1.01x faster                                                  |
| sphinx                           | 613 ms                                                 | 606 ms: 1.01x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 74.9 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| logging_silent                   | 72.5 ns                                                | 73.0 ns: 1.01x slower                                                  |
| dulwich_log                      | 29.2 ms                                                | 29.4 ms: 1.01x slower                                                  |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 197 ms: 1.02x slower                                                   |
| spectral_norm                    | 76.5 ms                                                | 77.8 ms: 1.02x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.0 ms: 1.02x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 77.8 ms: 1.02x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.2 ms: 1.03x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.01 us: 1.03x slower                                                  |
| logging_simple                   | 3.60 us                                                | 3.71 us: 1.03x slower                                                  |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                   |
| sympy_sum                        | 76.2 ms                                                | 79.4 ms: 1.04x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| pycparser                        | 673 ms                                                 | 704 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 58.2 ms: 1.05x slower                                                  |
| 2to3                             | 168 ms                                                 | 177 ms: 1.05x slower                                                   |
| connected_components             | 300 ms                                                 | 316 ms: 1.05x slower                                                   |
| shortest_path                    | 331 ms                                                 | 348 ms: 1.05x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 69.8 ms: 1.06x slower                                                  |
| chaos                            | 41.6 ms                                                | 44.3 ms: 1.06x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.02 ms: 1.06x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                 |
| sympy_str                        | 144 ms                                                 | 153 ms: 1.07x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 92.4 ms: 1.08x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.06 sec: 1.08x slower                                                 |
| sqlglot_optimize                 | 33.2 ms                                                | 36.0 ms: 1.08x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 525 us: 1.09x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 527 ms: 1.09x slower                                                   |
| mako                             | 7.44 ms                                                | 8.12 ms: 1.09x slower                                                  |
| nqueens                          | 59.5 ms                                                | 65.0 ms: 1.09x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.80 ms: 1.09x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 42.7 ms: 1.10x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 258 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 199 ms: 1.11x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 896 us: 1.11x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.8 ms: 1.11x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 34.0 ms: 1.12x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 16.4 ms: 1.12x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 77.6 ms: 1.12x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 50.0 ms: 1.12x slower                                                  |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 104 us: 1.13x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 83.3 ms: 1.13x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.11 ms: 1.14x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 58.5 ms: 1.14x slower                                                  |
| many_optionals                   | 403 us                                                 | 467 us: 1.16x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 169 us: 1.16x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 230 us: 1.17x slower                                                   |
| fannkuch                         | 250 ms                                                 | 298 ms: 1.19x slower                                                   |
| hexiom                           | 4.38 ms                                                | 5.26 ms: 1.20x slower                                                  |
| telco                            | 3.92 ms                                                | 4.74 ms: 1.21x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.57 ms: 1.22x slower                                                  |
| django_template                  | 19.7 ms                                                | 24.2 ms: 1.23x slower                                                  |
| richards_super                   | 34.6 ms                                                | 42.8 ms: 1.24x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.9 ms: 1.24x slower                                                  |
| richards                         | 30.6 ms                                                | 38.6 ms: 1.26x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 191 ms: 1.35x slower                                                   |
| nbody                            | 67.6 ms                                                | 92.1 ms: 1.36x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.06x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, sqlalchemy_declarative, float
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 98.68% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x