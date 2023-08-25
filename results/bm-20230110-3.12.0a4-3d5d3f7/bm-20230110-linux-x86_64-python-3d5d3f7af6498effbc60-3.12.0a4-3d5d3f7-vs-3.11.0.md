
# Results vs. 3.11.0

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                  |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                |
| html5lib       | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                 |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.49 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                 |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.54 ms: 1.32x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                  |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                 |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                  |
| unpickle             | 13.7 us                                                | 13.0 us: 1.06x faster                                                 |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                                 |
| pickle_list          | 4.11 us                                                | 4.02 us: 1.02x faster                                                 |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.54 ms: 1.00x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                 |
| genshi_text    | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                 |
| mako           | 10.1 ms                                                | 9.74 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                  |
| json_dumps              | 12.6 ms                                                | 9.54 ms: 1.32x faster                                                 |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.49 ms: 1.14x faster                                                 |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                 |
| gc_traversal            | 4.02 ms                                                | 3.57 ms: 1.13x faster                                                 |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                 |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                                |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.13 ms: 1.09x faster                                                 |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                 |
| logging_silent          | 101 ns                                                 | 93.5 ns: 1.08x faster                                                 |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                 |
| html5lib                | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                  |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                  |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                 |
| nqueens                 | 83.4 ms                                                | 78.0 ms: 1.07x faster                                                 |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                 |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                  |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                |
| unpickle                | 13.7 us                                                | 13.0 us: 1.06x faster                                                 |
| pyflate                 | 418 ms                                                 | 397 ms: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                |
| spectral_norm           | 100 ms                                                 | 95.0 ms: 1.05x faster                                                 |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                                 |
| telco                   | 6.58 ms                                                | 6.26 ms: 1.05x faster                                                 |
| djangocms               | 32.4 us                                                | 30.9 us: 1.05x faster                                                 |
| bench_thread_pool       | 819 us                                                 | 782 us: 1.05x faster                                                  |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                                 |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                                 |
| raytrace                | 297 ms                                                 | 284 ms: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                                  |
| regex_v8                | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                 |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                  |
| json                    | 4.94 ms                                                | 4.74 ms: 1.04x faster                                                 |
| unpack_sequence         | 43.1 ns                                                | 41.4 ns: 1.04x faster                                                 |
| async_generators        | 368 ms                                                 | 354 ms: 1.04x faster                                                  |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 65.7 ms: 1.04x faster                                                 |
| mako                    | 10.1 ms                                                | 9.74 ms: 1.04x faster                                                 |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 680 ms: 1.03x faster                                                  |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.03x faster                                                 |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.02x faster                                                 |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                  |
| pickle_list             | 4.11 us                                                | 4.02 us: 1.02x faster                                                 |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                  |
| chaos                   | 69.2 ms                                                | 67.7 ms: 1.02x faster                                                 |
| async_tree_memoization  | 627 ms                                                 | 616 ms: 1.02x faster                                                  |
| dask                    | 360 ms                                                 | 355 ms: 1.01x faster                                                  |
| coverage                | 100 ms                                                 | 99.0 ms: 1.01x faster                                                 |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                 |
| deepcopy                | 342 us                                                 | 339 us: 1.01x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                 |
| python_startup          | 8.52 ms                                                | 8.54 ms: 1.00x slower                                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.00x slower                                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 747 ms: 1.01x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                                 |
| python_startup_no_site  | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                 |
| crypto_pyaes            | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                 |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                 |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                                 |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                                 |
| regex_dna               | 204 ms                                                 | 209 ms: 1.02x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.06x slower                                                 |
| generators              | 73.5 ms                                                | 79.1 ms: 1.08x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (9): pickle, thrift, coroutines, chameleon, django_template, nbody, bench_mp_pool, async_tree_io, xml_etree_process
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
