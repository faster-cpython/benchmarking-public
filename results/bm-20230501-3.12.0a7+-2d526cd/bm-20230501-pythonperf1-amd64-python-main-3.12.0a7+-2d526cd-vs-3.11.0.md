
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| html5lib       | 37.5 ms                                                     | 36.1 ms: 1.04x faster                                       |
| tornado_http   | 91.8 ms                                                     | 87.3 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.2 ms: 1.05x faster                                       |
| nbody          | 70.0 ms                                                     | 67.3 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.55 ms: 1.36x faster                                       |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.13x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                       |
| pickle_pure_python   | 200 us                                                      | 191 us: 1.04x faster                                        |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                       |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.6 ms: 1.04x slower                                       |
| pickle               | 6.61 us                                                     | 7.02 us: 1.06x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                       |
| unpickle             | 8.09 us                                                     | 8.73 us: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.80 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| python_startup         | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml     | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                       |
| genshi_text    | 17.0 ms                                                     | 14.9 ms: 1.13x faster                                       |
| mako           | 7.26 ms                                                     | 6.67 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 21.6 ms: 1.57x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 463 ms: 1.51x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.55 ms: 1.36x faster                                       |
| deltablue               | 2.61 ms                                                     | 2.12 ms: 1.23x faster                                       |
| sqlglot_parse           | 952 us                                                      | 791 us: 1.20x faster                                        |
| richards                | 30.6 ms                                                     | 25.6 ms: 1.19x faster                                       |
| unpack_sequence         | 46.1 ns                                                     | 38.7 ns: 1.19x faster                                       |
| mdp                     | 1.67 sec                                                    | 1.43 sec: 1.16x faster                                      |
| logging_silent          | 69.8 ns                                                     | 60.2 ns: 1.16x faster                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.01 ms: 1.16x faster                                       |
| genshi_xml              | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                       |
| genshi_text             | 17.0 ms                                                     | 14.9 ms: 1.13x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 135 us: 1.13x faster                                        |
| go                      | 97.3 ms                                                     | 86.6 ms: 1.12x faster                                       |
| hexiom                  | 4.55 ms                                                     | 4.06 ms: 1.12x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 56.8 ms: 1.12x faster                                       |
| raytrace                | 211 ms                                                      | 191 ms: 1.10x faster                                        |
| mako                    | 7.26 ms                                                     | 6.67 ms: 1.09x faster                                       |
| json                    | 3.25 ms                                                     | 3.02 ms: 1.08x faster                                       |
| async_tree_none         | 320 ms                                                      | 297 ms: 1.08x faster                                        |
| async_tree_io           | 779 ms                                                      | 724 ms: 1.08x faster                                        |
| nqueens                 | 64.9 ms                                                     | 60.6 ms: 1.07x faster                                       |
| coverage                | 55.9 ms                                                     | 52.3 ms: 1.07x faster                                       |
| mypy2                   | 229 ms                                                      | 215 ms: 1.07x faster                                        |
| async_tree_memoization  | 371 ms                                                      | 350 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 473 ms: 1.06x faster                                        |
| regex_compile           | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                       |
| chaos                   | 47.1 ms                                                     | 44.6 ms: 1.06x faster                                       |
| deepcopy_memo           | 25.2 us                                                     | 23.9 us: 1.05x faster                                       |
| tornado_http            | 91.8 ms                                                     | 87.3 ms: 1.05x faster                                       |
| deepcopy                | 246 us                                                      | 233 us: 1.05x faster                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                       |
| fannkuch                | 252 ms                                                      | 240 ms: 1.05x faster                                        |
| xml_etree_parse         | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                       |
| float                   | 54.6 ms                                                     | 52.2 ms: 1.05x faster                                       |
| pickle_pure_python      | 200 us                                                      | 191 us: 1.04x faster                                        |
| dulwich_log             | 44.5 ms                                                     | 42.7 ms: 1.04x faster                                       |
| nbody                   | 70.0 ms                                                     | 67.3 ms: 1.04x faster                                       |
| html5lib                | 37.5 ms                                                     | 36.1 ms: 1.04x faster                                       |
| pycparser               | 691 ms                                                      | 665 ms: 1.04x faster                                        |
| spectral_norm           | 67.9 ms                                                     | 65.4 ms: 1.04x faster                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 33.8 ms: 1.03x faster                                       |
| pyflate                 | 304 ms                                                      | 295 ms: 1.03x faster                                        |
| bench_thread_pool       | 852 us                                                      | 827 us: 1.03x faster                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| coroutines              | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                       |
| sqlglot_normalize       | 190 ms                                                      | 185 ms: 1.03x faster                                        |
| create_gc_cycles        | 693 us                                                      | 675 us: 1.03x faster                                        |
| pickle_dict             | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| python_startup          | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                       |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| logging_format          | 7.01 us                                                     | 6.89 us: 1.02x faster                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.02 sec: 1.01x faster                                      |
| comprehensions          | 15.9 us                                                     | 15.7 us: 1.01x faster                                       |
| logging_simple          | 6.61 us                                                     | 6.52 us: 1.01x faster                                       |
| pprint_safe_repr        | 512 ms                                                      | 505 ms: 1.01x faster                                        |
| 2to3                    | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 45.1 ms: 1.01x slower                                       |
| crypto_pyaes            | 47.6 ms                                                     | 48.1 ms: 1.01x slower                                       |
| regex_dna               | 115 ms                                                      | 117 ms: 1.01x slower                                        |
| sqlite_synth            | 1.68 us                                                     | 1.71 us: 1.02x slower                                       |
| xml_etree_process       | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                       |
| meteor_contest          | 74.7 ms                                                     | 77.0 ms: 1.03x slower                                       |
| json_loads              | 12.9 us                                                     | 13.3 us: 1.03x slower                                       |
| thrift                  | 491 us                                                      | 508 us: 1.03x slower                                        |
| telco                   | 3.90 ms                                                     | 4.07 ms: 1.04x slower                                       |
| xml_etree_generate      | 52.2 ms                                                     | 54.6 ms: 1.04x slower                                       |
| scimark_sor             | 75.6 ms                                                     | 79.1 ms: 1.05x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                       |
| pickle                  | 6.61 us                                                     | 7.02 us: 1.06x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.85 us: 1.06x slower                                       |
| bench_mp_pool           | 62.5 ms                                                     | 67.2 ms: 1.08x slower                                       |
| unpickle                | 8.09 us                                                     | 8.73 us: 1.08x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.80 us: 1.10x slower                                       |
| pathlib                 | 71.4 ms                                                     | 83.1 ms: 1.16x slower                                       |
| async_generators        | 178 ms                                                      | 227 ms: 1.28x slower                                        |
| dask                    | 264 ms                                                      | 360 ms: 1.36x slower                                        |
| Geometric mean          | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (5): docutils, deepcopy_reduce, gc_traversal, scimark_fft, pidigits
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
