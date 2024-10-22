# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.01x faster
- HPT reliability: 90.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 310 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.12x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.3 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_io              | 847 ms                                                       | 801 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 801 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.60 sec: 1.01x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 73.7 ms: 1.11x faster                                                       |
| nbody          | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                                      |
| xml_etree_process   | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| xml_etree_generate  | 85.3 ms                                                      | 78.7 ms: 1.08x faster                                                       |
| pickle_list         | 4.59 us                                                      | 4.51 us: 1.02x faster                                                       |
| xml_etree_iterparse | 100 ms                                                       | 98.3 ms: 1.02x faster                                                       |
| xml_etree_parse     | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_dumps          | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| pickle_dict         | 32.1 us                                                      | 32.4 us: 1.01x slower                                                       |
| unpickle            | 15.1 us                                                      | 15.4 us: 1.02x slower                                                       |
| pickle              | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| unpickle_list       | 4.62 us                                                      | 4.75 us: 1.03x slower                                                       |
| pickle_pure_python  | 318 us                                                       | 328 us: 1.03x slower                                                        |
| json_loads          | 24.0 us                                                      | 24.7 us: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 8.97 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.10 ms: 1.14x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.3 ms: 1.06x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 62.3 ms: 1.09x slower                                                       |
| django_template | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 26.9 us: 1.47x faster                                                       |
| deepcopy                   | 397 us                                                       | 289 us: 1.37x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.88 us: 1.23x faster                                                       |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.21x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.3 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| richards                   | 52.7 ms                                                      | 44.9 ms: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.10 ms: 1.14x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                                      |
| richards_super             | 59.8 ms                                                      | 52.9 ms: 1.13x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| float                      | 81.9 ms                                                      | 73.7 ms: 1.11x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| scimark_fft                | 314 ms                                                       | 283 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 78.7 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 3.96 ms: 1.08x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.19 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.78 sec: 1.07x faster                                                      |
| telco                      | 8.58 ms                                                      | 8.05 ms: 1.07x faster                                                       |
| go                         | 160 ms                                                       | 151 ms: 1.06x faster                                                        |
| pyflate                    | 492 ms                                                       | 465 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 801 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.05x faster                                                        |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 70.6 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 789 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.72 us: 1.03x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 70.3 ms: 1.02x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 801 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| pickle_list                | 4.59 us                                                      | 4.51 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 98.3 ms: 1.02x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 96.5 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| fannkuch                   | 365 ms                                                       | 361 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 8.97 ms: 1.00x slower                                                       |
| logging_format             | 7.07 us                                                      | 7.13 us: 1.01x slower                                                       |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| pickle_dict                | 32.1 us                                                      | 32.4 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.60 sec: 1.01x slower                                                      |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                                      |
| unpickle                   | 15.1 us                                                      | 15.4 us: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| thrift                     | 877 us                                                       | 896 us: 1.02x slower                                                        |
| logging_simple             | 6.40 us                                                      | 6.54 us: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| unpickle_list              | 4.62 us                                                      | 4.75 us: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                        |
| json_loads                 | 24.0 us                                                      | 24.7 us: 1.03x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 179 us: 1.03x slower                                                        |
| sympy_expand               | 505 ms                                                       | 524 ms: 1.04x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 102 ns: 1.04x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 939 us: 1.04x slower                                                        |
| sympy_str                  | 296 ms                                                       | 309 ms: 1.04x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.1 us: 1.05x slower                                                       |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 28.3 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 310 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.2 ms: 1.07x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.40 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.08x slower                                                       |
| chaos                      | 61.7 ms                                                      | 66.6 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 62.3 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 129 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                                        |
| raytrace                   | 289 ms                                                       | 316 ms: 1.09x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 6.95 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.6 ms: 1.10x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 97.2 ms: 1.10x slower                                                       |
| generators                 | 33.5 ms                                                      | 36.9 ms: 1.10x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.17 ms: 1.11x slower                                                       |
| django_template            | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.12x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 26.3 ms: 1.13x slower                                                       |
| pylint                     | 346 ms                                                       | 409 ms: 1.18x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 91.8 ns: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (3): unpickle_pure_python, json, coverage
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 90.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x