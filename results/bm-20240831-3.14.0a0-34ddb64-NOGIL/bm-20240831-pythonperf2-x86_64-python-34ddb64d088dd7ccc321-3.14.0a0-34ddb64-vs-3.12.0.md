# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 437 ms: 1.53x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.44 sec: 1.20x slower                                                      |
| tornado_http   | 121 ms                                                       | 169 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 909 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 373 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 484 ms: 1.12x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 963 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 645 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 421 ms: 1.07x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 524 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 686 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 145 ms: 1.89x slower                                                        |
| nbody          | 88.0 ms                                                      | 195 ms: 2.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.58x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.3 ms: 1.15x slower                                                       |
| regex_compile  | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.5 us: 1.21x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 118 ms: 1.37x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.38 sec: 1.56x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 96.7 ms: 1.66x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 593 us: 1.86x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 417 us: 1.99x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.41x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.4 ms: 1.50x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.44x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 68.9 ms: 1.81x slower                                                       |
| mako            | 10.0 ms                                                      | 21.9 ms: 2.19x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.99x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 2.99 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 909 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 373 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 484 ms: 1.12x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 963 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 645 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 421 ms: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 524 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 686 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.67 ms: 1.05x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.9 ms: 1.06x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 5.06 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| generators                 | 37.4 ms                                                      | 41.3 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.3 ms: 1.15x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 451 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.44 sec: 1.20x slower                                                      |
| json_loads                 | 24.4 us                                                      | 29.5 us: 1.21x slower                                                       |
| json                       | 5.12 ms                                                      | 6.19 ms: 1.21x slower                                                       |
| deepcopy                   | 368 us                                                       | 455 us: 1.23x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.24 sec: 1.26x slower                                                      |
| coroutines                 | 23.0 ms                                                      | 29.2 ms: 1.27x slower                                                       |
| async_generators           | 390 ms                                                       | 501 ms: 1.28x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.57 ms: 1.32x slower                                                       |
| scimark_fft                | 301 ms                                                       | 399 ms: 1.32x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 32.1 ms: 1.34x slower                                                       |
| meteor_contest             | 128 ms                                                       | 172 ms: 1.35x slower                                                        |
| comprehensions             | 21.9 us                                                      | 29.7 us: 1.36x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 118 ms: 1.37x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 90.5 ms: 1.38x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                       |
| tornado_http               | 121 ms                                                       | 169 ms: 1.39x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.77 sec: 1.43x slower                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 4.83 us: 1.43x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 53.4 us: 1.45x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 132 ms: 1.46x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 120 ms: 1.49x slower                                                        |
| python_startup             | 11.6 ms                                                      | 17.4 ms: 1.50x slower                                                       |
| sympy_str                  | 302 ms                                                       | 455 ms: 1.51x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.6 ms: 1.52x slower                                                       |
| 2to3                       | 285 ms                                                       | 437 ms: 1.53x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.38 sec: 1.56x slower                                                      |
| regex_compile              | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 264 ms: 1.63x slower                                                        |
| fannkuch                   | 350 ms                                                       | 571 ms: 1.63x slower                                                        |
| coverage                   | 66.7 ms                                                      | 109 ms: 1.64x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 96.7 ms: 1.66x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 192 ms: 1.66x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.5 us: 1.67x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 95.9 ms: 1.67x slower                                                       |
| sympy_expand               | 484 ms                                                       | 827 ms: 1.71x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.6 us: 1.73x slower                                                       |
| pyflate                    | 439 ms                                                       | 771 ms: 1.76x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.44 sec: 1.78x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.99 sec: 1.80x slower                                                      |
| django_template            | 38.2 ms                                                      | 68.9 ms: 1.81x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.73 ms: 1.82x slower                                                       |
| richards                   | 45.7 ms                                                      | 83.2 ms: 1.82x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 279 us: 1.84x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 170 ms: 1.86x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 593 us: 1.86x slower                                                        |
| float                      | 76.6 ms                                                      | 145 ms: 1.89x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.39 ms: 1.91x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 134 ms: 1.94x slower                                                        |
| go                         | 150 ms                                                       | 291 ms: 1.94x slower                                                        |
| chaos                      | 64.0 ms                                                      | 125 ms: 1.95x slower                                                        |
| richards_super             | 51.3 ms                                                      | 101 ms: 1.97x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 417 us: 1.99x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 11.9 ms: 1.99x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 191 ns: 2.03x slower                                                        |
| raytrace                   | 298 ms                                                       | 611 ms: 2.05x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.09x slower                                                       |
| mako                       | 10.0 ms                                                      | 21.9 ms: 2.19x slower                                                       |
| nbody                      | 88.0 ms                                                      | 195 ms: 2.22x slower                                                        |
| scimark_sor                | 109 ms                                                       | 250 ms: 2.29x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 237 ms: 2.40x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.35 ms: 2.58x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.08x