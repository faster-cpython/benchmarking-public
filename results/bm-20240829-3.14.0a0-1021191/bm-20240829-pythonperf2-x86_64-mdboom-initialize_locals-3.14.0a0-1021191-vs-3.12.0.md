# Results vs. 3.12.0

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 97.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.01x faster                                                     |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                   |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.38x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 551 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                     |
| nbody          | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                                    |
| float          | 76.6 ms                                                      | 78.4 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                    |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                     |
| regex_compile  | 144 ms                                                       | 142 ms: 1.01x faster                                                     |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                     |
| xml_etree_generate   | 86.1 ms                                                      | 85.7 ms: 1.00x faster                                                    |
| xml_etree_process    | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                    |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                    |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.04x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                    |
| tomli_loads          | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                             |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                    |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.03x slower                                                    |
| django_template | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.38x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                     |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                    |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 551 ms: 1.27x faster                                                     |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.25x faster                                                    |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                    |
| logging_format             | 7.48 us                                                      | 6.78 us: 1.10x faster                                                    |
| bench_thread_pool          | 950 us                                                       | 866 us: 1.10x faster                                                     |
| go                         | 150 ms                                                       | 137 ms: 1.10x faster                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                    |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                    |
| logging_simple             | 6.71 us                                                      | 6.27 us: 1.07x faster                                                    |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                     |
| bench_mp_pool              | 4.76 ms                                                      | 4.53 ms: 1.05x faster                                                    |
| async_generators           | 390 ms                                                       | 371 ms: 1.05x faster                                                     |
| raytrace                   | 298 ms                                                       | 285 ms: 1.05x faster                                                     |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                     |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                     |
| nbody                      | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                                    |
| chaos                      | 64.0 ms                                                      | 61.8 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.7 ms: 1.03x faster                                                    |
| scimark_lu                 | 98.8 ms                                                      | 95.6 ms: 1.03x faster                                                    |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                    |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.02x faster                                                     |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.02x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                   |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 807 ms                                                       | 795 ms: 1.01x faster                                                     |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.01x faster                                                   |
| regex_compile              | 144 ms                                                       | 142 ms: 1.01x faster                                                     |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                   |
| 2to3                       | 285 ms                                                       | 284 ms: 1.01x faster                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 85.7 ms: 1.00x faster                                                    |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.02x slower                                                   |
| xml_etree_process          | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                    |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.30 ms: 1.02x slower                                                    |
| float                      | 76.6 ms                                                      | 78.4 ms: 1.02x slower                                                    |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                    |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.03x slower                                                    |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                                    |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                     |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 6.20 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.04x slower                                                    |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.04x slower                                                     |
| sympy_expand               | 484 ms                                                       | 506 ms: 1.05x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                    |
| spectral_norm              | 91.6 ms                                                      | 96.5 ms: 1.05x slower                                                    |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                    |
| pyflate                    | 439 ms                                                       | 469 ms: 1.07x slower                                                     |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                    |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                     |
| django_template            | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                    |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                     |
| richards                   | 45.7 ms                                                      | 50.0 ms: 1.09x slower                                                    |
| richards_super             | 51.3 ms                                                      | 56.5 ms: 1.10x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                     |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                    |
| tomli_loads                | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                                   |
| coverage                   | 66.7 ms                                                      | 80.1 ms: 1.20x slower                                                    |
| telco                      | 6.96 ms                                                      | 8.37 ms: 1.20x slower                                                    |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.29x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (5): asyncio_websockets, pickle_pure_python, nqueens, fannkuch, xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-1021191/bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x