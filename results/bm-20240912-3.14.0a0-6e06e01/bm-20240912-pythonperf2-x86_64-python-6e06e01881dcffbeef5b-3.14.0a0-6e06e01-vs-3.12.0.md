# Results vs. 3.12.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.03x faster
- HPT reliability: 84.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 4.66 us                                                      | 4.56 us: 1.02x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 32.4 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.50 us: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.53 sec: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.2 us: 1.22x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                       |
| go                         | 150 ms                                                       | 134 ms: 1.11x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 865 us: 1.10x faster                                                        |
| raytrace                   | 298 ms                                                       | 272 ms: 1.09x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 48.7 ns: 1.09x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.87 us: 1.09x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 73.8 ms: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 361 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                       |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.7 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.8 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| unpickle_list              | 4.66 us                                                      | 4.56 us: 1.02x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.7 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.5 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 32.4 us: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 815 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| pickle_list                | 4.43 us                                                      | 4.50 us: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.29 ms: 1.02x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| float                      | 76.6 ms                                                      | 78.3 ms: 1.02x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 396 ms: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.24 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.3 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.21 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.3 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.5 ms: 1.10x slower                                                       |
| pyflate                    | 439 ms                                                       | 492 ms: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.53 sec: 1.17x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.33 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.8 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.45 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (6): nbody, xml_etree_iterparse, scimark_fft, pickle, django_template, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 84.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x