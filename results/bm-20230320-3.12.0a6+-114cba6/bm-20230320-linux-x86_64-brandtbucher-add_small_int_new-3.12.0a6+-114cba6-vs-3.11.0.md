
# Results vs. 3.11.0

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: 114cba6
- commit date: 2023-03-20
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| chameleon      | 6.47 ms                                                | 6.32 ms: 1.02x faster                                                     |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                    |
| html5lib       | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                     |
| tornado_http   | 96.3 ms                                                | 91.1 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                     |
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                     |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                     |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.53 ms: 1.32x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                      |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 99.1 ms: 1.05x faster                                                     |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                                     |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.20 us: 1.02x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.89 ms: 1.04x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                     |
| genshi_text    | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                     |
| mako           | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                     |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                      |
| json_dumps              | 12.6 ms                                                | 9.53 ms: 1.32x faster                                                     |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.15 ms: 1.17x faster                                                     |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                     |
| coroutines              | 25.5 ms                                                | 22.5 ms: 1.13x faster                                                     |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                      |
| richards                | 45.7 ms                                                | 41.8 ms: 1.09x faster                                                     |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                     |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                     |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                                     |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                     |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                      |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.19 ms: 1.07x faster                                                     |
| raytrace                | 297 ms                                                 | 277 ms: 1.07x faster                                                      |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                     |
| html5lib                | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                     |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                      |
| deepcopy                | 342 us                                                 | 322 us: 1.06x faster                                                      |
| nbody                   | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                     |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                      |
| chaos                   | 69.2 ms                                                | 65.4 ms: 1.06x faster                                                     |
| tornado_http            | 96.3 ms                                                | 91.1 ms: 1.06x faster                                                     |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                     |
| nqueens                 | 83.4 ms                                                | 79.1 ms: 1.05x faster                                                     |
| logging_silent          | 101 ns                                                 | 96.0 ns: 1.05x faster                                                     |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                                     |
| coverage                | 100 ms                                                 | 95.1 ms: 1.05x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                    |
| float                   | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 99.1 ms: 1.05x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.09 ms: 1.05x faster                                                     |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                    |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                      |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                                     |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                      |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                    |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                     |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                     |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                     |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                      |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.32 ms: 1.02x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 66.6 ms: 1.02x faster                                                     |
| pyflate                 | 418 ms                                                 | 410 ms: 1.02x faster                                                      |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                                     |
| telco                   | 6.58 ms                                                | 6.49 ms: 1.02x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                     |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                      |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                     |
| crypto_pyaes            | 74.7 ms                                                | 75.0 ms: 1.00x slower                                                     |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                     |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                                     |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                     |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                     |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                     |
| async_tree_memoization  | 627 ms                                                 | 640 ms: 1.02x slower                                                      |
| pickle_list             | 4.11 us                                                | 4.20 us: 1.02x slower                                                     |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                     |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                     |
| thrift                  | 756 us                                                 | 777 us: 1.03x slower                                                      |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.03x slower                                                     |
| python_startup          | 8.52 ms                                                | 8.89 ms: 1.04x slower                                                     |
| unpickle_list           | 4.91 us                                                | 5.12 us: 1.04x slower                                                     |
| comprehensions          | 22.4 us                                                | 23.6 us: 1.05x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                     |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                      |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (10): spectral_norm, unpickle, async_tree_none, djangocms, async_tree_io, django_template, bench_mp_pool, scimark_lu, unpack_sequence, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
