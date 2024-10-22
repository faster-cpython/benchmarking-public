# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.01x faster
- HPT reliability: 84.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 310 ms: 1.07x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| html5lib       | 71.9 ms                                                      | 68.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 396 ms: 1.16x faster                                                        |
| async_tree_none            | 372 ms                                                       | 330 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 315 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 567 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_io, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.33 ms: 1.01x faster                                                       |
| regex_v8       | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.15 sec: 1.12x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 79.0 ms: 1.08x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 98.6 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 61.3 ms: 1.07x slower                                                       |
| django_template | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.4 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 26.7 us: 1.48x faster                                                       |
| deepcopy                   | 397 us                                                       | 303 us: 1.31x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.21x faster                                                       |
| richards                   | 52.7 ms                                                      | 43.7 ms: 1.21x faster                                                       |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| richards_super             | 59.8 ms                                                      | 50.3 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 396 ms: 1.16x faster                                                        |
| async_tree_none            | 372 ms                                                       | 330 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.15 sec: 1.12x faster                                                      |
| xml_etree_process          | 60.9 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                       |
| float                      | 81.9 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 79.0 ms: 1.08x faster                                                       |
| scimark_fft                | 314 ms                                                       | 291 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.73 sec: 1.08x faster                                                      |
| async_tree_none_tg         | 340 ms                                                       | 315 ms: 1.08x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.18 ms: 1.07x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.11 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 567 ms: 1.06x faster                                                        |
| go                         | 160 ms                                                       | 152 ms: 1.05x faster                                                        |
| pyflate                    | 492 ms                                                       | 468 ms: 1.05x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 68.9 ms: 1.04x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 69.7 ms: 1.04x faster                                                       |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 780 ms: 1.04x faster                                                        |
| fannkuch                   | 365 ms                                                       | 350 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.14 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| coverage                   | 81.1 ms                                                      | 79.2 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 98.6 ms: 1.01x faster                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.33 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                      |
| scimark_lu                 | 97.8 ms                                                      | 96.7 ms: 1.01x faster                                                       |
| logging_format             | 7.07 us                                                      | 7.00 us: 1.01x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| thrift                     | 877 us                                                       | 894 us: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.02x slower                                                      |
| bench_thread_pool          | 901 us                                                       | 925 us: 1.03x slower                                                        |
| json                       | 5.22 ms                                                      | 5.37 ms: 1.03x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| sympy_expand               | 505 ms                                                       | 528 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 182 us: 1.05x slower                                                        |
| sympy_str                  | 296 ms                                                       | 311 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.6 ms: 1.06x slower                                                       |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.38 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 310 ms: 1.07x slower                                                        |
| raytrace                   | 289 ms                                                       | 309 ms: 1.07x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 61.3 ms: 1.07x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.09x slower                                                       |
| django_template            | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 130 ms: 1.09x slower                                                        |
| chaos                      | 61.7 ms                                                      | 67.6 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.6 ms: 1.10x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 29.4 ms: 1.10x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 7.00 ms: 1.11x slower                                                       |
| generators                 | 33.5 ms                                                      | 37.2 ms: 1.11x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 98.2 ms: 1.11x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.20 ms: 1.12x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 26.4 ms: 1.13x slower                                                       |
| pylint                     | 346 ms                                                       | 409 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_io, logging_simple, pycparser, asyncio_tcp_ssl, dulwich_log, pickle_pure_python, tornado_http, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 84.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x