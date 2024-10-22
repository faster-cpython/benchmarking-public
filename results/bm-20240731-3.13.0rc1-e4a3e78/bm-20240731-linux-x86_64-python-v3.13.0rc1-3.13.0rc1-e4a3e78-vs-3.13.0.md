# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 97.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 266 ms: 1.00x slower                                         |
| chameleon      | 6.85 ms                                                | 6.88 ms: 1.00x slower                                        |
| docutils       | 2.58 sec                                               | 2.77 sec: 1.07x slower                                       |
| html5lib       | 64.5 ms                                                | 66.6 ms: 1.03x slower                                        |
| tornado_http   | 91.5 ms                                                | 91.0 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 440 ms: 1.06x faster                                         |
| coroutines                 | 22.5 ms                                                | 22.0 ms: 1.02x faster                                        |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                       |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                         |
| async_tree_none            | 354 ms                                                 | 367 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 594 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 572 ms: 1.05x slower                                         |
| async_tree_io              | 843 ms                                                 | 893 ms: 1.06x slower                                         |
| async_tree_none_tg         | 320 ms                                                 | 341 ms: 1.07x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 895 ms: 1.08x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.7 ms: 1.02x faster                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.85 ms: 1.01x faster                                        |
| regex_compile  | 131 ms                                                 | 132 ms: 1.00x slower                                         |
| regex_v8       | 25.3 ms                                                | 26.3 ms: 1.04x slower                                        |
| regex_dna      | 220 ms                                                 | 237 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                        |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                         |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                         |
| xml_etree_generate   | 87.0 ms                                                | 88.0 ms: 1.01x slower                                        |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                        |
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.6 ms: 1.03x faster                                        |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 714 ms: 1.50x faster                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 440 ms: 1.06x faster                                         |
| mdp                        | 2.74 sec                                               | 2.66 sec: 1.03x faster                                       |
| json                       | 5.20 ms                                                | 5.04 ms: 1.03x faster                                        |
| telco                      | 8.45 ms                                                | 8.23 ms: 1.03x faster                                        |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.03x faster                                        |
| django_template            | 34.4 ms                                                | 33.6 ms: 1.03x faster                                        |
| float                      | 78.5 ms                                                | 76.7 ms: 1.02x faster                                        |
| coroutines                 | 22.5 ms                                                | 22.0 ms: 1.02x faster                                        |
| gc_traversal               | 3.81 ms                                                | 3.73 ms: 1.02x faster                                        |
| hexiom                     | 6.13 ms                                                | 6.02 ms: 1.02x faster                                        |
| pprint_safe_repr           | 744 ms                                                 | 734 ms: 1.01x faster                                         |
| richards                   | 48.1 ms                                                | 47.5 ms: 1.01x faster                                        |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.01x faster                                        |
| regex_effbot               | 3.88 ms                                                | 3.85 ms: 1.01x faster                                        |
| pathlib                    | 17.1 ms                                                | 16.9 ms: 1.01x faster                                        |
| richards_super             | 54.4 ms                                                | 54.0 ms: 1.01x faster                                        |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                         |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                        |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                        |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                       |
| tornado_http               | 91.5 ms                                                | 91.0 ms: 1.01x faster                                        |
| comprehensions             | 16.4 us                                                | 16.3 us: 1.00x faster                                        |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x faster                                        |
| bench_thread_pool          | 815 us                                                 | 812 us: 1.00x faster                                         |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                         |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| 2to3                       | 265 ms                                                 | 266 ms: 1.00x slower                                         |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.00x slower                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                       |
| regex_compile              | 131 ms                                                 | 132 ms: 1.00x slower                                         |
| dulwich_log                | 63.0 ms                                                | 63.2 ms: 1.00x slower                                        |
| crypto_pyaes               | 73.0 ms                                                | 73.3 ms: 1.00x slower                                        |
| chameleon                  | 6.85 ms                                                | 6.88 ms: 1.00x slower                                        |
| deepcopy                   | 352 us                                                 | 354 us: 1.01x slower                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                        |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                         |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.01x slower                                        |
| deltablue                  | 3.15 ms                                                | 3.17 ms: 1.01x slower                                        |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                         |
| nqueens                    | 80.6 ms                                                | 81.4 ms: 1.01x slower                                        |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                        |
| xml_etree_generate         | 87.0 ms                                                | 88.0 ms: 1.01x slower                                        |
| deepcopy_memo              | 38.0 us                                                | 38.5 us: 1.01x slower                                        |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                         |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                         |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 68.1 ms: 1.03x slower                                        |
| html5lib                   | 64.5 ms                                                | 66.6 ms: 1.03x slower                                        |
| async_tree_none            | 354 ms                                                 | 367 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 594 ms: 1.04x slower                                         |
| pyflate                    | 460 ms                                                 | 477 ms: 1.04x slower                                         |
| regex_v8                   | 25.3 ms                                                | 26.3 ms: 1.04x slower                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.91 sec: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 572 ms: 1.05x slower                                         |
| async_tree_io              | 843 ms                                                 | 893 ms: 1.06x slower                                         |
| async_tree_none_tg         | 320 ms                                                 | 341 ms: 1.07x slower                                         |
| dask                       | 338 ms                                                 | 361 ms: 1.07x slower                                         |
| docutils                   | 2.58 sec                                               | 2.77 sec: 1.07x slower                                       |
| regex_dna                  | 220 ms                                                 | 237 ms: 1.08x slower                                         |
| fannkuch                   | 381 ms                                                 | 411 ms: 1.08x slower                                         |
| scimark_sor                | 122 ms                                                 | 132 ms: 1.08x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 895 ms: 1.08x slower                                         |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (27): pycparser, logging_format, scimark_fft, thrift, xml_etree_parse, scimark_lu, logging_simple, nbody, asyncio_websockets, deepcopy_reduce, sympy_expand, meteor_contest, go, scimark_sparse_mat_mult, sqlglot_transpile, bench_mp_pool, sqlglot_optimize, json_loads, genshi_text, genshi_xml, raytrace, tomli_loads, coverage, xml_etree_process, sympy_str, async_tree_memoization, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x