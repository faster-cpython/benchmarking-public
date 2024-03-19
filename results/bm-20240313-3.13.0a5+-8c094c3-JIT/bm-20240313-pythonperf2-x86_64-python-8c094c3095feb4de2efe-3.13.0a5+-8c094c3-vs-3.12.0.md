# Results vs. 3.12.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: linux-x86_64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 307 ms: 1.08x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.41 ms: 1.02x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| tornado_http   | 121 ms                                                       | 126 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 442 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 438 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 710 ms: 1.02x slower                                                         |
| async_tree_memoization     | 544 ms                                                       | 554 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 709 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 559 ms: 1.03x slower                                                         |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 261 ms: 1.01x faster                                                         |
| float          | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                        |
| nbody          | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| regex_compile  | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| regex_dna      | 239 ms                                                       | 253 ms: 1.06x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.5 us: 1.07x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                         |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.60 us: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 86.0 ms: 1.00x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 234 us: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 15.6 ms: 1.34x slower                                                        |
| python_startup_no_site | 8.64 ms                                                      | 14.1 ms: 1.63x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.75 ms: 1.03x faster                                                        |
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 117 us: 1.29x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.0 us: 1.15x faster                                                        |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.11x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.5 us: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.8 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.69 us: 1.03x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.75 ms: 1.03x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.02x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.29 us: 1.02x faster                                                        |
| async_tree_none            | 452 ms                                                       | 442 ms: 1.02x faster                                                         |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| async_generators           | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| pidigits                   | 265 ms                                                       | 261 ms: 1.01x faster                                                         |
| unpickle_list              | 4.66 us                                                      | 4.60 us: 1.01x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 160 ms: 1.01x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.00x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 86.0 ms: 1.00x faster                                                        |
| deepcopy                   | 368 us                                                       | 370 us: 1.00x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.76 us: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| regex_compile              | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 431 ms                                                       | 438 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 710 ms: 1.02x slower                                                         |
| async_tree_memoization     | 544 ms                                                       | 554 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 709 ms: 1.02x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 37.6 us: 1.02x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 972 us: 1.02x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.41 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.03x slower                                                         |
| float                      | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.4 ms: 1.03x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.6 ms: 1.03x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 94.4 ms: 1.03x slower                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 559 ms: 1.03x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 836 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                        |
| dask                       | 392 ms                                                       | 406 ms: 1.04x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                                       |
| tornado_http               | 121 ms                                                       | 126 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.85 ms: 1.04x slower                                                        |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                                       |
| raytrace                   | 298 ms                                                       | 312 ms: 1.05x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.7 ms: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 511 ms: 1.06x slower                                                         |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                        |
| chaos                      | 64.0 ms                                                      | 67.6 ms: 1.06x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.31 sec: 1.06x slower                                                       |
| regex_dna                  | 239 ms                                                       | 253 ms: 1.06x slower                                                         |
| nbody                      | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                        |
| 2to3                       | 285 ms                                                       | 307 ms: 1.08x slower                                                         |
| scimark_fft                | 301 ms                                                       | 325 ms: 1.08x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.09 ms: 1.09x slower                                                        |
| richards_super             | 51.3 ms                                                      | 56.2 ms: 1.09x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.12 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 63.3 ms: 1.10x slower                                                        |
| mypy2                      | 830 ms                                                       | 915 ms: 1.10x slower                                                         |
| richards                   | 45.7 ms                                                      | 50.5 ms: 1.10x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 76.2 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 234 us: 1.12x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 3.92 ms: 1.13x slower                                                        |
| fannkuch                   | 350 ms                                                       | 396 ms: 1.13x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                         |
| go                         | 150 ms                                                       | 174 ms: 1.16x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.76 ms: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.13 ms: 1.17x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 62.2 ns: 1.17x slower                                                        |
| pyflate                    | 439 ms                                                       | 524 ms: 1.19x slower                                                         |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.25 ms: 1.22x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 122 ms: 1.24x slower                                                         |
| python_startup             | 11.6 ms                                                      | 15.6 ms: 1.34x slower                                                        |
| scimark_sor                | 109 ms                                                       | 152 ms: 1.39x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 7.02 ms: 1.47x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 14.1 ms: 1.63x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (5): create_gc_cycles, asyncio_websockets, logging_format, sympy_str, unpickle
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.11x