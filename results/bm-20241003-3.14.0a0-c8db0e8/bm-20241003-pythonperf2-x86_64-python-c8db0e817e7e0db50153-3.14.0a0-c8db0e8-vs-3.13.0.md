# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-x86_64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.03x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 786 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| async_generators           | 359 ms                                                       | 357 ms: 1.01x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.0 ms: 1.05x faster                                                       |
| nbody          | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.2 ms: 1.00x faster                                                       |
| regex_dna      | 244 ms                                                       | 248 ms: 1.02x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| pickle_dict          | 32.1 us                                                      | 31.6 us: 1.01x faster                                                       |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.55 us: 1.01x faster                                                       |
| unpickle             | 15.1 us                                                      | 15.4 us: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| unpickle_list        | 4.62 us                                                      | 4.74 us: 1.03x slower                                                       |
| xml_etree_parse      | 145 ms                                                       | 150 ms: 1.04x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.56 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                       |
| django_template | 38.9 ms                                                      | 40.6 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 282 us: 1.41x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 28.8 us: 1.37x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| go                         | 160 ms                                                       | 132 ms: 1.21x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.8 ms: 1.16x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| scimark_fft                | 314 ms                                                       | 290 ms: 1.08x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.7 ms: 1.08x faster                                                       |
| raytrace                   | 289 ms                                                       | 269 ms: 1.07x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.4 ms: 1.06x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                       |
| float                      | 81.9 ms                                                      | 78.0 ms: 1.05x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.2 ms: 1.05x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.74 us: 1.05x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.20 ms: 1.05x faster                                                       |
| scimark_sor                | 126 ms                                                       | 120 ms: 1.05x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 93.7 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.13 us: 1.04x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 786 ms: 1.04x faster                                                        |
| fannkuch                   | 365 ms                                                       | 352 ms: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| sympy_expand               | 505 ms                                                       | 488 ms: 1.03x faster                                                        |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.95 sec: 1.03x faster                                                      |
| thrift                     | 877 us                                                       | 852 us: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                       |
| unpack_sequence            | 56.8 ns                                                      | 55.3 ns: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.03x faster                                                      |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.03x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.46 sec: 1.03x faster                                                      |
| hexiom                     | 6.33 ms                                                      | 6.19 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.34 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 58.7 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.22 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| pickle_dict                | 32.1 us                                                      | 31.6 us: 1.01x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.9 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.55 us: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                       |
| async_generators           | 359 ms                                                       | 357 ms: 1.01x faster                                                        |
| pyflate                    | 492 ms                                                       | 490 ms: 1.00x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.2 ms: 1.00x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 88.9 ms: 1.01x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 98.6 ns: 1.01x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.0 ms: 1.01x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.3 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                      |
| unpickle                   | 15.1 us                                                      | 15.4 us: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.9 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| regex_dna                  | 244 ms                                                       | 248 ms: 1.02x slower                                                        |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 4.74 us: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| nbody                      | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| xml_etree_parse            | 145 ms                                                       | 150 ms: 1.04x slower                                                        |
| django_template            | 38.9 ms                                                      | 40.6 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.56 sec: 1.07x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.45 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 1.40 sec: 301.09x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (8): comprehensions, pylint, spectral_norm, asyncio_tcp_ssl, python_startup_no_site, pidigits, bench_thread_pool, pprint_safe_repr
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x