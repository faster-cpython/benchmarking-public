
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: 8b9f269
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                        |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                        |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.5 ms: 1.06x faster                                                        |
| float          | 77.2 ms                                                | 73.3 ms: 1.05x faster                                                        |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                        |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                         |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                        |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.65 ms: 1.30x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                        |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                        |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.36 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.79 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.7 ms: 1.08x faster                                                        |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                        |
| genshi_text     | 21.6 ms                                                | 21.4 ms: 1.01x faster                                                        |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.46x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.65 ms: 1.30x faster                                                        |
| mypy2                   | 420 ms                                                 | 335 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.66 ms: 1.10x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| coroutines              | 25.5 ms                                                | 23.4 ms: 1.09x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.7 ms: 1.08x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.18 ms: 1.07x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                         |
| nbody                   | 93.1 ms                                                | 87.5 ms: 1.06x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                       |
| spectral_norm           | 100 ms                                                 | 94.4 ms: 1.06x faster                                                        |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                         |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                        |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                        |
| float                   | 77.2 ms                                                | 73.3 ms: 1.05x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                                        |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                                         |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                        |
| logging_silent          | 101 ns                                                 | 96.6 ns: 1.05x faster                                                        |
| coverage                | 100 ms                                                 | 95.7 ms: 1.05x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.9 ms: 1.04x faster                                                        |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                         |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                         |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 789 us: 1.04x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 678 ms: 1.03x faster                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                        |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                         |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                        |
| sympy_expand            | 475 ms                                                 | 463 ms: 1.03x faster                                                         |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                        |
| nqueens                 | 83.4 ms                                                | 81.6 ms: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                        |
| sympy_str               | 290 ms                                                 | 286 ms: 1.02x faster                                                         |
| telco                   | 6.58 ms                                                | 6.49 ms: 1.01x faster                                                        |
| chaos                   | 69.2 ms                                                | 68.2 ms: 1.01x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                        |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                                         |
| chameleon               | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                        |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                                        |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                         |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                        |
| genshi_text             | 21.6 ms                                                | 21.4 ms: 1.01x faster                                                        |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                                         |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                         |
| pickle_dict             | 31.1 us                                                | 31.5 us: 1.01x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.01x slower                                                        |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                        |
| go                      | 140 ms                                                 | 142 ms: 1.02x slower                                                         |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.79 ms: 1.03x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 649 ms: 1.03x slower                                                         |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                        |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                        |
| thrift                  | 756 us                                                 | 793 us: 1.05x slower                                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.36 us: 1.06x slower                                                        |
| comprehensions          | 22.4 us                                                | 24.0 us: 1.07x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                        |
| async_generators        | 368 ms                                                 | 415 ms: 1.13x slower                                                         |
| dask                    | 360 ms                                                 | 508 ms: 1.41x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (10): unpack_sequence, async_tree_none, pathlib, djangocms, fannkuch, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_io, dulwich_log, scimark_monte_carlo
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
