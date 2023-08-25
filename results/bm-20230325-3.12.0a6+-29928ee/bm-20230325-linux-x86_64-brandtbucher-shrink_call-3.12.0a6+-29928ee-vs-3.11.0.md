
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 29928ee
- commit date: 2023-03-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.55 ms: 1.01x slower                                               |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                              |
| html5lib       | 64.5 ms                                                | 61.5 ms: 1.05x faster                                               |
| tornado_http   | 96.3 ms                                                | 91.4 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.9 ms: 1.06x faster                                               |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| float          | 77.2 ms                                                | 74.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                               |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                               |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.48 ms: 1.33x faster                                               |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                |
| json_loads           | 26.5 us                                                | 24.4 us: 1.08x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 55.9 ms: 1.04x slower                                               |
| unpickle_list        | 4.91 us                                                | 5.23 us: 1.06x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 81.4 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.9 ms: 1.10x faster                                               |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.01x faster                                               |
| mako            | 10.1 ms                                                | 9.98 ms: 1.01x faster                                               |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.2 ms: 2.43x faster                                               |
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.48 ms: 1.33x faster                                               |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                               |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.15x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                |
| genshi_xml              | 51.8 ms                                                | 46.9 ms: 1.10x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                               |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.09x faster                                               |
| json_loads              | 26.5 us                                                | 24.4 us: 1.08x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.18 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                |
| nbody                   | 93.1 ms                                                | 87.9 ms: 1.06x faster                                               |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                               |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.06x faster                                                |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                               |
| tornado_http            | 96.3 ms                                                | 91.4 ms: 1.05x faster                                               |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| chaos                   | 69.2 ms                                                | 65.8 ms: 1.05x faster                                               |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                               |
| html5lib                | 64.5 ms                                                | 61.5 ms: 1.05x faster                                               |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                              |
| deepcopy                | 342 us                                                 | 327 us: 1.05x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.05x faster                                               |
| bench_thread_pool       | 819 us                                                 | 784 us: 1.04x faster                                                |
| logging_silent          | 101 ns                                                 | 97.0 ns: 1.04x faster                                               |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                |
| richards                | 45.7 ms                                                | 44.2 ms: 1.04x faster                                               |
| nqueens                 | 83.4 ms                                                | 80.6 ms: 1.03x faster                                               |
| float                   | 77.2 ms                                                | 74.7 ms: 1.03x faster                                               |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.03x faster                                              |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                              |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                               |
| spectral_norm           | 100 ms                                                 | 97.3 ms: 1.03x faster                                               |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.03x faster                                               |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| crypto_pyaes            | 74.7 ms                                                | 73.1 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                               |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.01x faster                                               |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                               |
| mako                    | 10.1 ms                                                | 9.98 ms: 1.01x faster                                               |
| coverage                | 100 ms                                                 | 99.1 ms: 1.01x faster                                               |
| fannkuch                | 388 ms                                                 | 384 ms: 1.01x faster                                                |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                               |
| chameleon               | 6.47 ms                                                | 6.55 ms: 1.01x slower                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                                |
| regex_dna               | 204 ms                                                 | 207 ms: 1.01x slower                                                |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 638 ms: 1.02x slower                                                |
| unpack_sequence         | 43.1 ns                                                | 44.0 ns: 1.02x slower                                               |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                               |
| pyflate                 | 418 ms                                                 | 431 ms: 1.03x slower                                                |
| thrift                  | 756 us                                                 | 783 us: 1.03x slower                                                |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                               |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                               |
| xml_etree_process       | 53.9 ms                                                | 55.9 ms: 1.04x slower                                               |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.06x slower                                               |
| unpickle_list           | 4.91 us                                                | 5.23 us: 1.06x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 81.4 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                               |
| async_generators        | 368 ms                                                 | 408 ms: 1.11x slower                                                |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (11): async_tree_none, unpickle, telco, async_tree_io, sqlalchemy_imperative, dulwich_log, djangocms, async_tree_cpu_io_mixed, bench_mp_pool, pickle_list, sympy_sum
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
