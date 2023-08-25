
# Results vs. 3.11.0

- fork: python
- ref: 044bcc1771fe7e2f8eba
- machine: windows-amd64
- commit hash: 044bcc1
- commit date: 2022-11-04
- overall geometric mean: 1.00x slower \*
- HPT reliability: 92.48%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 207 ms: 1.01x faster                                                        |
| chameleon      | 5.11 ms                                                     | 5.21 ms: 1.02x slower                                                       |
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                                      |
| html5lib       | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 65.2 ms: 1.07x faster                                                       |
| pidigits       | 148 ms                                                      | 149 ms: 1.00x slower                                                        |
| float          | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.9 ms: 1.04x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.56 ms: 1.36x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 89.9 ms: 1.07x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 143 us: 1.06x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle_pure_python   | 200 us                                                      | 205 us: 1.03x slower                                                        |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.63 us: 1.03x slower                                                       |
| pickle               | 6.61 us                                                     | 6.92 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 66.0 ms: 1.06x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.89 us: 1.08x slower                                                       |
| unpickle             | 8.09 us                                                     | 9.31 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 22.9 ms: 1.05x faster                                                       |
| mako            | 7.26 ms                                                     | 7.05 ms: 1.03x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 7.56 ms                                                     | 5.56 ms: 1.36x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 38.9 ns: 1.18x faster                                                       |
| pylint                  | 326 ms                                                      | 286 ms: 1.14x faster                                                        |
| json                    | 3.25 ms                                                     | 2.94 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.39 ms: 1.07x faster                                                       |
| nbody                   | 70.0 ms                                                     | 65.2 ms: 1.07x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.9 ms: 1.07x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 143 us: 1.06x faster                                                        |
| django_template         | 24.1 ms                                                     | 22.9 ms: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| regex_compile           | 90.6 ms                                                     | 86.9 ms: 1.04x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 43.0 ms: 1.04x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.9 ms: 1.04x faster                                                       |
| raytrace                | 211 ms                                                      | 204 ms: 1.04x faster                                                        |
| mako                    | 7.26 ms                                                     | 7.05 ms: 1.03x faster                                                       |
| coverage                | 55.9 ms                                                     | 54.4 ms: 1.03x faster                                                       |
| richards                | 30.6 ms                                                     | 29.8 ms: 1.03x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.44 ms: 1.03x faster                                                       |
| html5lib                | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                                       |
| pyflate                 | 304 ms                                                      | 298 ms: 1.02x faster                                                        |
| mypy2                   | 229 ms                                                      | 225 ms: 1.02x faster                                                        |
| go                      | 97.3 ms                                                     | 95.5 ms: 1.02x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.57 ms: 1.02x faster                                                       |
| fannkuch                | 252 ms                                                      | 248 ms: 1.02x faster                                                        |
| deepcopy                | 246 us                                                      | 242 us: 1.01x faster                                                        |
| create_gc_cycles        | 693 us                                                      | 683 us: 1.01x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 62.9 ms: 1.01x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                                      |
| 2to3                    | 209 ms                                                      | 207 ms: 1.01x faster                                                        |
| sympy_str               | 182 ms                                                      | 180 ms: 1.01x faster                                                        |
| thrift                  | 491 us                                                      | 487 us: 1.01x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 149 ms: 1.00x slower                                                        |
| telco                   | 3.90 ms                                                     | 3.94 ms: 1.01x slower                                                       |
| scimark_sor             | 75.6 ms                                                     | 76.2 ms: 1.01x slower                                                       |
| xml_etree_process       | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                                       |
| deepcopy_memo           | 25.2 us                                                     | 25.4 us: 1.01x slower                                                       |
| sqlglot_parse           | 952 us                                                      | 961 us: 1.01x slower                                                        |
| docutils                | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                                      |
| sympy_expand            | 295 ms                                                      | 299 ms: 1.01x slower                                                        |
| meteor_contest          | 74.7 ms                                                     | 75.9 ms: 1.02x slower                                                       |
| chameleon               | 5.11 ms                                                     | 5.21 ms: 1.02x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.7 ms: 1.02x slower                                                       |
| dask                    | 264 ms                                                      | 269 ms: 1.02x slower                                                        |
| logging_silent          | 69.8 ns                                                     | 71.3 ns: 1.02x slower                                                       |
| float                   | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 514 ms: 1.03x slower                                                        |
| regex_v8                | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                                       |
| bench_thread_pool       | 852 us                                                      | 875 us: 1.03x slower                                                        |
| pickle_pure_python      | 200 us                                                      | 205 us: 1.03x slower                                                        |
| logging_format          | 7.01 us                                                     | 7.21 us: 1.03x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.50 ms: 1.03x slower                                                       |
| async_tree_io           | 779 ms                                                      | 803 ms: 1.03x slower                                                        |
| genshi_text             | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| async_generators        | 178 ms                                                      | 183 ms: 1.03x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.63 us: 1.03x slower                                                       |
| chaos                   | 47.1 ms                                                     | 48.8 ms: 1.04x slower                                                       |
| coroutines              | 14.6 ms                                                     | 15.2 ms: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.4 ms: 1.04x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 49.7 ms: 1.05x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 732 ms: 1.05x slower                                                        |
| pickle                  | 6.61 us                                                     | 6.92 us: 1.05x slower                                                       |
| async_tree_none         | 320 ms                                                      | 336 ms: 1.05x slower                                                        |
| scimark_fft             | 178 ms                                                      | 188 ms: 1.06x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 66.0 ms: 1.06x slower                                                       |
| regex_dna               | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.06x slower                                                       |
| generators              | 33.8 ms                                                     | 36.1 ms: 1.07x slower                                                       |
| spectral_norm           | 67.9 ms                                                     | 72.7 ms: 1.07x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.89 us: 1.08x slower                                                       |
| comprehensions          | 15.9 us                                                     | 17.2 us: 1.08x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 403 ms: 1.09x slower                                                        |
| unpickle                | 8.09 us                                                     | 9.31 us: 1.15x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (14): python_startup, pprint_safe_repr, python_startup_no_site, nqueens, sqlglot_normalize, logging_simple, xml_etree_generate, sqlglot_transpile, sympy_sum, sqlglot_optimize, deepcopy_reduce, tornado_http, genshi_xml, pycparser
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 92.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
