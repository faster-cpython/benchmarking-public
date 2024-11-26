# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.011x faster
- HPT reliability: 80.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| chameleon      | 7.49 ms                                                      | 7.20 ms: 1.04x faster                                            |
| docutils       | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                           |
| html5lib       | 72.9 ms                                                      | 74.1 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 427 ms: 1.07x faster                                             |
| asyncio_websockets        | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| async_generators          | 364 ms                                                       | 362 ms: 1.01x faster                                             |
| coroutines                | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 614 ms: 1.03x slower                                             |
| async_tree_memoization    | 447 ms                                                       | 464 ms: 1.04x slower                                             |
| async_tree_io             | 832 ms                                                       | 875 ms: 1.05x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 905 ms: 1.10x slower                                             |
| Geometric mean            | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.7 ms: 1.04x faster                                            |
| float          | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                            |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                            |
| regex_effbot   | 3.51 ms                                                      | 3.54 ms: 1.01x slower                                            |
| regex_dna      | 238 ms                                                       | 251 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 315 us: 1.02x faster                                             |
| unpickle_pure_python | 216 us                                                       | 214 us: 1.01x faster                                             |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                            |
| xml_etree_process    | 60.7 ms                                                      | 61.5 ms: 1.01x slower                                            |
| xml_etree_generate   | 85.2 ms                                                      | 86.9 ms: 1.02x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.03x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 106 ms: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| genshi_xml      | 58.0 ms                                                      | 56.8 ms: 1.02x faster                                            |
| django_template | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                     | 1.02 sec                                                     | 768 ms: 1.33x faster                                             |
| create_gc_cycles          | 2.65 ms                                                      | 2.02 ms: 1.31x faster                                            |
| python_startup            | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                            |
| scimark_sor               | 125 ms                                                       | 116 ms: 1.08x faster                                             |
| async_tree_memoization_tg | 458 ms                                                       | 427 ms: 1.07x faster                                             |
| coverage                  | 84.5 ms                                                      | 79.6 ms: 1.06x faster                                            |
| json                      | 5.62 ms                                                      | 5.31 ms: 1.06x faster                                            |
| telco                     | 8.77 ms                                                      | 8.29 ms: 1.06x faster                                            |
| fannkuch                  | 384 ms                                                       | 365 ms: 1.05x faster                                             |
| pycparser                 | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                           |
| nqueens                   | 92.3 ms                                                      | 88.6 ms: 1.04x faster                                            |
| chameleon                 | 7.49 ms                                                      | 7.20 ms: 1.04x faster                                            |
| genshi_text               | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| nbody                     | 92.1 ms                                                      | 88.7 ms: 1.04x faster                                            |
| bench_mp_pool             | 4.82 ms                                                      | 4.64 ms: 1.04x faster                                            |
| deepcopy_memo             | 38.9 us                                                      | 37.5 us: 1.04x faster                                            |
| bench_thread_pool         | 929 us                                                       | 901 us: 1.03x faster                                             |
| deepcopy                  | 388 us                                                       | 377 us: 1.03x faster                                             |
| meteor_contest            | 130 ms                                                       | 126 ms: 1.03x faster                                             |
| pprint_safe_repr          | 835 ms                                                       | 814 ms: 1.03x faster                                             |
| go                        | 167 ms                                                       | 163 ms: 1.02x faster                                             |
| pprint_pformat            | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                           |
| pickle_pure_python        | 322 us                                                       | 315 us: 1.02x faster                                             |
| genshi_xml                | 58.0 ms                                                      | 56.8 ms: 1.02x faster                                            |
| typing_runtime_protocols  | 176 us                                                       | 172 us: 1.02x faster                                             |
| richards_super            | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                            |
| asyncio_websockets        | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| pathlib                   | 17.4 ms                                                      | 17.1 ms: 1.02x faster                                            |
| float                     | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                            |
| comprehensions            | 17.3 us                                                      | 17.0 us: 1.02x faster                                            |
| logging_silent            | 97.5 ns                                                      | 95.9 ns: 1.02x faster                                            |
| thrift                    | 918 us                                                       | 903 us: 1.02x faster                                             |
| raytrace                  | 267 ms                                                       | 263 ms: 1.02x faster                                             |
| deepcopy_reduce           | 3.49 us                                                      | 3.44 us: 1.02x faster                                            |
| hexiom                    | 6.47 ms                                                      | 6.38 ms: 1.01x faster                                            |
| generators                | 33.9 ms                                                      | 33.4 ms: 1.01x faster                                            |
| scimark_lu                | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                            |
| sympy_expand              | 506 ms                                                       | 500 ms: 1.01x faster                                             |
| unpickle_pure_python      | 216 us                                                       | 214 us: 1.01x faster                                             |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                            |
| 2to3                      | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| async_generators          | 364 ms                                                       | 362 ms: 1.01x faster                                             |
| sympy_sum                 | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| sympy_str                 | 297 ms                                                       | 295 ms: 1.00x faster                                             |
| sympy_integrate           | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                            |
| spectral_norm             | 97.4 ms                                                      | 97.6 ms: 1.00x slower                                            |
| regex_v8                  | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                            |
| sqlglot_optimize          | 58.7 ms                                                      | 58.9 ms: 1.00x slower                                            |
| pidigits                  | 252 ms                                                       | 253 ms: 1.00x slower                                             |
| mdp                       | 2.53 sec                                                     | 2.54 sec: 1.00x slower                                           |
| chaos                     | 60.6 ms                                                      | 60.9 ms: 1.01x slower                                            |
| sqlglot_transpile         | 1.76 ms                                                      | 1.77 ms: 1.01x slower                                            |
| django_template           | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                            |
| bpe_tokeniser             | 5.09 sec                                                     | 5.13 sec: 1.01x slower                                           |
| logging_format            | 6.95 us                                                      | 7.01 us: 1.01x slower                                            |
| regex_effbot              | 3.51 ms                                                      | 3.54 ms: 1.01x slower                                            |
| richards                  | 52.5 ms                                                      | 53.0 ms: 1.01x slower                                            |
| json_loads                | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| python_startup_no_site    | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                            |
| json_dumps                | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                            |
| dulwich_log               | 65.5 ms                                                      | 66.3 ms: 1.01x slower                                            |
| scimark_monte_carlo       | 65.2 ms                                                      | 66.1 ms: 1.01x slower                                            |
| xml_etree_process         | 60.7 ms                                                      | 61.5 ms: 1.01x slower                                            |
| crypto_pyaes              | 73.5 ms                                                      | 74.6 ms: 1.01x slower                                            |
| scimark_fft               | 298 ms                                                       | 302 ms: 1.01x slower                                             |
| html5lib                  | 72.9 ms                                                      | 74.1 ms: 1.02x slower                                            |
| xml_etree_generate        | 85.2 ms                                                      | 86.9 ms: 1.02x slower                                            |
| sqlglot_parse             | 1.37 ms                                                      | 1.40 ms: 1.03x slower                                            |
| gc_traversal              | 4.48 ms                                                      | 4.60 ms: 1.03x slower                                            |
| coroutines                | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| logging_simple            | 6.28 us                                                      | 6.47 us: 1.03x slower                                            |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 614 ms: 1.03x slower                                             |
| xml_etree_parse           | 144 ms                                                       | 149 ms: 1.03x slower                                             |
| async_tree_memoization    | 447 ms                                                       | 464 ms: 1.04x slower                                             |
| regex_dna                 | 238 ms                                                       | 251 ms: 1.05x slower                                             |
| async_tree_io             | 832 ms                                                       | 875 ms: 1.05x slower                                             |
| docutils                  | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                           |
| xml_etree_iterparse       | 99.8 ms                                                      | 106 ms: 1.07x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 905 ms: 1.10x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (11): pylint, async_tree_none, pyflate, deltablue, sqlglot_normalize, tornado_http, mako, tomli_loads, regex_compile, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: asyncio_tcp, asyncio_tcp_ssl, dask

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 80.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x