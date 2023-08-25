
# Results vs. 3.11.0

- fork: python
- ref: da1980afcb8820ffaa05
- machine: linux-x86_64
- commit hash: da1980a
- commit date: 2023-05-03
- overall geometric mean: 1.01x slower \*
- HPT reliability: 96.52%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 271 ms: 1.05x slower                                                   |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                 |
| tornado_http   | 96.3 ms                                                | 99.9 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.18x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.0 ms: 1.25x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 220 us: 1.04x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                   |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                   |
| unpickle_list        | 4.91 us                                                | 5.10 us: 1.04x slower                                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| unpickle             | 13.7 us                                                | 14.8 us: 1.09x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.58 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 32.3 ms: 2.27x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                                   |
| json_dumps              | 12.6 ms                                                | 10.0 ms: 1.25x faster                                                  |
| mypy2                   | 420 ms                                                 | 352 ms: 1.19x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.18x faster                                                  |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.64 ms: 1.10x faster                                                  |
| nbody                   | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                  |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                 |
| async_tree_none         | 526 ms                                                 | 500 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 220 us: 1.04x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 153 ms: 1.04x faster                                                   |
| json_loads              | 26.5 us                                                | 25.7 us: 1.03x faster                                                  |
| async_tree_memoization  | 627 ms                                                 | 612 ms: 1.03x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                 |
| richards                | 45.7 ms                                                | 44.7 ms: 1.02x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.23 ms: 1.02x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 724 ms: 1.02x faster                                                   |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                   |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.64 ms: 1.01x faster                                                  |
| nqueens                 | 83.4 ms                                                | 82.8 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                 |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                  |
| chaos                   | 69.2 ms                                                | 69.9 ms: 1.01x slower                                                  |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                  |
| bench_thread_pool       | 819 us                                                 | 836 us: 1.02x slower                                                   |
| pickle_dict             | 31.1 us                                                | 31.8 us: 1.02x slower                                                  |
| logging_silent          | 101 ns                                                 | 104 ns: 1.03x slower                                                   |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                 |
| telco                   | 6.58 ms                                                | 6.78 ms: 1.03x slower                                                  |
| pickle_pure_python      | 306 us                                                 | 316 us: 1.03x slower                                                   |
| raytrace                | 297 ms                                                 | 306 ms: 1.03x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.2 us: 1.03x slower                                                  |
| docutils                | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                 |
| tornado_http            | 96.3 ms                                                | 99.9 ms: 1.04x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.10 us: 1.04x slower                                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 55.5 ms: 1.04x slower                                                  |
| 2to3                    | 259 ms                                                 | 271 ms: 1.05x slower                                                   |
| pprint_safe_repr        | 701 ms                                                 | 734 ms: 1.05x slower                                                   |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                                   |
| deepcopy_memo           | 37.0 us                                                | 38.9 us: 1.05x slower                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.73 ms: 1.05x slower                                                  |
| logging_simple          | 6.03 us                                                | 6.35 us: 1.05x slower                                                  |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                                   |
| logging_format          | 6.68 us                                                | 7.06 us: 1.06x slower                                                  |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.06x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.06x slower                                                   |
| float                   | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.0 ms: 1.06x slower                                                  |
| dulwich_log             | 63.7 ms                                                | 67.8 ms: 1.06x slower                                                  |
| crypto_pyaes            | 74.7 ms                                                | 79.6 ms: 1.07x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                                  |
| scimark_sor             | 118 ms                                                 | 127 ms: 1.07x slower                                                   |
| python_startup          | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                  |
| scimark_fft             | 328 ms                                                 | 353 ms: 1.07x slower                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 73.3 ms: 1.08x slower                                                  |
| mako                    | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                  |
| deepcopy                | 342 us                                                 | 370 us: 1.08x slower                                                   |
| unpickle                | 13.7 us                                                | 14.8 us: 1.09x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                  |
| spectral_norm           | 100 ms                                                 | 109 ms: 1.09x slower                                                   |
| pyflate                 | 418 ms                                                 | 456 ms: 1.09x slower                                                   |
| meteor_contest          | 107 ms                                                 | 118 ms: 1.10x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.58 us: 1.11x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.28 us: 1.12x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 49.9 ns: 1.16x slower                                                  |
| async_generators        | 368 ms                                                 | 453 ms: 1.23x slower                                                   |
| dask                    | 360 ms                                                 | 542 ms: 1.51x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): json, bench_mp_pool, regex_dna
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 96.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
