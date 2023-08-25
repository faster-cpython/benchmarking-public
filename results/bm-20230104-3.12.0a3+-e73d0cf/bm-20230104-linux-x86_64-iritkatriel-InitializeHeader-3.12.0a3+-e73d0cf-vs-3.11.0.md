
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| chameleon      | 6.47 ms                                                | 6.17 ms: 1.05x faster                                                   |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                  |
| html5lib       | 64.5 ms                                                | 60.1 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                   |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                   |
| regex_compile  | 138 ms                                                 | 131 ms: 1.05x faster                                                    |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                   |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.42 ms: 1.34x faster                                                   |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                                    |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                    |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                   |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                   |
| xml_etree_generate   | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                   |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                   |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_process, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.48 ms: 1.00x faster                                                   |
| python_startup_no_site | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.3 ms: 1.12x faster                                                   |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.06x faster                                                   |
| mako            | 10.1 ms                                                | 9.83 ms: 1.03x faster                                                   |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.42 ms: 1.34x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                                    |
| logging_silent          | 101 ns                                                 | 90.4 ns: 1.12x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 46.3 ms: 1.12x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                   |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                    |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.34 ms: 1.10x faster                                                   |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.10 ms: 1.10x faster                                                   |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                    |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                                   |
| float                   | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                   |
| html5lib                | 64.5 ms                                                | 60.1 ms: 1.07x faster                                                   |
| pyflate                 | 418 ms                                                 | 391 ms: 1.07x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 774 us: 1.06x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 64.4 ms: 1.06x faster                                                   |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.06x faster                                                   |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                    |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                    |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                                   |
| regex_compile           | 138 ms                                                 | 131 ms: 1.05x faster                                                    |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                                    |
| chameleon               | 6.47 ms                                                | 6.17 ms: 1.05x faster                                                   |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.09 ms: 1.05x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                                   |
| json                    | 4.94 ms                                                | 4.73 ms: 1.05x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 674 ms: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                    |
| unpack_sequence         | 43.1 ns                                                | 41.5 ns: 1.04x faster                                                   |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                    |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                    |
| go                      | 140 ms                                                 | 135 ms: 1.03x faster                                                    |
| nqueens                 | 83.4 ms                                                | 80.6 ms: 1.03x faster                                                   |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                    |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                    |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                   |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                    |
| mako                    | 10.1 ms                                                | 9.83 ms: 1.03x faster                                                   |
| spectral_norm           | 100 ms                                                 | 97.5 ms: 1.03x faster                                                   |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                   |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                    |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                                   |
| chaos                   | 69.2 ms                                                | 67.9 ms: 1.02x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                   |
| coverage                | 100 ms                                                 | 98.7 ms: 1.01x faster                                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                   |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                   |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                   |
| xml_etree_generate      | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                   |
| python_startup          | 8.52 ms                                                | 8.48 ms: 1.00x faster                                                   |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                   |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.02x slower                                                    |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                   |
| regex_dna               | 204 ms                                                 | 211 ms: 1.03x slower                                                    |
| generators              | 73.5 ms                                                | 77.1 ms: 1.05x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (11): meteor_contest, async_tree_memoization, thrift, async_tree_none, djangocms, xml_etree_process, nbody, pickle_list, bench_mp_pool, sqlglot_transpile, xml_etree_iterparse
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
