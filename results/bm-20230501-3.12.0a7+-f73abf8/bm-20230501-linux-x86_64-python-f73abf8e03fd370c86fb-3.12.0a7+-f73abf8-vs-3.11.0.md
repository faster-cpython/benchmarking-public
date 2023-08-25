
# Results vs. 3.11.0

- fork: python
- ref: f73abf8e03fd370c86fb
- machine: linux-x86_64
- commit hash: f73abf8
- commit date: 2023-05-01
- overall geometric mean: 1.00x slower \*
- HPT reliability: 96.76%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.04x slower                                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| tornado_http   | 96.3 ms                                                | 98.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                  |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                   |
| float          | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                  |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.25x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 319 us: 1.04x slower                                                   |
| unpickle_list        | 4.91 us                                                | 5.19 us: 1.06x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.0 ms: 1.10x slower                                                  |
| unpickle             | 13.7 us                                                | 15.7 us: 1.15x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.79 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.06 ms: 1.06x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.65 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                  |
| genshi_text    | 21.6 ms                                                | 22.7 ms: 1.05x slower                                                  |
| mako           | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.0 ms: 2.37x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 511 ms: 1.80x faster                                                   |
| json_dumps              | 12.6 ms                                                | 10.1 ms: 1.25x faster                                                  |
| mypy2                   | 420 ms                                                 | 349 ms: 1.20x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                  |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                  |
| richards                | 45.7 ms                                                | 43.3 ms: 1.06x faster                                                  |
| async_tree_none         | 526 ms                                                 | 499 ms: 1.05x faster                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.05x faster                                                  |
| async_tree_io           | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                 |
| unpickle_pure_python    | 228 us                                                 | 217 us: 1.05x faster                                                   |
| nbody                   | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                  |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.54 ms: 1.04x faster                                                  |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                 |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                   |
| json_loads              | 26.5 us                                                | 25.8 us: 1.03x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.22 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 722 ms: 1.02x faster                                                   |
| gc_traversal            | 4.02 ms                                                | 3.94 ms: 1.02x faster                                                  |
| async_tree_memoization  | 627 ms                                                 | 614 ms: 1.02x faster                                                   |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                 |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                   |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                   |
| bench_thread_pool       | 819 us                                                 | 834 us: 1.02x slower                                                   |
| tornado_http            | 96.3 ms                                                | 98.5 ms: 1.02x slower                                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| spectral_norm           | 100 ms                                                 | 102 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 54.5 ms: 1.03x slower                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                 |
| telco                   | 6.58 ms                                                | 6.76 ms: 1.03x slower                                                  |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| docutils                | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| raytrace                | 297 ms                                                 | 306 ms: 1.03x slower                                                   |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                                   |
| 2to3                    | 259 ms                                                 | 268 ms: 1.04x slower                                                   |
| pickle_dict             | 31.1 us                                                | 32.3 us: 1.04x slower                                                  |
| scimark_lu              | 110 ms                                                 | 114 ms: 1.04x slower                                                   |
| logging_format          | 6.68 us                                                | 6.95 us: 1.04x slower                                                  |
| logging_simple          | 6.03 us                                                | 6.28 us: 1.04x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.7 ms: 1.04x slower                                                  |
| regex_compile           | 138 ms                                                 | 144 ms: 1.04x slower                                                   |
| pickle_pure_python      | 306 us                                                 | 319 us: 1.04x slower                                                   |
| pprint_safe_repr        | 701 ms                                                 | 733 ms: 1.04x slower                                                   |
| genshi_text             | 21.6 ms                                                | 22.7 ms: 1.05x slower                                                  |
| deepcopy_memo           | 37.0 us                                                | 39.0 us: 1.05x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.19 us: 1.06x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.06x slower                                                   |
| meteor_contest          | 107 ms                                                 | 113 ms: 1.06x slower                                                   |
| deepcopy                | 342 us                                                 | 363 us: 1.06x slower                                                   |
| float                   | 77.2 ms                                                | 82.0 ms: 1.06x slower                                                  |
| pyflate                 | 418 ms                                                 | 444 ms: 1.06x slower                                                   |
| python_startup          | 8.52 ms                                                | 9.06 ms: 1.06x slower                                                  |
| dulwich_log             | 63.7 ms                                                | 67.7 ms: 1.06x slower                                                  |
| crypto_pyaes            | 74.7 ms                                                | 79.5 ms: 1.06x slower                                                  |
| scimark_sor             | 118 ms                                                 | 126 ms: 1.07x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 73.0 ms: 1.07x slower                                                  |
| mako                    | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                  |
| thrift                  | 756 us                                                 | 811 us: 1.07x slower                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.83 ms: 1.07x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                  |
| scimark_fft             | 328 ms                                                 | 356 ms: 1.08x slower                                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.20 us: 1.09x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 84.0 ms: 1.10x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 47.5 ns: 1.10x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.65 ms: 1.11x slower                                                  |
| unpickle                | 13.7 us                                                | 15.7 us: 1.15x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.79 us: 1.17x slower                                                  |
| async_generators        | 368 ms                                                 | 442 ms: 1.20x slower                                                   |
| dask                    | 360 ms                                                 | 539 ms: 1.50x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (6): bench_mp_pool, logging_silent, create_gc_cycles, regex_v8, html5lib, json
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 96.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
