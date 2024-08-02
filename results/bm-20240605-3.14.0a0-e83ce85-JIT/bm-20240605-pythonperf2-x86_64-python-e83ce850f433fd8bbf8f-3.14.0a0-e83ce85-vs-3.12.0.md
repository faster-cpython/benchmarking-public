# Results vs. 3.12.0

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-x86_64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.01x slower
- HPT reliability: 51.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                      |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 439 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 352 ms: 1.22x faster                                                        |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 893 ms: 1.17x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 918 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 482 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 629 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.1 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 73.2 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| xml_etree_process    | 58.4 ms                                                      | 58.1 ms: 1.01x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 33.3 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.59 us: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.96 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.46 ms: 1.10x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.19 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 41.8 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 439 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 352 ms: 1.22x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                       |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 893 ms: 1.17x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 69.9 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 918 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 482 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 629 ms: 1.11x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.19 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.1 ms: 1.08x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.95 ms: 1.06x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                       |
| scimark_fft                | 301 ms                                                       | 284 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.5 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.7 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| float                      | 76.6 ms                                                      | 73.2 ms: 1.05x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.16 us: 1.05x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.58 us: 1.02x faster                                                       |
| raytrace                   | 298 ms                                                       | 292 ms: 1.02x faster                                                        |
| fannkuch                   | 350 ms                                                       | 344 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 799 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                      | 58.1 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.00x faster                                                      |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 382 ms: 1.01x slower                                                        |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 37.5 us: 1.02x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.3 us: 1.02x slower                                                       |
| async_generators           | 390 ms                                                       | 399 ms: 1.02x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.02x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                       |
| dask                       | 392 ms                                                       | 405 ms: 1.03x slower                                                        |
| sympy_str                  | 302 ms                                                       | 312 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.59 us: 1.04x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                      |
| json                       | 5.12 ms                                                      | 5.32 ms: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.8 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.96 us: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                       |
| pyflate                    | 439 ms                                                       | 469 ms: 1.07x slower                                                        |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| go                         | 150 ms                                                       | 161 ms: 1.07x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.62 us: 1.07x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                      |
| django_template            | 38.2 ms                                                      | 41.8 ms: 1.10x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.46 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 127 ms: 1.10x slower                                                        |
| sympy_expand               | 484 ms                                                       | 531 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 63.3 ms: 1.10x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 99.7 ms: 1.11x slower                                                       |
| deepcopy                   | 368 us                                                       | 411 us: 1.11x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.76 ms: 1.13x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 107 ns: 1.14x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 113 ms: 1.14x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.75 ms: 1.16x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.27 ms: 1.19x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| scimark_sor                | 109 ms                                                       | 130 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.96 ms: 1.23x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.38 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (7): pickle_pure_python, dulwich_log, bench_thread_pool, asyncio_websockets, xml_etree_parse, sqlite_synth, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 51.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x