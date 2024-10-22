# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 361 ms: 1.00x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.3 ms: 1.05x faster                                                       |
| nbody          | 88.0 ms                                                      | 87.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.50 us: 1.02x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                       |
| unpickle_list        | 4.62 us                                                      | 4.56 us: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pickle_dict          | 32.1 us                                                      | 32.4 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| unpickle             | 15.1 us                                                      | 15.5 us: 1.02x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.53 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (3): pickle_pure_python, pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 38.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.2 us: 1.31x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                       |
| go                         | 160 ms                                                       | 134 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                        |
| unpack_sequence            | 56.8 ns                                                      | 48.7 ns: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.16x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.3 ms: 1.14x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                        |
| scimark_sor                | 126 ms                                                       | 117 ms: 1.07x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                       |
| raytrace                   | 289 ms                                                       | 272 ms: 1.06x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.5 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.3 ms: 1.05x faster                                                       |
| scimark_fft                | 314 ms                                                       | 300 ms: 1.05x faster                                                        |
| float                      | 81.9 ms                                                      | 78.3 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 865 us: 1.04x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                      |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.33 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.87 us: 1.03x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.97 sec: 1.03x faster                                                      |
| fannkuch                   | 365 ms                                                       | 356 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.7 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                                        |
| thrift                     | 877 us                                                       | 859 us: 1.02x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.21 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.50 us: 1.02x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| django_template            | 38.9 ms                                                      | 38.3 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| unpickle_list              | 4.62 us                                                      | 4.56 us: 1.01x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| nbody                      | 88.0 ms                                                      | 87.2 ms: 1.01x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 500 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 88.5 ms: 1.00x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.00x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 815 ms: 1.00x slower                                                        |
| async_generators           | 359 ms                                                       | 361 ms: 1.00x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                      |
| pickle_dict                | 32.1 us                                                      | 32.4 us: 1.01x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.8 ms: 1.01x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| chaos                      | 61.7 ms                                                      | 62.7 ms: 1.02x slower                                                       |
| coverage                   | 81.1 ms                                                      | 82.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| unpickle                   | 15.1 us                                                      | 15.5 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 67.3 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.8 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.85 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.53 sec: 1.05x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.64 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.45 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (13): mako, pickle_pure_python, logging_simple, sqlglot_normalize, pickle, pyflate, python_startup_no_site, scimark_sparse_mat_mult, pidigits, json, xml_etree_generate, pylint, typing_runtime_protocols
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x