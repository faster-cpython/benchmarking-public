# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 291 ms: 1.00x slower                                               |
| chameleon      | 7.42 ms                                                      | 7.37 ms: 1.01x faster                                              |
| docutils       | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                             |
| html5lib       | 71.9 ms                                                      | 74.6 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                       | 434 ms: 1.06x faster                                               |
| asyncio_tcp               | 380 ms                                                       | 372 ms: 1.02x faster                                               |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                             |
| asyncio_websockets        | 382 ms                                                       | 390 ms: 1.02x slower                                               |
| async_tree_none_tg        | 340 ms                                                       | 347 ms: 1.02x slower                                               |
| async_generators          | 359 ms                                                       | 368 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 615 ms: 1.03x slower                                               |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                              |
| async_tree_memoization    | 452 ms                                                       | 466 ms: 1.03x slower                                               |
| async_tree_io             | 847 ms                                                       | 879 ms: 1.04x slower                                               |
| async_tree_io_tg          | 819 ms                                                       | 913 ms: 1.12x slower                                               |
| Geometric mean            | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (2): async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.5 ms: 1.02x faster                                              |
| pidigits       | 253 ms                                                       | 254 ms: 1.00x slower                                               |
| nbody          | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.4 ms: 1.03x faster                                              |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| regex_dna      | 244 ms                                                       | 248 ms: 1.02x slower                                               |
| regex_effbot   | 3.37 ms                                                      | 3.74 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                               |
| unpickle_list        | 4.62 us                                                      | 4.56 us: 1.01x faster                                              |
| pickle_dict          | 32.1 us                                                      | 31.7 us: 1.01x faster                                              |
| json_loads           | 24.0 us                                                      | 23.8 us: 1.01x faster                                              |
| unpickle             | 15.1 us                                                      | 15.0 us: 1.01x faster                                              |
| tomli_loads          | 2.41 sec                                                     | 2.42 sec: 1.01x slower                                             |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                              |
| xml_etree_generate   | 85.3 ms                                                      | 87.4 ms: 1.02x slower                                              |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| unpickle_pure_python | 214 us                                                       | 229 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, pickle, xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.93 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 26.4 ms: 1.01x faster                                              |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mypy2                     | 1.05 sec                                                     | 769 ms: 1.36x faster                                               |
| raytrace                  | 289 ms                                                       | 260 ms: 1.11x faster                                               |
| unpack_sequence           | 56.8 ns                                                      | 52.6 ns: 1.08x faster                                              |
| scimark_sor               | 126 ms                                                       | 118 ms: 1.07x faster                                               |
| async_tree_memoization_tg | 461 ms                                                       | 434 ms: 1.06x faster                                               |
| deepcopy_memo             | 39.5 us                                                      | 37.7 us: 1.05x faster                                              |
| deepcopy                  | 397 us                                                       | 381 us: 1.04x faster                                               |
| scimark_fft               | 314 ms                                                       | 302 ms: 1.04x faster                                               |
| regex_v8                  | 26.2 ms                                                      | 25.4 ms: 1.03x faster                                              |
| deepcopy_reduce           | 3.54 us                                                      | 3.44 us: 1.03x faster                                              |
| chaos                     | 61.7 ms                                                      | 60.1 ms: 1.03x faster                                              |
| pickle_pure_python        | 318 us                                                       | 311 us: 1.02x faster                                               |
| logging_simple            | 6.40 us                                                      | 6.25 us: 1.02x faster                                              |
| pyflate                   | 492 ms                                                       | 481 ms: 1.02x faster                                               |
| asyncio_tcp               | 380 ms                                                       | 372 ms: 1.02x faster                                               |
| pycparser                 | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                             |
| float                     | 81.9 ms                                                      | 80.5 ms: 1.02x faster                                              |
| richards_super            | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                              |
| unpickle_list             | 4.62 us                                                      | 4.56 us: 1.01x faster                                              |
| logging_format            | 7.07 us                                                      | 6.97 us: 1.01x faster                                              |
| richards                  | 52.7 ms                                                      | 52.0 ms: 1.01x faster                                              |
| pathlib                   | 17.4 ms                                                      | 17.2 ms: 1.01x faster                                              |
| pickle_dict               | 32.1 us                                                      | 31.7 us: 1.01x faster                                              |
| genshi_text               | 26.6 ms                                                      | 26.4 ms: 1.01x faster                                              |
| scimark_lu                | 97.8 ms                                                      | 96.9 ms: 1.01x faster                                              |
| json_loads                | 24.0 us                                                      | 23.8 us: 1.01x faster                                              |
| coverage                  | 81.1 ms                                                      | 80.4 ms: 1.01x faster                                              |
| unpickle                  | 15.1 us                                                      | 15.0 us: 1.01x faster                                              |
| logging_silent            | 97.7 ns                                                      | 96.9 ns: 1.01x faster                                              |
| comprehensions            | 17.3 us                                                      | 17.1 us: 1.01x faster                                              |
| regex_compile             | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| deltablue                 | 3.41 ms                                                      | 3.39 ms: 1.01x faster                                              |
| chameleon                 | 7.42 ms                                                      | 7.37 ms: 1.01x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 65.1 ms: 1.01x faster                                              |
| crypto_pyaes              | 72.8 ms                                                      | 72.4 ms: 1.01x faster                                              |
| python_startup_no_site    | 8.94 ms                                                      | 8.93 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                             |
| 2to3                      | 291 ms                                                       | 291 ms: 1.00x slower                                               |
| spectral_norm             | 97.4 ms                                                      | 97.8 ms: 1.00x slower                                              |
| pidigits                  | 253 ms                                                       | 254 ms: 1.00x slower                                               |
| bpe_tokeniser             | 5.10 sec                                                     | 5.13 sec: 1.01x slower                                             |
| sqlglot_transpile         | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                              |
| meteor_contest            | 128 ms                                                       | 129 ms: 1.01x slower                                               |
| sympy_integrate           | 23.3 ms                                                      | 23.5 ms: 1.01x slower                                              |
| sqlglot_optimize          | 59.7 ms                                                      | 60.1 ms: 1.01x slower                                              |
| thrift                    | 877 us                                                       | 882 us: 1.01x slower                                               |
| tomli_loads               | 2.41 sec                                                     | 2.42 sec: 1.01x slower                                             |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                               |
| telco                     | 8.58 ms                                                      | 8.65 ms: 1.01x slower                                              |
| sympy_expand              | 505 ms                                                       | 509 ms: 1.01x slower                                               |
| mdp                       | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                             |
| sympy_str                 | 296 ms                                                       | 299 ms: 1.01x slower                                               |
| fannkuch                  | 365 ms                                                       | 369 ms: 1.01x slower                                               |
| django_template           | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| pprint_safe_repr          | 812 ms                                                       | 823 ms: 1.01x slower                                               |
| generators                | 33.5 ms                                                      | 34.0 ms: 1.02x slower                                              |
| regex_dna                 | 244 ms                                                       | 248 ms: 1.02x slower                                               |
| typing_runtime_protocols  | 174 us                                                       | 177 us: 1.02x slower                                               |
| pprint_pformat            | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                             |
| scimark_monte_carlo       | 64.9 ms                                                      | 66.2 ms: 1.02x slower                                              |
| sqlite_synth              | 2.79 us                                                      | 2.84 us: 1.02x slower                                              |
| json_dumps                | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                              |
| asyncio_websockets        | 382 ms                                                       | 390 ms: 1.02x slower                                               |
| flaskblogging             | 4.62 ms                                                      | 4.72 ms: 1.02x slower                                              |
| async_tree_none_tg        | 340 ms                                                       | 347 ms: 1.02x slower                                               |
| xml_etree_generate        | 85.3 ms                                                      | 87.4 ms: 1.02x slower                                              |
| sqlglot_parse             | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                              |
| xml_etree_iterparse       | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| async_generators          | 359 ms                                                       | 368 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 615 ms: 1.03x slower                                               |
| aiohttp                   | 1.07 ms                                                      | 1.10 ms: 1.03x slower                                              |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                              |
| async_tree_memoization    | 452 ms                                                       | 466 ms: 1.03x slower                                               |
| go                        | 160 ms                                                       | 165 ms: 1.03x slower                                               |
| sqlglot_normalize         | 118 ms                                                       | 122 ms: 1.03x slower                                               |
| nqueens                   | 88.2 ms                                                      | 91.1 ms: 1.03x slower                                              |
| html5lib                  | 71.9 ms                                                      | 74.6 ms: 1.04x slower                                              |
| async_tree_io             | 847 ms                                                       | 879 ms: 1.04x slower                                               |
| nbody                     | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                              |
| dask                      | 379 ms                                                       | 396 ms: 1.04x slower                                               |
| docutils                  | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                             |
| unpickle_pure_python      | 214 us                                                       | 229 us: 1.07x slower                                               |
| gc_traversal              | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                              |
| regex_effbot              | 3.37 ms                                                      | 3.74 ms: 1.11x slower                                              |
| async_tree_io_tg          | 819 ms                                                       | 913 ms: 1.12x slower                                               |
| create_gc_cycles          | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                              |
| Geometric mean            | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (17): bench_mp_pool, async_tree_none, mako, json, tornado_http, bench_thread_pool, xml_etree_parse, genshi_xml, pickle, hexiom, scimark_sparse_mat_mult, python_startup, xml_etree_process, gunicorn, pickle_list, async_tree_cpu_io_mixed_tg, pylint

# HPT report

- Reliability score: 99.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x