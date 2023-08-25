
# Results vs. 3.11.0

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: 7f90633
- commit date: 2023-04-28
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.04x slower                                                         |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                       |
| tornado_http   | 96.3 ms                                                | 105 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.2 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| float          | 77.2 ms                                                | 82.1 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                        |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                         |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.01x slower                                                        |
| regex_compile  | 138 ms                                                 | 143 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.2 ms: 1.24x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                                         |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| pickle_pure_python   | 306 us                                                 | 317 us: 1.04x slower                                                         |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                                        |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                        |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 84.2 ms: 1.11x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.70 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.08 ms: 1.07x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 50.8 ms: 1.02x faster                                                        |
| genshi_text    | 21.6 ms                                                | 22.7 ms: 1.05x slower                                                        |
| mako           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.1 ms: 2.37x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 508 ms: 1.81x faster                                                         |
| json_dumps              | 12.6 ms                                                | 10.2 ms: 1.24x faster                                                        |
| mypy2                   | 420 ms                                                 | 352 ms: 1.19x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                        |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                        |
| nbody                   | 93.1 ms                                                | 88.2 ms: 1.06x faster                                                        |
| richards                | 45.7 ms                                                | 43.4 ms: 1.05x faster                                                        |
| nqueens                 | 83.4 ms                                                | 79.3 ms: 1.05x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 217 us: 1.05x faster                                                         |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.53 ms: 1.04x faster                                                        |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                                         |
| logging_silent          | 101 ns                                                 | 98.2 ns: 1.03x faster                                                        |
| json_loads              | 26.5 us                                                | 25.8 us: 1.03x faster                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.66 ms: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| gc_traversal            | 4.02 ms                                                | 3.94 ms: 1.02x faster                                                        |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 50.8 ms: 1.02x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                       |
| json                    | 4.94 ms                                                | 4.88 ms: 1.01x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                       |
| chaos                   | 69.2 ms                                                | 68.8 ms: 1.00x faster                                                        |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                       |
| raytrace                | 297 ms                                                 | 301 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                         |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.01x slower                                                        |
| bench_thread_pool       | 819 us                                                 | 835 us: 1.02x slower                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 54.4 ms: 1.02x slower                                                        |
| pprint_safe_repr        | 701 ms                                                 | 721 ms: 1.03x slower                                                         |
| comprehensions          | 22.4 us                                                | 23.1 us: 1.03x slower                                                        |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                                         |
| logging_simple          | 6.03 us                                                | 6.24 us: 1.03x slower                                                        |
| logging_format          | 6.68 us                                                | 6.91 us: 1.03x slower                                                        |
| 2to3                    | 259 ms                                                 | 268 ms: 1.04x slower                                                         |
| pickle_pure_python      | 306 us                                                 | 317 us: 1.04x slower                                                         |
| regex_compile           | 138 ms                                                 | 143 ms: 1.04x slower                                                         |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                         |
| docutils                | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.69 ms: 1.04x slower                                                        |
| meteor_contest          | 107 ms                                                 | 112 ms: 1.05x slower                                                         |
| pickle_dict             | 31.1 us                                                | 32.6 us: 1.05x slower                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 71.3 ms: 1.05x slower                                                        |
| crypto_pyaes            | 74.7 ms                                                | 78.6 ms: 1.05x slower                                                        |
| genshi_text             | 21.6 ms                                                | 22.7 ms: 1.05x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 661 ms: 1.05x slower                                                         |
| deepcopy_memo           | 37.0 us                                                | 39.1 us: 1.06x slower                                                        |
| dulwich_log             | 63.7 ms                                                | 67.3 ms: 1.06x slower                                                        |
| pyflate                 | 418 ms                                                 | 444 ms: 1.06x slower                                                         |
| thrift                  | 756 us                                                 | 803 us: 1.06x slower                                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                                         |
| float                   | 77.2 ms                                                | 82.1 ms: 1.06x slower                                                        |
| python_startup          | 8.52 ms                                                | 9.08 ms: 1.07x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.69 us: 1.07x slower                                                        |
| deepcopy                | 342 us                                                 | 365 us: 1.07x slower                                                         |
| pickle                  | 10.1 us                                                | 10.8 us: 1.07x slower                                                        |
| telco                   | 6.58 ms                                                | 7.06 ms: 1.07x slower                                                        |
| mako                    | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.17 us: 1.08x slower                                                        |
| scimark_fft             | 328 ms                                                 | 355 ms: 1.08x slower                                                         |
| spectral_norm           | 100 ms                                                 | 108 ms: 1.08x slower                                                         |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.5 ms: 1.09x slower                                                        |
| tornado_http            | 96.3 ms                                                | 105 ms: 1.09x slower                                                         |
| xml_etree_process       | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                        |
| unpickle                | 13.7 us                                                | 14.9 us: 1.09x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 84.2 ms: 1.11x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.70 us: 1.14x slower                                                        |
| async_generators        | 368 ms                                                 | 439 ms: 1.19x slower                                                         |
| unpack_sequence         | 43.1 ns                                                | 52.1 ns: 1.21x slower                                                        |
| dask                    | 360 ms                                                 | 540 ms: 1.50x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (6): xml_etree_parse, async_tree_none, unpickle_list, bench_mp_pool, coverage, html5lib
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
