# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x slower
- HPT reliability: 89.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 290 ms: 1.00x faster                                               |
| chameleon      | 7.42 ms                                                      | 7.54 ms: 1.02x slower                                              |
| html5lib       | 71.9 ms                                                      | 73.7 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                             |
| async_tree_memoization_tg | 461 ms                                                       | 463 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 603 ms: 1.00x slower                                               |
| async_tree_none           | 372 ms                                                       | 375 ms: 1.01x slower                                               |
| async_tree_none_tg        | 340 ms                                                       | 343 ms: 1.01x slower                                               |
| asyncio_websockets        | 382 ms                                                       | 386 ms: 1.01x slower                                               |
| asyncio_tcp               | 380 ms                                                       | 384 ms: 1.01x slower                                               |
| async_generators          | 359 ms                                                       | 366 ms: 1.02x slower                                               |
| coroutines                | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                              |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (4): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 81.6 ms: 1.00x faster                                              |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                              |
| regex_dna      | 244 ms                                                       | 246 ms: 1.01x slower                                               |
| regex_effbot   | 3.37 ms                                                      | 3.55 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.31 us: 1.06x faster                                              |
| pickle_dict          | 32.1 us                                                      | 30.4 us: 1.06x faster                                              |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                              |
| xml_etree_process    | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                              |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                               |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                               |
| tomli_loads          | 2.41 sec                                                     | 2.43 sec: 1.01x slower                                             |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                              |
| json_loads           | 24.0 us                                                      | 24.5 us: 1.02x slower                                              |
| xml_etree_parse      | 145 ms                                                       | 149 ms: 1.03x slower                                               |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| unpickle_list        | 4.62 us                                                      | 4.81 us: 1.04x slower                                              |
| unpickle             | 15.1 us                                                      | 16.0 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.94 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.7 ms: 1.03x faster                                              |
| genshi_xml     | 57.3 ms                                                      | 56.0 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| raytrace                  | 289 ms                                                       | 262 ms: 1.10x faster                                               |
| pickle_list               | 4.59 us                                                      | 4.31 us: 1.06x faster                                              |
| scimark_sor               | 126 ms                                                       | 118 ms: 1.06x faster                                               |
| pickle_dict               | 32.1 us                                                      | 30.4 us: 1.06x faster                                              |
| deepcopy_memo             | 39.5 us                                                      | 37.9 us: 1.04x faster                                              |
| scimark_fft               | 314 ms                                                       | 302 ms: 1.04x faster                                               |
| regex_v8                  | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                              |
| genshi_text               | 26.6 ms                                                      | 25.7 ms: 1.03x faster                                              |
| deepcopy                  | 397 us                                                       | 384 us: 1.03x faster                                               |
| pickle                    | 10.5 us                                                      | 10.2 us: 1.03x faster                                              |
| deepcopy_reduce           | 3.54 us                                                      | 3.44 us: 1.03x faster                                              |
| genshi_xml                | 57.3 ms                                                      | 56.0 ms: 1.02x faster                                              |
| xml_etree_process         | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                              |
| spectral_norm             | 97.4 ms                                                      | 95.8 ms: 1.02x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                              |
| chaos                     | 61.7 ms                                                      | 60.9 ms: 1.01x faster                                              |
| gunicorn                  | 1.04 ms                                                      | 1.03 ms: 1.01x faster                                              |
| pyflate                   | 492 ms                                                       | 487 ms: 1.01x faster                                               |
| pycparser                 | 1.26 sec                                                     | 1.24 sec: 1.01x faster                                             |
| richards_super            | 59.8 ms                                                      | 59.3 ms: 1.01x faster                                              |
| generators                | 33.5 ms                                                      | 33.2 ms: 1.01x faster                                              |
| pickle_pure_python        | 318 us                                                       | 316 us: 1.01x faster                                               |
| scimark_lu                | 97.8 ms                                                      | 97.1 ms: 1.01x faster                                              |
| deltablue                 | 3.41 ms                                                      | 3.39 ms: 1.01x faster                                              |
| telco                     | 8.58 ms                                                      | 8.52 ms: 1.01x faster                                              |
| richards                  | 52.7 ms                                                      | 52.5 ms: 1.01x faster                                              |
| float                     | 81.9 ms                                                      | 81.6 ms: 1.00x faster                                              |
| 2to3                      | 291 ms                                                       | 290 ms: 1.00x faster                                               |
| pidigits                  | 253 ms                                                       | 252 ms: 1.00x faster                                               |
| python_startup_no_site    | 8.94 ms                                                      | 8.94 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                             |
| sympy_expand              | 505 ms                                                       | 506 ms: 1.00x slower                                               |
| crypto_pyaes              | 72.8 ms                                                      | 73.0 ms: 1.00x slower                                              |
| sqlglot_transpile         | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                              |
| async_tree_memoization_tg | 461 ms                                                       | 463 ms: 1.00x slower                                               |
| sympy_integrate           | 23.3 ms                                                      | 23.4 ms: 1.00x slower                                              |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 603 ms: 1.00x slower                                               |
| unpickle_pure_python      | 214 us                                                       | 216 us: 1.01x slower                                               |
| sympy_str                 | 296 ms                                                       | 298 ms: 1.01x slower                                               |
| sqlite_synth              | 2.79 us                                                      | 2.81 us: 1.01x slower                                              |
| sqlglot_optimize          | 59.7 ms                                                      | 60.1 ms: 1.01x slower                                              |
| async_tree_none           | 372 ms                                                       | 375 ms: 1.01x slower                                               |
| mdp                       | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                             |
| async_tree_none_tg        | 340 ms                                                       | 343 ms: 1.01x slower                                               |
| meteor_contest            | 128 ms                                                       | 130 ms: 1.01x slower                                               |
| nqueens                   | 88.2 ms                                                      | 89.1 ms: 1.01x slower                                              |
| asyncio_websockets        | 382 ms                                                       | 386 ms: 1.01x slower                                               |
| asyncio_tcp               | 380 ms                                                       | 384 ms: 1.01x slower                                               |
| pprint_safe_repr          | 812 ms                                                       | 820 ms: 1.01x slower                                               |
| typing_runtime_protocols  | 174 us                                                       | 176 us: 1.01x slower                                               |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                               |
| regex_dna                 | 244 ms                                                       | 246 ms: 1.01x slower                                               |
| tomli_loads               | 2.41 sec                                                     | 2.43 sec: 1.01x slower                                             |
| pprint_pformat            | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                             |
| aiohttp                   | 1.07 ms                                                      | 1.08 ms: 1.01x slower                                              |
| json                      | 5.22 ms                                                      | 5.29 ms: 1.01x slower                                              |
| json_dumps                | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                              |
| sqlglot_normalize         | 118 ms                                                       | 120 ms: 1.02x slower                                               |
| chameleon                 | 7.42 ms                                                      | 7.54 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult   | 4.29 ms                                                      | 4.36 ms: 1.02x slower                                              |
| sqlglot_parse             | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                              |
| async_generators          | 359 ms                                                       | 366 ms: 1.02x slower                                               |
| json_loads                | 24.0 us                                                      | 24.5 us: 1.02x slower                                              |
| thrift                    | 877 us                                                       | 895 us: 1.02x slower                                               |
| logging_format            | 7.07 us                                                      | 7.23 us: 1.02x slower                                              |
| create_gc_cycles          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                              |
| html5lib                  | 71.9 ms                                                      | 73.7 ms: 1.02x slower                                              |
| xml_etree_parse           | 145 ms                                                       | 149 ms: 1.03x slower                                               |
| xml_etree_iterparse       | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| logging_simple            | 6.40 us                                                      | 6.60 us: 1.03x slower                                              |
| go                        | 160 ms                                                       | 166 ms: 1.03x slower                                               |
| bench_mp_pool             | 4.65 ms                                                      | 4.81 ms: 1.03x slower                                              |
| coverage                  | 81.1 ms                                                      | 84.3 ms: 1.04x slower                                              |
| unpickle_list             | 4.62 us                                                      | 4.81 us: 1.04x slower                                              |
| regex_effbot              | 3.37 ms                                                      | 3.55 ms: 1.05x slower                                              |
| unpickle                  | 15.1 us                                                      | 16.0 us: 1.05x slower                                              |
| coroutines                | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                              |
| unpack_sequence           | 56.8 ns                                                      | 62.5 ns: 1.10x slower                                              |
| Geometric mean            | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (25): nbody, async_tree_io, comprehensions, async_tree_io_tg, gc_traversal, tornado_http, fannkuch, docutils, django_template, pathlib, scimark_monte_carlo, flaskblogging, async_tree_cpu_io_mixed_tg, xml_etree_generate, hexiom, bpe_tokeniser, python_startup, pylint, dask, mako, logging_silent, regex_compile, mypy2, bench_thread_pool, async_tree_memoization

# HPT report

- Reliability score: 89.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x