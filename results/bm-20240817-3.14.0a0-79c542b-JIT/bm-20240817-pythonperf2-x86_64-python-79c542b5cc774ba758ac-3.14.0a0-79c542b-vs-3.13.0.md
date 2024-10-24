# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.01x faster
- HPT reliability: 76.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.28 sec: 1.17x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.4 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 384 ms: 1.20x faster                                                        |
| async_tree_none            | 372 ms                                                       | 321 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 560 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 773 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (2): coroutines, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.0 ms: 1.09x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_dna      | 244 ms                                                       | 261 ms: 1.07x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.67 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 77.7 ms: 1.10x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.4 ms: 1.05x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 98.0 ms: 1.02x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                        |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.16 ms: 1.14x faster                                                       |
| django_template | 38.9 ms                                                      | 42.1 ms: 1.08x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 64.5 ms: 1.13x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 30.3 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 27.2 us: 1.45x faster                                                       |
| deepcopy                   | 397 us                                                       | 301 us: 1.32x faster                                                        |
| scimark_sor                | 126 ms                                                       | 101 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| richards                   | 52.7 ms                                                      | 43.8 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 384 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.1 ms: 1.19x faster                                                       |
| richards_super             | 59.8 ms                                                      | 50.7 ms: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 321 ms: 1.16x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.16 ms: 1.14x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                                      |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| scimark_fft                | 314 ms                                                       | 285 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 77.7 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.11 ms: 1.10x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                        |
| telco                      | 8.58 ms                                                      | 7.85 ms: 1.09x faster                                                       |
| float                      | 81.9 ms                                                      | 75.0 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 560 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.00 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 773 ms: 1.06x faster                                                        |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 69.2 ms: 1.05x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.4 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.87 sec: 1.05x faster                                                      |
| coverage                   | 81.1 ms                                                      | 78.0 ms: 1.04x faster                                                       |
| pyflate                    | 492 ms                                                       | 475 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.2 ms: 1.03x faster                                                       |
| raytrace                   | 289 ms                                                       | 283 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 98.0 ms: 1.02x faster                                                       |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 804 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.4 ms: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.16 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| go                         | 160 ms                                                       | 163 ms: 1.01x slower                                                        |
| logging_simple             | 6.40 us                                                      | 6.49 us: 1.01x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                      |
| json                       | 5.22 ms                                                      | 5.31 ms: 1.02x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 99.5 ns: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 920 us: 1.02x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.58 sec: 1.02x slower                                                      |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                        |
| thrift                     | 877 us                                                       | 898 us: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 396 ms: 1.04x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.84 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.4 ms: 1.05x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.05x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                                       |
| sympy_expand               | 505 ms                                                       | 535 ms: 1.06x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.37 ms: 1.06x slower                                                       |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                        |
| sympy_str                  | 296 ms                                                       | 315 ms: 1.06x slower                                                        |
| chaos                      | 61.7 ms                                                      | 65.9 ms: 1.07x slower                                                       |
| regex_dna                  | 244 ms                                                       | 261 ms: 1.07x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 188 us: 1.08x slower                                                        |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                                        |
| django_template            | 38.9 ms                                                      | 42.1 ms: 1.08x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.67 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 129 ms: 1.09x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.93 ms: 1.09x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.95 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.96 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 65.9 ms: 1.10x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 172 ms: 1.12x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 99.0 ms: 1.12x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 64.5 ms: 1.13x slower                                                       |
| generators                 | 33.5 ms                                                      | 37.8 ms: 1.13x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 30.3 ms: 1.14x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 26.7 ms: 1.15x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.28 sec: 1.17x slower                                                      |
| pylint                     | 346 ms                                                       | 405 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (4): pycparser, coroutines, asyncio_tcp, pickle_pure_python
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 76.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x