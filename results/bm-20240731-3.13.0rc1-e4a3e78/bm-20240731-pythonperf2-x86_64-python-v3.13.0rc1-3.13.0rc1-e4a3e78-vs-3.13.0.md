# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.013x faster
- HPT reliability: 77.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                               |
| chameleon      | 7.49 ms                                                      | 7.33 ms: 1.02x faster                                              |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 440 ms: 1.04x faster                                               |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                               |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                              |
| async_generators          | 364 ms                                                       | 370 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 612 ms: 1.03x slower                                               |
| async_tree_memoization    | 447 ms                                                       | 466 ms: 1.04x slower                                               |
| async_tree_io             | 832 ms                                                       | 895 ms: 1.08x slower                                               |
| async_tree_io_tg          | 823 ms                                                       | 911 ms: 1.11x slower                                               |
| Geometric mean            | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.3 ms: 1.02x faster                                              |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.39 ms: 1.04x faster                                              |
| regex_dna      | 238 ms                                                       | 245 ms: 1.03x slower                                               |
| regex_v8       | 24.9 ms                                                      | 26.4 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.19 sec: 1.11x faster                                             |
| json_loads           | 24.7 us                                                      | 24.1 us: 1.03x faster                                              |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.02x faster                                               |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                               |
| pickle_pure_python   | 322 us                                                       | 317 us: 1.02x faster                                               |
| xml_etree_generate   | 85.2 ms                                                      | 86.2 ms: 1.01x slower                                              |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.18x faster                                              |
| python_startup_no_site | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                              |
| genshi_text     | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                              |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| mako            | 10.3 ms                                                      | 10.5 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                       |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mypy2                     | 1.02 sec                                                     | 769 ms: 1.33x faster                                               |
| create_gc_cycles          | 2.65 ms                                                      | 2.01 ms: 1.32x faster                                              |
| python_startup            | 15.6 ms                                                      | 13.3 ms: 1.18x faster                                              |
| tomli_loads               | 2.43 sec                                                     | 2.19 sec: 1.11x faster                                             |
| genshi_xml                | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                              |
| json                      | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                              |
| fannkuch                  | 384 ms                                                       | 356 ms: 1.08x faster                                               |
| genshi_text               | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                              |
| go                        | 167 ms                                                       | 158 ms: 1.06x faster                                               |
| coverage                  | 84.5 ms                                                      | 79.8 ms: 1.06x faster                                              |
| pyflate                   | 493 ms                                                       | 469 ms: 1.05x faster                                               |
| richards_super            | 60.2 ms                                                      | 57.4 ms: 1.05x faster                                              |
| async_tree_memoization_tg | 458 ms                                                       | 440 ms: 1.04x faster                                               |
| telco                     | 8.77 ms                                                      | 8.43 ms: 1.04x faster                                              |
| regex_effbot              | 3.51 ms                                                      | 3.39 ms: 1.04x faster                                              |
| thrift                    | 918 us                                                       | 888 us: 1.03x faster                                               |
| richards                  | 52.5 ms                                                      | 50.9 ms: 1.03x faster                                              |
| json_loads                | 24.7 us                                                      | 24.1 us: 1.03x faster                                              |
| bench_thread_pool         | 929 us                                                       | 907 us: 1.02x faster                                               |
| chameleon                 | 7.49 ms                                                      | 7.33 ms: 1.02x faster                                              |
| nqueens                   | 92.3 ms                                                      | 90.4 ms: 1.02x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 64.2 ms: 1.02x faster                                              |
| pycparser                 | 1.28 sec                                                     | 1.26 sec: 1.02x faster                                             |
| float                     | 81.6 ms                                                      | 80.3 ms: 1.02x faster                                              |
| unpickle_pure_python      | 216 us                                                       | 213 us: 1.02x faster                                               |
| xml_etree_parse           | 144 ms                                                       | 141 ms: 1.02x faster                                               |
| deepcopy_memo             | 38.9 us                                                      | 38.3 us: 1.02x faster                                              |
| pickle_pure_python        | 322 us                                                       | 317 us: 1.02x faster                                               |
| deltablue                 | 3.38 ms                                                      | 3.34 ms: 1.01x faster                                              |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                               |
| mdp                       | 2.53 sec                                                     | 2.49 sec: 1.01x faster                                             |
| 2to3                      | 293 ms                                                       | 289 ms: 1.01x faster                                               |
| pathlib                   | 17.4 ms                                                      | 17.2 ms: 1.01x faster                                              |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                              |
| hexiom                    | 6.47 ms                                                      | 6.40 ms: 1.01x faster                                              |
| typing_runtime_protocols  | 176 us                                                       | 174 us: 1.01x faster                                               |
| meteor_contest            | 130 ms                                                       | 129 ms: 1.01x faster                                               |
| pprint_pformat            | 1.70 sec                                                     | 1.69 sec: 1.01x faster                                             |
| chaos                     | 60.6 ms                                                      | 60.1 ms: 1.01x faster                                              |
| raytrace                  | 267 ms                                                       | 265 ms: 1.01x faster                                               |
| deepcopy                  | 388 us                                                       | 385 us: 1.01x faster                                               |
| gc_traversal              | 4.48 ms                                                      | 4.45 ms: 1.01x faster                                              |
| crypto_pyaes              | 73.5 ms                                                      | 73.1 ms: 1.01x faster                                              |
| comprehensions            | 17.3 us                                                      | 17.2 us: 1.00x faster                                              |
| pprint_safe_repr          | 835 ms                                                       | 831 ms: 1.00x faster                                               |
| spectral_norm             | 97.4 ms                                                      | 97.6 ms: 1.00x slower                                              |
| sympy_integrate           | 23.4 ms                                                      | 23.5 ms: 1.00x slower                                              |
| sympy_str                 | 297 ms                                                       | 298 ms: 1.00x slower                                               |
| sympy_expand              | 506 ms                                                       | 508 ms: 1.00x slower                                               |
| python_startup_no_site    | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                              |
| pidigits                  | 252 ms                                                       | 254 ms: 1.01x slower                                               |
| xml_etree_generate        | 85.2 ms                                                      | 86.2 ms: 1.01x slower                                              |
| django_template           | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| sympy_sum                 | 154 ms                                                       | 156 ms: 1.01x slower                                               |
| mako                      | 10.3 ms                                                      | 10.5 ms: 1.01x slower                                              |
| sqlglot_transpile         | 1.76 ms                                                      | 1.79 ms: 1.02x slower                                              |
| scimark_lu                | 97.4 ms                                                      | 99.0 ms: 1.02x slower                                              |
| scimark_sor               | 125 ms                                                       | 127 ms: 1.02x slower                                               |
| sqlglot_optimize          | 58.7 ms                                                      | 59.7 ms: 1.02x slower                                              |
| async_generators          | 364 ms                                                       | 370 ms: 1.02x slower                                               |
| sqlglot_normalize         | 119 ms                                                       | 121 ms: 1.02x slower                                               |
| scimark_monte_carlo       | 65.2 ms                                                      | 67.0 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 612 ms: 1.03x slower                                               |
| regex_dna                 | 238 ms                                                       | 245 ms: 1.03x slower                                               |
| logging_simple            | 6.28 us                                                      | 6.46 us: 1.03x slower                                              |
| sqlglot_parse             | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                              |
| xml_etree_iterparse       | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| scimark_fft               | 298 ms                                                       | 308 ms: 1.03x slower                                               |
| json_dumps                | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                              |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                              |
| async_tree_memoization    | 447 ms                                                       | 466 ms: 1.04x slower                                               |
| regex_v8                  | 24.9 ms                                                      | 26.4 ms: 1.06x slower                                              |
| docutils                  | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                             |
| async_tree_io             | 832 ms                                                       | 895 ms: 1.08x slower                                               |
| async_tree_io_tg          | 823 ms                                                       | 911 ms: 1.11x slower                                               |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (15): bench_mp_pool, tornado_http, async_tree_none, html5lib, generators, nbody, bpe_tokeniser, regex_compile, deepcopy_reduce, logging_silent, xml_etree_process, logging_format, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl, dask

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 77.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x