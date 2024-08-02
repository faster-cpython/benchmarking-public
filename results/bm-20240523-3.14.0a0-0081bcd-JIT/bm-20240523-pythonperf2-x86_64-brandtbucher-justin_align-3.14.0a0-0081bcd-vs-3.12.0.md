# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.01x slower
- HPT reliability: 67.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                      |
| chameleon      | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                                     |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                      |
| async_tree_none            | 452 ms                                                       | 377 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 909 ms: 1.15x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 480 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                      |
| nbody          | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                     |
| float          | 76.6 ms                                                      | 77.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                      |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                      |
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                     |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                     |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                      |
| pickle_list          | 4.43 us                                                      | 4.40 us: 1.01x faster                                                     |
| pickle_dict          | 32.5 us                                                      | 32.4 us: 1.00x faster                                                     |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                     |
| unpickle             | 14.8 us                                                      | 14.9 us: 1.01x slower                                                     |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                     |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                     |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.45 ms: 1.09x slower                                                     |
| python_startup         | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                                     |
| django_template | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 431 ms: 1.25x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                      |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                     |
| async_tree_none            | 452 ms                                                       | 377 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 588 ms: 1.19x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                      |
| pathlib                    | 18.9 ms                                                      | 16.4 ms: 1.15x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 909 ms: 1.15x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 480 ms: 1.13x faster                                                      |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                     |
| spectral_norm              | 91.6 ms                                                      | 82.2 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                     |
| generators                 | 37.4 ms                                                      | 34.8 ms: 1.08x faster                                                     |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.6 ms: 1.05x faster                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                     |
| nbody                      | 88.0 ms                                                      | 84.1 ms: 1.05x faster                                                     |
| richards                   | 45.7 ms                                                      | 43.8 ms: 1.05x faster                                                     |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                    |
| logging_format             | 7.48 us                                                      | 7.22 us: 1.04x faster                                                     |
| raytrace                   | 298 ms                                                       | 288 ms: 1.04x faster                                                      |
| scimark_fft                | 301 ms                                                       | 291 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.07 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                      |
| async_generators           | 390 ms                                                       | 381 ms: 1.02x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.58 us: 1.02x faster                                                     |
| fannkuch                   | 350 ms                                                       | 345 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                    |
| richards_super             | 51.3 ms                                                      | 50.9 ms: 1.01x faster                                                     |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                    |
| pickle_list                | 4.43 us                                                      | 4.40 us: 1.01x faster                                                     |
| pickle_dict                | 32.5 us                                                      | 32.4 us: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                    |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                     |
| unpickle                   | 14.8 us                                                      | 14.9 us: 1.01x slower                                                     |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                     |
| float                      | 76.6 ms                                                      | 77.6 ms: 1.01x slower                                                     |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                      |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                     |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                      |
| deepcopy_memo              | 36.8 us                                                      | 37.3 us: 1.01x slower                                                     |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                    |
| dulwich_log                | 65.4 ms                                                      | 66.5 ms: 1.02x slower                                                     |
| pyflate                    | 439 ms                                                       | 447 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                      |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                     |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                     |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                     |
| sympy_str                  | 302 ms                                                       | 312 ms: 1.03x slower                                                      |
| chaos                      | 64.0 ms                                                      | 66.1 ms: 1.03x slower                                                     |
| dask                       | 392 ms                                                       | 406 ms: 1.04x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                     |
| chameleon                  | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                                     |
| sympy_integrate            | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                     |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                      |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                                      |
| django_template            | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                     |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                     |
| nqueens                    | 89.9 ms                                                      | 97.8 ms: 1.09x slower                                                     |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                      |
| sympy_expand               | 484 ms                                                       | 528 ms: 1.09x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.45 ms: 1.09x slower                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.71 us: 1.10x slower                                                     |
| sqlglot_optimize           | 57.5 ms                                                      | 63.5 ms: 1.11x slower                                                     |
| deepcopy                   | 368 us                                                       | 411 us: 1.12x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.74 ms: 1.13x slower                                                     |
| deltablue                  | 3.24 ms                                                      | 3.75 ms: 1.16x slower                                                     |
| python_startup             | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                     |
| scimark_lu                 | 98.8 ms                                                      | 115 ms: 1.16x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.14 ms: 1.17x slower                                                     |
| scimark_sor                | 109 ms                                                       | 130 ms: 1.19x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                      |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                     |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                     |
| gc_traversal               | 3.48 ms                                                      | 4.94 ms: 1.42x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (8): pprint_safe_repr, sqlite_synth, asyncio_tcp, bench_thread_pool, meteor_contest, unpickle_list, asyncio_websockets, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 67.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x