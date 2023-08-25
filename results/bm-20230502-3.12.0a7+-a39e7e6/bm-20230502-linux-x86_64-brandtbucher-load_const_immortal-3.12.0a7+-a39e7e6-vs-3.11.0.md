
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: a39e7e6
- commit date: 2023-05-02
- overall geometric mean: 1.01x slower \*
- HPT reliability: 94.91%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 270 ms: 1.04x slower                                                        |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                      |
| tornado_http   | 96.3 ms                                                | 99.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.3 ms: 1.03x faster                                                       |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| float          | 77.2 ms                                                | 81.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                       |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                                        |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                       |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.0 ms: 1.25x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 220 us: 1.04x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                       |
| json_loads           | 26.5 us                                                | 26.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| pickle_pure_python   | 306 us                                                 | 317 us: 1.04x slower                                                        |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                       |
| unpickle             | 13.7 us                                                | 14.7 us: 1.08x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 59.4 ms: 1.10x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 84.8 ms: 1.11x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.74 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 32.8 ms: 2.24x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                        |
| json_dumps              | 12.6 ms                                                | 10.0 ms: 1.25x faster                                                       |
| mypy2                   | 420 ms                                                 | 351 ms: 1.20x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                       |
| coroutines              | 25.5 ms                                                | 23.1 ms: 1.10x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.24 sec: 1.05x faster                                                      |
| async_tree_none         | 526 ms                                                 | 503 ms: 1.05x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 220 us: 1.04x faster                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.35 ms: 1.04x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.54 ms: 1.04x faster                                                       |
| nqueens                 | 83.4 ms                                                | 80.6 ms: 1.03x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.89 ms: 1.03x faster                                                       |
| nbody                   | 93.1 ms                                                | 90.3 ms: 1.03x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                        |
| richards                | 45.7 ms                                                | 44.6 ms: 1.03x faster                                                       |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                      |
| async_tree_memoization  | 627 ms                                                 | 615 ms: 1.02x faster                                                        |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 727 ms: 1.02x faster                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.02x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.27 ms: 1.02x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.58 sec: 1.01x faster                                                      |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                                       |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                        |
| json_loads              | 26.5 us                                                | 26.2 us: 1.01x faster                                                       |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                                        |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                                       |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                       |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                       |
| json                    | 4.94 ms                                                | 5.00 ms: 1.01x slower                                                       |
| deepcopy_memo           | 37.0 us                                                | 37.6 us: 1.01x slower                                                       |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                        |
| bench_thread_pool       | 819 us                                                 | 838 us: 1.02x slower                                                        |
| pathlib                 | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                       |
| raytrace                | 297 ms                                                 | 304 ms: 1.03x slower                                                        |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.50 sec: 1.03x slower                                                      |
| docutils                | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                      |
| pickle_pure_python      | 306 us                                                 | 317 us: 1.04x slower                                                        |
| tornado_http            | 96.3 ms                                                | 99.8 ms: 1.04x slower                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 55.3 ms: 1.04x slower                                                       |
| 2to3                    | 259 ms                                                 | 270 ms: 1.04x slower                                                        |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                       |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                                        |
| telco                   | 6.58 ms                                                | 6.94 ms: 1.05x slower                                                       |
| logging_simple          | 6.03 us                                                | 6.36 us: 1.05x slower                                                       |
| float                   | 77.2 ms                                                | 81.6 ms: 1.06x slower                                                       |
| regex_compile           | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| pprint_safe_repr        | 701 ms                                                 | 742 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.77 ms: 1.06x slower                                                       |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.06x slower                                                        |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                       |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.1 ms: 1.06x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.69 us: 1.07x slower                                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.07x slower                                                        |
| deepcopy                | 342 us                                                 | 366 us: 1.07x slower                                                        |
| logging_format          | 6.68 us                                                | 7.16 us: 1.07x slower                                                       |
| mako                    | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |
| dulwich_log             | 63.7 ms                                                | 68.3 ms: 1.07x slower                                                       |
| pyflate                 | 418 ms                                                 | 450 ms: 1.08x slower                                                        |
| unpickle                | 13.7 us                                                | 14.7 us: 1.08x slower                                                       |
| crypto_pyaes            | 74.7 ms                                                | 80.6 ms: 1.08x slower                                                       |
| python_startup          | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                       |
| scimark_fft             | 328 ms                                                 | 356 ms: 1.08x slower                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 73.8 ms: 1.09x slower                                                       |
| spectral_norm           | 100 ms                                                 | 109 ms: 1.09x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.21 us: 1.09x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 59.4 ms: 1.10x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 84.8 ms: 1.11x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.74 ms: 1.12x slower                                                       |
| pickle_list             | 4.11 us                                                | 4.62 us: 1.12x slower                                                       |
| async_generators        | 368 ms                                                 | 451 ms: 1.22x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 53.4 ns: 1.24x slower                                                       |
| dask                    | 360 ms                                                 | 542 ms: 1.51x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (3): logging_silent, xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 94.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
