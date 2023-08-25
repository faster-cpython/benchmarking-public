
# Results vs. 3.11.0

- fork: python
- ref: 144aaa74bbd77aee822e
- machine: linux-x86_64
- commit hash: 144aaa7
- commit date: 2023-02-04
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.25 ms: 1.04x faster                                                  |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                  |
| tornado_http   | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                   |
| nbody          | 93.1 ms                                                | 97.5 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                  |
| regex_compile  | 138 ms                                                 | 126 ms: 1.09x faster                                                   |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                  |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.48 ms: 1.33x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                   |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                                   |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.01x slower                                                  |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.02x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                                  |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.93 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| genshi_text    | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                  |
| mako           | 10.1 ms                                                | 9.79 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 491 ms: 1.88x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.48 ms: 1.33x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.15x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 997 us: 1.10x faster                                                   |
| gc_traversal            | 4.02 ms                                                | 3.65 ms: 1.10x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                  |
| logging_silent          | 101 ns                                                 | 92.3 ns: 1.10x faster                                                  |
| regex_compile           | 138 ms                                                 | 126 ms: 1.09x faster                                                   |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                   |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                                   |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.15 ms: 1.08x faster                                                  |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                  |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                   |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                   |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| float                   | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                  |
| chaos                   | 69.2 ms                                                | 65.0 ms: 1.06x faster                                                  |
| nqueens                 | 83.4 ms                                                | 78.3 ms: 1.06x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                 |
| logging_format          | 6.68 us                                                | 6.29 us: 1.06x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                  |
| coverage                | 100 ms                                                 | 94.5 ms: 1.06x faster                                                  |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                   |
| deepcopy                | 342 us                                                 | 323 us: 1.06x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.71 us: 1.06x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.05 ms: 1.05x faster                                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                   |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                  |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                                   |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                   |
| json                    | 4.94 ms                                                | 4.72 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.25 ms: 1.04x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                 |
| crypto_pyaes            | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                  |
| pyflate                 | 418 ms                                                 | 404 ms: 1.03x faster                                                   |
| unpack_sequence         | 43.1 ns                                                | 41.7 ns: 1.03x faster                                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| mako                    | 10.1 ms                                                | 9.79 ms: 1.03x faster                                                  |
| spectral_norm           | 100 ms                                                 | 97.2 ms: 1.03x faster                                                  |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                   |
| tornado_http            | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                                   |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 67.2 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                 |
| coroutines              | 25.5 ms                                                | 25.7 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 760 ms: 1.03x slower                                                   |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 652 ms: 1.04x slower                                                   |
| generators              | 73.5 ms                                                | 76.4 ms: 1.04x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.12 us: 1.04x slower                                                  |
| nbody                   | 93.1 ms                                                | 97.5 ms: 1.05x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.93 ms: 1.05x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                  |
| unpickle                | 13.7 us                                                | 14.9 us: 1.09x slower                                                  |
| dask                    | 360 ms                                                 | 497 ms: 1.38x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (9): djangocms, telco, async_tree_none, bench_mp_pool, scimark_lu, django_template, deepcopy_reduce, thrift, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230204-3.12.0a4+-144aaa7/bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
