
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: a748e80
- commit date: 2023-01-29
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                                              |
| chameleon      | 6.47 ms                                                | 6.91 ms: 1.07x slower                                                             |
| docutils       | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                            |
| tornado_http   | 96.3 ms                                                | 106 ms: 1.10x slower                                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                              |
| float          | 77.2 ms                                                | 79.1 ms: 1.02x slower                                                             |
| nbody          | 93.1 ms                                                | 98.0 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.68 ms: 1.09x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                                              |
| regex_compile  | 138 ms                                                 | 142 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                              |
| unpickle_list        | 4.91 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                              |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.13 ms: 1.07x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.56 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 50.5 ms: 1.03x faster                                                             |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                             |
| genshi_text     | 21.6 ms                                                | 22.5 ms: 1.05x slower                                                             |
| django_template | 32.6 ms                                                | 34.8 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 516 ms: 1.78x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 360 ms: 1.17x faster                                                              |
| comprehensions          | 22.4 us                                                | 20.4 us: 1.10x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.68 ms: 1.09x faster                                                             |
| logging_silent          | 101 ns                                                 | 94.6 ns: 1.07x faster                                                             |
| nqueens                 | 83.4 ms                                                | 78.1 ms: 1.07x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 214 us: 1.07x faster                                                              |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                             |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                              |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                              |
| deltablue               | 3.67 ms                                                | 3.51 ms: 1.05x faster                                                             |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                              |
| hexiom                  | 6.37 ms                                                | 6.12 ms: 1.04x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                            |
| chaos                   | 69.2 ms                                                | 67.1 ms: 1.03x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                              |
| genshi_xml              | 51.8 ms                                                | 50.5 ms: 1.03x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                            |
| async_generators        | 368 ms                                                 | 362 ms: 1.02x faster                                                              |
| unpickle_list           | 4.91 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                                             |
| scimark_sor             | 118 ms                                                 | 117 ms: 1.01x faster                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                             |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| thrift                  | 756 us                                                 | 761 us: 1.01x slower                                                              |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                                              |
| pyflate                 | 418 ms                                                 | 423 ms: 1.01x slower                                                              |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                             |
| telco                   | 6.58 ms                                                | 6.67 ms: 1.01x slower                                                             |
| sympy_integrate         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                                             |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                             |
| pickle_pure_python      | 306 us                                                 | 311 us: 1.02x slower                                                              |
| coroutines              | 25.5 ms                                                | 25.9 ms: 1.02x slower                                                             |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                              |
| bench_thread_pool       | 819 us                                                 | 838 us: 1.02x slower                                                              |
| float                   | 77.2 ms                                                | 79.1 ms: 1.02x slower                                                             |
| async_tree_none         | 526 ms                                                 | 540 ms: 1.03x slower                                                              |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                              |
| docutils                | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                            |
| deepcopy_memo           | 37.0 us                                                | 38.1 us: 1.03x slower                                                             |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                            |
| crypto_pyaes            | 74.7 ms                                                | 76.9 ms: 1.03x slower                                                             |
| regex_compile           | 138 ms                                                 | 142 ms: 1.03x slower                                                              |
| raytrace                | 297 ms                                                 | 307 ms: 1.03x slower                                                              |
| sympy_sum               | 167 ms                                                 | 172 ms: 1.04x slower                                                              |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                                             |
| 2to3                    | 259 ms                                                 | 269 ms: 1.04x slower                                                              |
| async_tree_io           | 1.30 sec                                               | 1.35 sec: 1.04x slower                                                            |
| scimark_monte_carlo     | 68.1 ms                                                | 70.7 ms: 1.04x slower                                                             |
| json                    | 4.94 ms                                                | 5.14 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                             |
| meteor_contest          | 107 ms                                                 | 111 ms: 1.04x slower                                                              |
| sympy_str               | 290 ms                                                 | 302 ms: 1.04x slower                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 770 ms: 1.04x slower                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 55.4 ms: 1.04x slower                                                             |
| generators              | 73.5 ms                                                | 76.8 ms: 1.05x slower                                                             |
| genshi_text             | 21.6 ms                                                | 22.5 ms: 1.05x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 736 ms: 1.05x slower                                                              |
| spectral_norm           | 100 ms                                                 | 105 ms: 1.05x slower                                                              |
| sympy_expand            | 475 ms                                                 | 499 ms: 1.05x slower                                                              |
| nbody                   | 93.1 ms                                                | 98.0 ms: 1.05x slower                                                             |
| logging_format          | 6.68 us                                                | 7.05 us: 1.06x slower                                                             |
| logging_simple          | 6.03 us                                                | 6.40 us: 1.06x slower                                                             |
| deepcopy                | 342 us                                                 | 363 us: 1.06x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.12 us: 1.06x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 115 ms: 1.06x slower                                                              |
| django_template         | 32.6 ms                                                | 34.8 ms: 1.07x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                                             |
| chameleon               | 6.47 ms                                                | 6.91 ms: 1.07x slower                                                             |
| dask                    | 360 ms                                                 | 385 ms: 1.07x slower                                                              |
| xml_etree_generate      | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.13 ms: 1.07x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                             |
| dulwich_log             | 63.7 ms                                                | 68.4 ms: 1.07x slower                                                             |
| scimark_fft             | 328 ms                                                 | 357 ms: 1.09x slower                                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.56 ms: 1.09x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 687 ms: 1.09x slower                                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.87 ms: 1.10x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 47.3 ns: 1.10x slower                                                             |
| tornado_http            | 96.3 ms                                                | 106 ms: 1.10x slower                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.54 ms: 1.10x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.57 us: 1.11x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (6): unpickle, scimark_sparse_mat_mult, bench_mp_pool, html5lib, json_loads, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
