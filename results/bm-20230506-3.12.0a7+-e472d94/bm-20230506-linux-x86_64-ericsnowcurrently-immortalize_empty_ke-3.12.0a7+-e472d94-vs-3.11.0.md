
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: immortalize_empty_ke
- machine: linux-x86_64
- commit hash: e472d94
- commit date: 2023-05-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 270 ms: 1.04x slower                                                              |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                            |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| float          | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.74 ms: 1.07x faster                                                             |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                             |
| regex_dna      | 204 ms                                                 | 211 ms: 1.04x slower                                                              |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.99 ms: 1.26x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                                              |
| json_loads           | 26.5 us                                                | 25.5 us: 1.04x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.02x faster                                                              |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                                             |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                                             |
| pickle_pure_python   | 306 us                                                 | 318 us: 1.04x slower                                                              |
| pickle               | 10.1 us                                                | 10.7 us: 1.07x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 59.9 ms: 1.11x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.58 us: 1.11x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 85.9 ms: 1.13x slower                                                             |
| unpickle             | 13.7 us                                                | 15.7 us: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.70 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.1 ms: 2.36x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 513 ms: 1.80x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.99 ms: 1.26x faster                                                             |
| mypy2                   | 420 ms                                                 | 354 ms: 1.19x faster                                                              |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.74 ms: 1.07x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 218 us: 1.05x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                             |
| async_tree_none         | 526 ms                                                 | 504 ms: 1.04x faster                                                              |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                                              |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                             |
| json_loads              | 26.5 us                                                | 25.5 us: 1.04x faster                                                             |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                                             |
| json                    | 4.94 ms                                                | 4.81 ms: 1.03x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.21 ms: 1.03x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.58 ms: 1.02x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.66 ms: 1.02x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                            |
| async_tree_memoization  | 627 ms                                                 | 615 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 725 ms: 1.02x faster                                                              |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                              |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.02x faster                                                              |
| gc_traversal            | 4.02 ms                                                | 3.97 ms: 1.01x faster                                                             |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                                             |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                             |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                                             |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                                             |
| spectral_norm           | 100 ms                                                 | 101 ms: 1.01x slower                                                              |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                              |
| bench_thread_pool       | 819 us                                                 | 834 us: 1.02x slower                                                              |
| deepcopy_memo           | 37.0 us                                                | 37.8 us: 1.02x slower                                                             |
| pycparser               | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                            |
| regex_v8                | 22.0 ms                                                | 22.8 ms: 1.03x slower                                                             |
| comprehensions          | 22.4 us                                                | 23.2 us: 1.03x slower                                                             |
| docutils                | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                            |
| regex_dna               | 204 ms                                                 | 211 ms: 1.04x slower                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 55.1 ms: 1.04x slower                                                             |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                              |
| pickle_pure_python      | 306 us                                                 | 318 us: 1.04x slower                                                              |
| 2to3                    | 259 ms                                                 | 270 ms: 1.04x slower                                                              |
| sqlglot_normalize       | 108 ms                                                 | 112 ms: 1.04x slower                                                              |
| raytrace                | 297 ms                                                 | 310 ms: 1.05x slower                                                              |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                                              |
| mako                    | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                             |
| logging_silent          | 101 ns                                                 | 106 ns: 1.05x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.53 sec: 1.05x slower                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.74 ms: 1.05x slower                                                             |
| deepcopy                | 342 us                                                 | 361 us: 1.06x slower                                                              |
| pathlib                 | 18.2 ms                                                | 19.3 ms: 1.06x slower                                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.9 ms: 1.06x slower                                                             |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.06x slower                                                              |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                                              |
| pyflate                 | 418 ms                                                 | 443 ms: 1.06x slower                                                              |
| pprint_safe_repr        | 701 ms                                                 | 744 ms: 1.06x slower                                                              |
| float                   | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                             |
| telco                   | 6.58 ms                                                | 7.00 ms: 1.06x slower                                                             |
| crypto_pyaes            | 74.7 ms                                                | 79.6 ms: 1.07x slower                                                             |
| pickle                  | 10.1 us                                                | 10.7 us: 1.07x slower                                                             |
| tornado_http            | 96.3 ms                                                | 103 ms: 1.07x slower                                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 73.0 ms: 1.07x slower                                                             |
| dulwich_log             | 63.7 ms                                                | 68.4 ms: 1.08x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.19 ms: 1.08x slower                                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.17 us: 1.08x slower                                                             |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                                              |
| logging_format          | 6.68 us                                                | 7.31 us: 1.09x slower                                                             |
| logging_simple          | 6.03 us                                                | 6.61 us: 1.10x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.78 us: 1.10x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 47.9 ns: 1.11x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 59.9 ms: 1.11x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.58 us: 1.11x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.70 ms: 1.12x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 85.9 ms: 1.13x slower                                                             |
| unpickle                | 13.7 us                                                | 15.7 us: 1.15x slower                                                             |
| async_generators        | 368 ms                                                 | 449 ms: 1.22x slower                                                              |
| dask                    | 360 ms                                                 | 538 ms: 1.50x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, nbody, bench_mp_pool
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.08% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
