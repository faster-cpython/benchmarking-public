
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 030016a
- commit date: 2023-04-06
- overall geometric mean: 1.02x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 271 ms: 1.05x slower                                                              |
| chameleon      | 6.47 ms                                                | 6.94 ms: 1.07x slower                                                             |
| docutils       | 2.63 sec                                               | 2.80 sec: 1.06x slower                                                            |
| html5lib       | 64.5 ms                                                | 66.6 ms: 1.03x slower                                                             |
| tornado_http   | 96.3 ms                                                | 104 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.1 ms: 1.02x faster                                                             |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| float          | 77.2 ms                                                | 81.0 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                              |
| regex_compile  | 138 ms                                                 | 148 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.96 ms: 1.26x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                                              |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                              |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.01x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                              |
| unpickle_list        | 4.91 us                                                | 5.14 us: 1.05x slower                                                             |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.45 us: 1.08x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.10x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                             |
| genshi_text     | 21.6 ms                                                | 22.9 ms: 1.06x slower                                                             |
| django_template | 32.6 ms                                                | 35.6 ms: 1.09x slower                                                             |
| mako            | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.8 ms: 2.31x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 517 ms: 1.78x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.96 ms: 1.26x faster                                                             |
| mypy2                   | 420 ms                                                 | 366 ms: 1.15x faster                                                              |
| coroutines              | 25.5 ms                                                | 22.8 ms: 1.12x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                             |
| gc_traversal            | 4.02 ms                                                | 3.66 ms: 1.10x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| unpickle_pure_python    | 228 us                                                 | 219 us: 1.04x faster                                                              |
| json_loads              | 26.5 us                                                | 25.8 us: 1.03x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                             |
| nbody                   | 93.1 ms                                                | 91.1 ms: 1.02x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.59 ms: 1.02x faster                                                             |
| nqueens                 | 83.4 ms                                                | 81.9 ms: 1.02x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                              |
| coverage                | 100 ms                                                 | 98.5 ms: 1.02x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.33 ms: 1.01x faster                                                             |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.01x faster                                                             |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                              |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                              |
| fannkuch                | 388 ms                                                 | 391 ms: 1.01x slower                                                              |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                            |
| logging_silent          | 101 ns                                                 | 103 ns: 1.01x slower                                                              |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.02x slower                                                             |
| chaos                   | 69.2 ms                                                | 70.5 ms: 1.02x slower                                                             |
| telco                   | 6.58 ms                                                | 6.73 ms: 1.02x slower                                                             |
| bench_thread_pool       | 819 us                                                 | 838 us: 1.02x slower                                                              |
| async_tree_none         | 526 ms                                                 | 539 ms: 1.02x slower                                                              |
| mdp                     | 2.62 sec                                               | 2.68 sec: 1.03x slower                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                            |
| async_tree_cpu_io_mixed | 739 ms                                                 | 761 ms: 1.03x slower                                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.64 ms: 1.03x slower                                                             |
| html5lib                | 64.5 ms                                                | 66.6 ms: 1.03x slower                                                             |
| pickle_pure_python      | 306 us                                                 | 316 us: 1.03x slower                                                              |
| scimark_lu              | 110 ms                                                 | 114 ms: 1.04x slower                                                              |
| deepcopy_memo           | 37.0 us                                                | 38.5 us: 1.04x slower                                                             |
| json                    | 4.94 ms                                                | 5.15 ms: 1.04x slower                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 55.6 ms: 1.05x slower                                                             |
| 2to3                    | 259 ms                                                 | 271 ms: 1.05x slower                                                              |
| logging_format          | 6.68 us                                                | 7.00 us: 1.05x slower                                                             |
| unpickle_list           | 4.91 us                                                | 5.14 us: 1.05x slower                                                             |
| float                   | 77.2 ms                                                | 81.0 ms: 1.05x slower                                                             |
| pprint_safe_repr        | 701 ms                                                 | 737 ms: 1.05x slower                                                              |
| djangocms               | 32.4 us                                                | 34.1 us: 1.05x slower                                                             |
| logging_simple          | 6.03 us                                                | 6.35 us: 1.05x slower                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 71.9 ms: 1.06x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                             |
| sympy_integrate         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                             |
| thrift                  | 756 us                                                 | 802 us: 1.06x slower                                                              |
| genshi_text             | 21.6 ms                                                | 22.9 ms: 1.06x slower                                                             |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 115 ms: 1.06x slower                                                              |
| meteor_contest          | 107 ms                                                 | 113 ms: 1.06x slower                                                              |
| docutils                | 2.63 sec                                               | 2.80 sec: 1.06x slower                                                            |
| sympy_expand            | 475 ms                                                 | 506 ms: 1.07x slower                                                              |
| spectral_norm           | 100 ms                                                 | 107 ms: 1.07x slower                                                              |
| crypto_pyaes            | 74.7 ms                                                | 80.0 ms: 1.07x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                                             |
| scimark_fft             | 328 ms                                                 | 352 ms: 1.07x slower                                                              |
| chameleon               | 6.47 ms                                                | 6.94 ms: 1.07x slower                                                             |
| regex_compile           | 138 ms                                                 | 148 ms: 1.07x slower                                                              |
| deepcopy                | 342 us                                                 | 367 us: 1.07x slower                                                              |
| tornado_http            | 96.3 ms                                                | 104 ms: 1.08x slower                                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 149 ms: 1.08x slower                                                              |
| pickle_list             | 4.11 us                                                | 4.45 us: 1.08x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 680 ms: 1.08x slower                                                              |
| django_template         | 32.6 ms                                                | 35.6 ms: 1.09x slower                                                             |
| mako                    | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                             |
| dulwich_log             | 63.7 ms                                                | 69.8 ms: 1.10x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 59.0 ms: 1.10x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                             |
| sympy_str               | 290 ms                                                 | 319 ms: 1.10x slower                                                              |
| sympy_sum               | 167 ms                                                 | 183 ms: 1.10x slower                                                              |
| xml_etree_generate      | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.8 ms: 1.10x slower                                                             |
| pyflate                 | 418 ms                                                 | 464 ms: 1.11x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.26 us: 1.11x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.90 ms: 1.12x slower                                                             |
| comprehensions          | 22.4 us                                                | 25.1 us: 1.12x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.57 ms: 1.12x slower                                                             |
| scimark_sor             | 118 ms                                                 | 137 ms: 1.16x slower                                                              |
| async_generators        | 368 ms                                                 | 429 ms: 1.16x slower                                                              |
| unpack_sequence         | 43.1 ns                                                | 53.0 ns: 1.23x slower                                                             |
| dask                    | 360 ms                                                 | 555 ms: 1.54x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (5): unpickle, go, bench_mp_pool, raytrace, richards
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x
