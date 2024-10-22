# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 57.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 306 ms: 1.05x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.8 ms: 1.02x faster                                                       |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| async_tree_none            | 372 ms                                                       | 340 ms: 1.09x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 414 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 583 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 805 ms: 1.02x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 394 ms: 1.03x slower                                                        |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.1 ms: 1.09x faster                                                       |
| nbody          | 88.0 ms                                                      | 82.6 ms: 1.06x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 82.5 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.22 ms: 1.13x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.7 ms: 1.08x slower                                                       |
| django_template | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 64.7 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 27.7 us: 1.42x faster                                                       |
| deepcopy                   | 397 us                                                       | 305 us: 1.30x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.5 ms: 1.18x faster                                                       |
| richards                   | 52.7 ms                                                      | 44.9 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.05 us: 1.16x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.22 ms: 1.13x faster                                                       |
| richards_super             | 59.8 ms                                                      | 53.0 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                        |
| pyflate                    | 492 ms                                                       | 445 ms: 1.11x faster                                                        |
| async_tree_none            | 372 ms                                                       | 340 ms: 1.09x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 414 ms: 1.09x faster                                                        |
| float                      | 81.9 ms                                                      | 75.1 ms: 1.09x faster                                                       |
| scimark_fft                | 314 ms                                                       | 293 ms: 1.07x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                       |
| nbody                      | 88.0 ms                                                      | 82.6 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| fannkuch                   | 365 ms                                                       | 346 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.09 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 70.3 ms: 1.04x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 82.5 ms: 1.03x faster                                                       |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.34 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 583 ms: 1.03x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 796 ms: 1.02x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 805 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| html5lib                   | 71.9 ms                                                      | 70.8 ms: 1.02x faster                                                       |
| coverage                   | 81.1 ms                                                      | 80.2 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.2 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 65.3 ms: 1.00x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.53 sec: 1.00x slower                                                      |
| bpe_tokeniser              | 5.10 sec                                                     | 5.12 sec: 1.00x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.47 us: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| go                         | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.25 us: 1.03x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 394 ms: 1.03x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 929 us: 1.03x slower                                                        |
| raytrace                   | 289 ms                                                       | 298 ms: 1.03x slower                                                        |
| sympy_expand               | 505 ms                                                       | 521 ms: 1.03x slower                                                        |
| thrift                     | 877 us                                                       | 908 us: 1.04x slower                                                        |
| sympy_str                  | 296 ms                                                       | 308 ms: 1.04x slower                                                        |
| scimark_sor                | 126 ms                                                       | 131 ms: 1.04x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 102 ns: 1.05x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 6.66 ms: 1.05x slower                                                       |
| 2to3                       | 291 ms                                                       | 306 ms: 1.05x slower                                                        |
| generators                 | 33.5 ms                                                      | 35.3 ms: 1.06x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.06x slower                                                       |
| dask                       | 379 ms                                                       | 400 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 63.2 ms: 1.06x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                                       |
| json                       | 5.22 ms                                                      | 5.54 ms: 1.06x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 164 ms: 1.07x slower                                                        |
| chaos                      | 61.7 ms                                                      | 66.0 ms: 1.07x slower                                                       |
| pylint                     | 346 ms                                                       | 372 ms: 1.07x slower                                                        |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 3.66 ms: 1.07x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 94.8 ms: 1.07x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 28.7 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.44 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 189 us: 1.09x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 25.5 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.93 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 130 ms: 1.10x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| django_template            | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 64.7 ms: 1.13x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 114 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (6): xml_etree_iterparse, asyncio_tcp, asyncio_tcp_ssl, pycparser, json_dumps, bench_mp_pool
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 57.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x