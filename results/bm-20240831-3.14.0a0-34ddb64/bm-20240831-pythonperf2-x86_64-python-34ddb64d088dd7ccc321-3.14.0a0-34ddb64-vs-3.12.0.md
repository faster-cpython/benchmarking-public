# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.032x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 115 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 396 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 816 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                       |
| float          | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 26.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100.0 ms: 1.03x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.59 sec: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 396 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.3 ms: 1.32x faster                                                       |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 816 ms: 1.28x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.8 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.23x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.1 ms: 1.11x faster                                                       |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 861 us: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 271 ms: 1.10x faster                                                        |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.27 us: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.06x faster                                                       |
| tornado_http               | 121 ms                                                       | 115 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.8 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.8 ms: 1.04x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 100.0 ms: 1.03x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.11 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| nqueens                    | 89.9 ms                                                      | 89.3 ms: 1.01x faster                                                       |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 354 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.21 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 97.6 ns: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 68.2 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.3 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.27 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.1 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.3 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.6 ms: 1.13x slower                                                       |
| pyflate                    | 439 ms                                                       | 496 ms: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.13 ms: 1.17x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.59 sec: 1.20x slower                                                      |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (6): bench_mp_pool, xml_etree_parse, scimark_fft, pprint_safe_repr, regex_dna, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x