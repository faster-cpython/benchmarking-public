# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 284 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 809 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 785 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                       |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| regex_dna      | 244 ms                                                       | 248 ms: 1.02x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.1 us                                                      | 30.0 us: 1.07x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.30 us: 1.07x faster                                                       |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| unpickle_list        | 4.62 us                                                      | 4.57 us: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.8 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.64 sec: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.0 us: 1.31x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| go                         | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.7 ms: 1.13x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| scimark_sor                | 126 ms                                                       | 115 ms: 1.09x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 30.0 us: 1.07x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.0 ms: 1.07x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.30 us: 1.07x faster                                                       |
| richards                   | 52.7 ms                                                      | 49.7 ms: 1.06x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| scimark_fft                | 314 ms                                                       | 298 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 809 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 785 ms: 1.04x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 865 us: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.89 sec: 1.04x faster                                                      |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.29 ms: 1.04x faster                                                       |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.16 ms: 1.03x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| float                      | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                       | 284 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.3 ms: 1.02x faster                                                       |
| raytrace                   | 289 ms                                                       | 283 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 22.8 ms: 1.02x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 96.0 ms: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                                      |
| thrift                     | 877 us                                                       | 863 us: 1.02x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                                        |
| sympy_expand               | 505 ms                                                       | 498 ms: 1.01x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.9 ms: 1.01x faster                                                       |
| unpickle_list              | 4.62 us                                                      | 4.57 us: 1.01x faster                                                       |
| pyflate                    | 492 ms                                                       | 487 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 803 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| fannkuch                   | 365 ms                                                       | 361 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                        |
| nqueens                    | 88.2 ms                                                      | 87.6 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.8 ms: 1.01x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.0 ms: 1.01x slower                                                       |
| json                       | 5.22 ms                                                      | 5.26 ms: 1.01x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.50 us: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.0 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.6 ms: 1.02x slower                                                       |
| regex_dna                  | 244 ms                                                       | 248 ms: 1.02x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.21 us: 1.02x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.9 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 60.1 ns: 1.06x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.64 sec: 1.10x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.78 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (13): bench_mp_pool, comprehensions, mako, deltablue, async_generators, unpickle, meteor_contest, hexiom, coroutines, logging_silent, nbody, pickle_pure_python, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x