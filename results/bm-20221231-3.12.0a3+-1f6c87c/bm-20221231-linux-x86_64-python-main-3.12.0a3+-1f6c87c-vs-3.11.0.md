
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 1f6c87c
- commit date: 2022-12-31
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                  |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| html5lib       | 64.5 ms                                                | 60.3 ms: 1.07x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.2 ms: 1.08x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| regex_compile  | 138 ms                                                 | 131 ms: 1.05x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| regex_dna      | 204 ms                                                 | 215 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.33 ms: 1.35x faster                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                   |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                   |
| unpickle             | 13.7 us                                                | 12.7 us: 1.08x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.1 us: 1.03x faster                                  |
| pickle_list          | 4.11 us                                                | 4.00 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle               | 10.1 us                                                | 9.96 us: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.45 ms: 1.01x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.05 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.6 ms: 1.11x faster                                  |
| mako           | 10.1 ms                                                | 9.64 ms: 1.05x faster                                  |
| genshi_text    | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.33 ms: 1.35x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                   |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                  |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                   |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                  |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                  |
| logging_silent          | 101 ns                                                 | 91.4 ns: 1.11x faster                                  |
| richards                | 45.7 ms                                                | 41.5 ms: 1.10x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.08x faster                                  |
| float                   | 77.2 ms                                                | 71.2 ms: 1.08x faster                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                   |
| unpickle                | 13.7 us                                                | 12.7 us: 1.08x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| html5lib                | 64.5 ms                                                | 60.3 ms: 1.07x faster                                  |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                  |
| telco                   | 6.58 ms                                                | 6.19 ms: 1.06x faster                                  |
| spectral_norm           | 100 ms                                                 | 94.1 ms: 1.06x faster                                  |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                   |
| nqueens                 | 83.4 ms                                                | 78.9 ms: 1.06x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.06x faster                                  |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.06x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 64.5 ms: 1.05x faster                                  |
| regex_compile           | 138 ms                                                 | 131 ms: 1.05x faster                                   |
| bench_thread_pool       | 819 us                                                 | 777 us: 1.05x faster                                   |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                  |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                   |
| mako                    | 10.1 ms                                                | 9.64 ms: 1.05x faster                                  |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.30 ms: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                   |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                 |
| logging_format          | 6.68 us                                                | 6.44 us: 1.04x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.1 us: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                   |
| pickle_list             | 4.11 us                                                | 4.00 us: 1.03x faster                                  |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                 |
| unpack_sequence         | 43.1 ns                                                | 42.0 ns: 1.02x faster                                  |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| chaos                   | 69.2 ms                                                | 68.0 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                   |
| deepcopy                | 342 us                                                 | 338 us: 1.01x faster                                   |
| pickle                  | 10.1 us                                                | 9.96 us: 1.01x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 694 ms: 1.01x faster                                   |
| xml_etree_process       | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| thrift                  | 756 us                                                 | 749 us: 1.01x faster                                   |
| python_startup          | 8.52 ms                                                | 8.45 ms: 1.01x faster                                  |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 74.4 ms: 1.00x faster                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.05 ms: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| mdp                     | 2.62 sec                                               | 2.64 sec: 1.01x slower                                 |
| nbody                   | 93.1 ms                                                | 94.2 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 751 ms: 1.02x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| generators              | 73.5 ms                                                | 76.4 ms: 1.04x slower                                  |
| regex_dna               | 204 ms                                                 | 215 ms: 1.06x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none, djangocms, pathlib, coroutines, bench_mp_pool, deepcopy_reduce, xml_etree_generate, django_template, coverage
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221231-3.12.0a3+-1f6c87c/bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
