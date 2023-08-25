
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.00x faster \*
- HPT reliability: 92.14%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                   |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.9 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.0 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 81.2 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.94 ms: 1.27x faster                                  |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                   |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.85 us: 1.01x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.09x slower                                  |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.3 ms: 1.12x slower                                  |
| pickle_list          | 4.11 us                                                | 4.74 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 11.0 ms: 1.09x slower                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.3 ms: 2.35x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 512 ms: 1.80x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.94 ms: 1.27x faster                                  |
| mypy2                   | 420 ms                                                 | 351 ms: 1.20x faster                                   |
| coroutines              | 25.5 ms                                                | 22.1 ms: 1.15x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.68 ms: 1.09x faster                                  |
| richards                | 45.7 ms                                                | 43.0 ms: 1.06x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.32 ms: 1.06x faster                                  |
| nbody                   | 93.1 ms                                                | 88.0 ms: 1.06x faster                                  |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.06x faster                                 |
| async_tree_none         | 526 ms                                                 | 498 ms: 1.06x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 216 us: 1.06x faster                                   |
| deltablue               | 3.67 ms                                                | 3.51 ms: 1.05x faster                                  |
| json_loads              | 26.5 us                                                | 25.4 us: 1.04x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.64 ms: 1.04x faster                                  |
| nqueens                 | 83.4 ms                                                | 80.2 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.80 ms: 1.03x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.22 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 721 ms: 1.02x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| async_tree_memoization  | 627 ms                                                 | 613 ms: 1.02x faster                                   |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| fannkuch                | 388 ms                                                 | 380 ms: 1.02x faster                                   |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                 |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| logging_silent          | 101 ns                                                 | 99.3 ns: 1.02x faster                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| mdp                     | 2.62 sec                                               | 2.58 sec: 1.02x faster                                 |
| unpickle_list           | 4.91 us                                                | 4.85 us: 1.01x faster                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| chaos                   | 69.2 ms                                                | 68.9 ms: 1.00x faster                                  |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| bench_thread_pool       | 819 us                                                 | 829 us: 1.01x slower                                   |
| raytrace                | 297 ms                                                 | 301 ms: 1.02x slower                                   |
| pickle_pure_python      | 306 us                                                 | 311 us: 1.02x slower                                   |
| deepcopy_memo           | 37.0 us                                                | 37.8 us: 1.02x slower                                  |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                   |
| pprint_pformat          | 1.46 sec                                               | 1.49 sec: 1.02x slower                                 |
| sqlglot_optimize        | 53.1 ms                                                | 54.7 ms: 1.03x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                   |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                   |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.03x slower                                  |
| docutils                | 2.63 sec                                               | 2.72 sec: 1.04x slower                                 |
| pprint_safe_repr        | 701 ms                                                 | 728 ms: 1.04x slower                                   |
| tornado_http            | 96.3 ms                                                | 99.9 ms: 1.04x slower                                  |
| 2to3                    | 259 ms                                                 | 269 ms: 1.04x slower                                   |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                  |
| telco                   | 6.58 ms                                                | 6.88 ms: 1.05x slower                                  |
| logging_simple          | 6.03 us                                                | 6.31 us: 1.05x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 45.1 ns: 1.05x slower                                  |
| logging_format          | 6.68 us                                                | 7.00 us: 1.05x slower                                  |
| deepcopy                | 342 us                                                 | 358 us: 1.05x slower                                   |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                   |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| float                   | 77.2 ms                                                | 81.2 ms: 1.05x slower                                  |
| pyflate                 | 418 ms                                                 | 441 ms: 1.05x slower                                   |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                   |
| dulwich_log             | 63.7 ms                                                | 67.7 ms: 1.06x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.14 us: 1.07x slower                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 72.7 ms: 1.07x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 80.2 ms: 1.07x slower                                  |
| python_startup          | 8.52 ms                                                | 9.17 ms: 1.08x slower                                  |
| spectral_norm           | 100 ms                                                 | 108 ms: 1.08x slower                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.3 ms: 1.08x slower                                  |
| scimark_fft             | 328 ms                                                 | 358 ms: 1.09x slower                                   |
| mako                    | 10.1 ms                                                | 11.0 ms: 1.09x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.91 ms: 1.09x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.76 us: 1.09x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 59.0 ms: 1.09x slower                                  |
| unpickle                | 13.7 us                                                | 15.1 us: 1.11x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.69 ms: 1.11x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 85.3 ms: 1.12x slower                                  |
| pickle_list             | 4.11 us                                                | 4.74 us: 1.15x slower                                  |
| async_generators        | 368 ms                                                 | 451 ms: 1.22x slower                                   |
| dask                    | 360 ms                                                 | 537 ms: 1.49x slower                                   |
| Geometric mean          | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 92.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
