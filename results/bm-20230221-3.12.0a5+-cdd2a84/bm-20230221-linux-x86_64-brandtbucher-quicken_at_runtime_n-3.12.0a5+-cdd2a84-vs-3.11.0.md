
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: cdd2a84
- commit date: 2023-02-21
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                        |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                         |
| nbody          | 93.1 ms                                                | 96.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                        |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                         |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.45 ms: 1.33x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 195 us: 1.17x faster                                                         |
| json_loads           | 26.5 us                                                | 23.6 us: 1.12x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.6 ms: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                        |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.30 us: 1.04x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.34 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                        |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| mako            | 10.1 ms                                                | 9.82 ms: 1.03x faster                                                        |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.5 ms: 2.49x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.45 ms: 1.33x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 195 us: 1.17x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.16 ms: 1.16x faster                                                        |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.13x faster                                                         |
| coroutines              | 25.5 ms                                                | 22.8 ms: 1.12x faster                                                        |
| json_loads              | 26.5 us                                                | 23.6 us: 1.12x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                                        |
| logging_silent          | 101 ns                                                 | 92.9 ns: 1.09x faster                                                        |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                         |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                         |
| hexiom                  | 6.37 ms                                                | 5.95 ms: 1.07x faster                                                        |
| nqueens                 | 83.4 ms                                                | 78.2 ms: 1.07x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                         |
| fannkuch                | 388 ms                                                 | 364 ms: 1.06x faster                                                         |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.23 ms: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                       |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 50.4 ms: 1.05x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                         |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                                         |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| pyflate                 | 418 ms                                                 | 400 ms: 1.04x faster                                                         |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                       |
| chaos                   | 69.2 ms                                                | 66.4 ms: 1.04x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                                        |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                                         |
| coverage                | 100 ms                                                 | 96.4 ms: 1.04x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                         |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 792 us: 1.03x faster                                                         |
| spectral_norm           | 100 ms                                                 | 96.8 ms: 1.03x faster                                                        |
| go                      | 140 ms                                                 | 135 ms: 1.03x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                         |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                        |
| mako                    | 10.1 ms                                                | 9.82 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 66.5 ms: 1.02x faster                                                        |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                         |
| crypto_pyaes            | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                        |
| tornado_http            | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                        |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                        |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                                         |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                        |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                        |
| thrift                  | 756 us                                                 | 764 us: 1.01x slower                                                         |
| xml_etree_process       | 53.9 ms                                                | 54.6 ms: 1.01x slower                                                        |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| nbody                   | 93.1 ms                                                | 96.0 ms: 1.03x slower                                                        |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                         |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                        |
| pickle_dict             | 31.1 us                                                | 32.4 us: 1.04x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.30 us: 1.04x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.34 ms: 1.05x slower                                                        |
| async_generators        | 368 ms                                                 | 408 ms: 1.11x slower                                                         |
| dask                    | 360 ms                                                 | 502 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (10): unpickle, deepcopy_reduce, sqlalchemy_declarative, sqlalchemy_imperative, bench_mp_pool, unpack_sequence, async_tree_cpu_io_mixed, regex_v8, async_tree_none, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
