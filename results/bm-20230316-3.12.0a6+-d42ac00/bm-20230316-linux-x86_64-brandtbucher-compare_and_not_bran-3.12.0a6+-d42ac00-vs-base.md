
# Results vs. base

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: d42ac00
- commit date: 2023-03-16
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                         |
| chameleon      | 6.47 ms                                                                | 6.52 ms: 1.01x slower                                                        |
| docutils       | 2.52 sec                                                               | 2.54 sec: 1.01x slower                                                       |
| html5lib       | 60.7 ms                                                                | 62.0 ms: 1.02x slower                                                        |
| tornado_http   | 91.0 ms                                                                | 91.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.8 ms                                                                | 87.7 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.62 ms                                                                | 3.45 ms: 1.05x faster                                                        |
| regex_v8       | 21.7 ms                                                                | 21.8 ms: 1.01x slower                                                        |
| regex_compile  | 133 ms                                                                 | 135 ms: 1.01x slower                                                         |
| regex_dna      | 200 ms                                                                 | 208 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list          | 4.28 us                                                                | 4.16 us: 1.03x faster                                                        |
| pickle               | 10.5 us                                                                | 10.3 us: 1.02x faster                                                        |
| unpickle_list        | 5.08 us                                                                | 5.00 us: 1.02x faster                                                        |
| xml_etree_generate   | 81.1 ms                                                                | 80.3 ms: 1.01x faster                                                        |
| xml_etree_process    | 56.1 ms                                                                | 55.7 ms: 1.01x faster                                                        |
| pickle_dict          | 31.0 us                                                                | 30.9 us: 1.00x faster                                                        |
| json_loads           | 24.0 us                                                                | 24.4 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 98.5 ms                                                                | 100 ms: 1.02x slower                                                         |
| pickle_pure_python   | 280 us                                                                 | 289 us: 1.03x slower                                                         |
| unpickle_pure_python | 197 us                                                                 | 203 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.93 ms                                                                | 8.91 ms: 1.00x faster                                                        |
| python_startup_no_site | 6.52 ms                                                                | 6.52 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                                | 9.95 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot            | 3.62 ms                                                                | 3.45 ms: 1.05x faster                                                        |
| unpack_sequence         | 44.2 ns                                                                | 42.3 ns: 1.05x faster                                                        |
| pickle_list             | 4.28 us                                                                | 4.16 us: 1.03x faster                                                        |
| spectral_norm           | 92.3 ms                                                                | 90.0 ms: 1.03x faster                                                        |
| pickle                  | 10.5 us                                                                | 10.3 us: 1.02x faster                                                        |
| unpickle_list           | 5.08 us                                                                | 5.00 us: 1.02x faster                                                        |
| crypto_pyaes            | 75.1 ms                                                                | 73.9 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 104 ms                                                                 | 103 ms: 1.01x faster                                                         |
| nbody                   | 88.8 ms                                                                | 87.7 ms: 1.01x faster                                                        |
| xml_etree_generate      | 81.1 ms                                                                | 80.3 ms: 1.01x faster                                                        |
| comprehensions          | 24.1 us                                                                | 23.8 us: 1.01x faster                                                        |
| xml_etree_process       | 56.1 ms                                                                | 55.7 ms: 1.01x faster                                                        |
| coroutines              | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                        |
| mako                    | 10.0 ms                                                                | 9.95 ms: 1.01x faster                                                        |
| generators              | 29.5 ms                                                                | 29.4 ms: 1.01x faster                                                        |
| pathlib                 | 17.8 ms                                                                | 17.7 ms: 1.00x faster                                                        |
| python_startup          | 8.93 ms                                                                | 8.91 ms: 1.00x faster                                                        |
| sqlglot_optimize        | 51.0 ms                                                                | 50.9 ms: 1.00x faster                                                        |
| pickle_dict             | 31.0 us                                                                | 30.9 us: 1.00x faster                                                        |
| python_startup_no_site  | 6.52 ms                                                                | 6.52 ms: 1.00x faster                                                        |
| gc_traversal            | 3.67 ms                                                                | 3.66 ms: 1.00x faster                                                        |
| regex_v8                | 21.7 ms                                                                | 21.8 ms: 1.01x slower                                                        |
| docutils                | 2.52 sec                                                               | 2.54 sec: 1.01x slower                                                       |
| 2to3                    | 250 ms                                                                 | 252 ms: 1.01x slower                                                         |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                         |
| async_generators        | 410 ms                                                                 | 414 ms: 1.01x slower                                                         |
| chameleon               | 6.47 ms                                                                | 6.52 ms: 1.01x slower                                                        |
| tornado_http            | 91.0 ms                                                                | 91.9 ms: 1.01x slower                                                        |
| deepcopy                | 324 us                                                                 | 327 us: 1.01x slower                                                         |
| sqlite_synth            | 2.62 us                                                                | 2.65 us: 1.01x slower                                                        |
| nqueens                 | 79.9 ms                                                                | 80.9 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                                | 1.73 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 682 ms                                                                 | 691 ms: 1.01x slower                                                         |
| regex_compile           | 133 ms                                                                 | 135 ms: 1.01x slower                                                         |
| dulwich_log             | 62.9 ms                                                                | 63.8 ms: 1.01x slower                                                        |
| thrift                  | 769 us                                                                 | 780 us: 1.01x slower                                                         |
| json_loads              | 24.0 us                                                                | 24.4 us: 1.02x slower                                                        |
| xml_etree_iterparse     | 98.5 ms                                                                | 100 ms: 1.02x slower                                                         |
| logging_format          | 6.22 us                                                                | 6.32 us: 1.02x slower                                                        |
| scimark_fft             | 306 ms                                                                 | 311 ms: 1.02x slower                                                         |
| mdp                     | 2.43 sec                                                               | 2.47 sec: 1.02x slower                                                       |
| logging_simple          | 5.62 us                                                                | 5.73 us: 1.02x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                                | 1.43 ms: 1.02x slower                                                        |
| logging_silent          | 93.4 ns                                                                | 95.2 ns: 1.02x slower                                                        |
| deltablue               | 3.15 ms                                                                | 3.21 ms: 1.02x slower                                                        |
| dask                    | 500 ms                                                                 | 510 ms: 1.02x slower                                                         |
| html5lib                | 60.7 ms                                                                | 62.0 ms: 1.02x slower                                                        |
| scimark_monte_carlo     | 66.0 ms                                                                | 67.5 ms: 1.02x slower                                                        |
| richards                | 42.0 ms                                                                | 43.0 ms: 1.02x slower                                                        |
| scimark_sor             | 106 ms                                                                 | 109 ms: 1.03x slower                                                         |
| deepcopy_memo           | 33.1 us                                                                | 34.0 us: 1.03x slower                                                        |
| coverage                | 94.2 ms                                                                | 97.2 ms: 1.03x slower                                                        |
| pickle_pure_python      | 280 us                                                                 | 289 us: 1.03x slower                                                         |
| unpickle_pure_python    | 197 us                                                                 | 203 us: 1.03x slower                                                         |
| pyflate                 | 412 ms                                                                 | 425 ms: 1.03x slower                                                         |
| raytrace                | 278 ms                                                                 | 289 ms: 1.04x slower                                                         |
| fannkuch                | 367 ms                                                                 | 382 ms: 1.04x slower                                                         |
| chaos                   | 66.0 ms                                                                | 68.7 ms: 1.04x slower                                                        |
| regex_dna               | 200 ms                                                                 | 208 ms: 1.04x slower                                                         |
| go                      | 132 ms                                                                 | 139 ms: 1.05x slower                                                         |
| async_tree_memoization  | 614 ms                                                                 | 648 ms: 1.05x slower                                                         |
| scimark_sparse_mat_mult | 4.17 ms                                                                | 4.41 ms: 1.06x slower                                                        |
| pycparser               | 1.09 sec                                                               | 1.17 sec: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (31): djangocms, async_tree_none, async_tree_cpu_io_mixed, django_template, sqlalchemy_imperative, asyncio_tcp, xml_etree_parse, sympy_str, create_gc_cycles, sympy_sum, pidigits, sympy_integrate, bench_mp_pool, sympy_expand, float, aiohttp, deepcopy_reduce, bench_thread_pool, json_dumps, gunicorn, mypy2, hexiom, sqlalchemy_declarative, scimark_lu, genshi_xml, pprint_pformat, json, genshi_text, async_tree_io, telco, unpickle
