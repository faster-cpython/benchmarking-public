# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.044x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                           |
| tornado_http   | 103 ms                                                 | 91.5 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 966 ms: 1.22x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 489 ms: 1.18x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 995 ms: 1.16x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 390 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 498 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 635 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                           |
| async_tree_none            | 472 ms                                                 | 424 ms: 1.11x faster                                                           |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                          |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                           |
| float          | 84.7 ms                                                | 97.0 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                          |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                           |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                         |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                           |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                          |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                                          |
| unpickle_list        | 5.29 us                                                | 5.22 us: 1.01x faster                                                          |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                          |
| xml_etree_generate   | 89.2 ms                                                | 93.0 ms: 1.04x slower                                                          |
| xml_etree_process    | 61.7 ms                                                | 65.1 ms: 1.05x slower                                                          |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.05x slower                                                          |
| xml_etree_parse      | 159 ms                                                 | 184 ms: 1.16x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 150 ms: 1.40x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                          |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                          |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 966 ms: 1.22x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                          |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 489 ms: 1.18x faster                                                           |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 995 ms: 1.16x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 390 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 498 ms: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 635 ms: 1.14x faster                                                           |
| logging_format             | 7.23 us                                                | 6.34 us: 1.14x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                          |
| tornado_http               | 103 ms                                                 | 91.5 ms: 1.12x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 73.4 ms: 1.11x faster                                                          |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                           |
| async_tree_none            | 472 ms                                                 | 424 ms: 1.11x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                         |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                                          |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                          |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                          |
| unpack_sequence            | 54.0 ns                                                | 49.5 ns: 1.09x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 790 us: 1.07x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 64.8 ms: 1.06x faster                                                          |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                          |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                          |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                          |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                           |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.88 ms: 1.04x faster                                                          |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 480 ms: 1.02x faster                                                           |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                           |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.31 ms: 1.02x faster                                                          |
| unpickle_list              | 5.29 us                                                | 5.22 us: 1.01x faster                                                          |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 54.3 ms: 1.01x faster                                                          |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                           |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                          |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                          |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                          |
| richards_super             | 51.5 ms                                                | 52.4 ms: 1.02x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                          |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                          |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.41 ms: 1.03x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                         |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                         |
| xml_etree_generate         | 89.2 ms                                                | 93.0 ms: 1.04x slower                                                          |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                           |
| xml_etree_process          | 61.7 ms                                                | 65.1 ms: 1.05x slower                                                          |
| pickle_list                | 5.08 us                                                | 5.36 us: 1.05x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                          |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.68 ms: 1.14x slower                                                          |
| float                      | 84.7 ms                                                | 97.0 ms: 1.15x slower                                                          |
| xml_etree_parse            | 159 ms                                                 | 184 ms: 1.16x slower                                                           |
| telco                      | 7.10 ms                                                | 8.42 ms: 1.19x slower                                                          |
| coverage                   | 72.7 ms                                                | 86.6 ms: 1.19x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 150 ms: 1.40x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                   |

Benchmark hidden because not significant (7): sqlglot_transpile, typing_runtime_protocols, sqlite_synth, bench_mp_pool, docutils, json_dumps, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240927-3.14.0a0-9d28e99/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.044x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.96x