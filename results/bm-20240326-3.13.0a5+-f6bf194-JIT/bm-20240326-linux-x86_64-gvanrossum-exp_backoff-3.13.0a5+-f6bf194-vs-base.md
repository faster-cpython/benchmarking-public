# Results vs. base

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: f6bf194
- commit date: 2024-03-26
- overall geometric mean: 1.01x faster
- HPT reliability: 69.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 276 ms                                                                 | 279 ms: 1.01x slower                                              |
| chameleon      | 6.88 ms                                                                | 7.17 ms: 1.04x slower                                             |
| docutils       | 2.90 sec                                                               | 2.84 sec: 1.02x faster                                            |
| html5lib       | 67.8 ms                                                                | 66.2 ms: 1.03x faster                                             |
| tornado_http   | 96.8 ms                                                                | 96.5 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 602 ms                                                                 | 583 ms: 1.03x faster                                              |
| async_tree_none_tg         | 350 ms                                                                 | 341 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed    | 615 ms                                                                 | 599 ms: 1.03x faster                                              |
| async_tree_none            | 354 ms                                                                 | 386 ms: 1.09x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (4): async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 77.5 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 147 ms                                                                 | 139 ms: 1.06x faster                                              |
| regex_effbot   | 3.75 ms                                                                | 3.77 ms: 1.01x slower                                             |
| regex_v8       | 25.3 ms                                                                | 25.7 ms: 1.01x slower                                             |
| regex_dna      | 217 ms                                                                 | 227 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 241 us                                                                 | 232 us: 1.04x faster                                              |
| pickle_dict          | 34.3 us                                                                | 33.5 us: 1.02x faster                                             |
| tomli_loads          | 2.09 sec                                                               | 2.06 sec: 1.01x faster                                            |
| json_loads           | 28.6 us                                                                | 28.7 us: 1.01x slower                                             |
| json_dumps           | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                             |
| unpickle_list        | 5.29 us                                                                | 5.43 us: 1.03x slower                                             |
| pickle               | 11.6 us                                                                | 12.0 us: 1.04x slower                                             |
| unpickle             | 15.2 us                                                                | 17.0 us: 1.12x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 36.1 ms                                                                | 35.8 ms: 1.01x faster                                             |
| mako            | 10.8 ms                                                                | 10.9 ms: 1.00x slower                                             |
| genshi_text     | 24.3 ms                                                                | 25.2 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpack_sequence            | 86.5 ns                                                                | 51.5 ns: 1.68x faster                                             |
| scimark_lu                 | 134 ms                                                                 | 115 ms: 1.16x faster                                              |
| richards                   | 46.7 ms                                                                | 44.1 ms: 1.06x faster                                             |
| regex_compile              | 147 ms                                                                 | 139 ms: 1.06x faster                                              |
| hexiom                     | 7.23 ms                                                                | 6.87 ms: 1.05x faster                                             |
| scimark_sor                | 131 ms                                                                 | 124 ms: 1.05x faster                                              |
| go                         | 155 ms                                                                 | 148 ms: 1.05x faster                                              |
| raytrace                   | 289 ms                                                                 | 275 ms: 1.05x faster                                              |
| unpickle_pure_python       | 241 us                                                                 | 232 us: 1.04x faster                                              |
| richards_super             | 52.6 ms                                                                | 50.7 ms: 1.04x faster                                             |
| deltablue                  | 3.44 ms                                                                | 3.32 ms: 1.04x faster                                             |
| dulwich_log                | 70.9 ms                                                                | 68.6 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed_tg | 602 ms                                                                 | 583 ms: 1.03x faster                                              |
| mypy2                      | 789 ms                                                                 | 766 ms: 1.03x faster                                              |
| async_tree_none_tg         | 350 ms                                                                 | 341 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed    | 615 ms                                                                 | 599 ms: 1.03x faster                                              |
| html5lib                   | 67.8 ms                                                                | 66.2 ms: 1.03x faster                                             |
| nqueens                    | 90.1 ms                                                                | 87.9 ms: 1.03x faster                                             |
| sqlglot_optimize           | 58.1 ms                                                                | 56.7 ms: 1.02x faster                                             |
| comprehensions             | 18.4 us                                                                | 18.0 us: 1.02x faster                                             |
| docutils                   | 2.90 sec                                                               | 2.84 sec: 1.02x faster                                            |
| pickle_dict                | 34.3 us                                                                | 33.5 us: 1.02x faster                                             |
| sympy_integrate            | 21.8 ms                                                                | 21.3 ms: 1.02x faster                                             |
| scimark_fft                | 351 ms                                                                 | 344 ms: 1.02x faster                                              |
| scimark_sparse_mat_mult    | 5.02 ms                                                                | 4.93 ms: 1.02x faster                                             |
| tomli_loads                | 2.09 sec                                                               | 2.06 sec: 1.01x faster                                            |
| pyflate                    | 493 ms                                                                 | 486 ms: 1.01x faster                                              |
| telco                      | 8.69 ms                                                                | 8.58 ms: 1.01x faster                                             |
| deepcopy_memo              | 39.5 us                                                                | 39.0 us: 1.01x faster                                             |
| sympy_sum                  | 165 ms                                                                 | 163 ms: 1.01x faster                                              |
| django_template            | 36.1 ms                                                                | 35.8 ms: 1.01x faster                                             |
| asyncio_tcp                | 510 ms                                                                 | 506 ms: 1.01x faster                                              |
| sqlglot_normalize          | 113 ms                                                                 | 112 ms: 1.01x faster                                              |
| sympy_str                  | 291 ms                                                                 | 289 ms: 1.01x faster                                              |
| python_startup             | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.86 sec                                                               | 1.85 sec: 1.00x faster                                            |
| tornado_http               | 96.8 ms                                                                | 96.5 ms: 1.00x faster                                             |
| mako                       | 10.8 ms                                                                | 10.9 ms: 1.00x slower                                             |
| json_loads                 | 28.6 us                                                                | 28.7 us: 1.01x slower                                             |
| crypto_pyaes               | 75.0 ms                                                                | 75.5 ms: 1.01x slower                                             |
| regex_effbot               | 3.75 ms                                                                | 3.77 ms: 1.01x slower                                             |
| 2to3                       | 276 ms                                                                 | 279 ms: 1.01x slower                                              |
| json                       | 5.37 ms                                                                | 5.42 ms: 1.01x slower                                             |
| logging_simple             | 5.96 us                                                                | 6.02 us: 1.01x slower                                             |
| async_generators           | 463 ms                                                                 | 468 ms: 1.01x slower                                              |
| float                      | 76.7 ms                                                                | 77.5 ms: 1.01x slower                                             |
| create_gc_cycles           | 1.67 ms                                                                | 1.69 ms: 1.01x slower                                             |
| pprint_safe_repr           | 753 ms                                                                 | 762 ms: 1.01x slower                                              |
| logging_silent             | 104 ns                                                                 | 105 ns: 1.01x slower                                              |
| fannkuch                   | 396 ms                                                                 | 401 ms: 1.01x slower                                              |
| logging_format             | 6.57 us                                                                | 6.66 us: 1.01x slower                                             |
| json_dumps                 | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                             |
| regex_v8                   | 25.3 ms                                                                | 25.7 ms: 1.01x slower                                             |
| spectral_norm              | 114 ms                                                                 | 116 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 111 us                                                                 | 114 us: 1.03x slower                                              |
| unpickle_list              | 5.29 us                                                                | 5.43 us: 1.03x slower                                             |
| coroutines                 | 23.0 ms                                                                | 23.6 ms: 1.03x slower                                             |
| generators                 | 29.5 ms                                                                | 30.3 ms: 1.03x slower                                             |
| pprint_pformat             | 1.51 sec                                                               | 1.57 sec: 1.04x slower                                            |
| pickle                     | 11.6 us                                                                | 12.0 us: 1.04x slower                                             |
| genshi_text                | 24.3 ms                                                                | 25.2 ms: 1.04x slower                                             |
| coverage                   | 96.4 ms                                                                | 100 ms: 1.04x slower                                              |
| chameleon                  | 6.88 ms                                                                | 7.17 ms: 1.04x slower                                             |
| gc_traversal               | 3.69 ms                                                                | 3.86 ms: 1.05x slower                                             |
| regex_dna                  | 217 ms                                                                 | 227 ms: 1.05x slower                                              |
| pycparser                  | 1.17 sec                                                               | 1.24 sec: 1.06x slower                                            |
| thrift                     | 810 us                                                                 | 858 us: 1.06x slower                                              |
| async_tree_none            | 354 ms                                                                 | 386 ms: 1.09x slower                                              |
| unpickle                   | 15.2 us                                                                | 17.0 us: 1.12x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (33): pylint, async_tree_io, djangocms, nbody, gunicorn, deepcopy_reduce, genshi_xml, async_tree_memoization_tg, pickle_pure_python, pathlib, xml_etree_generate, deepcopy, dask, bench_thread_pool, meteor_contest, xml_etree_iterparse, xml_etree_parse, python_startup_no_site, pidigits, mdp, sympy_expand, xml_etree_process, asyncio_websockets, bench_mp_pool, pickle_list, chaos, sqlite_synth, sqlglot_transpile, aiohttp, scimark_monte_carlo, async_tree_io_tg, sqlglot_parse, async_tree_memoization


# HPT report

- Reliability score: 69.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.99x