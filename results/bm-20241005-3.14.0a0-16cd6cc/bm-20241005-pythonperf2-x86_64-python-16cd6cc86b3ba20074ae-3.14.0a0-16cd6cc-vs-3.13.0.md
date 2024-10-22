# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.04x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.0 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 786 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 821 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                                       |
| nbody          | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                       |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 242 ms: 1.01x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 86.1 ms: 1.01x slower                                                       |
| xml_etree_process    | 60.9 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 218 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| pickle_dict          | 32.1 us                                                      | 32.8 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| pickle_list          | 4.59 us                                                      | 4.71 us: 1.03x slower                                                       |
| unpickle_list        | 4.62 us                                                      | 4.76 us: 1.03x slower                                                       |
| xml_etree_parse      | 145 ms                                                       | 150 ms: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.54 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 25.5 ms: 1.04x faster                                                       |
| django_template | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.5 us: 1.34x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                       |
| go                         | 160 ms                                                       | 135 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 29.1 ms: 1.15x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| unpack_sequence            | 56.8 ns                                                      | 50.7 ns: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.07x faster                                                        |
| raytrace                   | 289 ms                                                       | 273 ms: 1.06x faster                                                        |
| scimark_fft                | 314 ms                                                       | 297 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.19 ms: 1.05x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 93.5 ms: 1.05x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.5 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 786 ms: 1.04x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.80 us: 1.04x faster                                                       |
| float                      | 81.9 ms                                                      | 78.8 ms: 1.04x faster                                                       |
| tornado_http               | 120 ms                                                       | 115 ms: 1.04x faster                                                        |
| richards_super             | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                                       |
| async_tree_io              | 847 ms                                                       | 821 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.2 ms: 1.03x faster                                                       |
| sympy_expand               | 505 ms                                                       | 491 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                        |
| fannkuch                   | 365 ms                                                       | 355 ms: 1.03x faster                                                        |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.03x faster                                                        |
| thrift                     | 877 us                                                       | 855 us: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.98 sec: 1.02x faster                                                      |
| sqlite_synth               | 2.79 us                                                      | 2.72 us: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.48 sec: 1.02x faster                                                      |
| logging_simple             | 6.40 us                                                      | 6.28 us: 1.02x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.23 ms: 1.02x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.35 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 58.8 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.0 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 803 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.01x faster                                                        |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| regex_dna                  | 244 ms                                                       | 242 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| nqueens                    | 88.2 ms                                                      | 88.8 ms: 1.01x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 86.1 ms: 1.01x slower                                                       |
| xml_etree_process          | 60.9 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.6 ms: 1.02x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 218 us: 1.02x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 919 us: 1.02x slower                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 74.2 ms: 1.02x slower                                                       |
| chaos                      | 61.7 ms                                                      | 63.0 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| nbody                      | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                       |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                       |
| pickle_dict                | 32.1 us                                                      | 32.8 us: 1.02x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| pyflate                    | 492 ms                                                       | 504 ms: 1.03x slower                                                        |
| pickle_list                | 4.59 us                                                      | 4.71 us: 1.03x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.41 ms: 1.03x slower                                                       |
| unpickle_list              | 4.62 us                                                      | 4.76 us: 1.03x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| xml_etree_parse            | 145 ms                                                       | 150 ms: 1.03x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| coverage                   | 81.1 ms                                                      | 85.7 ms: 1.06x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.54 sec: 1.06x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.81 ms: 1.17x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 1.33 sec: 285.72x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (10): typing_runtime_protocols, pycparser, unpickle, async_generators, spectral_norm, pylint, python_startup, python_startup_no_site, pidigits, mako
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x