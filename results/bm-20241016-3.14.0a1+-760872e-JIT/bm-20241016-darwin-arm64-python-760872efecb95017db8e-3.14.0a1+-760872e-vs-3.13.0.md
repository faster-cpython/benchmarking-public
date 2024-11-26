# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: darwin-arm64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.041x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 183 ms: 1.02x faster                                                   |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| html5lib       | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                  |
| sphinx         | 603 ms                                                 | 666 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 62.8 ms: 1.12x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.9 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                   |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 610 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.3 ms: 1.16x faster                                                  |
| nbody          | 74.0 ms                                                | 65.3 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 75.0 ms: 1.05x faster                                                  |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                 |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.24x faster                                                   |
| pickle_pure_python   | 214 us                                                 | 178 us: 1.20x faster                                                   |
| xml_etree_process    | 41.0 ms                                                | 34.5 ms: 1.19x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 50.3 ms: 1.13x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 72.5 ms: 1.01x faster                                                  |
| json_dumps           | 6.52 ms                                                | 7.12 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 14.6 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.8 us: 1.63x faster                                                  |
| deepcopy                         | 237 us                                                 | 152 us: 1.55x faster                                                   |
| deepcopy_reduce                  | 2.07 us                                                | 1.50 us: 1.38x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                 |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.24x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                   |
| scimark_sor                      | 105 ms                                                 | 86.2 ms: 1.22x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 178 us: 1.20x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 64.4 ms: 1.19x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 34.5 ms: 1.19x faster                                                  |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| go                               | 115 ms                                                 | 98.0 ms: 1.17x faster                                                  |
| float                            | 56.0 ms                                                | 48.3 ms: 1.16x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.13 us: 1.15x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.40 us: 1.15x faster                                                  |
| nbody                            | 74.0 ms                                                | 65.3 ms: 1.13x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 50.3 ms: 1.13x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 62.8 ms: 1.12x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.9 ms: 1.12x faster                                                  |
| thrift                           | 466 us                                                 | 418 us: 1.11x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 45.6 ms: 1.11x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.43 ms: 1.10x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 69.3 ms: 1.10x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 998 ms: 1.09x faster                                                   |
| raytrace                         | 181 ms                                                 | 167 ms: 1.08x faster                                                   |
| html5lib                         | 36.6 ms                                                | 33.9 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                   |
| fannkuch                         | 284 ms                                                 | 264 ms: 1.08x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 497 ms: 1.07x faster                                                   |
| nqueens                          | 62.5 ms                                                | 58.4 ms: 1.07x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 472 us: 1.07x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 94.8 us: 1.07x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.04 sec: 1.07x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| json                             | 3.03 ms                                                | 2.87 ms: 1.06x faster                                                  |
| richards_super                   | 39.1 ms                                                | 37.1 ms: 1.05x faster                                                  |
| richards                         | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                                   |
| telco                            | 4.76 ms                                                | 4.54 ms: 1.05x faster                                                  |
| pathlib                          | 23.4 ms                                                | 22.3 ms: 1.05x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 75.0 ms: 1.05x faster                                                  |
| coverage                         | 46.0 ms                                                | 43.9 ms: 1.05x faster                                                  |
| pycparser                        | 705 ms                                                 | 678 ms: 1.04x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 182 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                   |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| 2to3                             | 187 ms                                                 | 183 ms: 1.02x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 72.5 ms: 1.01x faster                                                  |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                                   |
| bench_mp_pool                    | 62.5 ms                                                | 61.8 ms: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 245 ms: 1.01x faster                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 53.9 ms: 1.01x faster                                                  |
| chaos                            | 41.2 ms                                                | 41.4 ms: 1.00x slower                                                  |
| python_startup_no_site           | 14.5 ms                                                | 14.6 ms: 1.01x slower                                                  |
| dulwich_log                      | 28.5 ms                                                | 28.7 ms: 1.01x slower                                                  |
| hexiom                           | 4.86 ms                                                | 4.92 ms: 1.01x slower                                                  |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.2 ms: 1.02x slower                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.96 ms: 1.02x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 875 us: 1.02x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.03x slower                                                  |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.14 ms: 1.05x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 36.8 ms: 1.05x slower                                                  |
| sympy_sum                        | 75.4 ms                                                | 79.7 ms: 1.06x slower                                                  |
| comprehensions                   | 12.3 us                                                | 13.0 us: 1.06x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 7.12 ms: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| sphinx                           | 603 ms                                                 | 666 ms: 1.11x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.31 ms: 1.12x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| pylint                           | 180 ms                                                 | 212 ms: 1.18x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 610 ms: 1.23x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, xml_etree_parse, tornado_http, logging_silent, python_startup, pidigits, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x