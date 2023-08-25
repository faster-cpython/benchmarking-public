
# Results vs. 3.11.0

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster \*
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 257 ms: 1.01x faster                                   |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 77.2 ms                                                | 76.6 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                  |
| regex_dna      | 204 ms                                                 | 192 ms: 1.06x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|--------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle           | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| json_loads         | 26.5 us                                                | 26.2 us: 1.01x faster                                  |
| json_dumps         | 12.6 ms                                                | 12.5 ms: 1.01x faster                                  |
| xml_etree_generate | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| unpickle_list      | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| pickle_dict        | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| pickle_list        | 4.11 us                                                | 4.16 us: 1.01x slower                                  |
| Geometric mean     | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (6): pickle, pickle_pure_python, xml_etree_process, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.47 ms: 1.01x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 5.97 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 10.1 ms                                                | 9.83 ms: 1.03x faster                                  |
| genshi_text    | 21.6 ms                                                | 21.7 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.39 ms: 1.18x faster                                  |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                 |
| regex_dna               | 204 ms                                                 | 192 ms: 1.06x faster                                   |
| aiohttp                 | 1.10 ms                                                | 1.05 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| gunicorn                | 1.18 ms                                                | 1.13 ms: 1.04x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 884 ms: 1.04x faster                                   |
| async_generators        | 368 ms                                                 | 357 ms: 1.03x faster                                   |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                 |
| scimark_sor             | 118 ms                                                 | 115 ms: 1.03x faster                                   |
| logging_format          | 6.68 us                                                | 6.49 us: 1.03x faster                                  |
| mako                    | 10.1 ms                                                | 9.83 ms: 1.03x faster                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| sqlite_synth            | 2.52 us                                                | 2.46 us: 1.02x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| raytrace                | 297 ms                                                 | 291 ms: 1.02x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.38 ms: 1.02x faster                                  |
| spectral_norm           | 100 ms                                                 | 98.4 ms: 1.02x faster                                  |
| chaos                   | 69.2 ms                                                | 68.2 ms: 1.01x faster                                  |
| sympy_expand            | 475 ms                                                 | 468 ms: 1.01x faster                                   |
| flaskblogging           | 7.12 ms                                                | 7.02 ms: 1.01x faster                                  |
| logging_silent          | 101 ns                                                 | 99.8 ns: 1.01x faster                                  |
| json_loads              | 26.5 us                                                | 26.2 us: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                  |
| logging_simple          | 6.03 us                                                | 5.97 us: 1.01x faster                                  |
| json_dumps              | 12.6 ms                                                | 12.5 ms: 1.01x faster                                  |
| float                   | 77.2 ms                                                | 76.6 ms: 1.01x faster                                  |
| bench_thread_pool       | 819 us                                                 | 812 us: 1.01x faster                                   |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 36.8 us: 1.01x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.01x faster                                 |
| python_startup          | 8.52 ms                                                | 8.47 ms: 1.01x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 697 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.01 ms                                                | 5.97 ms: 1.01x faster                                  |
| 2to3                    | 259 ms                                                 | 257 ms: 1.01x faster                                   |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.01x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 53.3 ms: 1.00x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| coroutines              | 25.5 ms                                                | 25.6 ms: 1.00x slower                                  |
| genshi_text             | 21.6 ms                                                | 21.7 ms: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| generators              | 73.5 ms                                                | 74.1 ms: 1.01x slower                                  |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                   |
| fannkuch                | 388 ms                                                 | 392 ms: 1.01x slower                                   |
| pickle_list             | 4.11 us                                                | 4.16 us: 1.01x slower                                  |
| dask                    | 360 ms                                                 | 365 ms: 1.01x slower                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.2 ms: 1.02x slower                                  |
| deepcopy                | 342 us                                                 | 348 us: 1.02x slower                                   |
| thrift                  | 756 us                                                 | 770 us: 1.02x slower                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 141 ms: 1.02x slower                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.63 ms: 1.03x slower                                  |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                   |
| gc_traversal            | 4.02 ms                                                | 4.15 ms: 1.03x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.04 us: 1.03x slower                                  |
| mdp                     | 2.62 sec                                               | 2.77 sec: 1.06x slower                                 |
| unpack_sequence         | 43.1 ns                                                | 48.8 ns: 1.13x slower                                  |
| Geometric mean          | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (32): html5lib, pickle, async_tree_none, scimark_monte_carlo, json, genshi_xml, nqueens, pyflate, scimark_fft, djangocms, richards, pickle_pure_python, nbody, tornado_http, hexiom, create_gc_cycles, xml_etree_process, regex_compile, xml_etree_iterparse, bench_mp_pool, unpickle_pure_python, async_tree_memoization, dulwich_log, async_tree_io, telco, deltablue, mypy2, async_tree_cpu_io_mixed, chameleon, django_template, xml_etree_parse, pylint
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 98.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
