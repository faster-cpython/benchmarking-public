# Results vs. base

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.00x slower
- HPT reliability: 98.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                      | 287 ms: 1.00x slower                                                                  |
| docutils       | 2.98 sec                                                                    | 2.97 sec: 1.00x faster                                                                |
| tornado_http   | 119 ms                                                                      | 117 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 553 ms                                                                      | 542 ms: 1.02x faster                                                                  |
| coroutines                 | 22.1 ms                                                                     | 21.9 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 377 ms                                                                      | 374 ms: 1.01x faster                                                                  |
| async_tree_io_tg           | 767 ms                                                                      | 775 ms: 1.01x slower                                                                  |
| async_tree_memoization_tg  | 382 ms                                                                      | 386 ms: 1.01x slower                                                                  |
| async_generators           | 361 ms                                                                      | 368 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (7): asyncio_websockets, asyncio_tcp_ssl, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                                     | 80.6 ms: 1.01x faster                                                                 |
| pidigits       | 253 ms                                                                      | 253 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                                     | 3.40 ms: 1.03x faster                                                                 |
| regex_v8       | 25.9 ms                                                                     | 25.5 ms: 1.01x faster                                                                 |
| regex_dna      | 237 ms                                                                      | 245 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps          | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                                 |
| pickle_pure_python  | 317 us                                                                      | 319 us: 1.00x slower                                                                  |
| xml_etree_process   | 58.9 ms                                                                     | 59.7 ms: 1.01x slower                                                                 |
| xml_etree_iterparse | 103 ms                                                                      | 104 ms: 1.01x slower                                                                  |
| xml_etree_generate  | 83.8 ms                                                                     | 85.4 ms: 1.02x slower                                                                 |
| Geometric mean      | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                                 |
| python_startup_no_site | 9.07 ms                                                                     | 9.06 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 25.6 ms                                                                     | 25.0 ms: 1.03x faster                                                                 |
| django_template | 39.7 ms                                                                     | 40.2 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| gc_traversal               | 4.72 ms                                                                     | 4.49 ms: 1.05x faster                                                                 |
| pycparser                  | 1.27 sec                                                                    | 1.21 sec: 1.05x faster                                                                |
| pyflate                    | 504 ms                                                                      | 485 ms: 1.04x faster                                                                  |
| regex_effbot               | 3.50 ms                                                                     | 3.40 ms: 1.03x faster                                                                 |
| nqueens                    | 89.6 ms                                                                     | 87.2 ms: 1.03x faster                                                                 |
| genshi_text                | 25.6 ms                                                                     | 25.0 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 73.0 ms                                                                     | 71.3 ms: 1.02x faster                                                                 |
| logging_format             | 7.00 us                                                                     | 6.86 us: 1.02x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 553 ms                                                                      | 542 ms: 1.02x faster                                                                  |
| tornado_http               | 119 ms                                                                      | 117 ms: 1.01x faster                                                                  |
| regex_v8                   | 25.9 ms                                                                     | 25.5 ms: 1.01x faster                                                                 |
| meteor_contest             | 128 ms                                                                      | 126 ms: 1.01x faster                                                                  |
| sympy_sum                  | 156 ms                                                                      | 154 ms: 1.01x faster                                                                  |
| sympy_integrate            | 23.5 ms                                                                     | 23.2 ms: 1.01x faster                                                                 |
| coroutines                 | 22.1 ms                                                                     | 21.9 ms: 1.01x faster                                                                 |
| json_dumps                 | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                                 |
| sqlglot_optimize           | 59.2 ms                                                                     | 58.6 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 68.9 ms                                                                     | 68.3 ms: 1.01x faster                                                                 |
| float                      | 81.3 ms                                                                     | 80.6 ms: 1.01x faster                                                                 |
| sqlglot_parse              | 1.40 ms                                                                     | 1.39 ms: 1.01x faster                                                                 |
| richards                   | 52.5 ms                                                                     | 52.1 ms: 1.01x faster                                                                 |
| deepcopy_reduce            | 2.92 us                                                                     | 2.90 us: 1.01x faster                                                                 |
| asyncio_tcp                | 377 ms                                                                      | 374 ms: 1.01x faster                                                                  |
| hexiom                     | 6.37 ms                                                                     | 6.34 ms: 1.00x faster                                                                 |
| sqlglot_transpile          | 1.79 ms                                                                     | 1.78 ms: 1.00x faster                                                                 |
| pathlib                    | 16.0 ms                                                                     | 15.9 ms: 1.00x faster                                                                 |
| docutils                   | 2.98 sec                                                                    | 2.97 sec: 1.00x faster                                                                |
| python_startup             | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                                 |
| python_startup_no_site     | 9.07 ms                                                                     | 9.06 ms: 1.00x faster                                                                 |
| 2to3                       | 287 ms                                                                      | 287 ms: 1.00x slower                                                                  |
| pidigits                   | 253 ms                                                                      | 253 ms: 1.00x slower                                                                  |
| spectral_norm              | 94.9 ms                                                                     | 95.2 ms: 1.00x slower                                                                 |
| pprint_safe_repr           | 814 ms                                                                      | 818 ms: 1.00x slower                                                                  |
| dulwich_log                | 66.0 ms                                                                     | 66.2 ms: 1.00x slower                                                                 |
| bpe_tokeniser              | 4.92 sec                                                                    | 4.94 sec: 1.00x slower                                                                |
| pickle_pure_python         | 317 us                                                                      | 319 us: 1.00x slower                                                                  |
| sympy_expand               | 501 ms                                                                      | 503 ms: 1.00x slower                                                                  |
| go                         | 162 ms                                                                      | 163 ms: 1.01x slower                                                                  |
| raytrace                   | 273 ms                                                                      | 275 ms: 1.01x slower                                                                  |
| comprehensions             | 17.3 us                                                                     | 17.4 us: 1.01x slower                                                                 |
| scimark_lu                 | 97.3 ms                                                                     | 97.9 ms: 1.01x slower                                                                 |
| richards_super             | 59.1 ms                                                                     | 59.5 ms: 1.01x slower                                                                 |
| scimark_fft                | 294 ms                                                                      | 297 ms: 1.01x slower                                                                  |
| async_tree_io_tg           | 767 ms                                                                      | 775 ms: 1.01x slower                                                                  |
| mdp                        | 2.52 sec                                                                    | 2.55 sec: 1.01x slower                                                                |
| django_template            | 39.7 ms                                                                     | 40.2 ms: 1.01x slower                                                                 |
| async_tree_memoization_tg  | 382 ms                                                                      | 386 ms: 1.01x slower                                                                  |
| telco                      | 7.80 ms                                                                     | 7.89 ms: 1.01x slower                                                                 |
| xml_etree_process          | 58.9 ms                                                                     | 59.7 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                                    | 1.68 sec: 1.01x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                                      | 104 ms: 1.01x slower                                                                  |
| fannkuch                   | 367 ms                                                                      | 373 ms: 1.02x slower                                                                  |
| xml_etree_generate         | 83.8 ms                                                                     | 85.4 ms: 1.02x slower                                                                 |
| async_generators           | 361 ms                                                                      | 368 ms: 1.02x slower                                                                  |
| generators                 | 28.3 ms                                                                     | 29.0 ms: 1.02x slower                                                                 |
| regex_dna                  | 237 ms                                                                      | 245 ms: 1.03x slower                                                                  |
| scimark_sparse_mat_mult    | 4.01 ms                                                                     | 4.15 ms: 1.04x slower                                                                 |
| chaos                      | 60.6 ms                                                                     | 62.9 ms: 1.04x slower                                                                 |
| deepcopy_memo              | 29.0 us                                                                     | 30.7 us: 1.06x slower                                                                 |
| coverage                   | 78.7 ms                                                                     | 84.2 ms: 1.07x slower                                                                 |
| scimark_sor                | 110 ms                                                                      | 120 ms: 1.09x slower                                                                  |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (30): json_loads, logging_simple, thrift, create_gc_cycles, pylint, genshi_xml, bench_mp_pool, xml_etree_parse, deltablue, sqlglot_normalize, nbody, asyncio_websockets, sympy_str, regex_compile, asyncio_tcp_ssl, unpickle_pure_python, logging_silent, typing_runtime_protocols, bench_thread_pool, html5lib, deepcopy, tomli_loads, json, dask, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, mako, async_tree_none, async_tree_memoization

# HPT report

- Reliability score: 98.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x