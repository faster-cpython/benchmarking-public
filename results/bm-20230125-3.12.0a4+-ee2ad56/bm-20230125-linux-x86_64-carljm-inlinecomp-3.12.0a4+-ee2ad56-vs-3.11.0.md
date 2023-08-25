
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp
- machine: linux-x86_64
- commit hash: ee2ad56
- commit date: 2023-01-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                         |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                        |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                       |
| html5lib       | 64.5 ms                                                | 60.1 ms: 1.07x faster                                        |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                        |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                         |
| nbody          | 93.1 ms                                                | 93.9 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                        |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                         |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.04x faster                                        |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.57 ms: 1.32x faster                                        |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                         |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                         |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                         |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                        |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 78.2 ms: 1.03x slower                                        |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                        |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                        |
| pickle_list          | 4.11 us                                                | 4.29 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.89 ms: 1.04x slower                                        |
| python_startup_no_site | 6.01 ms                                                | 6.44 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.11x faster                                        |
| mako            | 10.1 ms                                                | 9.70 ms: 1.04x faster                                        |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                        |
| django_template | 32.6 ms                                                | 32.8 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 492 ms: 1.87x faster                                         |
| json_dumps              | 12.6 ms                                                | 9.57 ms: 1.32x faster                                        |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                        |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                        |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                         |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.99 ms: 1.13x faster                                        |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                         |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                        |
| gc_traversal            | 4.02 ms                                                | 3.64 ms: 1.11x faster                                        |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.11x faster                                        |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.10x faster                                         |
| logging_silent          | 101 ns                                                 | 91.7 ns: 1.10x faster                                        |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                        |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.09x faster                                         |
| nqueens                 | 83.4 ms                                                | 76.9 ms: 1.08x faster                                        |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                       |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                         |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                         |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                         |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                        |
| richards                | 45.7 ms                                                | 42.6 ms: 1.07x faster                                        |
| html5lib                | 64.5 ms                                                | 60.1 ms: 1.07x faster                                        |
| chaos                   | 69.2 ms                                                | 64.6 ms: 1.07x faster                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                         |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                        |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.07x faster                                        |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                        |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                         |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                        |
| sympy_expand            | 475 ms                                                 | 450 ms: 1.05x faster                                         |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 64.7 ms: 1.05x faster                                        |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                         |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                        |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                         |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                       |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                         |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                         |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                         |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                         |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                        |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                       |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                         |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                       |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                        |
| mako                    | 10.1 ms                                                | 9.70 ms: 1.04x faster                                        |
| spectral_norm           | 100 ms                                                 | 96.2 ms: 1.04x faster                                        |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                         |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                        |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                         |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.04x faster                                        |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                        |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                        |
| pprint_safe_repr        | 701 ms                                                 | 684 ms: 1.03x faster                                         |
| crypto_pyaes            | 74.7 ms                                                | 72.9 ms: 1.02x faster                                        |
| dulwich_log             | 63.7 ms                                                | 62.2 ms: 1.02x faster                                        |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                         |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                        |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                        |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                        |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                        |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                         |
| thrift                  | 756 us                                                 | 748 us: 1.01x faster                                         |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                         |
| coroutines              | 25.5 ms                                                | 25.6 ms: 1.00x slower                                        |
| django_template         | 32.6 ms                                                | 32.8 ms: 1.01x slower                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                        |
| nbody                   | 93.1 ms                                                | 93.9 ms: 1.01x slower                                        |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 754 ms: 1.02x slower                                         |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                         |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                        |
| xml_etree_generate      | 76.2 ms                                                | 78.2 ms: 1.03x slower                                        |
| unpickle_list           | 4.91 us                                                | 5.05 us: 1.03x slower                                        |
| unpack_sequence         | 43.1 ns                                                | 44.4 ns: 1.03x slower                                        |
| generators              | 73.5 ms                                                | 75.9 ms: 1.03x slower                                        |
| pickle_dict             | 31.1 us                                                | 32.4 us: 1.04x slower                                        |
| python_startup          | 8.52 ms                                                | 8.89 ms: 1.04x slower                                        |
| pickle_list             | 4.11 us                                                | 4.29 us: 1.04x slower                                        |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.44 ms: 1.07x slower                                        |
| dask                    | 360 ms                                                 | 500 ms: 1.39x slower                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (4): djangocms, xml_etree_process, sqlglot_transpile, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230125-3.12.0a4+-ee2ad56/bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
