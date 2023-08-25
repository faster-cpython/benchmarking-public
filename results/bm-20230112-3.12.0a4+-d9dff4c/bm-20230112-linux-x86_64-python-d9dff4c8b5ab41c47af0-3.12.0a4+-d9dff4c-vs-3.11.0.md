
# Results vs. 3.11.0

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                  |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                 |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                   |
| nbody          | 93.1 ms                                                | 94.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                                   |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.39 ms: 1.34x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                   |
| json_loads           | 26.5 us                                                | 23.6 us: 1.12x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                                  |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                  |
| pickle_list          | 4.11 us                                                | 4.04 us: 1.02x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.58 ms: 1.01x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                  |
| mako            | 10.1 ms                                                | 9.77 ms: 1.03x faster                                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.39 ms: 1.34x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                  |
| logging_silent          | 101 ns                                                 | 89.8 ns: 1.13x faster                                                  |
| json_loads              | 26.5 us                                                | 23.6 us: 1.12x faster                                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                  |
| richards                | 45.7 ms                                                | 41.3 ms: 1.11x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.11 ms: 1.09x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.8 us: 1.09x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                   |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| float                   | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.80 ms: 1.06x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 64.5 ms: 1.06x faster                                                  |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 776 us: 1.06x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.3 ms: 1.06x faster                                                  |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                   |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                 |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                                   |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                 |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 673 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| logging_format          | 6.68 us                                                | 6.42 us: 1.04x faster                                                  |
| telco                   | 6.58 ms                                                | 6.33 ms: 1.04x faster                                                  |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| nqueens                 | 83.4 ms                                                | 80.3 ms: 1.04x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                   |
| chaos                   | 69.2 ms                                                | 66.8 ms: 1.04x faster                                                  |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                   |
| mako                    | 10.1 ms                                                | 9.77 ms: 1.03x faster                                                  |
| coroutines              | 25.5 ms                                                | 24.7 ms: 1.03x faster                                                  |
| spectral_norm           | 100 ms                                                 | 97.1 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                   |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                 |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                                  |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                   |
| pickle_list             | 4.11 us                                                | 4.04 us: 1.02x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                  |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.00x faster                                                  |
| python_startup          | 8.52 ms                                                | 8.58 ms: 1.01x slower                                                  |
| coverage                | 100 ms                                                 | 101 ms: 1.01x slower                                                   |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                                   |
| nbody                   | 93.1 ms                                                | 94.4 ms: 1.01x slower                                                  |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.98 us: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 754 ms: 1.02x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 45.1 ns: 1.05x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 657 ms: 1.05x slower                                                   |
| dask                    | 360 ms                                                 | 495 ms: 1.38x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (9): djangocms, meteor_contest, thrift, bench_mp_pool, xml_etree_generate, crypto_pyaes, deepcopy_reduce, pickle, async_tree_none
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
