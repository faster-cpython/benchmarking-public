# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.46x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 442 ms: 1.55x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.52 sec: 1.23x slower                                                      |
| tornado_http   | 121 ms                                                       | 170 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 920 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 479 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 387 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 634 ms: 1.10x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 964 ms: 1.08x faster                                                        |
| async_tree_none            | 452 ms                                                       | 428 ms: 1.06x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 533 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 688 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 143 ms: 1.87x slower                                                        |
| nbody          | 88.0 ms                                                      | 196 ms: 2.23x slower                                                        |
| Geometric mean | (ref)                                                        | 1.58x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.59 ms: 1.00x slower                                                       |
| regex_dna      | 239 ms                                                       | 255 ms: 1.07x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 28.5 ms: 1.20x slower                                                       |
| regex_compile  | 144 ms                                                       | 234 ms: 1.63x slower                                                        |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 112 ms: 1.09x slower                                                        |
| json_loads           | 24.4 us                                                      | 30.1 us: 1.24x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 116 ms: 1.34x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.6 ms: 1.43x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.43 sec: 1.59x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 95.7 ms: 1.64x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 608 us: 1.91x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 427 us: 2.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.43x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.9 ms: 1.38x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.3 ms: 1.49x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.44x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 68.4 ms: 1.79x slower                                                       |
| mako            | 10.0 ms                                                      | 21.8 ms: 2.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.98x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 2.90 ms: 1.20x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 920 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 479 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 387 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 634 ms: 1.10x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 964 ms: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| async_tree_none            | 452 ms                                                       | 428 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 533 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 688 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.59 ms: 1.00x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 4.95 ms: 1.04x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.8 ms: 1.05x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.70 ms: 1.07x slower                                                       |
| regex_dna                  | 239 ms                                                       | 255 ms: 1.07x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 112 ms: 1.09x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| generators                 | 37.4 ms                                                      | 42.4 ms: 1.13x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 452 ms: 1.19x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 28.5 ms: 1.20x slower                                                       |
| json                       | 5.12 ms                                                      | 6.19 ms: 1.21x slower                                                       |
| deepcopy                   | 368 us                                                       | 450 us: 1.22x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.52 sec: 1.23x slower                                                      |
| json_loads                 | 24.4 us                                                      | 30.1 us: 1.24x slower                                                       |
| mdp                        | 2.57 sec                                                     | 3.25 sec: 1.26x slower                                                      |
| async_generators           | 390 ms                                                       | 511 ms: 1.31x slower                                                        |
| scimark_fft                | 301 ms                                                       | 394 ms: 1.31x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 30.5 ms: 1.33x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 116 ms: 1.34x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.65 ms: 1.34x slower                                                       |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.36x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 32.9 ms: 1.37x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.9 ms: 1.38x slower                                                       |
| tornado_http               | 121 ms                                                       | 170 ms: 1.40x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 51.7 us: 1.41x slower                                                       |
| comprehensions             | 21.9 us                                                      | 30.9 us: 1.41x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.78 us: 1.42x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.76 sec: 1.42x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 14.6 ms: 1.43x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 130 ms: 1.45x slower                                                        |
| python_startup             | 11.6 ms                                                      | 17.3 ms: 1.49x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 122 ms: 1.52x slower                                                        |
| sympy_str                  | 302 ms                                                       | 462 ms: 1.53x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.7 ms: 1.54x slower                                                       |
| 2to3                       | 285 ms                                                       | 442 ms: 1.55x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.43 sec: 1.59x slower                                                      |
| regex_compile              | 144 ms                                                       | 234 ms: 1.63x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 189 ms: 1.63x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 95.7 ms: 1.64x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 266 ms: 1.64x slower                                                        |
| coverage                   | 66.7 ms                                                      | 110 ms: 1.65x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 95.9 ms: 1.67x slower                                                       |
| fannkuch                   | 350 ms                                                       | 593 ms: 1.69x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.9 us: 1.72x slower                                                       |
| sympy_expand               | 484 ms                                                       | 837 ms: 1.73x slower                                                        |
| logging_simple             | 6.71 us                                                      | 11.9 us: 1.78x slower                                                       |
| pyflate                    | 439 ms                                                       | 785 ms: 1.79x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.70 ms: 1.79x slower                                                       |
| django_template            | 38.2 ms                                                      | 68.4 ms: 1.79x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 165 ms: 1.80x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.47 sec: 1.82x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 3.04 sec: 1.84x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 279 us: 1.84x slower                                                        |
| float                      | 76.6 ms                                                      | 143 ms: 1.87x slower                                                        |
| richards                   | 45.7 ms                                                      | 85.7 ms: 1.87x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 608 us: 1.91x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.42 ms: 1.93x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 135 ms: 1.95x slower                                                        |
| chaos                      | 64.0 ms                                                      | 126 ms: 1.97x slower                                                        |
| richards_super             | 51.3 ms                                                      | 103 ms: 2.00x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 427 us: 2.04x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 12.2 ms: 2.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 2.88 ms: 2.09x slower                                                       |
| raytrace                   | 298 ms                                                       | 626 ms: 2.10x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 202 ns: 2.14x slower                                                        |
| mako                       | 10.0 ms                                                      | 21.8 ms: 2.18x slower                                                       |
| nbody                      | 88.0 ms                                                      | 196 ms: 2.23x slower                                                        |
| go                         | 150 ms                                                       | 351 ms: 2.34x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 238 ms: 2.41x slower                                                        |
| scimark_sor                | 109 ms                                                       | 266 ms: 2.45x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.55 ms: 2.64x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.46x slower                                                                |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: 1.08x