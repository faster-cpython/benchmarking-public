
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 2f67464
- commit date: 2023-05-03
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.28%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 270 ms: 1.04x slower                                                        |
| docutils       | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                      |
| tornado_http   | 96.3 ms                                                | 99.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                       |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| float          | 77.2 ms                                                | 81.9 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                       |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                       |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                        |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                        |
| json_loads           | 26.5 us                                                | 26.0 us: 1.02x faster                                                       |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 306 us                                                 | 318 us: 1.04x slower                                                        |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.48 us: 1.09x slower                                                       |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 60.4 ms: 1.12x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 86.3 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.16 ms: 1.07x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.0 ms: 2.37x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                       |
| mypy2                   | 420 ms                                                 | 354 ms: 1.19x faster                                                        |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                       |
| async_tree_none         | 526 ms                                                 | 500 ms: 1.05x faster                                                        |
| async_tree_io           | 1.30 sec                                               | 1.24 sec: 1.05x faster                                                      |
| nbody                   | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.35 ms: 1.04x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 219 us: 1.04x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 153 ms: 1.03x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.57 ms: 1.03x faster                                                       |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 722 ms: 1.02x faster                                                        |
| fannkuch                | 388 ms                                                 | 379 ms: 1.02x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.94 ms: 1.02x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                       |
| async_tree_memoization  | 627 ms                                                 | 615 ms: 1.02x faster                                                        |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                        |
| json_loads              | 26.5 us                                                | 26.0 us: 1.02x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.30 ms: 1.01x faster                                                       |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.01x slower                                                       |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| json                    | 4.94 ms                                                | 4.98 ms: 1.01x slower                                                       |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                       |
| bench_thread_pool       | 819 us                                                 | 833 us: 1.02x slower                                                        |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.02x slower                                                       |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                        |
| regex_dna               | 204 ms                                                 | 209 ms: 1.02x slower                                                        |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                        |
| raytrace                | 297 ms                                                 | 306 ms: 1.03x slower                                                        |
| pickle_dict             | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| tornado_http            | 96.3 ms                                                | 99.8 ms: 1.04x slower                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.51 sec: 1.04x slower                                                      |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                        |
| pickle_pure_python      | 306 us                                                 | 318 us: 1.04x slower                                                        |
| 2to3                    | 259 ms                                                 | 270 ms: 1.04x slower                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 55.4 ms: 1.04x slower                                                       |
| logging_simple          | 6.03 us                                                | 6.31 us: 1.05x slower                                                       |
| sqlglot_normalize       | 108 ms                                                 | 113 ms: 1.05x slower                                                        |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                       |
| docutils                | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                      |
| deepcopy_memo           | 37.0 us                                                | 38.8 us: 1.05x slower                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.74 ms: 1.05x slower                                                       |
| pprint_safe_repr        | 701 ms                                                 | 740 ms: 1.05x slower                                                        |
| mako                    | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                       |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| logging_format          | 6.68 us                                                | 7.08 us: 1.06x slower                                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                                        |
| float                   | 77.2 ms                                                | 81.9 ms: 1.06x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.68 us: 1.07x slower                                                       |
| dulwich_log             | 63.7 ms                                                | 68.0 ms: 1.07x slower                                                       |
| telco                   | 6.58 ms                                                | 7.05 ms: 1.07x slower                                                       |
| pickle                  | 10.1 us                                                | 10.8 us: 1.07x slower                                                       |
| deepcopy                | 342 us                                                 | 367 us: 1.07x slower                                                        |
| python_startup          | 8.52 ms                                                | 9.16 ms: 1.07x slower                                                       |
| scimark_fft             | 328 ms                                                 | 353 ms: 1.08x slower                                                        |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.3 ms: 1.08x slower                                                       |
| pyflate                 | 418 ms                                                 | 450 ms: 1.08x slower                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 73.4 ms: 1.08x slower                                                       |
| crypto_pyaes            | 74.7 ms                                                | 80.5 ms: 1.08x slower                                                       |
| spectral_norm           | 100 ms                                                 | 108 ms: 1.08x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.48 us: 1.09x slower                                                       |
| deepcopy_reduce         | 2.94 us                                                | 3.23 us: 1.10x slower                                                       |
| unpickle                | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 60.4 ms: 1.12x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 86.3 ms: 1.13x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 50.0 ns: 1.16x slower                                                       |
| async_generators        | 368 ms                                                 | 455 ms: 1.23x slower                                                        |
| dask                    | 360 ms                                                 | 542 ms: 1.51x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (7): richards, nqueens, bench_mp_pool, xml_etree_iterparse, mdp, chaos, logging_silent
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.28% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
