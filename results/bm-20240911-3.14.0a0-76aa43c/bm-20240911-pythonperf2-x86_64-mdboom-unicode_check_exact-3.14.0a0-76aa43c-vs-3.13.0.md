# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                       |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                     |
| html5lib       | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                      |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                       |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 787 ms: 1.04x faster                                                       |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                       |
| async_generators           | 359 ms                                                       | 354 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                      |
| float          | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.03x faster                                                       |
| regex_v8       | 26.2 ms                                                      | 26.7 ms: 1.02x slower                                                      |
| regex_dna      | 244 ms                                                       | 254 ms: 1.04x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.18 us: 1.10x faster                                                      |
| pickle_dict          | 32.1 us                                                      | 29.6 us: 1.08x faster                                                      |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.4 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                       |
| unpickle             | 15.1 us                                                      | 15.3 us: 1.01x slower                                                      |
| unpickle_list        | 4.62 us                                                      | 4.76 us: 1.03x slower                                                      |
| tomli_loads          | 2.41 sec                                                     | 2.51 sec: 1.04x slower                                                     |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                      |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                      |
| genshi_xml      | 57.3 ms                                                      | 53.0 ms: 1.08x faster                                                      |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                      |
| django_template | 38.9 ms                                                      | 38.6 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 280 us: 1.42x faster                                                       |
| deepcopy_memo              | 39.5 us                                                      | 29.7 us: 1.33x faster                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                      |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                       |
| go                         | 160 ms                                                       | 136 ms: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                       |
| generators                 | 33.5 ms                                                      | 29.1 ms: 1.15x faster                                                      |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                      |
| unpack_sequence            | 56.8 ns                                                      | 51.6 ns: 1.10x faster                                                      |
| pickle_list                | 4.59 us                                                      | 4.18 us: 1.10x faster                                                      |
| pickle_dict                | 32.1 us                                                      | 29.6 us: 1.08x faster                                                      |
| genshi_xml                 | 57.3 ms                                                      | 53.0 ms: 1.08x faster                                                      |
| raytrace                   | 289 ms                                                       | 269 ms: 1.07x faster                                                       |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.07x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.1 ms: 1.07x faster                                                      |
| scimark_fft                | 314 ms                                                       | 295 ms: 1.06x faster                                                       |
| richards                   | 52.7 ms                                                      | 49.6 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.24 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.12 ms: 1.04x faster                                                      |
| async_tree_io_tg           | 819 ms                                                       | 787 ms: 1.04x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.82 us: 1.04x faster                                                      |
| bpe_tokeniser              | 5.10 sec                                                     | 4.92 sec: 1.04x faster                                                     |
| nbody                      | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                      |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                                      |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                       |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 874 us: 1.03x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| logging_simple             | 6.40 us                                                      | 6.21 us: 1.03x faster                                                      |
| scimark_lu                 | 97.8 ms                                                      | 95.2 ms: 1.03x faster                                                      |
| thrift                     | 877 us                                                       | 853 us: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                     |
| regex_compile              | 144 ms                                                       | 141 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 356 ms: 1.02x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 58.4 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                      |
| float                      | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                      |
| async_generators           | 359 ms                                                       | 354 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                       |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.8 ms: 1.01x faster                                                      |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 84.4 ms: 1.01x faster                                                      |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                     |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                      |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                      |
| sympy_expand               | 505 ms                                                       | 500 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 804 ms: 1.01x faster                                                       |
| chaos                      | 61.7 ms                                                      | 61.2 ms: 1.01x faster                                                      |
| hexiom                     | 6.33 ms                                                      | 6.29 ms: 1.01x faster                                                      |
| django_template            | 38.9 ms                                                      | 38.6 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                      |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.00x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 88.6 ms: 1.00x slower                                                      |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.44 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                      |
| logging_silent             | 97.7 ns                                                      | 98.7 ns: 1.01x slower                                                      |
| pyflate                    | 492 ms                                                       | 497 ms: 1.01x slower                                                       |
| unpickle                   | 15.1 us                                                      | 15.3 us: 1.01x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 66.6 ms: 1.02x slower                                                      |
| regex_v8                   | 26.2 ms                                                      | 26.7 ms: 1.02x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.2 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                      |
| unpickle_list              | 4.62 us                                                      | 4.76 us: 1.03x slower                                                      |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                     |
| tomli_loads                | 2.41 sec                                                     | 2.51 sec: 1.04x slower                                                     |
| regex_dna                  | 244 ms                                                       | 254 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.04x slower                                                      |
| coverage                   | 81.1 ms                                                      | 85.2 ms: 1.05x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.89 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                               |

Benchmark hidden because not significant (7): pidigits, pprint_pformat, bench_mp_pool, comprehensions, xml_etree_parse, pylint, json
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x