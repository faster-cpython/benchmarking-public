# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: darwin-arm64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| html5lib       | 36.6 ms                                                | 30.2 ms: 1.21x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.9 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.2 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 122 ms: 1.13x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| async_generators                 | 295 ms                                                 | 280 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 465 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 462 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 545 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 60.9 ms: 1.22x faster                                                 |
| float          | 56.0 ms                                                | 49.3 ms: 1.14x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 66.9 ms: 1.18x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 182 us: 1.18x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 141 us: 1.16x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.3 ms: 1.10x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| json_dumps           | 6.52 ms                                                | 6.39 ms: 1.02x faster                                                 |
| json_loads           | 17.0 us                                                | 17.1 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 74.2 ms: 1.01x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 15.1 ms: 1.25x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 12.4 ms: 1.17x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.89 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 237 us                                                 | 144 us: 1.64x faster                                                  |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| go                               | 115 ms                                                 | 79.0 ms: 1.46x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 897 us: 1.30x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.1 ms: 1.30x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.14 ms: 1.25x faster                                                 |
| python_startup                   | 18.9 ms                                                | 15.1 ms: 1.25x faster                                                 |
| comprehensions                   | 12.3 us                                                | 9.99 us: 1.23x faster                                                 |
| nbody                            | 74.0 ms                                                | 60.9 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.2 ms: 1.21x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                 |
| raytrace                         | 181 ms                                                 | 150 ms: 1.21x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.10 ms: 1.19x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 452 ms: 1.18x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 182 us: 1.18x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.06 us: 1.18x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 66.9 ms: 1.18x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 924 ms: 1.17x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.9 ms: 1.17x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 12.4 ms: 1.17x faster                                                 |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| nqueens                          | 62.5 ms                                                | 53.6 ms: 1.17x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.2 ms: 1.16x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 141 us: 1.16x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.36 us: 1.16x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 60.8 ns: 1.15x faster                                                 |
| chaos                            | 41.2 ms                                                | 35.8 ms: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 744 us: 1.15x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                                 |
| float                            | 56.0 ms                                                | 49.3 ms: 1.14x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 67.6 ms: 1.13x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 93.0 ms: 1.13x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 905 us: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 122 ms: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 450 us: 1.12x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 68.0 ms: 1.12x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                  |
| richards                         | 35.2 ms                                                | 31.5 ms: 1.12x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                                 |
| mako                             | 7.68 ms                                                | 6.89 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.5 us: 1.11x faster                                                 |
| richards_super                   | 39.1 ms                                                | 35.4 ms: 1.11x faster                                                 |
| pycparser                        | 705 ms                                                 | 639 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.4 ms                                                | 68.5 ms: 1.10x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 37.3 ms: 1.10x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                  |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                                  |
| fannkuch                         | 284 ms                                                 | 261 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 50.5 ms: 1.07x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| async_generators                 | 295 ms                                                 | 280 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.5 ms                                                | 27.2 ms: 1.05x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.42 sec: 1.05x faster                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.13 sec: 1.04x faster                                                |
| coverage                         | 46.0 ms                                                | 44.6 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| json                             | 3.03 ms                                                | 2.95 ms: 1.03x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 72.0 ms: 1.03x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| json_dumps                       | 6.52 ms                                                | 6.39 ms: 1.02x faster                                                 |
| pathlib                          | 23.4 ms                                                | 22.9 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.01x slower                                                 |
| xml_etree_iterparse              | 73.6 ms                                                | 74.2 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 465 ms: 1.01x slower                                                  |
| telco                            | 4.76 ms                                                | 4.82 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 462 ms: 1.03x slower                                                  |
| xml_etree_parse                  | 107 ms                                                 | 111 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 545 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): pylint, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.098x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.55x