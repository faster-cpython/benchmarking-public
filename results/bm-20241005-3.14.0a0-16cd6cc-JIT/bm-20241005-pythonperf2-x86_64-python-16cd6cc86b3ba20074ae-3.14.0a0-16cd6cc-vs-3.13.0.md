# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.06x slower
- HPT reliability: 71.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 317 ms: 1.09x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.2 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 123 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 324 ms: 1.15x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 406 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 392 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.5 ms: 1.08x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                       |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 26.6 ms: 1.02x slower                                                       |
| regex_dna      | 244 ms                                                       | 252 ms: 1.03x slower                                                        |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.75 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                                      |
| xml_etree_generate   | 85.3 ms                                                      | 78.4 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.23 us: 1.08x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 30.4 us: 1.05x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 140 ms: 1.04x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 97.5 ms: 1.03x faster                                                       |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| unpickle_list        | 4.62 us                                                      | 4.58 us: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                       |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                       |
| django_template | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.0 ms: 1.09x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 63.6 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.2 us: 1.40x faster                                                       |
| deepcopy                   | 397 us                                                       | 300 us: 1.32x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                       |
| richards                   | 52.7 ms                                                      | 44.7 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.9 ms: 1.17x faster                                                       |
| scimark_sor                | 126 ms                                                       | 107 ms: 1.17x faster                                                        |
| richards_super             | 59.8 ms                                                      | 51.8 ms: 1.15x faster                                                       |
| async_tree_none            | 372 ms                                                       | 324 ms: 1.15x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.61 ms: 1.13x faster                                                       |
| scimark_fft                | 314 ms                                                       | 280 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 406 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                                      |
| xml_etree_generate         | 85.3 ms                                                      | 78.4 ms: 1.09x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| float                      | 81.9 ms                                                      | 75.5 ms: 1.08x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.23 us: 1.08x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 755 ms: 1.08x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.21 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.80 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| pickle_dict                | 32.1 us                                                      | 30.4 us: 1.05x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 779 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.04x faster                                                      |
| go                         | 160 ms                                                       | 154 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.12 ms: 1.04x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 140 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 94.4 ms: 1.04x faster                                                       |
| pyflate                    | 492 ms                                                       | 478 ms: 1.03x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 97.5 ms: 1.03x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.1 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.2 ms: 1.01x faster                                                       |
| unpickle_list              | 4.62 us                                                      | 4.58 us: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| pidigits                   | 253 ms                                                       | 254 ms: 1.01x slower                                                        |
| json                       | 5.22 ms                                                      | 5.26 ms: 1.01x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.6 ms: 1.02x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| tornado_http               | 120 ms                                                       | 123 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.02x slower                                                        |
| thrift                     | 877 us                                                       | 899 us: 1.03x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.26 us: 1.03x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| regex_dna                  | 244 ms                                                       | 252 ms: 1.03x slower                                                        |
| coverage                   | 81.1 ms                                                      | 84.0 ms: 1.03x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.62 us: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.30 ms: 1.05x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.2 ms: 1.05x slower                                                       |
| sympy_expand               | 505 ms                                                       | 532 ms: 1.05x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 952 us: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 185 us: 1.06x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.87 ms: 1.06x slower                                                       |
| django_template            | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                       |
| sympy_str                  | 296 ms                                                       | 322 ms: 1.09x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 29.0 ms: 1.09x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                       |
| 2to3                       | 291 ms                                                       | 317 ms: 1.09x slower                                                        |
| chaos                      | 61.7 ms                                                      | 67.3 ms: 1.09x slower                                                       |
| async_generators           | 359 ms                                                       | 392 ms: 1.09x slower                                                        |
| raytrace                   | 289 ms                                                       | 320 ms: 1.11x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 63.6 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.75 ms: 1.11x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.54 ms: 1.11x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 7.08 ms: 1.12x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 135 ms: 1.14x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 101 ms: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                      |
| generators                 | 33.5 ms                                                      | 38.4 ms: 1.15x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 27.3 ms: 1.17x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 70.2 ms: 1.18x slower                                                       |
| pylint                     | 346 ms                                                       | 419 ms: 1.21x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 89.3 ns: 1.57x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 1.87 sec: 401.92x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (3): logging_silent, json_loads, unpickle
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 71.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x