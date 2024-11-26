# Results vs. 3.13.0

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.046x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 176 ms: 1.07x faster                                                      |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                    |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 259 ms: 1.11x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 64.7 ms: 1.08x faster                                                     |
| async_tree_memoization           | 268 ms                                                 | 248 ms: 1.08x faster                                                      |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.03x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 534 ms: 1.07x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 683 ms: 1.33x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 707 ms: 1.48x slower                                                      |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.6 ms: 1.20x faster                                                     |
| nbody          | 74.0 ms                                                | 63.3 ms: 1.17x faster                                                     |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                     |
| regex_compile  | 78.6 ms                                                | 73.9 ms: 1.06x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                     |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                    |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.25x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 177 us: 1.21x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 34.8 ms: 1.18x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                | 51.2 ms: 1.11x faster                                                     |
| json_dumps           | 6.52 ms                                                | 6.36 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 73.6 ms                                                | 72.3 ms: 1.02x faster                                                     |
| json_loads           | 17.0 us                                                | 17.1 us: 1.01x slower                                                     |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 17.4 ms: 1.09x faster                                                     |
| python_startup_no_site | 14.5 ms                                                | 14.2 ms: 1.02x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                     |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 40.4 ms: 1.18x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.2 us: 1.69x faster                                                     |
| deepcopy                         | 237 us                                                 | 155 us: 1.53x faster                                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                     |
| create_gc_cycles                 | 1.17 ms                                                | 903 us: 1.29x faster                                                      |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                    |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.25x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 177 us: 1.21x faster                                                      |
| float                            | 56.0 ms                                                | 46.6 ms: 1.20x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.01 us: 1.20x faster                                                     |
| bench_mp_pool                    | 62.5 ms                                                | 52.2 ms: 1.20x faster                                                     |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                     |
| scimark_sor                      | 105 ms                                                 | 88.9 ms: 1.19x faster                                                     |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.30 us: 1.18x faster                                                     |
| xml_etree_process                | 41.0 ms                                                | 34.8 ms: 1.18x faster                                                     |
| scimark_lu                       | 76.7 ms                                                | 65.2 ms: 1.18x faster                                                     |
| nbody                            | 74.0 ms                                                | 63.3 ms: 1.17x faster                                                     |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                                     |
| logging_silent                   | 70.1 ns                                                | 62.5 ns: 1.12x faster                                                     |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| spectral_norm                    | 76.3 ms                                                | 68.1 ms: 1.12x faster                                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 259 ms: 1.11x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                      |
| xml_etree_generate               | 57.0 ms                                                | 51.2 ms: 1.11x faster                                                     |
| thrift                           | 466 us                                                 | 428 us: 1.09x faster                                                      |
| python_startup                   | 18.9 ms                                                | 17.4 ms: 1.09x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 64.7 ms: 1.08x faster                                                     |
| async_tree_memoization           | 268 ms                                                 | 248 ms: 1.08x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 94.0 us: 1.08x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| nqueens                          | 62.5 ms                                                | 58.3 ms: 1.07x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                     |
| 2to3                             | 187 ms                                                 | 176 ms: 1.07x faster                                                      |
| regex_compile                    | 78.6 ms                                                | 73.9 ms: 1.06x faster                                                     |
| pyflate                          | 351 ms                                                 | 331 ms: 1.06x faster                                                      |
| fannkuch                         | 284 ms                                                 | 267 ms: 1.06x faster                                                      |
| pprint_safe_repr                 | 533 ms                                                 | 503 ms: 1.06x faster                                                      |
| bench_thread_pool                | 505 us                                                 | 477 us: 1.06x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.03 sec: 1.05x faster                                                    |
| bpe_tokeniser                    | 3.25 sec                                               | 3.09 sec: 1.05x faster                                                    |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                      |
| crypto_pyaes                     | 54.2 ms                                                | 51.9 ms: 1.05x faster                                                     |
| pycparser                        | 705 ms                                                 | 677 ms: 1.04x faster                                                      |
| raytrace                         | 181 ms                                                 | 174 ms: 1.04x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 48.6 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| sqlglot_normalize                | 189 ms                                                 | 183 ms: 1.03x faster                                                      |
| hexiom                           | 4.86 ms                                                | 4.71 ms: 1.03x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                     |
| mdp                              | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                    |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                     |
| json                             | 3.03 ms                                                | 2.95 ms: 1.03x faster                                                     |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                      |
| json_dumps                       | 6.52 ms                                                | 6.36 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                      |
| python_startup_no_site           | 14.5 ms                                                | 14.2 ms: 1.02x faster                                                     |
| chaos                            | 41.2 ms                                                | 40.3 ms: 1.02x faster                                                     |
| xml_etree_iterparse              | 73.6 ms                                                | 72.3 ms: 1.02x faster                                                     |
| coverage                         | 46.0 ms                                                | 45.4 ms: 1.01x faster                                                     |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                      |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.01x slower                                                     |
| sympy_sum                        | 75.4 ms                                                | 76.0 ms: 1.01x slower                                                     |
| meteor_contest                   | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                     |
| dulwich_log                      | 28.5 ms                                                | 28.8 ms: 1.01x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 35.5 ms: 1.02x slower                                                     |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                     |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                     |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.07 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.03x slower                                                      |
| pathlib                          | 23.4 ms                                                | 24.2 ms: 1.04x slower                                                     |
| comprehensions                   | 12.3 us                                                | 12.8 us: 1.05x slower                                                     |
| async_tree_io_tg                 | 497 ms                                                 | 534 ms: 1.07x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                    |
| pylint                           | 180 ms                                                 | 206 ms: 1.14x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                      |
| genshi_xml                       | 34.4 ms                                                | 40.4 ms: 1.18x slower                                                     |
| richards_super                   | 39.1 ms                                                | 46.8 ms: 1.20x slower                                                     |
| richards                         | 35.2 ms                                                | 45.0 ms: 1.28x slower                                                     |
| async_tree_eager_io              | 514 ms                                                 | 683 ms: 1.33x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 707 ms: 1.48x slower                                                      |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (5): async_generators, telco, sqlglot_parse, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.48x