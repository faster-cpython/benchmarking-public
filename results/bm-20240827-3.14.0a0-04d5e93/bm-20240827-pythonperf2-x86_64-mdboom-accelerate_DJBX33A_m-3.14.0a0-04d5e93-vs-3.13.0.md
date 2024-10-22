# Results vs. 3.13.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.5 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 317 ms: 1.18x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 814 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 794 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.4 ms: 1.04x faster                                                       |
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.7 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.53 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.37 sec: 1.02x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 86.7 ms: 1.02x slower                                                       |
| json_loads           | 24.0 us                                                      | 24.8 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 26.1 ms: 1.02x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 57.9 ms: 1.01x slower                                                       |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.3 us: 1.30x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 317 ms: 1.18x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.5 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| raytrace                   | 289 ms                                                       | 270 ms: 1.07x faster                                                        |
| scimark_sor                | 126 ms                                                       | 119 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.9 ms: 1.05x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 858 us: 1.05x faster                                                        |
| thrift                     | 877 us                                                       | 837 us: 1.05x faster                                                        |
| regex_dna                  | 244 ms                                                       | 233 ms: 1.05x faster                                                        |
| float                      | 81.9 ms                                                      | 78.4 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.89 sec: 1.04x faster                                                      |
| async_tree_io              | 847 ms                                                       | 814 ms: 1.04x faster                                                        |
| scimark_fft                | 314 ms                                                       | 303 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.0 ms: 1.03x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.84 us: 1.03x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 94.6 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 794 ms: 1.03x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.33 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 354 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| pyflate                    | 492 ms                                                       | 479 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.1 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.7 ms: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 26.1 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.29 us: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.23 ms: 1.02x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.37 sec: 1.02x faster                                                      |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 212 us: 1.01x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 804 ms: 1.01x faster                                                        |
| chaos                      | 61.7 ms                                                      | 61.2 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.39 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 97.0 ms: 1.00x faster                                                       |
| sqlglot_normalize          | 118 ms                                                       | 118 ms: 1.00x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.52 sec: 1.00x faster                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.5 ms: 1.01x slower                                                       |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 57.9 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.08 ms: 1.01x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 86.7 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.6 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.37 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.8 us: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.53 ms: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.38 ms: 1.06x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                       |
| go                         | 160 ms                                                       | 183 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (12): mako, nqueens, logging_silent, asyncio_tcp_ssl, pickle_pure_python, crypto_pyaes, pidigits, scimark_monte_carlo, pycparser, asyncio_websockets, bench_mp_pool, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x