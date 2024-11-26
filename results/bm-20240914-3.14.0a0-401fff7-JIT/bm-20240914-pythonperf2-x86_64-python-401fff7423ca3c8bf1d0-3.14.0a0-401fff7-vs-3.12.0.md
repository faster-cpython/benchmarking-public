# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.023x faster
- HPT reliability: 82.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 309 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 805 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 818 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 78.7 ms: 1.12x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| regex_compile  | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 78.5 ms: 1.10x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.22 us: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.69 us: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.18 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 41.6 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.5 us: 1.39x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 805 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 818 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.21x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.7 ms: 1.15x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| nbody                      | 88.0 ms                                                      | 78.7 ms: 1.12x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 78.5 ms: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.18 ms: 1.09x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.05x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.22 us: 1.05x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.20 us: 1.04x faster                                                       |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.06 ms: 1.04x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| float                      | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 783 ms: 1.03x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 922 us: 1.03x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                       |
| generators                 | 37.4 ms                                                      | 36.5 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.02x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.7 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                      |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 97.5 ms: 1.01x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.69 us: 1.01x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                      |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                       |
| richards_super             | 51.3 ms                                                      | 52.4 ms: 1.02x slower                                                       |
| sympy_str                  | 302 ms                                                       | 308 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.6 ms: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.03x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 397 ms: 1.03x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.03x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                       |
| pyflate                    | 439 ms                                                       | 454 ms: 1.04x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.00 ms: 1.05x slower                                                       |
| raytrace                   | 298 ms                                                       | 313 ms: 1.05x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.08x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 97.0 ms: 1.08x slower                                                       |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.08x slower                                                        |
| 2to3                       | 285 ms                                                       | 309 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.93 ms: 1.09x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.6 ms: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 26.3 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 65.0 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.08 ms: 1.16x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.95 ms: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.4 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.36 ms: 1.25x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 87.7 ns: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (3): tornado_http, deltablue, go
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 82.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x