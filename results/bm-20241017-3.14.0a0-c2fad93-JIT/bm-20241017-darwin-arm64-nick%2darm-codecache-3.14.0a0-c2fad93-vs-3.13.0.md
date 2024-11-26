# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 170 ms: 1.10x faster                                           |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                         |
| html5lib       | 36.6 ms                                                | 32.7 ms: 1.12x faster                                          |
| sphinx         | 603 ms                                                 | 625 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                          |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                           |
| async_tree_none                  | 215 ms                                                 | 198 ms: 1.09x faster                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                           |
| async_generators                 | 295 ms                                                 | 288 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                           |
| async_tree_io_tg                 | 497 ms                                                 | 539 ms: 1.08x slower                                           |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                           |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.32x slower                                           |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.2 ms: 1.21x faster                                          |
| nbody          | 74.0 ms                                                | 63.7 ms: 1.16x faster                                          |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 72.0 ms: 1.09x faster                                          |
| regex_v8       | 17.0 ms                                                | 17.0 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.25x faster                                         |
| unpickle_pure_python | 164 us                                                 | 131 us: 1.25x faster                                           |
| pickle_pure_python   | 214 us                                                 | 176 us: 1.22x faster                                           |
| xml_etree_process    | 41.0 ms                                                | 33.9 ms: 1.21x faster                                          |
| xml_etree_generate   | 57.0 ms                                                | 49.5 ms: 1.15x faster                                          |
| json_dumps           | 6.52 ms                                                | 6.16 ms: 1.06x faster                                          |
| json_loads           | 17.0 us                                                | 16.4 us: 1.03x faster                                          |
| xml_etree_iterparse  | 73.6 ms                                                | 72.4 ms: 1.02x faster                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.2 ms: 1.02x slower                                          |
| python_startup_no_site | 14.5 ms                                                | 14.9 ms: 1.03x slower                                          |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.43 ms: 1.19x faster                                          |
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                          |
| django_template | 22.2 ms                                                | 20.2 ms: 1.10x faster                                          |
| genshi_xml      | 34.4 ms                                                | 32.1 ms: 1.07x faster                                          |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.6 us: 1.65x faster                                          |
| deepcopy                         | 237 us                                                 | 149 us: 1.59x faster                                           |
| deepcopy_reduce                  | 2.07 us                                                | 1.49 us: 1.39x faster                                          |
| generators                       | 31.5 ms                                                | 24.2 ms: 1.30x faster                                          |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.25x faster                                         |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.25x faster                                           |
| logging_silent                   | 70.1 ns                                                | 56.4 ns: 1.24x faster                                          |
| scimark_sor                      | 105 ms                                                 | 85.8 ms: 1.23x faster                                          |
| pickle_pure_python               | 214 us                                                 | 176 us: 1.22x faster                                           |
| float                            | 56.0 ms                                                | 46.2 ms: 1.21x faster                                          |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                          |
| xml_etree_process                | 41.0 ms                                                | 33.9 ms: 1.21x faster                                          |
| scimark_lu                       | 76.7 ms                                                | 64.0 ms: 1.20x faster                                          |
| go                               | 115 ms                                                 | 96.1 ms: 1.20x faster                                          |
| mako                             | 7.68 ms                                                | 6.43 ms: 1.19x faster                                          |
| logging_simple                   | 3.60 us                                                | 3.02 us: 1.19x faster                                          |
| richards                         | 35.2 ms                                                | 29.9 ms: 1.18x faster                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                           |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                          |
| pprint_safe_repr                 | 533 ms                                                 | 456 ms: 1.17x faster                                           |
| richards_super                   | 39.1 ms                                                | 33.4 ms: 1.17x faster                                          |
| logging_format                   | 3.89 us                                                | 3.33 us: 1.17x faster                                          |
| nbody                            | 74.0 ms                                                | 63.7 ms: 1.16x faster                                          |
| deltablue                        | 2.68 ms                                                | 2.31 ms: 1.16x faster                                          |
| xml_etree_generate               | 57.0 ms                                                | 49.5 ms: 1.15x faster                                          |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                          |
| pprint_pformat                   | 1.08 sec                                               | 952 ms: 1.14x faster                                           |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 44.6 ms: 1.13x faster                                          |
| pyflate                          | 351 ms                                                 | 314 ms: 1.12x faster                                           |
| html5lib                         | 36.6 ms                                                | 32.7 ms: 1.12x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                           |
| spectral_norm                    | 76.3 ms                                                | 68.6 ms: 1.11x faster                                          |
| nqueens                          | 62.5 ms                                                | 56.6 ms: 1.11x faster                                          |
| fannkuch                         | 284 ms                                                 | 257 ms: 1.11x faster                                           |
| 2to3                             | 187 ms                                                 | 170 ms: 1.10x faster                                           |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                           |
| django_template                  | 22.2 ms                                                | 20.2 ms: 1.10x faster                                          |
| regex_compile                    | 78.6 ms                                                | 72.0 ms: 1.09x faster                                          |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                           |
| async_tree_none                  | 215 ms                                                 | 198 ms: 1.09x faster                                           |
| hexiom                           | 4.86 ms                                                | 4.47 ms: 1.09x faster                                          |
| pycparser                        | 705 ms                                                 | 650 ms: 1.09x faster                                           |
| sqlglot_normalize                | 189 ms                                                 | 174 ms: 1.08x faster                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                           |
| genshi_xml                       | 34.4 ms                                                | 32.1 ms: 1.07x faster                                          |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                          |
| bench_thread_pool                | 505 us                                                 | 475 us: 1.06x faster                                           |
| sqlglot_parse                    | 856 us                                                 | 808 us: 1.06x faster                                           |
| json_dumps                       | 6.52 ms                                                | 6.16 ms: 1.06x faster                                          |
| coverage                         | 46.0 ms                                                | 43.5 ms: 1.06x faster                                          |
| pathlib                          | 23.4 ms                                                | 22.2 ms: 1.05x faster                                          |
| bpe_tokeniser                    | 3.25 sec                                               | 3.08 sec: 1.05x faster                                         |
| json                             | 3.03 ms                                                | 2.89 ms: 1.05x faster                                          |
| telco                            | 4.76 ms                                                | 4.56 ms: 1.04x faster                                          |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                           |
| crypto_pyaes                     | 54.2 ms                                                | 52.2 ms: 1.04x faster                                          |
| sqlglot_transpile                | 1.02 ms                                                | 984 us: 1.04x faster                                           |
| chaos                            | 41.2 ms                                                | 39.8 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 33.8 ms: 1.03x faster                                          |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.03x faster                                          |
| bench_mp_pool                    | 62.5 ms                                                | 61.0 ms: 1.03x faster                                          |
| sympy_str                        | 145 ms                                                 | 142 ms: 1.02x faster                                           |
| async_generators                 | 295 ms                                                 | 288 ms: 1.02x faster                                           |
| xml_etree_iterparse              | 73.6 ms                                                | 72.4 ms: 1.02x faster                                          |
| sympy_sum                        | 75.4 ms                                                | 74.5 ms: 1.01x faster                                          |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                         |
| raytrace                         | 181 ms                                                 | 180 ms: 1.00x faster                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.97 ms: 1.00x faster                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| regex_v8                         | 17.0 ms                                                | 17.0 ms: 1.00x slower                                          |
| dulwich_log                      | 28.5 ms                                                | 28.6 ms: 1.00x slower                                          |
| meteor_contest                   | 74.0 ms                                                | 74.5 ms: 1.01x slower                                          |
| comprehensions                   | 12.3 us                                                | 12.5 us: 1.02x slower                                          |
| python_startup                   | 18.9 ms                                                | 19.2 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                           |
| python_startup_no_site           | 14.5 ms                                                | 14.9 ms: 1.03x slower                                          |
| sphinx                           | 603 ms                                                 | 625 ms: 1.04x slower                                           |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                          |
| async_tree_io_tg                 | 497 ms                                                 | 539 ms: 1.08x slower                                           |
| create_gc_cycles                 | 1.17 ms                                                | 1.29 ms: 1.10x slower                                          |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                           |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.32x slower                                           |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                   |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, xml_etree_parse, tornado_http, gc_traversal, asyncio_websockets, regex_effbot, regex_dna, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.072x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x