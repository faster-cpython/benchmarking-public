# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.043x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 181 ms: 1.03x faster                                                  |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| html5lib       | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                 |
| sphinx         | 603 ms                                                 | 666 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.15x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 63.0 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 198 ms: 1.09x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                  |
| async_generators                 | 295 ms                                                 | 290 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 541 ms: 1.09x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 683 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.4 ms: 1.21x faster                                                 |
| nbody          | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 76.1 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                |
| unpickle_pure_python | 164 us                                                 | 131 us: 1.25x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 177 us: 1.21x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 34.3 ms: 1.19x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 49.4 ms: 1.15x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.10 ms: 1.07x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.1 ms: 1.01x slower                                                 |
| python_startup_no_site | 14.5 ms                                                | 14.8 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.41 ms: 1.20x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                 |
| django_template | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                                 |
| deepcopy                         | 237 us                                                 | 155 us: 1.53x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.25x faster                                                  |
| logging_silent                   | 70.1 ns                                                | 56.4 ns: 1.24x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 85.8 ms: 1.23x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 177 us: 1.21x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                 |
| float                            | 56.0 ms                                                | 46.4 ms: 1.21x faster                                                 |
| mako                             | 7.68 ms                                                | 6.41 ms: 1.20x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 64.1 ms: 1.20x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 34.3 ms: 1.19x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                                  |
| nbody                            | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.4 ms: 1.15x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 49.4 ms: 1.15x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.41 us: 1.14x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 45.1 ms: 1.12x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 63.0 ms: 1.11x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 68.7 ms: 1.11x faster                                                 |
| thrift                           | 466 us                                                 | 420 us: 1.11x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.42 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| nqueens                          | 62.5 ms                                                | 57.1 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 323 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 198 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| html5lib                         | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.08x faster                                                |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.10 ms: 1.07x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.07x faster                                                 |
| telco                            | 4.76 ms                                                | 4.50 ms: 1.06x faster                                                 |
| fannkuch                         | 284 ms                                                 | 269 ms: 1.06x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 506 ms: 1.05x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 480 us: 1.05x faster                                                  |
| json                             | 3.03 ms                                                | 2.89 ms: 1.05x faster                                                 |
| pathlib                          | 23.4 ms                                                | 22.3 ms: 1.05x faster                                                 |
| coverage                         | 46.0 ms                                                | 43.9 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.10 sec: 1.05x faster                                                |
| crypto_pyaes                     | 54.2 ms                                                | 51.9 ms: 1.04x faster                                                 |
| go                               | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                 |
| pycparser                        | 705 ms                                                 | 682 ms: 1.03x faster                                                  |
| 2to3                             | 187 ms                                                 | 181 ms: 1.03x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 76.1 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| async_generators                 | 295 ms                                                 | 290 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 187 ms: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 62.2 ms: 1.00x faster                                                 |
| chaos                            | 41.2 ms                                                | 41.0 ms: 1.00x faster                                                 |
| richards_super                   | 39.1 ms                                                | 39.0 ms: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.99 ms: 1.00x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.50 sec: 1.01x slower                                                |
| python_startup                   | 18.9 ms                                                | 19.1 ms: 1.01x slower                                                 |
| richards                         | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                 |
| hexiom                           | 4.86 ms                                                | 4.96 ms: 1.02x slower                                                 |
| python_startup_no_site           | 14.5 ms                                                | 14.8 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| sympy_str                        | 145 ms                                                 | 150 ms: 1.03x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 76.3 ms: 1.03x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| sympy_sum                        | 75.4 ms                                                | 78.3 ms: 1.04x slower                                                 |
| comprehensions                   | 12.3 us                                                | 12.8 us: 1.04x slower                                                 |
| raytrace                         | 181 ms                                                 | 191 ms: 1.05x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 37.5 ms: 1.07x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 541 ms: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| create_gc_cycles                 | 1.17 ms                                                | 1.29 ms: 1.10x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                 |
| sphinx                           | 603 ms                                                 | 666 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                  |
| pylint                           | 180 ms                                                 | 212 ms: 1.18x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 683 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, sympy_expand, gc_traversal, sqlglot_parse, asyncio_websockets, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x