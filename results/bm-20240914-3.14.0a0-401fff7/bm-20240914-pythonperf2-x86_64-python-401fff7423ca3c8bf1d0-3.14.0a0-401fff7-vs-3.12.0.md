# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.03x faster
- HPT reliability: 95.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| float          | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                       |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.60 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.64 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.56 sec: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 783 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.29x faster                                                       |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.6 ms: 1.11x faster                                                       |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 863 us: 1.10x faster                                                        |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 358 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.98 us: 1.07x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 49.6 ns: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.35 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                      |
| scimark_lu                 | 98.8 ms                                                      | 95.1 ms: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.09 ms: 1.03x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.2 ms: 1.03x faster                                                       |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.7 ms: 1.01x faster                                                       |
| unpickle_list              | 4.66 us                                                      | 4.60 us: 1.01x faster                                                       |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.75 us: 1.01x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 803 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.25 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.04x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.64 us: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                       |
| float                      | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.36 ms: 1.07x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.5 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.8 ms: 1.11x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| pyflate                    | 439 ms                                                       | 503 ms: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.56 sec: 1.18x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.34 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.7 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.65 ms: 1.34x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (4): scimark_monte_carlo, pprint_pformat, asyncio_websockets, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x