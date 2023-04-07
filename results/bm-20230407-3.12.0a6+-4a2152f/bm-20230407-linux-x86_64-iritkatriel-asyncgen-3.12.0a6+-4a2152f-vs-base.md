
# Results vs. base

- fork: iritkatriel
- ref: asyncgen
- machine: linux-x86_64
- commit hash: 4a2152f
- commit date: 2023-04-07
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                            |
| docutils       | 2.54 sec                                                               | 2.55 sec: 1.01x slower                                          |
| tornado_http   | 91.8 ms                                                                | 90.9 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x faster                                            |
| nbody          | 86.7 ms                                                                | 87.4 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.64 ms                                                                | 3.74 ms: 1.03x slower                                           |
| regex_v8       | 21.8 ms                                                                | 22.4 ms: 1.03x slower                                           |
| regex_dna      | 202 ms                                                                 | 213 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_iterparse  | 102 ms                                                                 | 99.4 ms: 1.02x faster                                           |
| xml_etree_process    | 56.1 ms                                                                | 55.0 ms: 1.02x faster                                           |
| unpickle_pure_python | 201 us                                                                 | 198 us: 1.01x faster                                            |
| xml_etree_generate   | 81.3 ms                                                                | 80.6 ms: 1.01x faster                                           |
| pickle_pure_python   | 289 us                                                                 | 287 us: 1.01x faster                                            |
| pickle               | 10.3 us                                                                | 10.4 us: 1.01x slower                                           |
| pickle_dict          | 31.6 us                                                                | 32.2 us: 1.02x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (6): json_loads, json_dumps, unpickle_list, xml_etree_parse, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 8.83 ms                                                                | 8.84 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 34.0 ms                                                                | 33.0 ms: 1.03x faster                                           |
| mako            | 10.0 ms                                                                | 9.97 ms: 1.00x faster                                           |
| genshi_text     | 21.5 ms                                                                | 21.6 ms: 1.01x slower                                           |
| genshi_xml      | 47.0 ms                                                                | 47.8 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization  | 658 ms                                                                 | 637 ms: 1.03x faster                                            |
| deepcopy_memo           | 35.0 us                                                                | 34.0 us: 1.03x faster                                           |
| deepcopy_reduce         | 2.98 us                                                                | 2.90 us: 1.03x faster                                           |
| deepcopy                | 331 us                                                                 | 322 us: 1.03x faster                                            |
| django_template         | 34.0 ms                                                                | 33.0 ms: 1.03x faster                                           |
| coverage                | 98.0 ms                                                                | 95.4 ms: 1.03x faster                                           |
| coroutines              | 23.9 ms                                                                | 23.3 ms: 1.03x faster                                           |
| async_generators        | 416 ms                                                                 | 407 ms: 1.02x faster                                            |
| xml_etree_iterparse     | 102 ms                                                                 | 99.4 ms: 1.02x faster                                           |
| chaos                   | 67.7 ms                                                                | 66.3 ms: 1.02x faster                                           |
| xml_etree_process       | 56.1 ms                                                                | 55.0 ms: 1.02x faster                                           |
| scimark_sor             | 113 ms                                                                 | 111 ms: 1.02x faster                                            |
| logging_silent          | 96.1 ns                                                                | 94.5 ns: 1.02x faster                                           |
| raytrace                | 284 ms                                                                 | 280 ms: 1.02x faster                                            |
| deltablue               | 3.24 ms                                                                | 3.19 ms: 1.01x faster                                           |
| unpack_sequence         | 43.2 ns                                                                | 42.7 ns: 1.01x faster                                           |
| unpickle_pure_python    | 201 us                                                                 | 198 us: 1.01x faster                                            |
| pprint_safe_repr        | 695 ms                                                                 | 687 ms: 1.01x faster                                            |
| scimark_lu              | 110 ms                                                                 | 108 ms: 1.01x faster                                            |
| dulwich_log             | 63.7 ms                                                                | 63.0 ms: 1.01x faster                                           |
| pprint_pformat          | 1.43 sec                                                               | 1.41 sec: 1.01x faster                                          |
| xml_etree_generate      | 81.3 ms                                                                | 80.6 ms: 1.01x faster                                           |
| logging_simple          | 5.76 us                                                                | 5.70 us: 1.01x faster                                           |
| pickle_pure_python      | 289 us                                                                 | 287 us: 1.01x faster                                            |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                            |
| logging_format          | 6.31 us                                                                | 6.25 us: 1.01x faster                                           |
| tornado_http            | 91.8 ms                                                                | 90.9 ms: 1.01x faster                                           |
| meteor_contest          | 103 ms                                                                 | 103 ms: 1.01x faster                                            |
| telco                   | 6.51 ms                                                                | 6.46 ms: 1.01x faster                                           |
| sqlglot_optimize        | 51.6 ms                                                                | 51.2 ms: 1.01x faster                                           |
| sqlglot_transpile       | 1.73 ms                                                                | 1.72 ms: 1.01x faster                                           |
| sqlite_synth            | 2.63 us                                                                | 2.61 us: 1.01x faster                                           |
| mako                    | 10.0 ms                                                                | 9.97 ms: 1.00x faster                                           |
| sympy_str               | 285 ms                                                                 | 284 ms: 1.00x faster                                            |
| sqlglot_parse           | 1.44 ms                                                                | 1.43 ms: 1.00x faster                                           |
| sympy_expand            | 461 ms                                                                 | 460 ms: 1.00x faster                                            |
| sympy_integrate         | 20.4 ms                                                                | 20.4 ms: 1.00x faster                                           |
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                            |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x faster                                            |
| python_startup          | 8.83 ms                                                                | 8.84 ms: 1.00x slower                                           |
| create_gc_cycles        | 1.46 ms                                                                | 1.47 ms: 1.00x slower                                           |
| asyncio_tcp             | 506 ms                                                                 | 507 ms: 1.00x slower                                            |
| generators              | 29.5 ms                                                                | 29.6 ms: 1.00x slower                                           |
| docutils                | 2.54 sec                                                               | 2.55 sec: 1.01x slower                                          |
| genshi_text             | 21.5 ms                                                                | 21.6 ms: 1.01x slower                                           |
| nbody                   | 86.7 ms                                                                | 87.4 ms: 1.01x slower                                           |
| pyflate                 | 417 ms                                                                 | 421 ms: 1.01x slower                                            |
| spectral_norm           | 95.2 ms                                                                | 96.2 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult | 4.27 ms                                                                | 4.33 ms: 1.01x slower                                           |
| pickle                  | 10.3 us                                                                | 10.4 us: 1.01x slower                                           |
| pathlib                 | 17.8 ms                                                                | 18.1 ms: 1.02x slower                                           |
| richards                | 43.6 ms                                                                | 44.3 ms: 1.02x slower                                           |
| pickle_dict             | 31.6 us                                                                | 32.2 us: 1.02x slower                                           |
| genshi_xml              | 47.0 ms                                                                | 47.8 ms: 1.02x slower                                           |
| regex_effbot            | 3.64 ms                                                                | 3.74 ms: 1.03x slower                                           |
| scimark_monte_carlo     | 67.1 ms                                                                | 68.9 ms: 1.03x slower                                           |
| pycparser               | 1.11 sec                                                               | 1.14 sec: 1.03x slower                                          |
| regex_v8                | 21.8 ms                                                                | 22.4 ms: 1.03x slower                                           |
| fannkuch                | 376 ms                                                                 | 394 ms: 1.05x slower                                            |
| regex_dna               | 202 ms                                                                 | 213 ms: 1.05x slower                                            |
| gc_traversal            | 4.07 ms                                                                | 4.32 ms: 1.06x slower                                           |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (33): sqlalchemy_imperative, dask, json, float, async_tree_cpu_io_mixed, json_loads, async_tree_none, json_dumps, async_tree_io, regex_compile, go, thrift, unpickle_list, xml_etree_parse, djangocms, chameleon, mypy2, gunicorn, aiohttp, mdp, pickle_list, python_startup_no_site, sympy_sum, bench_mp_pool, bench_thread_pool, hexiom, comprehensions, scimark_fft, unpickle, nqueens, crypto_pyaes, sqlalchemy_declarative, html5lib
