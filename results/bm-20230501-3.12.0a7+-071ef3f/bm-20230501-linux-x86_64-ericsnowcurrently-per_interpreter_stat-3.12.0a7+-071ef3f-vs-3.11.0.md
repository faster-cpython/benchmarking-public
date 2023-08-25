
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_stat
- machine: linux-x86_64
- commit hash: 071ef3f
- commit date: 2023-05-01
- overall geometric mean: 1.00x slower \*
- HPT reliability: 98.68%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 271 ms: 1.05x slower                                                              |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                            |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                             |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                              |
| float          | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.17x faster                                                             |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                             |
| regex_dna      | 204 ms                                                 | 209 ms: 1.03x slower                                                              |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                              |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                                             |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                                             |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                              |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                                             |
| unpickle             | 13.7 us                                                | 14.4 us: 1.06x slower                                                             |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.60 us: 1.12x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 60.4 ms: 1.12x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 85.8 ms: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.15 ms: 1.07x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 50.8 ms: 1.02x faster                                                             |
| genshi_text    | 21.6 ms                                                | 22.3 ms: 1.03x slower                                                             |
| mako           | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 513 ms: 1.80x faster                                                              |
| json_dumps              | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                             |
| mypy2                   | 420 ms                                                 | 352 ms: 1.19x faster                                                              |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.17x faster                                                             |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                             |
| nbody                   | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                             |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.47 ms: 1.06x faster                                                             |
| async_tree_none         | 526 ms                                                 | 499 ms: 1.06x faster                                                              |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                            |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                              |
| unpickle_pure_python    | 228 us                                                 | 218 us: 1.05x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                             |
| nqueens                 | 83.4 ms                                                | 80.0 ms: 1.04x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.12 ms: 1.04x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 153 ms: 1.03x faster                                                              |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 720 ms: 1.03x faster                                                              |
| async_tree_memoization  | 627 ms                                                 | 612 ms: 1.02x faster                                                              |
| json_loads              | 26.5 us                                                | 25.9 us: 1.02x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                             |
| logging_silent          | 101 ns                                                 | 99.0 ns: 1.02x faster                                                             |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 50.8 ms: 1.02x faster                                                             |
| fannkuch                | 388 ms                                                 | 381 ms: 1.02x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                            |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                            |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                                             |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                             |
| raytrace                | 297 ms                                                 | 302 ms: 1.02x slower                                                              |
| bench_thread_pool       | 819 us                                                 | 834 us: 1.02x slower                                                              |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                                              |
| scimark_sor             | 118 ms                                                 | 121 ms: 1.02x slower                                                              |
| regex_dna               | 204 ms                                                 | 209 ms: 1.03x slower                                                              |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                                              |
| genshi_text             | 21.6 ms                                                | 22.3 ms: 1.03x slower                                                             |
| pickle_pure_python      | 306 us                                                 | 316 us: 1.03x slower                                                              |
| deepcopy_memo           | 37.0 us                                                | 38.3 us: 1.03x slower                                                             |
| spectral_norm           | 100 ms                                                 | 104 ms: 1.04x slower                                                              |
| logging_simple          | 6.03 us                                                | 6.25 us: 1.04x slower                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.51 sec: 1.04x slower                                                            |
| docutils                | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                            |
| pickle_dict             | 31.1 us                                                | 32.4 us: 1.04x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.19 ms: 1.04x slower                                                             |
| regex_compile           | 138 ms                                                 | 144 ms: 1.04x slower                                                              |
| crypto_pyaes            | 74.7 ms                                                | 77.9 ms: 1.04x slower                                                             |
| logging_format          | 6.68 us                                                | 6.98 us: 1.04x slower                                                             |
| telco                   | 6.58 ms                                                | 6.88 ms: 1.04x slower                                                             |
| 2to3                    | 259 ms                                                 | 271 ms: 1.05x slower                                                              |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 55.7 ms: 1.05x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 113 ms: 1.05x slower                                                              |
| float                   | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 738 ms: 1.05x slower                                                              |
| thrift                  | 756 us                                                 | 797 us: 1.05x slower                                                              |
| unpickle                | 13.7 us                                                | 14.4 us: 1.06x slower                                                             |
| mako                    | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.67 us: 1.06x slower                                                             |
| tornado_http            | 96.3 ms                                                | 102 ms: 1.06x slower                                                              |
| meteor_contest          | 107 ms                                                 | 113 ms: 1.06x slower                                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.07x slower                                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 72.5 ms: 1.07x slower                                                             |
| deepcopy                | 342 us                                                 | 367 us: 1.07x slower                                                              |
| dulwich_log             | 63.7 ms                                                | 68.3 ms: 1.07x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.15 ms: 1.07x slower                                                             |
| pickle                  | 10.1 us                                                | 10.8 us: 1.07x slower                                                             |
| pyflate                 | 418 ms                                                 | 449 ms: 1.07x slower                                                              |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.3 ms: 1.08x slower                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.86 ms: 1.08x slower                                                             |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.24 us: 1.10x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.60 us: 1.12x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 60.4 ms: 1.12x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 85.8 ms: 1.13x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 50.6 ns: 1.18x slower                                                             |
| async_generators        | 368 ms                                                 | 451 ms: 1.22x slower                                                              |
| dask                    | 360 ms                                                 | 540 ms: 1.50x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (6): json, bench_mp_pool, xml_etree_iterparse, create_gc_cycles, chaos, html5lib
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 98.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
