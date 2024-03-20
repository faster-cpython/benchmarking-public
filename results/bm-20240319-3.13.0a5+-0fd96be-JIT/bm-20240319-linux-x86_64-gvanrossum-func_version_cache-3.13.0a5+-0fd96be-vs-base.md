# Results vs. base

- fork: gvanrossum
- ref: func_version_cache
- machine: linux-x86_64
- commit hash: 0fd96be
- commit date: 2024-03-19
- overall geometric mean: 1.00x faster
- HPT reliability: 80.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 7.00 ms                                                                | 6.93 ms: 1.01x faster                                                    |
| docutils       | 2.76 sec                                                               | 2.75 sec: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io  | 1.20 sec                                                               | 1.22 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x faster                                                     |
| nbody          | 91.9 ms                                                                | 92.6 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                                | 3.58 ms: 1.08x faster                                                    |
| regex_v8       | 25.7 ms                                                                | 24.3 ms: 1.06x faster                                                    |
| regex_dna      | 222 ms                                                                 | 219 ms: 1.01x faster                                                     |
| regex_compile  | 141 ms                                                                 | 143 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python | 313 us                                                                 | 304 us: 1.03x faster                                                     |
| tomli_loads        | 2.08 sec                                                               | 2.06 sec: 1.01x faster                                                   |
| pickle             | 11.7 us                                                                | 11.6 us: 1.01x faster                                                    |
| pickle_list        | 4.96 us                                                                | 4.93 us: 1.01x faster                                                    |
| pickle_dict        | 33.7 us                                                                | 33.5 us: 1.01x faster                                                    |
| xml_etree_parse    | 160 ms                                                                 | 161 ms: 1.01x slower                                                     |
| json_loads         | 28.1 us                                                                | 28.7 us: 1.02x slower                                                    |
| unpickle_list      | 4.86 us                                                                | 5.05 us: 1.04x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (6): json_dumps, unpickle_pure_python, xml_etree_process, xml_etree_generate, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                                | 11.5 ms: 1.00x faster                                                    |
| python_startup_no_site | 10.1 ms                                                                | 10.1 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 35.4 ms                                                                | 34.5 ms: 1.03x faster                                                    |
| genshi_text     | 24.6 ms                                                                | 24.2 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5+-025ef7a | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot             | 3.88 ms                                                                | 3.58 ms: 1.08x faster                                                    |
| regex_v8                 | 25.7 ms                                                                | 24.3 ms: 1.06x faster                                                    |
| deepcopy_memo            | 40.0 us                                                                | 38.5 us: 1.04x faster                                                    |
| pickle_pure_python       | 313 us                                                                 | 304 us: 1.03x faster                                                     |
| django_template          | 35.4 ms                                                                | 34.5 ms: 1.03x faster                                                    |
| nqueens                  | 92.6 ms                                                                | 90.2 ms: 1.03x faster                                                    |
| scimark_monte_carlo      | 72.5 ms                                                                | 70.7 ms: 1.03x faster                                                    |
| thrift                   | 822 us                                                                 | 805 us: 1.02x faster                                                     |
| unpack_sequence          | 89.5 ns                                                                | 87.7 ns: 1.02x faster                                                    |
| gc_traversal             | 3.92 ms                                                                | 3.85 ms: 1.02x faster                                                    |
| genshi_text              | 24.6 ms                                                                | 24.2 ms: 1.01x faster                                                    |
| mdp                      | 2.67 sec                                                               | 2.63 sec: 1.01x faster                                                   |
| typing_runtime_protocols | 113 us                                                                 | 111 us: 1.01x faster                                                     |
| chameleon                | 7.00 ms                                                                | 6.93 ms: 1.01x faster                                                    |
| regex_dna                | 222 ms                                                                 | 219 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult  | 5.11 ms                                                                | 5.06 ms: 1.01x faster                                                    |
| tomli_loads              | 2.08 sec                                                               | 2.06 sec: 1.01x faster                                                   |
| scimark_lu               | 132 ms                                                                 | 131 ms: 1.01x faster                                                     |
| scimark_sor              | 130 ms                                                                 | 129 ms: 1.01x faster                                                     |
| pickle                   | 11.7 us                                                                | 11.6 us: 1.01x faster                                                    |
| deltablue                | 3.49 ms                                                                | 3.46 ms: 1.01x faster                                                    |
| pickle_list              | 4.96 us                                                                | 4.93 us: 1.01x faster                                                    |
| pickle_dict              | 33.7 us                                                                | 33.5 us: 1.01x faster                                                    |
| sqlglot_transpile        | 1.67 ms                                                                | 1.66 ms: 1.01x faster                                                    |
| hexiom                   | 7.07 ms                                                                | 7.03 ms: 1.01x faster                                                    |
| aiohttp                  | 1.20 ms                                                                | 1.19 ms: 1.00x faster                                                    |
| pidigits                 | 190 ms                                                                 | 190 ms: 1.00x faster                                                     |
| deepcopy_reduce          | 3.14 us                                                                | 3.13 us: 1.00x faster                                                    |
| logging_simple           | 5.86 us                                                                | 5.84 us: 1.00x faster                                                    |
| go                       | 159 ms                                                                 | 158 ms: 1.00x faster                                                     |
| docutils                 | 2.76 sec                                                               | 2.75 sec: 1.00x faster                                                   |
| python_startup           | 11.5 ms                                                                | 11.5 ms: 1.00x faster                                                    |
| python_startup_no_site   | 10.1 ms                                                                | 10.1 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.85 sec                                                               | 1.85 sec: 1.00x slower                                                   |
| sqlglot_optimize         | 56.9 ms                                                                | 57.2 ms: 1.00x slower                                                    |
| generators               | 29.5 ms                                                                | 29.6 ms: 1.00x slower                                                    |
| asyncio_tcp              | 501 ms                                                                 | 504 ms: 1.00x slower                                                     |
| sympy_integrate          | 21.2 ms                                                                | 21.3 ms: 1.01x slower                                                    |
| coroutines               | 22.5 ms                                                                | 22.7 ms: 1.01x slower                                                    |
| fannkuch                 | 397 ms                                                                 | 400 ms: 1.01x slower                                                     |
| nbody                    | 91.9 ms                                                                | 92.6 ms: 1.01x slower                                                    |
| sympy_str                | 287 ms                                                                 | 289 ms: 1.01x slower                                                     |
| coverage                 | 97.7 ms                                                                | 98.6 ms: 1.01x slower                                                    |
| async_generators         | 474 ms                                                                 | 478 ms: 1.01x slower                                                     |
| regex_compile            | 141 ms                                                                 | 143 ms: 1.01x slower                                                     |
| xml_etree_parse          | 160 ms                                                                 | 161 ms: 1.01x slower                                                     |
| sympy_expand             | 484 ms                                                                 | 490 ms: 1.01x slower                                                     |
| chaos                    | 63.5 ms                                                                | 64.3 ms: 1.01x slower                                                    |
| scimark_fft              | 344 ms                                                                 | 348 ms: 1.01x slower                                                     |
| sympy_sum                | 161 ms                                                                 | 164 ms: 1.02x slower                                                     |
| json                     | 5.17 ms                                                                | 5.27 ms: 1.02x slower                                                    |
| pyflate                  | 486 ms                                                                 | 495 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 745 ms                                                                 | 760 ms: 1.02x slower                                                     |
| json_loads               | 28.1 us                                                                | 28.7 us: 1.02x slower                                                    |
| async_tree_io            | 1.20 sec                                                               | 1.22 sec: 1.02x slower                                                   |
| comprehensions           | 17.5 us                                                                | 17.9 us: 1.02x slower                                                    |
| unpickle_list            | 4.86 us                                                                | 5.05 us: 1.04x slower                                                    |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (45): pprint_pformat, genshi_xml, html5lib, telco, deepcopy, json_dumps, richards_super, async_tree_none_tg, crypto_pyaes, create_gc_cycles, async_tree_memoization_tg, raytrace, dask, sqlite_synth, mako, richards, async_tree_memoization, pylint, pathlib, mypy2, asyncio_websockets, float, meteor_contest, logging_silent, sqlglot_normalize, bench_thread_pool, async_tree_cpu_io_mixed_tg, gunicorn, async_tree_none, tornado_http, unpickle_pure_python, async_tree_cpu_io_mixed, bench_mp_pool, async_tree_io_tg, 2to3, xml_etree_process, dulwich_log, xml_etree_generate, sqlglot_parse, spectral_norm, djangocms, logging_format, pycparser, xml_etree_iterparse, unpickle


# HPT report

- Reliability score: 80.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x