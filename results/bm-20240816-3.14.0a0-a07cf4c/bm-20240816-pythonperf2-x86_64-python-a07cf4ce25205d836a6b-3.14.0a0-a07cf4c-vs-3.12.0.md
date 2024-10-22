# Results vs. 3.12.0

- fork: python
- ref: a07cf4ce25205d836a6b
- machine: linux-x86_64
- commit hash: a07cf4c
- commit date: 2024-08-16
- overall geometric mean: 1.03x faster
- HPT reliability: 81.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 774 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                       |
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 774 ms: 1.36x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 293 us: 1.26x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.25x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.4 ms: 1.11x faster                                                       |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                        |
| async_generators           | 390 ms                                                       | 353 ms: 1.11x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 866 us: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.85 us: 1.09x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.24 us: 1.08x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.6 ms: 1.04x faster                                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.03x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                      |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 96.5 ns: 1.02x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                      |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 841 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.73 sec: 1.05x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 96.0 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.30 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 123 ms: 1.06x slower                                                        |
| float                      | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                                       |
| richards                   | 45.7 ms                                                      | 49.3 ms: 1.08x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| richards_super             | 51.3 ms                                                      | 55.9 ms: 1.09x slower                                                       |
| go                         | 150 ms                                                       | 164 ms: 1.10x slower                                                        |
| pyflate                    | 439 ms                                                       | 485 ms: 1.10x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.07 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.95 ms: 1.22x slower                                                       |
| coverage                   | 66.7 ms                                                      | 85.5 ms: 1.28x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.68 ms: 1.35x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (9): bench_mp_pool, asyncio_websockets, xml_etree_parse, pickle_pure_python, scimark_sor, nqueens, regex_dna, nbody, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240816-3.14.0a0-a07cf4c/bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 81.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x