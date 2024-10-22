# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 435 ms: 1.53x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.54 sec: 1.24x slower                                                      |
| tornado_http   | 121 ms                                                       | 163 ms: 1.34x slower                                                        |
| Geometric mean | (ref)                                                        | 1.36x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 372 ms: 1.16x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 911 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 479 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 634 ms: 1.10x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 967 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 430 ms: 1.05x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 531 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 687 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 144 ms: 1.88x slower                                                        |
| nbody          | 88.0 ms                                                      | 200 ms: 2.28x slower                                                        |
| Geometric mean | (ref)                                                        | 1.61x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.8 ms: 1.18x slower                                                       |
| regex_compile  | 144 ms                                                       | 233 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.8 us: 1.22x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 116 ms: 1.34x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.3 ms: 1.40x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.43 sec: 1.59x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 94.3 ms: 1.62x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 596 us: 1.87x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 421 us: 2.01x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.42x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.4 ms: 1.32x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.7 ms: 1.44x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 69.0 ms: 1.81x slower                                                       |
| mako            | 10.0 ms                                                      | 22.1 ms: 2.21x slower                                                       |
| Geometric mean  | (ref)                                                        | 2.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 2.88 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 372 ms: 1.16x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 911 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 479 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 634 ms: 1.10x faster                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.40 ms: 1.08x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 967 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 430 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 531 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 687 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.73 ms: 1.09x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| generators                 | 37.4 ms                                                      | 41.9 ms: 1.12x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.8 ms: 1.18x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 453 ms: 1.20x slower                                                        |
| json                       | 5.12 ms                                                      | 6.21 ms: 1.21x slower                                                       |
| json_loads                 | 24.4 us                                                      | 29.8 us: 1.22x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 28.1 ms: 1.22x slower                                                       |
| deepcopy                   | 368 us                                                       | 453 us: 1.23x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.54 sec: 1.24x slower                                                      |
| mdp                        | 2.57 sec                                                     | 3.27 sec: 1.27x slower                                                      |
| async_generators           | 390 ms                                                       | 508 ms: 1.30x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.4 ms: 1.32x slower                                                       |
| tornado_http               | 121 ms                                                       | 163 ms: 1.34x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 116 ms: 1.34x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 32.4 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                       | 175 ms: 1.37x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.3 us: 1.38x slower                                                       |
| scimark_fft                | 301 ms                                                       | 417 ms: 1.39x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.3 ms: 1.40x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.75 sec: 1.42x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.01 ms: 1.43x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.85 us: 1.44x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.7 ms: 1.44x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 53.2 us: 1.45x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 130 ms: 1.45x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.3 ms: 1.48x slower                                                       |
| sympy_str                  | 302 ms                                                       | 456 ms: 1.51x slower                                                        |
| 2to3                       | 285 ms                                                       | 435 ms: 1.53x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 124 ms: 1.54x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.43 sec: 1.59x slower                                                      |
| coverage                   | 66.7 ms                                                      | 107 ms: 1.61x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 94.3 ms: 1.62x slower                                                       |
| regex_compile              | 144 ms                                                       | 233 ms: 1.62x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 262 ms: 1.62x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 188 ms: 1.63x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.56 ms: 1.64x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 95.2 ms: 1.66x slower                                                       |
| logging_format             | 7.48 us                                                      | 12.7 us: 1.69x slower                                                       |
| sympy_expand               | 484 ms                                                       | 830 ms: 1.71x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.8 us: 1.76x slower                                                       |
| fannkuch                   | 350 ms                                                       | 614 ms: 1.76x slower                                                        |
| django_template            | 38.2 ms                                                      | 69.0 ms: 1.81x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.47 sec: 1.82x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 278 us: 1.83x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 3.04 sec: 1.83x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 169 ms: 1.85x slower                                                        |
| pyflate                    | 439 ms                                                       | 813 ms: 1.85x slower                                                        |
| richards                   | 45.7 ms                                                      | 85.1 ms: 1.86x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 596 us: 1.87x slower                                                        |
| float                      | 76.6 ms                                                      | 144 ms: 1.88x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.44 ms: 1.94x slower                                                       |
| chaos                      | 64.0 ms                                                      | 124 ms: 1.94x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 136 ms: 1.97x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 187 ns: 1.98x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 421 us: 2.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 103 ms: 2.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 12.1 ms: 2.02x slower                                                       |
| raytrace                   | 298 ms                                                       | 612 ms: 2.05x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.94 ms: 2.13x slower                                                       |
| mako                       | 10.0 ms                                                      | 22.1 ms: 2.21x slower                                                       |
| go                         | 150 ms                                                       | 338 ms: 2.26x slower                                                        |
| nbody                      | 88.0 ms                                                      | 200 ms: 2.28x slower                                                        |
| scimark_sor                | 109 ms                                                       | 266 ms: 2.44x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 242 ms: 2.45x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.40 ms: 2.60x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.45x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.08x