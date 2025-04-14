# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.001x slower
- HPT reliability: 61.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                               |
| chameleon      | 7.23 ms                                                      | 7.54 ms: 1.04x slower                                              |
| docutils       | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                             |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 816 ms: 1.29x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.26x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                               |
| async_tree_none            | 452 ms                                                       | 375 ms: 1.20x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 456 ms: 1.19x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 463 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 603 ms: 1.15x faster                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                               |
| float          | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                              |
| regex_compile  | 144 ms                                                       | 145 ms: 1.00x slower                                               |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                               |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.4 us: 1.07x faster                                              |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                              |
| pickle_list          | 4.43 us                                                      | 4.31 us: 1.03x faster                                              |
| xml_etree_generate   | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                              |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                               |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.00x slower                                              |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                              |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                               |
| unpickle_list        | 4.66 us                                                      | 4.81 us: 1.03x slower                                              |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.03x slower                                               |
| unpickle             | 14.8 us                                                      | 16.0 us: 1.08x slower                                              |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                              |
| tomli_loads          | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.94 ms: 1.03x slower                                              |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.8 ms: 1.02x slower                                              |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 816 ms: 1.29x faster                                               |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                              |
| async_tree_none_tg         | 431 ms                                                       | 343 ms: 1.26x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 842 ms: 1.24x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                               |
| async_tree_none            | 452 ms                                                       | 375 ms: 1.20x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 456 ms: 1.19x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 463 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 603 ms: 1.15x faster                                               |
| raytrace                   | 298 ms                                                       | 262 ms: 1.14x faster                                               |
| generators                 | 37.4 ms                                                      | 33.2 ms: 1.13x faster                                              |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                              |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                              |
| pickle_dict                | 32.5 us                                                      | 30.4 us: 1.07x faster                                              |
| async_generators           | 390 ms                                                       | 366 ms: 1.07x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.9 ms: 1.06x faster                                              |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                               |
| chaos                      | 64.0 ms                                                      | 60.9 ms: 1.05x faster                                              |
| bench_thread_pool          | 950 us                                                       | 906 us: 1.05x faster                                               |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.04x faster                                               |
| logging_format             | 7.48 us                                                      | 7.23 us: 1.04x faster                                              |
| dask                       | 392 ms                                                       | 379 ms: 1.03x faster                                               |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                              |
| pickle_list                | 4.43 us                                                      | 4.31 us: 1.03x faster                                              |
| docutils                   | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                              |
| scimark_lu                 | 98.8 ms                                                      | 97.1 ms: 1.02x faster                                              |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                              |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                               |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                               |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                              |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                             |
| xml_etree_generate         | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                              |
| nqueens                    | 89.9 ms                                                      | 89.1 ms: 1.01x faster                                              |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                               |
| regex_effbot               | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                              |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                             |
| scimark_fft                | 301 ms                                                       | 302 ms: 1.00x slower                                               |
| regex_compile              | 144 ms                                                       | 145 ms: 1.00x slower                                               |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.00x slower                                              |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                             |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                               |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                              |
| asyncio_tcp                | 378 ms                                                       | 384 ms: 1.02x slower                                               |
| pprint_safe_repr           | 807 ms                                                       | 820 ms: 1.02x slower                                               |
| django_template            | 38.2 ms                                                      | 38.8 ms: 1.02x slower                                              |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.44 us: 1.02x slower                                              |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                              |
| gunicorn                   | 1.00 ms                                                      | 1.03 ms: 1.03x slower                                              |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                               |
| deepcopy_memo              | 36.8 us                                                      | 37.9 us: 1.03x slower                                              |
| unpickle_list              | 4.66 us                                                      | 4.81 us: 1.03x slower                                              |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.03x slower                                               |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                               |
| json                       | 5.12 ms                                                      | 5.29 ms: 1.03x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.94 ms: 1.03x slower                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.36 ms: 1.04x slower                                              |
| logging_silent             | 94.4 ns                                                      | 97.8 ns: 1.04x slower                                              |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                               |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                               |
| deepcopy                   | 368 us                                                       | 384 us: 1.04x slower                                               |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                              |
| chameleon                  | 7.23 ms                                                      | 7.54 ms: 1.04x slower                                              |
| spectral_norm              | 91.6 ms                                                      | 95.8 ms: 1.05x slower                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.05x slower                                              |
| sympy_expand               | 484 ms                                                       | 506 ms: 1.05x slower                                               |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                              |
| aiohttp                    | 1.02 ms                                                      | 1.08 ms: 1.06x slower                                              |
| hexiom                     | 5.96 ms                                                      | 6.33 ms: 1.06x slower                                              |
| float                      | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                              |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                              |
| unpickle                   | 14.8 us                                                      | 16.0 us: 1.08x slower                                              |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                               |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                              |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                               |
| pyflate                    | 439 ms                                                       | 487 ms: 1.11x slower                                               |
| tomli_loads                | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                             |
| create_gc_cycles           | 1.59 ms                                                      | 1.80 ms: 1.13x slower                                              |
| richards                   | 45.7 ms                                                      | 52.5 ms: 1.15x slower                                              |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| richards_super             | 51.3 ms                                                      | 59.3 ms: 1.15x slower                                              |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                               |
| unpack_sequence            | 53.2 ns                                                      | 62.5 ns: 1.18x slower                                              |
| gc_traversal               | 3.48 ms                                                      | 4.10 ms: 1.18x slower                                              |
| telco                      | 6.96 ms                                                      | 8.52 ms: 1.22x slower                                              |
| coverage                   | 66.7 ms                                                      | 84.3 ms: 1.26x slower                                              |
| mypy2                      | 830 ms                                                       | 1.05 sec: 1.27x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (6): nbody, asyncio_websockets, coroutines, xml_etree_iterparse, pycparser, bench_mp_pool
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 61.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x