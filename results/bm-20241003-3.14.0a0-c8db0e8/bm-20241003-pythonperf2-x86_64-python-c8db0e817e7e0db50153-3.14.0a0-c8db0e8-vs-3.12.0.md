# Results vs. 3.12.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-x86_64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.031x faster
- HPT reliability: 81.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 786 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.0 ms: 1.02x slower                                                       |
| nbody          | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.6 us: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.74 us: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.55 us: 1.03x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 40.6 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 786 ms: 1.34x faster                                                        |
| deepcopy                   | 368 us                                                       | 282 us: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 28.8 us: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.27x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 819 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.16x faster                                                       |
| go                         | 150 ms                                                       | 132 ms: 1.13x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 71.9 ms: 1.12x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.74 us: 1.11x faster                                                       |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.13 us: 1.10x faster                                                       |
| async_generators           | 390 ms                                                       | 357 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 904 us: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.9 ms: 1.05x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.04x faster                                                      |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 31.6 us: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.3 ms: 1.03x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                      |
| fannkuch                   | 350 ms                                                       | 352 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| sympy_expand               | 484 ms                                                       | 488 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 814 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                       |
| float                      | 76.6 ms                                                      | 78.0 ms: 1.02x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.74 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.7 ms: 1.02x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.55 us: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.19 ms: 1.04x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 55.3 ns: 1.04x slower                                                       |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.6 ns: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 97.2 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.6 ms: 1.06x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.2 ms: 1.10x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.4 ms: 1.10x slower                                                       |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                       |
| pyflate                    | 439 ms                                                       | 490 ms: 1.12x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.20 ms: 1.18x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.56 sec: 1.19x slower                                                      |
| coverage                   | 66.7 ms                                                      | 82.0 ms: 1.23x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.45 ms: 1.28x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.40 sec: 294.18x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (2): pycparser, scimark_sparse_mat_mult
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 81.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x