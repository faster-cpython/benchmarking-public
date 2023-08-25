
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.02x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 274 ms: 1.06x slower                                                              |
| chameleon      | 6.47 ms                                                | 6.83 ms: 1.06x slower                                                             |
| docutils       | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                              |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                             |
| nbody          | 93.1 ms                                                | 96.7 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                             |
| regex_dna      | 204 ms                                                 | 203 ms: 1.01x faster                                                              |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| unpickle_list        | 4.91 us                                                | 4.79 us: 1.03x faster                                                             |
| pickle_dict          | 31.1 us                                                | 30.5 us: 1.02x faster                                                             |
| json_loads           | 26.5 us                                                | 26.6 us: 1.01x slower                                                             |
| pickle_pure_python   | 306 us                                                 | 309 us: 1.01x slower                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                              |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 79.5 ms: 1.04x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.35 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.77 ms: 1.03x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.21 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 51.0 ms: 1.01x faster                                                             |
| genshi_text     | 21.6 ms                                                | 22.2 ms: 1.03x slower                                                             |
| mako            | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                             |
| django_template | 32.6 ms                                                | 34.8 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 514 ms: 1.79x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.39 ms: 1.18x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 217 us: 1.05x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| regex_v8                | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                             |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                              |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                              |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.34 ms: 1.04x faster                                                             |
| gc_traversal            | 4.02 ms                                                | 3.90 ms: 1.03x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                            |
| unpickle_list           | 4.91 us                                                | 4.79 us: 1.03x faster                                                             |
| pickle_dict             | 31.1 us                                                | 30.5 us: 1.02x faster                                                             |
| richards                | 45.7 ms                                                | 44.9 ms: 1.02x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 51.0 ms: 1.01x faster                                                             |
| regex_dna               | 204 ms                                                 | 203 ms: 1.01x faster                                                              |
| json_loads              | 26.5 us                                                | 26.6 us: 1.01x slower                                                             |
| telco                   | 6.58 ms                                                | 6.64 ms: 1.01x slower                                                             |
| pathlib                 | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                             |
| pickle_pure_python      | 306 us                                                 | 309 us: 1.01x slower                                                              |
| json                    | 4.94 ms                                                | 5.00 ms: 1.01x slower                                                             |
| async_generators        | 368 ms                                                 | 375 ms: 1.02x slower                                                              |
| bench_thread_pool       | 819 us                                                 | 834 us: 1.02x slower                                                              |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                                              |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.49 sec: 1.02x slower                                                            |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                              |
| scimark_sor             | 118 ms                                                 | 121 ms: 1.02x slower                                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 69.6 ms: 1.02x slower                                                             |
| docutils                | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                            |
| thrift                  | 756 us                                                 | 775 us: 1.03x slower                                                              |
| deepcopy_memo           | 37.0 us                                                | 38.0 us: 1.03x slower                                                             |
| pyflate                 | 418 ms                                                 | 429 ms: 1.03x slower                                                              |
| genshi_text             | 21.6 ms                                                | 22.2 ms: 1.03x slower                                                             |
| python_startup          | 8.52 ms                                                | 8.77 ms: 1.03x slower                                                             |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                            |
| float                   | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.21 ms: 1.03x slower                                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 765 ms: 1.04x slower                                                              |
| djangocms               | 32.4 us                                                | 33.6 us: 1.04x slower                                                             |
| nbody                   | 93.1 ms                                                | 96.7 ms: 1.04x slower                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 55.2 ms: 1.04x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 729 ms: 1.04x slower                                                              |
| mako                    | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                             |
| logging_format          | 6.68 us                                                | 6.96 us: 1.04x slower                                                             |
| raytrace                | 297 ms                                                 | 309 ms: 1.04x slower                                                              |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 79.5 ms: 1.04x slower                                                             |
| coroutines              | 25.5 ms                                                | 26.6 ms: 1.04x slower                                                             |
| regex_compile           | 138 ms                                                 | 144 ms: 1.04x slower                                                              |
| logging_simple          | 6.03 us                                                | 6.31 us: 1.05x slower                                                             |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                                              |
| sympy_integrate         | 21.0 ms                                                | 22.0 ms: 1.05x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.65 us: 1.05x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                             |
| sympy_expand            | 475 ms                                                 | 501 ms: 1.05x slower                                                              |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.05x slower                                                              |
| chameleon               | 6.47 ms                                                | 6.83 ms: 1.06x slower                                                             |
| 2to3                    | 259 ms                                                 | 274 ms: 1.06x slower                                                              |
| pickle_list             | 4.11 us                                                | 4.35 us: 1.06x slower                                                             |
| crypto_pyaes            | 74.7 ms                                                | 79.0 ms: 1.06x slower                                                             |
| spectral_norm           | 100 ms                                                 | 106 ms: 1.06x slower                                                              |
| django_template         | 32.6 ms                                                | 34.8 ms: 1.07x slower                                                             |
| deepcopy                | 342 us                                                 | 366 us: 1.07x slower                                                              |
| sympy_str               | 290 ms                                                 | 311 ms: 1.07x slower                                                              |
| dulwich_log             | 63.7 ms                                                | 68.7 ms: 1.08x slower                                                             |
| meteor_contest          | 107 ms                                                 | 116 ms: 1.09x slower                                                              |
| sympy_sum               | 167 ms                                                 | 182 ms: 1.09x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.21 us: 1.09x slower                                                             |
| scimark_fft             | 328 ms                                                 | 359 ms: 1.09x slower                                                              |
| generators              | 73.5 ms                                                | 80.5 ms: 1.10x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 688 ms: 1.10x slower                                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.87 ms: 1.10x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.55 ms: 1.10x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 51.6 ns: 1.20x slower                                                             |
| dask                    | 360 ms                                                 | 545 ms: 1.51x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (9): html5lib, logging_silent, fannkuch, bench_mp_pool, mdp, chaos, hexiom, deltablue, unpickle
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
