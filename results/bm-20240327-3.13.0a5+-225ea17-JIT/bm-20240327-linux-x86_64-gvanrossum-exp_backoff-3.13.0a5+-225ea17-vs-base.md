# Results vs. base

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 225ea17
- commit date: 2024-03-27
- overall geometric mean: 1.01x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 276 ms                                                                 | 279 ms: 1.01x slower                                              |
| chameleon      | 6.88 ms                                                                | 7.21 ms: 1.05x slower                                             |
| html5lib       | 67.8 ms                                                                | 66.2 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 602 ms                                                                 | 583 ms: 1.03x faster                                              |
| async_tree_none_tg         | 350 ms                                                                 | 341 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed    | 615 ms                                                                 | 601 ms: 1.02x faster                                              |
| async_tree_none            | 354 ms                                                                 | 390 ms: 1.10x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 77.8 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 147 ms                                                                 | 146 ms: 1.01x faster                                              |
| regex_effbot   | 3.75 ms                                                                | 3.81 ms: 1.02x slower                                             |
| regex_v8       | 25.3 ms                                                                | 26.1 ms: 1.03x slower                                             |
| regex_dna      | 217 ms                                                                 | 229 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.09 sec                                                               | 2.07 sec: 1.01x faster                                            |
| unpickle_list        | 5.29 us                                                                | 5.24 us: 1.01x faster                                             |
| pickle_pure_python   | 306 us                                                                 | 308 us: 1.01x slower                                              |
| xml_etree_process    | 60.0 ms                                                                | 60.5 ms: 1.01x slower                                             |
| xml_etree_iterparse  | 107 ms                                                                 | 108 ms: 1.01x slower                                              |
| json_dumps           | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                             |
| xml_etree_generate   | 87.0 ms                                                                | 88.6 ms: 1.02x slower                                             |
| json_loads           | 28.6 us                                                                | 29.1 us: 1.02x slower                                             |
| unpickle_pure_python | 241 us                                                                 | 246 us: 1.02x slower                                              |
| pickle               | 11.6 us                                                                | 12.3 us: 1.06x slower                                             |
| pickle_list          | 4.94 us                                                                | 5.30 us: 1.07x slower                                             |
| unpickle             | 15.2 us                                                                | 16.4 us: 1.08x slower                                             |
| pickle_dict          | 34.3 us                                                                | 37.2 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                             |
| python_startup_no_site | 9.48 ms                                                                | 9.55 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 54.3 ms                                                                | 53.5 ms: 1.02x faster                                             |
| mako           | 10.8 ms                                                                | 10.8 ms: 1.01x faster                                             |
| genshi_text    | 24.3 ms                                                                | 24.5 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 602 ms                                                                 | 583 ms: 1.03x faster                                              |
| async_tree_none_tg         | 350 ms                                                                 | 341 ms: 1.03x faster                                              |
| html5lib                   | 67.8 ms                                                                | 66.2 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 615 ms                                                                 | 601 ms: 1.02x faster                                              |
| fannkuch                   | 396 ms                                                                 | 389 ms: 1.02x faster                                              |
| hexiom                     | 7.23 ms                                                                | 7.12 ms: 1.02x faster                                             |
| pyflate                    | 493 ms                                                                 | 485 ms: 1.02x faster                                              |
| nqueens                    | 90.1 ms                                                                | 88.7 ms: 1.02x faster                                             |
| genshi_xml                 | 54.3 ms                                                                | 53.5 ms: 1.02x faster                                             |
| comprehensions             | 18.4 us                                                                | 18.2 us: 1.01x faster                                             |
| go                         | 155 ms                                                                 | 154 ms: 1.01x faster                                              |
| tomli_loads                | 2.09 sec                                                               | 2.07 sec: 1.01x faster                                            |
| unpickle_list              | 5.29 us                                                                | 5.24 us: 1.01x faster                                             |
| deepcopy                   | 360 us                                                                 | 356 us: 1.01x faster                                              |
| mako                       | 10.8 ms                                                                | 10.8 ms: 1.01x faster                                             |
| scimark_fft                | 351 ms                                                                 | 348 ms: 1.01x faster                                              |
| regex_compile              | 147 ms                                                                 | 146 ms: 1.01x faster                                              |
| sqlglot_normalize          | 113 ms                                                                 | 112 ms: 1.01x faster                                              |
| asyncio_tcp_ssl            | 1.86 sec                                                               | 1.85 sec: 1.01x faster                                            |
| meteor_contest             | 111 ms                                                                 | 111 ms: 1.00x faster                                              |
| mdp                        | 2.65 sec                                                               | 2.65 sec: 1.00x faster                                            |
| asyncio_tcp                | 510 ms                                                                 | 508 ms: 1.00x faster                                              |
| python_startup             | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                             |
| richards_super             | 52.6 ms                                                                | 52.8 ms: 1.00x slower                                             |
| bench_thread_pool          | 852 us                                                                 | 856 us: 1.00x slower                                              |
| sympy_integrate            | 21.8 ms                                                                | 21.9 ms: 1.01x slower                                             |
| richards                   | 46.7 ms                                                                | 47.0 ms: 1.01x slower                                             |
| genshi_text                | 24.3 ms                                                                | 24.5 ms: 1.01x slower                                             |
| python_startup_no_site     | 9.48 ms                                                                | 9.55 ms: 1.01x slower                                             |
| pickle_pure_python         | 306 us                                                                 | 308 us: 1.01x slower                                              |
| xml_etree_process          | 60.0 ms                                                                | 60.5 ms: 1.01x slower                                             |
| async_generators           | 463 ms                                                                 | 467 ms: 1.01x slower                                              |
| sympy_str                  | 291 ms                                                                 | 293 ms: 1.01x slower                                              |
| scimark_monte_carlo        | 71.0 ms                                                                | 71.6 ms: 1.01x slower                                             |
| xml_etree_iterparse        | 107 ms                                                                 | 108 ms: 1.01x slower                                              |
| 2to3                       | 276 ms                                                                 | 279 ms: 1.01x slower                                              |
| sqlglot_transpile          | 1.64 ms                                                                | 1.66 ms: 1.01x slower                                             |
| json_dumps                 | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                             |
| sympy_sum                  | 165 ms                                                                 | 167 ms: 1.01x slower                                              |
| raytrace                   | 289 ms                                                                 | 293 ms: 1.01x slower                                              |
| sympy_expand               | 491 ms                                                                 | 497 ms: 1.01x slower                                              |
| deepcopy_reduce            | 3.17 us                                                                | 3.21 us: 1.01x slower                                             |
| sqlglot_parse              | 1.32 ms                                                                | 1.34 ms: 1.01x slower                                             |
| telco                      | 8.69 ms                                                                | 8.82 ms: 1.01x slower                                             |
| float                      | 76.7 ms                                                                | 77.8 ms: 1.01x slower                                             |
| regex_effbot               | 3.75 ms                                                                | 3.81 ms: 1.02x slower                                             |
| thrift                     | 810 us                                                                 | 823 us: 1.02x slower                                              |
| coverage                   | 96.4 ms                                                                | 97.9 ms: 1.02x slower                                             |
| logging_format             | 6.57 us                                                                | 6.68 us: 1.02x slower                                             |
| logging_silent             | 104 ns                                                                 | 105 ns: 1.02x slower                                              |
| create_gc_cycles           | 1.67 ms                                                                | 1.70 ms: 1.02x slower                                             |
| xml_etree_generate         | 87.0 ms                                                                | 88.6 ms: 1.02x slower                                             |
| json_loads                 | 28.6 us                                                                | 29.1 us: 1.02x slower                                             |
| unpickle_pure_python       | 241 us                                                                 | 246 us: 1.02x slower                                              |
| pprint_pformat             | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                            |
| scimark_sor                | 131 ms                                                                 | 134 ms: 1.02x slower                                              |
| json                       | 5.37 ms                                                                | 5.50 ms: 1.02x slower                                             |
| generators                 | 29.5 ms                                                                | 30.2 ms: 1.02x slower                                             |
| spectral_norm              | 114 ms                                                                 | 117 ms: 1.03x slower                                              |
| regex_v8                   | 25.3 ms                                                                | 26.1 ms: 1.03x slower                                             |
| typing_runtime_protocols   | 111 us                                                                 | 115 us: 1.03x slower                                              |
| chameleon                  | 6.88 ms                                                                | 7.21 ms: 1.05x slower                                             |
| regex_dna                  | 217 ms                                                                 | 229 ms: 1.05x slower                                              |
| pickle                     | 11.6 us                                                                | 12.3 us: 1.06x slower                                             |
| pycparser                  | 1.17 sec                                                               | 1.25 sec: 1.06x slower                                            |
| gc_traversal               | 3.69 ms                                                                | 3.95 ms: 1.07x slower                                             |
| pickle_list                | 4.94 us                                                                | 5.30 us: 1.07x slower                                             |
| unpickle                   | 15.2 us                                                                | 16.4 us: 1.08x slower                                             |
| pickle_dict                | 34.3 us                                                                | 37.2 us: 1.08x slower                                             |
| async_tree_none            | 354 ms                                                                 | 390 ms: 1.10x slower                                              |
| deltablue                  | 3.44 ms                                                                | 3.94 ms: 1.15x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (31): nbody, pprint_safe_repr, mypy2, deepcopy_memo, dask, scimark_sparse_mat_mult, django_template, sqlite_synth, sqlglot_optimize, tornado_http, crypto_pyaes, docutils, unpack_sequence, dulwich_log, pidigits, gunicorn, asyncio_websockets, djangocms, scimark_lu, async_tree_memoization_tg, bench_mp_pool, chaos, pathlib, xml_etree_parse, logging_simple, aiohttp, pylint, coroutines, async_tree_io_tg, async_tree_memoization, async_tree_io


# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.00x