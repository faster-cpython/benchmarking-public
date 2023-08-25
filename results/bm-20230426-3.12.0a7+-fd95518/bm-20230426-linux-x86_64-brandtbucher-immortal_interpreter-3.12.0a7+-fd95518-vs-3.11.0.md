
# Results vs. 3.11.0

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: fd95518
- commit date: 2023-04-26
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                                         |
| chameleon      | 6.47 ms                                                | 7.01 ms: 1.08x slower                                                        |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                       |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                        |
| tornado_http   | 96.3 ms                                                | 106 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.5 ms: 1.05x faster                                                        |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| float          | 77.2 ms                                                | 81.1 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.49 ms: 1.15x faster                                                        |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                                         |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                        |
| regex_compile  | 138 ms                                                 | 143 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.92 ms: 1.27x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                                         |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                        |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                                         |
| unpickle             | 13.7 us                                                | 14.7 us: 1.07x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 58.8 ms: 1.09x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.52 us: 1.10x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.13 ms: 1.07x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                | 22.8 ms: 1.06x slower                                                        |
| django_template | 32.6 ms                                                | 34.7 ms: 1.06x slower                                                        |
| mako            | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.2 ms: 2.35x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.82x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.92 ms: 1.27x faster                                                        |
| mypy2                   | 420 ms                                                 | 349 ms: 1.20x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.49 ms: 1.15x faster                                                        |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 216 us: 1.06x faster                                                         |
| richards                | 45.7 ms                                                | 43.4 ms: 1.05x faster                                                        |
| nbody                   | 93.1 ms                                                | 88.5 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| nqueens                 | 83.4 ms                                                | 79.8 ms: 1.04x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.53 ms: 1.04x faster                                                        |
| hexiom                  | 6.37 ms                                                | 6.13 ms: 1.04x faster                                                        |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                                         |
| json_loads              | 26.5 us                                                | 25.6 us: 1.03x faster                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                         |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| logging_silent          | 101 ns                                                 | 99.0 ns: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                       |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                         |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.99 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                       |
| raytrace                | 297 ms                                                 | 300 ms: 1.01x slower                                                         |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                        |
| regex_dna               | 204 ms                                                 | 207 ms: 1.01x slower                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.51 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.01x slower                                                         |
| html5lib                | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                        |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                        |
| bench_thread_pool       | 819 us                                                 | 835 us: 1.02x slower                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 54.3 ms: 1.02x slower                                                        |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                        |
| pickle_pure_python      | 306 us                                                 | 315 us: 1.03x slower                                                         |
| pprint_safe_repr        | 701 ms                                                 | 724 ms: 1.03x slower                                                         |
| logging_simple          | 6.03 us                                                | 6.22 us: 1.03x slower                                                        |
| scimark_sor             | 118 ms                                                 | 122 ms: 1.03x slower                                                         |
| sqlglot_normalize       | 108 ms                                                 | 112 ms: 1.03x slower                                                         |
| async_tree_memoization  | 627 ms                                                 | 650 ms: 1.04x slower                                                         |
| docutils                | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                       |
| regex_compile           | 138 ms                                                 | 143 ms: 1.04x slower                                                         |
| deepcopy_memo           | 37.0 us                                                | 38.5 us: 1.04x slower                                                        |
| 2to3                    | 259 ms                                                 | 269 ms: 1.04x slower                                                         |
| logging_format          | 6.68 us                                                | 6.96 us: 1.04x slower                                                        |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                        |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 71.3 ms: 1.05x slower                                                        |
| spectral_norm           | 100 ms                                                 | 105 ms: 1.05x slower                                                         |
| telco                   | 6.58 ms                                                | 6.90 ms: 1.05x slower                                                        |
| sympy_expand            | 475 ms                                                 | 498 ms: 1.05x slower                                                         |
| float                   | 77.2 ms                                                | 81.1 ms: 1.05x slower                                                        |
| meteor_contest          | 107 ms                                                 | 112 ms: 1.05x slower                                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.05x slower                                                         |
| genshi_text             | 21.6 ms                                                | 22.8 ms: 1.06x slower                                                        |
| thrift                  | 756 us                                                 | 800 us: 1.06x slower                                                         |
| dulwich_log             | 63.7 ms                                                | 67.8 ms: 1.06x slower                                                        |
| django_template         | 32.6 ms                                                | 34.7 ms: 1.06x slower                                                        |
| pyflate                 | 418 ms                                                 | 446 ms: 1.07x slower                                                         |
| deepcopy                | 342 us                                                 | 366 us: 1.07x slower                                                         |
| python_startup          | 8.52 ms                                                | 9.13 ms: 1.07x slower                                                        |
| scimark_fft             | 328 ms                                                 | 352 ms: 1.07x slower                                                         |
| mako                    | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                        |
| sympy_str               | 290 ms                                                 | 311 ms: 1.07x slower                                                         |
| sqlite_synth            | 2.52 us                                                | 2.71 us: 1.07x slower                                                        |
| unpickle                | 13.7 us                                                | 14.7 us: 1.07x slower                                                        |
| crypto_pyaes            | 74.7 ms                                                | 80.5 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.85 ms: 1.08x slower                                                        |
| chameleon               | 6.47 ms                                                | 7.01 ms: 1.08x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.19 us: 1.08x slower                                                        |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.5 ms: 1.09x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 58.8 ms: 1.09x slower                                                        |
| tornado_http            | 96.3 ms                                                | 106 ms: 1.10x slower                                                         |
| pickle_list             | 4.11 us                                                | 4.52 us: 1.10x slower                                                        |
| sympy_sum               | 167 ms                                                 | 183 ms: 1.10x slower                                                         |
| xml_etree_generate      | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                        |
| async_generators        | 368 ms                                                 | 437 ms: 1.19x slower                                                         |
| unpack_sequence         | 43.1 ns                                                | 54.1 ns: 1.25x slower                                                        |
| dask                    | 360 ms                                                 | 539 ms: 1.50x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (10): json, genshi_xml, bench_mp_pool, chaos, unpickle_list, async_tree_none, coverage, scimark_lu, pylint, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
