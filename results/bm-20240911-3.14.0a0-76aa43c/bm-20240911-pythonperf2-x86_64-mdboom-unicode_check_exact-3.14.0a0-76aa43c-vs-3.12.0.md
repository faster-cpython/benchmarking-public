# Results vs. 3.12.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 95.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                       |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                     |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 787 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                       |
| nbody          | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                      |
| float          | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.03x slower                                                      |
| regex_dna      | 239 ms                                                       | 254 ms: 1.06x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.7 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 29.6 us: 1.10x faster                                                      |
| pickle_list          | 4.43 us                                                      | 4.18 us: 1.06x faster                                                      |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 4.76 us: 1.02x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.04x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| tomli_loads          | 2.16 sec                                                     | 2.51 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                      |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.6 ms: 1.01x slower                                                      |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 787 ms: 1.34x faster                                                       |
| deepcopy                   | 368 us                                                       | 280 us: 1.32x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                      |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                      |
| crypto_pyaes               | 80.3 ms                                                      | 71.8 ms: 1.12x faster                                                      |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                       |
| async_generators           | 390 ms                                                       | 354 ms: 1.10x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 29.6 us: 1.10x faster                                                      |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.82 us: 1.10x faster                                                      |
| bench_thread_pool          | 950 us                                                       | 874 us: 1.09x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.21 us: 1.08x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                      |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.18 us: 1.06x faster                                                      |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                       |
| chaos                      | 64.0 ms                                                      | 61.2 ms: 1.05x faster                                                      |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.2 ms: 1.04x faster                                                      |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                      |
| scimark_lu                 | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                      |
| nbody                      | 88.0 ms                                                      | 84.9 ms: 1.04x faster                                                      |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                      |
| unpack_sequence            | 53.2 ns                                                      | 51.6 ns: 1.03x faster                                                      |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                     |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                       |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                      |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                     |
| pprint_safe_repr           | 807 ms                                                       | 804 ms: 1.00x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.00x faster                                                     |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                       |
| django_template            | 38.2 ms                                                      | 38.6 ms: 1.01x slower                                                      |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                      |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                     |
| sqlglot_optimize           | 57.5 ms                                                      | 58.4 ms: 1.02x slower                                                      |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 66.6 ms: 1.02x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 4.76 us: 1.02x slower                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.03x slower                                                      |
| json                       | 5.12 ms                                                      | 5.25 ms: 1.03x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                      |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.3 us: 1.04x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 98.7 ns: 1.05x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                      |
| float                      | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.29 ms: 1.06x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                                      |
| regex_dna                  | 239 ms                                                       | 254 ms: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                       |
| richards                   | 45.7 ms                                                      | 49.6 ms: 1.08x slower                                                      |
| richards_super             | 51.3 ms                                                      | 56.1 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.7 ms: 1.13x slower                                                      |
| pyflate                    | 439 ms                                                       | 497 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.51 sec: 1.16x slower                                                     |
| telco                      | 6.96 ms                                                      | 8.24 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                      |
| coverage                   | 66.7 ms                                                      | 85.2 ms: 1.28x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 4.89 ms: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                               |

Benchmark hidden because not significant (3): bench_mp_pool, pycparser, asyncio_websockets
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x