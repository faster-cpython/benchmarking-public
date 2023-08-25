
# Results vs. 3.11.0

- fork: python
- ref: 92d8bfffbf377e91d8b9
- machine: linux-x86_64
- commit hash: 92d8bff
- commit date: 2023-05-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.05%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 270 ms: 1.04x slower                                                   |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                 |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nbody          | 93.1 ms                                                | 90.6 ms: 1.03x faster                                                  |
| float          | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.0 ms: 1.00x faster                                                  |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                   |
| regex_compile  | 138 ms                                                 | 146 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.87 ms: 1.27x faster                                                  |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 220 us: 1.04x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.02x faster                                                   |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                   |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.54 us: 1.10x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.15 ms: 1.07x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.9 ms: 2.37x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.87 ms: 1.27x faster                                                  |
| mypy2                   | 420 ms                                                 | 353 ms: 1.19x faster                                                   |
| coroutines              | 25.5 ms                                                | 22.7 ms: 1.12x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                  |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.06x faster                                                 |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.05x faster                                                  |
| nqueens                 | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                  |
| json_loads              | 26.5 us                                                | 25.3 us: 1.05x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                                  |
| async_tree_none         | 526 ms                                                 | 505 ms: 1.04x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 220 us: 1.04x faster                                                   |
| json                    | 4.94 ms                                                | 4.77 ms: 1.04x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.57 ms: 1.03x faster                                                  |
| nbody                   | 93.1 ms                                                | 90.6 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                   |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.66 ms: 1.03x faster                                                  |
| async_tree_memoization  | 627 ms                                                 | 613 ms: 1.02x faster                                                   |
| richards                | 45.7 ms                                                | 44.8 ms: 1.02x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 727 ms: 1.02x faster                                                   |
| chaos                   | 69.2 ms                                                | 68.2 ms: 1.01x faster                                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                | 22.0 ms: 1.00x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                  |
| logging_silent          | 101 ns                                                 | 102 ns: 1.01x slower                                                   |
| bench_thread_pool       | 819 us                                                 | 831 us: 1.01x slower                                                   |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                                  |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                   |
| deepcopy_memo           | 37.0 us                                                | 37.7 us: 1.02x slower                                                  |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                   |
| mdp                     | 2.62 sec                                               | 2.68 sec: 1.02x slower                                                 |
| telco                   | 6.58 ms                                                | 6.77 ms: 1.03x slower                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                 |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                   |
| pathlib                 | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                  |
| pickle_pure_python      | 306 us                                                 | 316 us: 1.03x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.2 us: 1.03x slower                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 55.1 ms: 1.04x slower                                                  |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                   |
| docutils                | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                 |
| 2to3                    | 259 ms                                                 | 270 ms: 1.04x slower                                                   |
| crypto_pyaes            | 74.7 ms                                                | 77.8 ms: 1.04x slower                                                  |
| sqlglot_normalize       | 108 ms                                                 | 112 ms: 1.04x slower                                                   |
| raytrace                | 297 ms                                                 | 310 ms: 1.04x slower                                                   |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| pprint_safe_repr        | 701 ms                                                 | 734 ms: 1.05x slower                                                   |
| float                   | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                  |
| logging_simple          | 6.03 us                                                | 6.35 us: 1.05x slower                                                  |
| logging_format          | 6.68 us                                                | 7.05 us: 1.05x slower                                                  |
| regex_compile           | 138 ms                                                 | 146 ms: 1.05x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.75 ms: 1.06x slower                                                  |
| pyflate                 | 418 ms                                                 | 442 ms: 1.06x slower                                                   |
| deepcopy                | 342 us                                                 | 362 us: 1.06x slower                                                   |
| mako                    | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |
| tornado_http            | 96.3 ms                                                | 103 ms: 1.07x slower                                                   |
| spectral_norm           | 100 ms                                                 | 107 ms: 1.07x slower                                                   |
| dulwich_log             | 63.7 ms                                                | 68.1 ms: 1.07x slower                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 72.9 ms: 1.07x slower                                                  |
| python_startup          | 8.52 ms                                                | 9.15 ms: 1.07x slower                                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.4 ms: 1.08x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.74 us: 1.09x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.37 ms: 1.09x slower                                                  |
| scimark_fft             | 328 ms                                                 | 358 ms: 1.09x slower                                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.21 us: 1.09x slower                                                  |
| unpickle                | 13.7 us                                                | 15.0 us: 1.10x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.54 us: 1.10x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                  |
| async_generators        | 368 ms                                                 | 448 ms: 1.21x slower                                                   |
| unpack_sequence         | 43.1 ns                                                | 58.6 ns: 1.36x slower                                                  |
| dask                    | 360 ms                                                 | 539 ms: 1.50x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.05% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
