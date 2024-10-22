# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 396 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                       |
| float          | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_dna      | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.6 ms: 1.01x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.00x faster                                                        |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.02x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.59 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.8 us: 1.32x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| go                         | 160 ms                                                       | 135 ms: 1.19x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.3 ms: 1.18x faster                                                       |
| scimark_sor                | 126 ms                                                       | 108 ms: 1.16x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 396 ms: 1.14x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                                       |
| raytrace                   | 289 ms                                                       | 271 ms: 1.07x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.3 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.13 ms: 1.06x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| richards                   | 52.7 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.85 sec: 1.05x faster                                                      |
| bench_thread_pool          | 901 us                                                       | 861 us: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                       | 300 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.11 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 93.9 ms: 1.04x faster                                                       |
| tornado_http               | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                      |
| logging_format             | 7.07 us                                                      | 6.80 us: 1.04x faster                                                       |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                       |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| float                      | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 354 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| thrift                     | 877 us                                                       | 852 us: 1.03x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                       |
| regex_dna                  | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.27 us: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| sympy_expand               | 505 ms                                                       | 499 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.3 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.27 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 72.1 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 806 ms: 1.01x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.39 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.00x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.00x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| pyflate                    | 492 ms                                                       | 496 ms: 1.01x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 89.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.8 ms: 1.01x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.6 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 68.2 ms: 1.04x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.59 sec: 1.07x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, mako, json, coverage, xml_etree_iterparse, logging_silent, async_generators, sqlglot_transpile, chaos, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x