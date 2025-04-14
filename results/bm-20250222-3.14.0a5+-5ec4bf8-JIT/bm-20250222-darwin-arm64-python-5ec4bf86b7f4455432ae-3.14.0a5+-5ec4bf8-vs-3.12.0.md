# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 166 ms: 1.02x faster                                                   |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                  |
| sphinx         | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 371 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 420 ms: 1.26x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 62.8 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 176 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.4 ms: 1.14x faster                                                  |
| nbody          | 67.6 ms                                                | 64.6 ms: 1.05x faster                                                  |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.9 ms: 1.10x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 50.8 ms: 1.09x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.8 ms: 1.09x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.23 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| python_startup         | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.47 ms: 1.15x faster                                                  |
| genshi_text     | 14.7 ms                                                | 13.9 ms: 1.05x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 29.2 ms: 1.05x faster                                                  |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.0 ms: 2.67x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 371 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| deepcopy                         | 226 us                                                 | 151 us: 1.50x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.2 us: 1.43x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| generators                       | 29.4 ms                                                | 23.3 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 420 ms: 1.26x faster                                                   |
| comprehensions                   | 14.0 us                                                | 11.4 us: 1.22x faster                                                  |
| go                               | 98.5 ms                                                | 81.0 ms: 1.22x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| mako                             | 7.44 ms                                                | 6.47 ms: 1.15x faster                                                  |
| raytrace                         | 204 ms                                                 | 178 ms: 1.15x faster                                                   |
| float                            | 54.1 ms                                                | 47.4 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                   |
| html5lib                         | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.23 us: 1.11x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.94 sec: 1.11x faster                                                 |
| logging_silent                   | 72.5 ns                                                | 65.1 ns: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 68.9 ms: 1.10x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.54 us: 1.10x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 50.8 ms: 1.09x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 35.8 ms: 1.09x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.08x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.37 ms: 1.08x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 60.8 ms: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 79.8 ms: 1.07x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 71.2 ms: 1.07x faster                                                  |
| thrift                           | 468 us                                                 | 437 us: 1.07x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 182 ms: 1.07x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                  |
| sphinx                           | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| chaos                            | 41.6 ms                                                | 39.2 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.96 ms: 1.06x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.9 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.7 ms: 1.05x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 62.8 ms: 1.05x faster                                                  |
| nbody                            | 67.6 ms                                                | 64.6 ms: 1.05x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 29.2 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.1 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 73.7 ms: 1.03x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 43.3 ms: 1.03x faster                                                  |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| nqueens                          | 59.5 ms                                                | 58.4 ms: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| 2to3                             | 168 ms                                                 | 166 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| pyflate                          | 311 ms                                                 | 307 ms: 1.01x faster                                                   |
| pprint_pformat                   | 986 ms                                                 | 977 ms: 1.01x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| scimark_lu                       | 73.5 ms                                                | 73.2 ms: 1.00x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 33.1 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| sqlglot_normalize                | 180 ms                                                 | 180 ms: 1.00x slower                                                   |
| connected_components             | 300 ms                                                 | 301 ms: 1.00x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 92.2 us: 1.01x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 488 ms: 1.01x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.67 ms: 1.01x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 490 us: 1.01x slower                                                   |
| shortest_path                    | 331 ms                                                 | 338 ms: 1.02x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 239 ms: 1.02x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| richards_super                   | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                  |
| richards                         | 30.6 ms                                                | 32.1 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.03 ms: 1.06x slower                                                  |
| sqlglot_parse                    | 808 us                                                 | 861 us: 1.07x slower                                                   |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 55.3 ms: 1.08x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 74.8 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.10x slower                                                  |
| many_optionals                   | 403 us                                                 | 453 us: 1.12x slower                                                   |
| fannkuch                         | 250 ms                                                 | 282 ms: 1.13x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| telco                            | 3.92 ms                                                | 4.52 ms: 1.15x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.23 ms: 1.17x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.0 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 176 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (6): json, asyncio_websockets, hexiom, pickle_pure_python, sqlite_synth, pycparser
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x