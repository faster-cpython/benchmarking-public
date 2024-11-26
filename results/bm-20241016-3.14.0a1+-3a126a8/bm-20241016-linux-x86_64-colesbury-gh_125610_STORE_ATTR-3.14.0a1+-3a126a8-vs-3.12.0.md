# Results vs. 3.12.0

- fork: colesbury
- ref: gh_125610_STORE_ATTR
- machine: linux-x86_64
- commit hash: 3a126a8
- commit date: 2024-10-16
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                      |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                    |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 853 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 975 ms: 1.21x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                     |
| float          | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                      |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                     |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 853 ms: 1.36x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.32x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 975 ms: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                     |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                      |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                     |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                     |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                     |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                     |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                     |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 63.6 ms: 1.08x faster                                                     |
| float                      | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                     |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                     |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                                     |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                     |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                     |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                     |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                      |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                      |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 82.7 ms: 1.01x faster                                                     |
| pyflate                    | 482 ms                                                 | 480 ms: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 838 us: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                      |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                     |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.37 ms: 1.15x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (6): logging_silent, xml_etree_iterparse, regex_effbot, xml_etree_parse, spectral_norm, richards
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-3a126a8/bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.072x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x