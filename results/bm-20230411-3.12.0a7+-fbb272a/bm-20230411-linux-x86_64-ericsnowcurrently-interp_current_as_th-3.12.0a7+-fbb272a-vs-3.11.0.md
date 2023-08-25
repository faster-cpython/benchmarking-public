
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: interp_current_as_th
- machine: linux-x86_64
- commit hash: fbb272a
- commit date: 2023-04-11
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                             |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                            |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                             |
| tornado_http   | 96.3 ms                                                | 90.5 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 82.7 ms: 1.13x faster                                                             |
| float          | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                             |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                             |
| regex_compile  | 138 ms                                                 | 131 ms: 1.05x faster                                                              |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                             |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                              |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 98.7 ms: 1.05x faster                                                             |
| unpickle_list        | 4.91 us                                                | 4.67 us: 1.05x faster                                                             |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                             |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                             |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 80.2 ms: 1.05x slower                                                             |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.34 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.80 ms: 1.03x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                             |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                             |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.2 ms: 2.51x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                             |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.20 ms: 1.17x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.49 ms: 1.15x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                              |
| nbody                   | 93.1 ms                                                | 82.7 ms: 1.13x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                             |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.09x faster                                                             |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.09x faster                                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.12 ms: 1.09x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| logging_format          | 6.68 us                                                | 6.18 us: 1.08x faster                                                             |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                                              |
| raytrace                | 297 ms                                                 | 275 ms: 1.08x faster                                                              |
| chaos                   | 69.2 ms                                                | 64.1 ms: 1.08x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                              |
| logging_simple          | 6.03 us                                                | 5.62 us: 1.07x faster                                                             |
| logging_silent          | 101 ns                                                 | 94.3 ns: 1.07x faster                                                             |
| deepcopy                | 342 us                                                 | 321 us: 1.07x faster                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 49.9 ms: 1.06x faster                                                             |
| tornado_http            | 96.3 ms                                                | 90.5 ms: 1.06x faster                                                             |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                                             |
| spectral_norm           | 100 ms                                                 | 94.1 ms: 1.06x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 101 ms: 1.06x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                              |
| float                   | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                             |
| nqueens                 | 83.4 ms                                                | 78.8 ms: 1.06x faster                                                             |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                             |
| comprehensions          | 22.4 us                                                | 21.2 us: 1.06x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 98.7 ms: 1.05x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                            |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                             |
| regex_compile           | 138 ms                                                 | 131 ms: 1.05x faster                                                              |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.05x faster                                                              |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| unpickle_list           | 4.91 us                                                | 4.67 us: 1.05x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                            |
| json                    | 4.94 ms                                                | 4.72 ms: 1.05x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                                              |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                             |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                            |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                            |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                              |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                              |
| async_tree_memoization  | 627 ms                                                 | 605 ms: 1.04x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                             |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 682 ms: 1.03x faster                                                              |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 721 ms: 1.02x faster                                                              |
| coverage                | 100 ms                                                 | 97.8 ms: 1.02x faster                                                             |
| deepcopy_reduce         | 2.94 us                                                | 2.87 us: 1.02x faster                                                             |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 66.6 ms: 1.02x faster                                                             |
| async_tree_none         | 526 ms                                                 | 516 ms: 1.02x faster                                                              |
| unpack_sequence         | 43.1 ns                                                | 42.3 ns: 1.02x faster                                                             |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                             |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                              |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                             |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                                              |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                             |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                             |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                            |
| go                      | 140 ms                                                 | 139 ms: 1.00x faster                                                              |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                             |
| fannkuch                | 388 ms                                                 | 392 ms: 1.01x slower                                                              |
| thrift                  | 756 us                                                 | 767 us: 1.01x slower                                                              |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                             |
| python_startup          | 8.52 ms                                                | 8.80 ms: 1.03x slower                                                             |
| pickle_dict             | 31.1 us                                                | 32.1 us: 1.03x slower                                                             |
| regex_dna               | 204 ms                                                 | 214 ms: 1.05x slower                                                              |
| xml_etree_generate      | 76.2 ms                                                | 80.2 ms: 1.05x slower                                                             |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.34 us: 1.06x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.30 ms: 1.07x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                             |
| async_generators        | 368 ms                                                 | 405 ms: 1.10x slower                                                              |
| dask                    | 360 ms                                                 | 493 ms: 1.37x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                      |

Benchmark hidden because not significant (5): sqlalchemy_imperative, djangocms, bench_mp_pool, create_gc_cycles, pyflate
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
