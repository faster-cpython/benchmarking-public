# Results vs. 3.12.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.02x faster
- HPT reliability: 91.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 785 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 809 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.0 us: 1.09x faster                                                       |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.30 us: 1.03x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.57 us: 1.02x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.64 sec: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 785 ms: 1.34x faster                                                        |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 809 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.7 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.9 ms: 1.12x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 865 us: 1.10x faster                                                        |
| async_generators           | 390 ms                                                       | 358 ms: 1.09x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.0 us: 1.09x faster                                                       |
| go                         | 150 ms                                                       | 138 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                       |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.0 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.50 us: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.30 us: 1.03x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 96.0 ms: 1.03x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 87.6 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.02x faster                                                        |
| unpickle_list              | 4.66 us                                                      | 4.57 us: 1.02x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                                       |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 284 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 803 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 58.3 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                                       |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.33 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                       |
| richards                   | 45.7 ms                                                      | 49.7 ms: 1.09x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.0 ms: 1.09x slower                                                       |
| pyflate                    | 439 ms                                                       | 487 ms: 1.11x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 60.1 ns: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.29 ms: 1.19x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.64 sec: 1.22x slower                                                      |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.78 ms: 1.37x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (6): bench_mp_pool, xml_etree_iterparse, pycparser, regex_effbot, asyncio_websockets, nbody
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 91.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x