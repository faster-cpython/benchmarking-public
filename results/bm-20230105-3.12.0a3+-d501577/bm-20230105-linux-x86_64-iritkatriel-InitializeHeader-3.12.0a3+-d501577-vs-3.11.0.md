
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| chameleon      | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                   |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.05x faster                                                  |
| html5lib       | 64.5 ms                                                | 59.9 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.9 ms: 1.07x faster                                                   |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                   |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                    |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                    |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                   |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                    |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                    |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                   |
| pickle_dict          | 31.1 us                                                | 29.8 us: 1.04x faster                                                   |
| pickle_list          | 4.11 us                                                | 4.00 us: 1.03x faster                                                   |
| pickle               | 10.1 us                                                | 9.96 us: 1.01x faster                                                   |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                   |
| xml_etree_generate   | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                   |
| genshi_text    | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                   |
| mako           | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.98 ms: 1.13x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                   |
| richards                | 45.7 ms                                                | 41.3 ms: 1.11x faster                                                   |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                   |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                    |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                                   |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                    |
| html5lib                | 64.5 ms                                                | 59.9 ms: 1.08x faster                                                   |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                   |
| float                   | 77.2 ms                                                | 71.9 ms: 1.07x faster                                                   |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                    |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                    |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                   |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                  |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                                   |
| bench_thread_pool       | 819 us                                                 | 777 us: 1.05x faster                                                    |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.05x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 64.6 ms: 1.05x faster                                                   |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                                   |
| hexiom                  | 6.37 ms                                                | 6.06 ms: 1.05x faster                                                   |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                   |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                    |
| raytrace                | 297 ms                                                 | 284 ms: 1.05x faster                                                    |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                    |
| spectral_norm           | 100 ms                                                 | 95.9 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                    |
| pickle_dict             | 31.1 us                                                | 29.8 us: 1.04x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 674 ms: 1.04x faster                                                    |
| mako                    | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                   |
| telco                   | 6.58 ms                                                | 6.36 ms: 1.04x faster                                                   |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                    |
| nqueens                 | 83.4 ms                                                | 80.8 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                   |
| pickle_list             | 4.11 us                                                | 4.00 us: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                   |
| chaos                   | 69.2 ms                                                | 67.5 ms: 1.02x faster                                                   |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                    |
| deepcopy                | 342 us                                                 | 334 us: 1.02x faster                                                    |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                    |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                                   |
| thrift                  | 756 us                                                 | 743 us: 1.02x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                                    |
| unpack_sequence         | 43.1 ns                                                | 42.5 ns: 1.01x faster                                                   |
| pickle                  | 10.1 us                                                | 9.96 us: 1.01x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                   |
| python_startup          | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                   |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.00x faster                                                   |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                    |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                                   |
| async_tree_memoization  | 627 ms                                                 | 638 ms: 1.02x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                  |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                    |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 758 ms: 1.03x slower                                                    |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                   |
| mdp                     | 2.62 sec                                               | 2.74 sec: 1.05x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (9): pathlib, xml_etree_process, sqlglot_parse, bench_mp_pool, async_tree_none, django_template, nbody, coverage, djangocms
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230105-3.12.0a3+-d501577/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
