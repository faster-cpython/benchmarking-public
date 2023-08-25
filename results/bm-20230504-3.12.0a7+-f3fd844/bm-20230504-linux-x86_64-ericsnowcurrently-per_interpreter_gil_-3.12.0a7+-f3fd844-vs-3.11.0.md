
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 272 ms: 1.05x slower                                                              |
| docutils       | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                            |
| tornado_http   | 96.3 ms                                                | 100 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.1 ms: 1.03x faster                                                             |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| float          | 77.2 ms                                                | 82.4 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                             |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x slower                                                              |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                             |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                             |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                              |
| unpickle_pure_python | 228 us                                                 | 222 us: 1.03x faster                                                              |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                             |
| unpickle_list        | 4.91 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 320 us: 1.04x slower                                                              |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 59.9 ms: 1.11x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.06x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.4 ms: 2.34x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                                              |
| json_dumps              | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                             |
| mypy2                   | 420 ms                                                 | 353 ms: 1.19x faster                                                              |
| coroutines              | 25.5 ms                                                | 23.1 ms: 1.10x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.06x faster                                                            |
| json_loads              | 26.5 us                                                | 25.1 us: 1.06x faster                                                             |
| async_tree_none         | 526 ms                                                 | 502 ms: 1.05x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.54 ms: 1.04x faster                                                             |
| richards                | 45.7 ms                                                | 44.1 ms: 1.04x faster                                                             |
| nbody                   | 93.1 ms                                                | 90.1 ms: 1.03x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                              |
| unpickle_pure_python    | 228 us                                                 | 222 us: 1.03x faster                                                              |
| json                    | 4.94 ms                                                | 4.82 ms: 1.03x faster                                                             |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                             |
| async_tree_memoization  | 627 ms                                                 | 616 ms: 1.02x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                            |
| async_tree_cpu_io_mixed | 739 ms                                                 | 726 ms: 1.02x faster                                                              |
| unpickle_list           | 4.91 us                                                | 4.83 us: 1.02x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                             |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                              |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                            |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x slower                                                              |
| gc_traversal            | 4.02 ms                                                | 4.04 ms: 1.00x slower                                                             |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                                              |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                             |
| hexiom                  | 6.37 ms                                                | 6.43 ms: 1.01x slower                                                             |
| chaos                   | 69.2 ms                                                | 70.3 ms: 1.02x slower                                                             |
| logging_silent          | 101 ns                                                 | 103 ns: 1.02x slower                                                              |
| nqueens                 | 83.4 ms                                                | 84.9 ms: 1.02x slower                                                             |
| pathlib                 | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                             |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                              |
| bench_thread_pool       | 819 us                                                 | 842 us: 1.03x slower                                                              |
| comprehensions          | 22.4 us                                                | 23.2 us: 1.03x slower                                                             |
| raytrace                | 297 ms                                                 | 307 ms: 1.04x slower                                                              |
| telco                   | 6.58 ms                                                | 6.84 ms: 1.04x slower                                                             |
| tornado_http            | 96.3 ms                                                | 100 ms: 1.04x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.52 sec: 1.04x slower                                                            |
| docutils                | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                            |
| pickle_pure_python      | 306 us                                                 | 320 us: 1.04x slower                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 55.5 ms: 1.05x slower                                                             |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                                              |
| 2to3                    | 259 ms                                                 | 272 ms: 1.05x slower                                                              |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                                              |
| crypto_pyaes            | 74.7 ms                                                | 78.7 ms: 1.05x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.06x slower                                                              |
| mako                    | 10.1 ms                                                | 10.6 ms: 1.06x slower                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.75 ms: 1.06x slower                                                             |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                                              |
| logging_format          | 6.68 us                                                | 7.08 us: 1.06x slower                                                             |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| deepcopy_memo           | 37.0 us                                                | 39.3 us: 1.06x slower                                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.0 ms: 1.06x slower                                                             |
| logging_simple          | 6.03 us                                                | 6.43 us: 1.07x slower                                                             |
| unpickle                | 13.7 us                                                | 14.6 us: 1.07x slower                                                             |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.07x slower                                                              |
| sqlite_synth            | 2.52 us                                                | 2.69 us: 1.07x slower                                                             |
| pyflate                 | 418 ms                                                 | 446 ms: 1.07x slower                                                              |
| float                   | 77.2 ms                                                | 82.4 ms: 1.07x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 749 ms: 1.07x slower                                                              |
| python_startup          | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 73.0 ms: 1.07x slower                                                             |
| spectral_norm           | 100 ms                                                 | 108 ms: 1.08x slower                                                              |
| dulwich_log             | 63.7 ms                                                | 68.5 ms: 1.08x slower                                                             |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                                              |
| deepcopy                | 342 us                                                 | 374 us: 1.09x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.26 us: 1.11x slower                                                             |
| meteor_contest          | 107 ms                                                 | 118 ms: 1.11x slower                                                              |
| pickle_list             | 4.11 us                                                | 4.57 us: 1.11x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 59.9 ms: 1.11x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 49.1 ns: 1.14x slower                                                             |
| async_generators        | 368 ms                                                 | 450 ms: 1.22x slower                                                              |
| dask                    | 360 ms                                                 | 543 ms: 1.51x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
