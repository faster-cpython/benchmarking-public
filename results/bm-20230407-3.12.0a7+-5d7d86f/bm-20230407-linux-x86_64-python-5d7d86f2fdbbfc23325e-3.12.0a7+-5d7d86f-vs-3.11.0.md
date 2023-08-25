
# Results vs. 3.11.0

- fork: python
- ref: 5d7d86f2fdbbfc23325e
- machine: linux-x86_64
- commit hash: 5d7d86f
- commit date: 2023-04-07
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                  |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.3 ms: 1.05x faster                                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| nbody          | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                  |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.9 ms: 1.04x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                  |
| pickle_dict          | 31.1 us                                                | 33.0 us: 1.06x slower                                                  |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.46 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 48.3 ms: 1.07x faster                                                  |
| genshi_text    | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                  |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.22 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.50 ms: 1.13x faster                                                  |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.05 ms: 1.11x faster                                                  |
| spectral_norm           | 100 ms                                                 | 91.2 ms: 1.10x faster                                                  |
| scimark_fft             | 328 ms                                                 | 301 ms: 1.09x faster                                                   |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                  |
| logging_format          | 6.68 us                                                | 6.23 us: 1.07x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 48.3 ms: 1.07x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.63 us: 1.07x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                   |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                  |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                                  |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                   |
| float                   | 77.2 ms                                                | 73.3 ms: 1.05x faster                                                  |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                  |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                   |
| nbody                   | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                  |
| logging_silent          | 101 ns                                                 | 96.5 ns: 1.05x faster                                                  |
| html5lib                | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                  |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                                  |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                                  |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.04x faster                                                   |
| coverage                | 100 ms                                                 | 95.9 ms: 1.04x faster                                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 99.9 ms: 1.04x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| async_tree_none         | 526 ms                                                 | 510 ms: 1.03x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                 |
| comprehensions          | 22.4 us                                                | 21.8 us: 1.03x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                 |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 719 ms: 1.03x faster                                                   |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 66.5 ms: 1.02x faster                                                  |
| tornado_http            | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 692 ms: 1.01x faster                                                   |
| pyflate                 | 418 ms                                                 | 413 ms: 1.01x faster                                                   |
| telco                   | 6.58 ms                                                | 6.51 ms: 1.01x faster                                                  |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                   |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                  |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                   |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 43.6 ns: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                  |
| thrift                  | 756 us                                                 | 784 us: 1.04x slower                                                   |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                  |
| pickle_dict             | 31.1 us                                                | 33.0 us: 1.06x slower                                                  |
| pickle                  | 10.1 us                                                | 10.8 us: 1.07x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.46 us: 1.08x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                  |
| async_generators        | 368 ms                                                 | 415 ms: 1.13x slower                                                   |
| dask                    | 360 ms                                                 | 500 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (10): async_tree_memoization, sqlalchemy_declarative, pathlib, djangocms, mako, chameleon, bench_mp_pool, django_template, sqlalchemy_imperative, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
