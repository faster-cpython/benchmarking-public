# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                                     |
| chameleon      | 7.23 ms                                                      | 7.33 ms: 1.01x slower                                                    |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                   |
| tornado_http   | 121 ms                                                       | 125 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 438 ms: 1.03x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 435 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                                     |
| async_tree_memoization     | 544 ms                                                       | 550 ms: 1.01x slower                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 557 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                                   |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                                     |
| float          | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                    |
| nbody          | 88.0 ms                                                      | 103 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                    |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                     |
| regex_compile  | 144 ms                                                       | 152 ms: 1.05x slower                                                     |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_list        | 4.66 us                                                      | 4.57 us: 1.02x faster                                                    |
| xml_etree_generate   | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                    |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                     |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                    |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                     |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                     |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.02x slower                                                    |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                    |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                    |
| tomli_loads          | 2.16 sec                                                     | 2.34 sec: 1.08x slower                                                   |
| unpickle_pure_python | 210 us                                                       | 241 us: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 14.2 ms: 1.22x slower                                                    |
| python_startup_no_site | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.33x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                                    |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 120 us: 1.27x faster                                                     |
| comprehensions             | 21.9 us                                                      | 19.3 us: 1.13x faster                                                    |
| generators                 | 37.4 ms                                                      | 34.2 ms: 1.09x faster                                                    |
| async_tree_none            | 452 ms                                                       | 438 ms: 1.03x faster                                                     |
| logging_format             | 7.48 us                                                      | 7.28 us: 1.03x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 3.30 us: 1.02x faster                                                    |
| unpickle_list              | 4.66 us                                                      | 4.57 us: 1.02x faster                                                    |
| crypto_pyaes               | 80.3 ms                                                      | 79.1 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.01x faster                                                    |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                     |
| pidigits                   | 265 ms                                                       | 262 ms: 1.01x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                    |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                     |
| logging_simple             | 6.71 us                                                      | 6.66 us: 1.01x faster                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                    |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                   |
| django_template            | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                                    |
| sympy_str                  | 302 ms                                                       | 305 ms: 1.01x slower                                                     |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 431 ms                                                       | 435 ms: 1.01x slower                                                     |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                                     |
| async_tree_memoization     | 544 ms                                                       | 550 ms: 1.01x slower                                                     |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                    |
| async_generators           | 390 ms                                                       | 395 ms: 1.01x slower                                                     |
| chameleon                  | 7.23 ms                                                      | 7.33 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                     |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                   |
| deepcopy_memo              | 36.8 us                                                      | 37.4 us: 1.02x slower                                                    |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.02x slower                                                    |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                    |
| deepcopy                   | 368 us                                                       | 378 us: 1.03x slower                                                     |
| raytrace                   | 298 ms                                                       | 306 ms: 1.03x slower                                                     |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 540 ms                                                       | 557 ms: 1.03x slower                                                     |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                   |
| bench_thread_pool          | 950 us                                                       | 979 us: 1.03x slower                                                     |
| tornado_http               | 121 ms                                                       | 125 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                                   |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                                    |
| dask                       | 392 ms                                                       | 405 ms: 1.03x slower                                                     |
| float                      | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                    |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                    |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                    |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                     |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.05x slower                                                    |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                                   |
| sympy_integrate            | 23.9 ms                                                      | 25.1 ms: 1.05x slower                                                    |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                    |
| dulwich_log                | 65.4 ms                                                      | 68.8 ms: 1.05x slower                                                    |
| regex_compile              | 144 ms                                                       | 152 ms: 1.05x slower                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.88 ms: 1.06x slower                                                    |
| sympy_expand               | 484 ms                                                       | 517 ms: 1.07x slower                                                     |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                                     |
| gunicorn                   | 1.00 ms                                                      | 1.08 ms: 1.08x slower                                                    |
| tomli_loads                | 2.16 sec                                                     | 2.34 sec: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.56 ms: 1.08x slower                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.80 sec: 1.09x slower                                                   |
| chaos                      | 64.0 ms                                                      | 69.9 ms: 1.09x slower                                                    |
| aiohttp                    | 1.02 ms                                                      | 1.11 ms: 1.09x slower                                                    |
| pprint_safe_repr           | 807 ms                                                       | 883 ms: 1.09x slower                                                     |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                    |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 57.5 ms                                                      | 63.4 ms: 1.10x slower                                                    |
| pycparser                  | 1.23 sec                                                     | 1.37 sec: 1.11x slower                                                   |
| mypy2                      | 830 ms                                                       | 922 ms: 1.11x slower                                                     |
| richards_super             | 51.3 ms                                                      | 57.6 ms: 1.12x slower                                                    |
| richards                   | 45.7 ms                                                      | 51.5 ms: 1.13x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 3.92 ms: 1.13x slower                                                    |
| unpickle_pure_python       | 210 us                                                       | 241 us: 1.15x slower                                                     |
| deltablue                  | 3.24 ms                                                      | 3.74 ms: 1.16x slower                                                    |
| go                         | 150 ms                                                       | 175 ms: 1.17x slower                                                     |
| scimark_fft                | 301 ms                                                       | 353 ms: 1.17x slower                                                     |
| nbody                      | 88.0 ms                                                      | 103 ms: 1.18x slower                                                     |
| scimark_monte_carlo        | 69.0 ms                                                      | 81.4 ms: 1.18x slower                                                    |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                     |
| telco                      | 6.96 ms                                                      | 8.30 ms: 1.19x slower                                                    |
| coverage                   | 66.7 ms                                                      | 80.0 ms: 1.20x slower                                                    |
| python_startup             | 11.6 ms                                                      | 14.2 ms: 1.22x slower                                                    |
| pyflate                    | 439 ms                                                       | 536 ms: 1.22x slower                                                     |
| fannkuch                   | 350 ms                                                       | 448 ms: 1.28x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 7.68 ms: 1.29x slower                                                    |
| scimark_lu                 | 98.8 ms                                                      | 134 ms: 1.36x slower                                                     |
| scimark_sor                | 109 ms                                                       | 156 ms: 1.43x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                    |
| unpack_sequence            | 53.2 ns                                                      | 80.1 ns: 1.51x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                             |

Benchmark hidden because not significant (8): coroutines, asyncio_websockets, pickle_dict, sympy_sum, bench_mp_pool, pickle_list, async_tree_cpu_io_mixed, create_gc_cycles
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.01x