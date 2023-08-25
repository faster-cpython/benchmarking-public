
# Results vs. 3.11.0

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                      |
| chameleon      | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                     |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                    |
| html5lib       | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.8 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 94.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                     |
| regex_compile  | 138 ms                                                 | 130 ms: 1.07x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.48 ms: 1.33x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                      |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.2 us: 1.03x faster                                                     |
| pickle               | 10.1 us                                                | 9.89 us: 1.02x faster                                                     |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                     |
| genshi_text    | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                     |
| mako           | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.48 ms: 1.33x faster                                                     |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.02 ms: 1.12x faster                                                     |
| genshi_xml              | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                     |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                      |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                     |
| logging_silent          | 101 ns                                                 | 93.9 ns: 1.08x faster                                                     |
| html5lib                | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                     |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                      |
| regex_compile           | 138 ms                                                 | 130 ms: 1.07x faster                                                      |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                     |
| nqueens                 | 83.4 ms                                                | 78.4 ms: 1.06x faster                                                     |
| float                   | 77.2 ms                                                | 72.8 ms: 1.06x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                      |
| telco                   | 6.58 ms                                                | 6.28 ms: 1.05x faster                                                     |
| scimark_monte_carlo     | 68.1 ms                                                | 65.1 ms: 1.05x faster                                                     |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                                      |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                      |
| async_generators        | 368 ms                                                 | 356 ms: 1.04x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.04x faster                                                     |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                     |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                      |
| coverage                | 100 ms                                                 | 96.9 ms: 1.03x faster                                                     |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                      |
| coroutines              | 25.5 ms                                                | 24.7 ms: 1.03x faster                                                     |
| pickle_dict             | 31.1 us                                                | 30.2 us: 1.03x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                                     |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                     |
| scimark_fft             | 328 ms                                                 | 319 ms: 1.03x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                     |
| chaos                   | 69.2 ms                                                | 67.5 ms: 1.02x faster                                                     |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                    |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                      |
| deepcopy                | 342 us                                                 | 335 us: 1.02x faster                                                      |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                      |
| spectral_norm           | 100 ms                                                 | 98.0 ms: 1.02x faster                                                     |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                     |
| raytrace                | 297 ms                                                 | 291 ms: 1.02x faster                                                      |
| pickle                  | 10.1 us                                                | 9.89 us: 1.02x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                                      |
| logging_format          | 6.68 us                                                | 6.64 us: 1.01x faster                                                     |
| python_startup          | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                     |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.01x slower                                                     |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                     |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                                     |
| deltablue               | 3.67 ms                                                | 3.71 ms: 1.01x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                                     |
| crypto_pyaes            | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                     |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                    |
| thrift                  | 756 us                                                 | 765 us: 1.01x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                     |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| nbody                   | 93.1 ms                                                | 94.9 ms: 1.02x slower                                                     |
| regex_dna               | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                                     |
| async_tree_cpu_io_mixed | 739 ms                                                 | 758 ms: 1.03x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                                    |
| deepcopy_reduce         | 2.94 us                                                | 3.03 us: 1.03x slower                                                     |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                     |
| async_tree_memoization  | 627 ms                                                 | 670 ms: 1.07x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (12): meteor_contest, unpack_sequence, djangocms, logging_simple, django_template, bench_mp_pool, xml_etree_process, unpickle, sqlglot_transpile, richards, unpickle_list, async_tree_none
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: mypy


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
