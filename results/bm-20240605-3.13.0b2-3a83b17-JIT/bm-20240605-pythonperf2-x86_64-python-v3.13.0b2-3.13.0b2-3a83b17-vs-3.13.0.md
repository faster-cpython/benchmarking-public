# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.002x faster
- HPT reliability: 93.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 305 ms: 1.04x slower                                             |
| html5lib       | 72.9 ms                                                      | 75.4 ms: 1.03x slower                                            |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 441 ms: 1.04x faster                                             |
| async_tree_none_tg        | 342 ms                                                       | 349 ms: 1.02x slower                                             |
| async_tree_none           | 370 ms                                                       | 380 ms: 1.03x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 628 ms: 1.05x slower                                             |
| async_generators          | 364 ms                                                       | 389 ms: 1.07x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 891 ms: 1.08x slower                                             |
| async_tree_io             | 832 ms                                                       | 921 ms: 1.11x slower                                             |
| Geometric mean            | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 82.9 ms: 1.11x faster                                            |
| float          | 81.6 ms                                                      | 74.2 ms: 1.10x faster                                            |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                             |
| regex_v8       | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                            |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                            |
| regex_dna      | 238 ms                                                       | 248 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                           |
| xml_etree_process    | 60.7 ms                                                      | 58.5 ms: 1.04x faster                                            |
| pickle_pure_python   | 322 us                                                       | 310 us: 1.04x faster                                             |
| xml_etree_generate   | 85.2 ms                                                      | 82.4 ms: 1.03x faster                                            |
| unpickle_pure_python | 216 us                                                       | 211 us: 1.03x faster                                             |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| json_loads           | 24.7 us                                                      | 24.4 us: 1.01x faster                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 99.3 ms: 1.01x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.8 ms: 1.13x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 9.44 ms: 1.06x slower                                            |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.10 ms: 1.13x faster                                            |
| genshi_text     | 27.2 ms                                                      | 28.2 ms: 1.04x slower                                            |
| django_template | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                            |
| genshi_xml      | 58.0 ms                                                      | 65.3 ms: 1.13x slower                                            |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles          | 2.65 ms                                                      | 1.94 ms: 1.37x faster                                            |
| mypy2                     | 1.02 sec                                                     | 852 ms: 1.20x faster                                             |
| spectral_norm             | 97.4 ms                                                      | 82.3 ms: 1.18x faster                                            |
| tomli_loads               | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                           |
| fannkuch                  | 384 ms                                                       | 331 ms: 1.16x faster                                             |
| richards_super            | 60.2 ms                                                      | 52.8 ms: 1.14x faster                                            |
| mako                      | 10.3 ms                                                      | 9.10 ms: 1.13x faster                                            |
| python_startup            | 15.6 ms                                                      | 13.8 ms: 1.13x faster                                            |
| richards                  | 52.5 ms                                                      | 46.5 ms: 1.13x faster                                            |
| nbody                     | 92.1 ms                                                      | 82.9 ms: 1.11x faster                                            |
| float                     | 81.6 ms                                                      | 74.2 ms: 1.10x faster                                            |
| pyflate                   | 493 ms                                                       | 449 ms: 1.10x faster                                             |
| telco                     | 8.77 ms                                                      | 8.05 ms: 1.09x faster                                            |
| json                      | 5.62 ms                                                      | 5.30 ms: 1.06x faster                                            |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 3.99 ms: 1.06x faster                                            |
| pprint_safe_repr          | 835 ms                                                       | 792 ms: 1.05x faster                                             |
| coverage                  | 84.5 ms                                                      | 80.7 ms: 1.05x faster                                            |
| deepcopy_memo             | 38.9 us                                                      | 37.2 us: 1.05x faster                                            |
| pprint_pformat            | 1.70 sec                                                     | 1.63 sec: 1.05x faster                                           |
| crypto_pyaes              | 73.5 ms                                                      | 70.6 ms: 1.04x faster                                            |
| async_tree_memoization_tg | 458 ms                                                       | 441 ms: 1.04x faster                                             |
| xml_etree_process         | 60.7 ms                                                      | 58.5 ms: 1.04x faster                                            |
| pickle_pure_python        | 322 us                                                       | 310 us: 1.04x faster                                             |
| xml_etree_generate        | 85.2 ms                                                      | 82.4 ms: 1.03x faster                                            |
| regex_compile             | 143 ms                                                       | 139 ms: 1.03x faster                                             |
| unpickle_pure_python      | 216 us                                                       | 211 us: 1.03x faster                                             |
| pycparser                 | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                           |
| scimark_fft               | 298 ms                                                       | 292 ms: 1.02x faster                                             |
| json_dumps                | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| json_loads                | 24.7 us                                                      | 24.4 us: 1.01x faster                                            |
| pidigits                  | 252 ms                                                       | 250 ms: 1.01x faster                                             |
| go                        | 167 ms                                                       | 166 ms: 1.01x faster                                             |
| xml_etree_iterparse       | 99.8 ms                                                      | 99.3 ms: 1.01x faster                                            |
| bpe_tokeniser             | 5.09 sec                                                     | 5.13 sec: 1.01x slower                                           |
| mdp                       | 2.53 sec                                                     | 2.55 sec: 1.01x slower                                           |
| xml_etree_parse           | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| dulwich_log               | 65.5 ms                                                      | 66.2 ms: 1.01x slower                                            |
| regex_v8                  | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                            |
| scimark_monte_carlo       | 65.2 ms                                                      | 65.9 ms: 1.01x slower                                            |
| generators                | 33.9 ms                                                      | 34.3 ms: 1.01x slower                                            |
| regex_effbot              | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                            |
| async_tree_none_tg        | 342 ms                                                       | 349 ms: 1.02x slower                                             |
| async_tree_none           | 370 ms                                                       | 380 ms: 1.03x slower                                             |
| hexiom                    | 6.47 ms                                                      | 6.65 ms: 1.03x slower                                            |
| comprehensions            | 17.3 us                                                      | 17.8 us: 1.03x slower                                            |
| logging_format            | 6.95 us                                                      | 7.17 us: 1.03x slower                                            |
| tornado_http              | 119 ms                                                       | 123 ms: 1.03x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| html5lib                  | 72.9 ms                                                      | 75.4 ms: 1.03x slower                                            |
| genshi_text               | 27.2 ms                                                      | 28.2 ms: 1.04x slower                                            |
| sqlglot_transpile         | 1.76 ms                                                      | 1.82 ms: 1.04x slower                                            |
| regex_dna                 | 238 ms                                                       | 248 ms: 1.04x slower                                             |
| sqlglot_parse             | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                            |
| 2to3                      | 293 ms                                                       | 305 ms: 1.04x slower                                             |
| sympy_str                 | 297 ms                                                       | 310 ms: 1.05x slower                                             |
| typing_runtime_protocols  | 176 us                                                       | 184 us: 1.05x slower                                             |
| sympy_expand              | 506 ms                                                       | 532 ms: 1.05x slower                                             |
| nqueens                   | 92.3 ms                                                      | 97.2 ms: 1.05x slower                                            |
| logging_simple            | 6.28 us                                                      | 6.61 us: 1.05x slower                                            |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 628 ms: 1.05x slower                                             |
| deepcopy_reduce           | 3.49 us                                                      | 3.68 us: 1.05x slower                                            |
| deepcopy                  | 388 us                                                       | 410 us: 1.06x slower                                             |
| python_startup_no_site    | 8.93 ms                                                      | 9.44 ms: 1.06x slower                                            |
| chaos                     | 60.6 ms                                                      | 64.4 ms: 1.06x slower                                            |
| django_template           | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                            |
| async_generators          | 364 ms                                                       | 389 ms: 1.07x slower                                             |
| sqlglot_normalize         | 119 ms                                                       | 127 ms: 1.07x slower                                             |
| sqlglot_optimize          | 58.7 ms                                                      | 62.9 ms: 1.07x slower                                            |
| sympy_sum                 | 154 ms                                                       | 165 ms: 1.07x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 891 ms: 1.08x slower                                             |
| sympy_integrate           | 23.4 ms                                                      | 25.4 ms: 1.09x slower                                            |
| pylint                    | 345 ms                                                       | 376 ms: 1.09x slower                                             |
| async_tree_io             | 832 ms                                                       | 921 ms: 1.11x slower                                             |
| raytrace                  | 267 ms                                                       | 297 ms: 1.11x slower                                             |
| genshi_xml                | 58.0 ms                                                      | 65.3 ms: 1.13x slower                                            |
| deltablue                 | 3.38 ms                                                      | 3.81 ms: 1.13x slower                                            |
| scimark_sor               | 125 ms                                                       | 144 ms: 1.15x slower                                             |
| scimark_lu                | 97.4 ms                                                      | 114 ms: 1.17x slower                                             |
| logging_silent            | 97.5 ns                                                      | 123 ns: 1.26x slower                                             |
| Geometric mean            | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (10): asyncio_websockets, thrift, bench_mp_pool, chameleon, meteor_contest, gc_traversal, pathlib, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_memoization
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, docutils, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 93.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x