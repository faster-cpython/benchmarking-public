
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                        |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                         |
| regex_dna      | 204 ms                                                 | 218 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                         |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle_list          | 4.11 us                                                | 4.13 us: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.02x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.86 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.42 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                        |
| genshi_text    | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| mako           | 10.1 ms                                                | 9.90 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                        |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                         |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.65 ms: 1.10x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                        |
| nqueens                 | 83.4 ms                                                | 76.2 ms: 1.09x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.02 ms: 1.08x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                        |
| fannkuch                | 388 ms                                                 | 361 ms: 1.08x faster                                                         |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                        |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                         |
| spectral_norm           | 100 ms                                                 | 93.4 ms: 1.07x faster                                                        |
| sympy_str               | 290 ms                                                 | 271 ms: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                        |
| richards                | 45.7 ms                                                | 42.8 ms: 1.07x faster                                                        |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                         |
| json                    | 4.94 ms                                                | 4.66 ms: 1.06x faster                                                        |
| float                   | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.0 ms: 1.06x faster                                                        |
| logging_silent          | 101 ns                                                 | 95.9 ns: 1.05x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.27 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                         |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.05x faster                                                         |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                         |
| chaos                   | 69.2 ms                                                | 66.4 ms: 1.04x faster                                                        |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 294 us: 1.04x faster                                                         |
| raytrace                | 297 ms                                                 | 286 ms: 1.04x faster                                                         |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                         |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                         |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                         |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                                         |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                         |
| logging_format          | 6.68 us                                                | 6.49 us: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                                       |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 51.8 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                        |
| mako                    | 10.1 ms                                                | 9.90 ms: 1.02x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                        |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| tornado_http            | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.6 ms: 1.01x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.95 us: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle_list             | 4.11 us                                                | 4.13 us: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                         |
| unpickle_list           | 4.91 us                                                | 4.98 us: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 44.2 ns: 1.03x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 645 ms: 1.03x slower                                                         |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.4 ms: 1.03x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.70 sec: 1.03x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.86 ms: 1.04x slower                                                        |
| generators              | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.42 ms: 1.07x slower                                                        |
| regex_dna               | 204 ms                                                 | 218 ms: 1.07x slower                                                         |
| async_generators        | 368 ms                                                 | 435 ms: 1.18x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (13): sqlalchemy_declarative, async_tree_none, sqlglot_normalize, dulwich_log, django_template, unpickle, regex_v8, nbody, bench_mp_pool, djangocms, pickle, thrift, coverage
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
