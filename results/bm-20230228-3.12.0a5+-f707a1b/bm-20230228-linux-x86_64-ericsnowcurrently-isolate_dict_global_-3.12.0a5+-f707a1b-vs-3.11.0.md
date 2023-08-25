
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_dict_global_
- machine: linux-x86_64
- commit hash: f707a1b
- commit date: 2023-02-28
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                             |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                            |
| html5lib       | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                             |
| tornado_http   | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                              |
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                             |
| nbody          | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                             |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                              |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                              |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.09x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                              |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                             |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                             |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (3): pickle_list, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.06 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.6 ms: 1.06x faster                                                             |
| mako            | 10.1 ms                                                | 9.81 ms: 1.03x faster                                                             |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                             |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                              |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                              |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                             |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                              |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.40 sec: 1.09x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.09x faster                                                              |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.08x faster                                                             |
| coverage                | 100 ms                                                 | 93.1 ms: 1.07x faster                                                             |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                              |
| logging_silent          | 101 ns                                                 | 94.5 ns: 1.07x faster                                                             |
| json                    | 4.94 ms                                                | 4.62 ms: 1.07x faster                                                             |
| spectral_norm           | 100 ms                                                 | 93.8 ms: 1.07x faster                                                             |
| logging_format          | 6.68 us                                                | 6.27 us: 1.07x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 48.6 ms: 1.06x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                              |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                            |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                              |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                                             |
| html5lib                | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                             |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                              |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                            |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                             |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                              |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                              |
| nqueens                 | 83.4 ms                                                | 80.5 ms: 1.04x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.16 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 679 ms: 1.03x faster                                                              |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                              |
| chameleon               | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                             |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                                             |
| raytrace                | 297 ms                                                 | 289 ms: 1.03x faster                                                              |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                             |
| mako                    | 10.1 ms                                                | 9.81 ms: 1.03x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 797 us: 1.03x faster                                                              |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                            |
| scimark_monte_carlo     | 68.1 ms                                                | 66.6 ms: 1.02x faster                                                             |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                              |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.42 ms: 1.02x faster                                                             |
| crypto_pyaes            | 74.7 ms                                                | 73.6 ms: 1.02x faster                                                             |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                                             |
| chaos                   | 69.2 ms                                                | 68.5 ms: 1.01x faster                                                             |
| tornado_http            | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                             |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                             |
| pyflate                 | 418 ms                                                 | 417 ms: 1.00x faster                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                             |
| nbody                   | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                             |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                                             |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                                              |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                             |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                                             |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.2 ms: 1.02x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 44.3 ns: 1.03x slower                                                             |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                              |
| xml_etree_process       | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 650 ms: 1.04x slower                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                             |
| thrift                  | 756 us                                                 | 793 us: 1.05x slower                                                              |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.06 ms: 1.06x slower                                                             |
| comprehensions          | 22.4 us                                                | 24.2 us: 1.08x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 417 ms: 1.13x slower                                                              |
| dask                    | 360 ms                                                 | 510 ms: 1.42x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (13): genshi_text, async_tree_none, pickle_list, sympy_str, async_tree_cpu_io_mixed, unpickle, bench_mp_pool, scimark_lu, dulwich_log, deepcopy_reduce, xml_etree_iterparse, djangocms, sqlalchemy_declarative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
