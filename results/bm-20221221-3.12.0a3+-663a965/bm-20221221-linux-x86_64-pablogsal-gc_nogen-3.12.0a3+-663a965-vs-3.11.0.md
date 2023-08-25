
# Results vs. 3.11.0

- fork: pablogsal
- ref: gc_nogen
- machine: linux-x86_64
- commit hash: 663a965
- commit date: 2022-12-21
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 243 ms: 1.06x faster                                          |
| chameleon      | 6.47 ms                                                | 6.29 ms: 1.03x faster                                         |
| docutils       | 2.63 sec                                               | 2.13 sec: 1.23x faster                                        |
| html5lib       | 64.5 ms                                                | 57.4 ms: 1.12x faster                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 77.2 ms                                                | 61.8 ms: 1.25x faster                                         |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.35 ms: 1.19x faster                                         |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                          |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                         |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.30 ms: 1.35x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 123 ms: 1.29x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 80.8 ms: 1.29x faster                                         |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                          |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                         |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                          |
| xml_etree_process    | 53.9 ms                                                | 51.5 ms: 1.05x faster                                         |
| xml_etree_generate   | 76.2 ms                                                | 73.0 ms: 1.04x faster                                         |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                         |
| pickle_list          | 4.11 us                                                | 4.16 us: 1.01x slower                                         |
| unpickle_list        | 4.91 us                                                | 5.03 us: 1.02x slower                                         |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                         |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                  |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.06 ms: 1.06x faster                                         |
| python_startup_no_site | 6.01 ms                                                | 5.88 ms: 1.02x faster                                         |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.2 ms: 1.12x faster                                         |
| mako            | 10.1 ms                                                | 9.50 ms: 1.06x faster                                         |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.05x faster                                         |
| django_template | 32.6 ms                                                | 32.8 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                               | 537 ms: 2.41x faster                                          |
| async_tree_none         | 526 ms                                                 | 269 ms: 1.96x faster                                          |
| async_tree_memoization  | 627 ms                                                 | 324 ms: 1.93x faster                                          |
| async_tree_cpu_io_mixed | 739 ms                                                 | 474 ms: 1.56x faster                                          |
| json_dumps              | 12.6 ms                                                | 9.30 ms: 1.35x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 123 ms: 1.29x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 80.8 ms: 1.29x faster                                         |
| float                   | 77.2 ms                                                | 61.8 ms: 1.25x faster                                         |
| docutils                | 2.63 sec                                               | 2.13 sec: 1.23x faster                                        |
| pycparser               | 1.18 sec                                               | 983 ms: 1.20x faster                                          |
| regex_effbot            | 3.99 ms                                                | 3.35 ms: 1.19x faster                                         |
| deltablue               | 3.67 ms                                                | 3.11 ms: 1.18x faster                                         |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                          |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                          |
| html5lib                | 64.5 ms                                                | 57.4 ms: 1.12x faster                                         |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                         |
| genshi_xml              | 51.8 ms                                                | 46.2 ms: 1.12x faster                                         |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                         |
| richards                | 45.7 ms                                                | 41.1 ms: 1.11x faster                                         |
| logging_silent          | 101 ns                                                 | 91.2 ns: 1.11x faster                                         |
| async_generators        | 368 ms                                                 | 334 ms: 1.10x faster                                          |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                         |
| scimark_fft             | 328 ms                                                 | 302 ms: 1.09x faster                                          |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                          |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                         |
| spectral_norm           | 100 ms                                                 | 93.6 ms: 1.07x faster                                         |
| nqueens                 | 83.4 ms                                                | 78.2 ms: 1.07x faster                                         |
| 2to3                    | 259 ms                                                 | 243 ms: 1.06x faster                                          |
| mako                    | 10.1 ms                                                | 9.50 ms: 1.06x faster                                         |
| python_startup          | 8.52 ms                                                | 8.06 ms: 1.06x faster                                         |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                          |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                         |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.05x faster                                         |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                          |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                         |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                          |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                          |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.05x faster                                         |
| xml_etree_process       | 53.9 ms                                                | 51.5 ms: 1.05x faster                                         |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                         |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                          |
| xml_etree_generate      | 76.2 ms                                                | 73.0 ms: 1.04x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                        |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                          |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                         |
| sympy_str               | 290 ms                                                 | 279 ms: 1.04x faster                                          |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 65.7 ms: 1.04x faster                                         |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                          |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                         |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                          |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                         |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                          |
| chameleon               | 6.47 ms                                                | 6.29 ms: 1.03x faster                                         |
| sqlglot_parse           | 1.40 ms                                                | 1.36 ms: 1.03x faster                                         |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                         |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| chaos                   | 69.2 ms                                                | 67.6 ms: 1.02x faster                                         |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                          |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                          |
| python_startup_no_site  | 6.01 ms                                                | 5.88 ms: 1.02x faster                                         |
| regex_dna               | 204 ms                                                 | 201 ms: 1.02x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                          |
| thrift                  | 756 us                                                 | 747 us: 1.01x faster                                          |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                         |
| unpack_sequence         | 43.1 ns                                                | 42.8 ns: 1.01x faster                                         |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                          |
| django_template         | 32.6 ms                                                | 32.8 ms: 1.01x slower                                         |
| crypto_pyaes            | 74.7 ms                                                | 75.3 ms: 1.01x slower                                         |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                         |
| pickle_list             | 4.11 us                                                | 4.16 us: 1.01x slower                                         |
| unpickle_list           | 4.91 us                                                | 5.03 us: 1.02x slower                                         |
| coroutines              | 25.5 ms                                                | 26.1 ms: 1.03x slower                                         |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                          |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                         |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                         |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                        |
| generators              | 73.5 ms                                                | 78.4 ms: 1.07x slower                                         |
| Geometric mean          | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (4): unpickle, bench_mp_pool, nbody, deepcopy_reduce
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-663a965/bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
