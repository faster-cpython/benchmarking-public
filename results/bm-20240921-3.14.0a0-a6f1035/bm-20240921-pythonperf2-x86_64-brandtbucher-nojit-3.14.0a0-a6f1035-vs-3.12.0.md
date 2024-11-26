# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.020x faster
- HPT reliability: 65.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                               |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                             |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 774 ms: 1.36x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 569 ms: 1.22x faster                                               |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                               |
| float          | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                               |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                              |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                               |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.3 us: 1.07x faster                                              |
| pickle_list          | 4.43 us                                                      | 4.18 us: 1.06x faster                                              |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                              |
| xml_etree_generate   | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                              |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                               |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                               |
| pickle_pure_python   | 318 us                                                       | 323 us: 1.01x slower                                               |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                              |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                              |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                               |
| unpickle_list        | 4.66 us                                                      | 4.81 us: 1.03x slower                                              |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.05x slower                                              |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                              |
| tomli_loads          | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                              |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                              |
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                               |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 774 ms: 1.36x faster                                               |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                              |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                               |
| deepcopy                   | 368 us                                                       | 291 us: 1.27x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                               |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 569 ms: 1.22x faster                                               |
| deepcopy_memo              | 36.8 us                                                      | 30.1 us: 1.22x faster                                              |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                              |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                               |
| crypto_pyaes               | 80.3 ms                                                      | 73.2 ms: 1.10x faster                                              |
| raytrace                   | 298 ms                                                       | 275 ms: 1.08x faster                                               |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                               |
| pickle_dict                | 32.5 us                                                      | 30.3 us: 1.07x faster                                              |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                               |
| bench_thread_pool          | 950 us                                                       | 894 us: 1.06x faster                                               |
| pickle_list                | 4.43 us                                                      | 4.18 us: 1.06x faster                                              |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                              |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                               |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                               |
| logging_format             | 7.48 us                                                      | 7.15 us: 1.05x faster                                              |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                               |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                              |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                               |
| chaos                      | 64.0 ms                                                      | 62.5 ms: 1.02x faster                                              |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.4 ms: 1.02x faster                                              |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.02x faster                                             |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                              |
| logging_simple             | 6.71 us                                                      | 6.58 us: 1.02x faster                                              |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                               |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                              |
| xml_etree_generate         | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                               |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                               |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                               |
| sqlite_synth               | 2.77 us                                                      | 2.75 us: 1.01x faster                                              |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                               |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                             |
| pprint_safe_repr           | 807 ms                                                       | 815 ms: 1.01x slower                                               |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                               |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                               |
| pickle_pure_python         | 318 us                                                       | 323 us: 1.01x slower                                               |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.01x slower                                             |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                             |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                              |
| nqueens                    | 89.9 ms                                                      | 91.4 ms: 1.02x slower                                              |
| dulwich_log                | 65.4 ms                                                      | 66.5 ms: 1.02x slower                                              |
| scimark_fft                | 301 ms                                                       | 307 ms: 1.02x slower                                               |
| json                       | 5.12 ms                                                      | 5.23 ms: 1.02x slower                                              |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                              |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 59.1 ms: 1.03x slower                                              |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                               |
| unpickle_list              | 4.66 us                                                      | 4.81 us: 1.03x slower                                              |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                              |
| unpack_sequence            | 53.2 ns                                                      | 55.2 ns: 1.04x slower                                              |
| django_template            | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                              |
| float                      | 76.6 ms                                                      | 79.6 ms: 1.04x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                              |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                               |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.05x slower                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.40 ms: 1.05x slower                                              |
| hexiom                     | 5.96 ms                                                      | 6.26 ms: 1.05x slower                                              |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                              |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                              |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                              |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                               |
| spectral_norm              | 91.6 ms                                                      | 97.6 ms: 1.06x slower                                              |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                              |
| richards_super             | 51.3 ms                                                      | 55.8 ms: 1.09x slower                                              |
| richards                   | 45.7 ms                                                      | 50.0 ms: 1.09x slower                                              |
| pyflate                    | 439 ms                                                       | 483 ms: 1.10x slower                                               |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                               |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                              |
| scimark_sor                | 109 ms                                                       | 129 ms: 1.18x slower                                               |
| tomli_loads                | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                             |
| telco                      | 6.96 ms                                                      | 8.45 ms: 1.21x slower                                              |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                              |
| coverage                   | 66.7 ms                                                      | 86.1 ms: 1.29x slower                                              |
| gc_traversal               | 3.48 ms                                                      | 4.70 ms: 1.35x slower                                              |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (4): bench_mp_pool, pycparser, scimark_lu, nbody
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 65.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x