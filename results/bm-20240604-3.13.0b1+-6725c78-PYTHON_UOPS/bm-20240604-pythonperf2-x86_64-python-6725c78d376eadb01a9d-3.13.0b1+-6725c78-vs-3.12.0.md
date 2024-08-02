# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 346 ms: 1.21x slower                                                         |
| chameleon      | 7.23 ms                                                      | 8.73 ms: 1.21x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.48 sec: 1.21x slower                                                       |
| tornado_http   | 121 ms                                                       | 130 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 881 ms: 1.20x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 367 ms: 1.17x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 461 ms: 1.17x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 480 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 921 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 619 ms: 1.13x faster                                                         |
| async_tree_none            | 452 ms                                                       | 402 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 656 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| float          | 76.6 ms                                                      | 97.4 ms: 1.27x slower                                                        |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                                        |
| regex_dna      | 239 ms                                                       | 247 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| regex_compile  | 144 ms                                                       | 216 ms: 1.50x slower                                                         |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 24.4 us: 1.00x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.49 us: 1.01x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.02x slower                                                        |
| pickle               | 10.5 us                                                      | 10.8 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 4.81 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 96.7 ms: 1.12x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 69.0 ms: 1.18x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.94 sec: 1.36x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 434 us: 1.37x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 305 us: 1.46x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.92 ms: 1.03x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 46.4 ms: 1.22x slower                                                        |
| mako            | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.33x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 881 ms: 1.20x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 367 ms: 1.17x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 461 ms: 1.17x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 480 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 921 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 619 ms: 1.13x faster                                                         |
| async_tree_none            | 452 ms                                                       | 402 ms: 1.12x faster                                                         |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 656 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 18.4 ms: 1.03x faster                                                        |
| json_loads                 | 24.4 us                                                      | 24.4 us: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.49 us: 1.01x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.02x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.84 us: 1.02x slower                                                        |
| asyncio_tcp                | 378 ms                                                       | 389 ms: 1.03x slower                                                         |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.03x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.81 us: 1.03x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.92 ms: 1.03x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.87 us: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.04x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 5.00 ms: 1.05x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.01 ms: 1.07x slower                                                        |
| tornado_http               | 121 ms                                                       | 130 ms: 1.07x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.77 sec: 1.08x slower                                                       |
| dask                       | 392 ms                                                       | 426 ms: 1.09x slower                                                         |
| json                       | 5.12 ms                                                      | 5.57 ms: 1.09x slower                                                        |
| mypy2                      | 830 ms                                                       | 908 ms: 1.09x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| raytrace                   | 298 ms                                                       | 333 ms: 1.12x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 96.7 ms: 1.12x slower                                                        |
| meteor_contest             | 128 ms                                                       | 144 ms: 1.13x slower                                                         |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.14x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 92.6 ms: 1.15x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.16 ms: 1.16x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 189 ms: 1.17x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.19 ms: 1.17x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 28.1 ms: 1.18x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 69.0 ms: 1.18x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.46 sec: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.5 ms: 1.19x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 8.73 ms: 1.21x slower                                                        |
| 2to3                       | 285 ms                                                       | 346 ms: 1.21x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.48 sec: 1.21x slower                                                       |
| django_template            | 38.2 ms                                                      | 46.4 ms: 1.22x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.10 us: 1.22x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 80.2 ms: 1.23x slower                                                        |
| sympy_str                  | 302 ms                                                       | 372 ms: 1.23x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 2.19 ms: 1.24x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 71.5 ms: 1.24x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 144 ms: 1.25x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.26x slower                                                        |
| comprehensions             | 21.9 us                                                      | 27.8 us: 1.27x slower                                                        |
| chaos                      | 64.0 ms                                                      | 81.1 ms: 1.27x slower                                                        |
| float                      | 76.6 ms                                                      | 97.4 ms: 1.27x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.12 sec: 1.28x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.28x slower                                                       |
| sympy_expand               | 484 ms                                                       | 625 ms: 1.29x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 2.07 ms: 1.30x slower                                                        |
| deepcopy                   | 368 us                                                       | 483 us: 1.31x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 199 us: 1.31x slower                                                         |
| telco                      | 6.96 ms                                                      | 9.17 ms: 1.32x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 120 ms: 1.34x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 4.70 ms: 1.35x slower                                                        |
| richards                   | 45.7 ms                                                      | 62.3 ms: 1.36x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.94 sec: 1.36x slower                                                       |
| richards_super             | 51.3 ms                                                      | 70.1 ms: 1.36x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 434 us: 1.37x slower                                                         |
| go                         | 150 ms                                                       | 206 ms: 1.38x slower                                                         |
| fannkuch                   | 350 ms                                                       | 490 ms: 1.40x slower                                                         |
| scimark_fft                | 301 ms                                                       | 425 ms: 1.41x slower                                                         |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 4.60 ms: 1.42x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 99.5 ms: 1.44x slower                                                        |
| mako                       | 10.0 ms                                                      | 14.5 ms: 1.45x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 305 us: 1.46x slower                                                         |
| pyflate                    | 439 ms                                                       | 654 ms: 1.49x slower                                                         |
| regex_compile              | 144 ms                                                       | 216 ms: 1.50x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 149 ms: 1.51x slower                                                         |
| scimark_sor                | 109 ms                                                       | 165 ms: 1.51x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.60 ms: 1.57x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 58.6 us: 1.59x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 149 ms: 1.62x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 155 ns: 1.64x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 10.7 ms: 1.80x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                                 |

Benchmark hidden because not significant (4): logging_format, coroutines, async_generators, asyncio_websockets
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.94x