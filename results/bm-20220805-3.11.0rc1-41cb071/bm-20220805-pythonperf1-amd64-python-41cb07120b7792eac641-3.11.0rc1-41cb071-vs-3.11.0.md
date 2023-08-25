
# Results vs. 3.11.0

- fork: python
- ref: 41cb07120b7792eac641
- machine: windows-amd64
- commit hash: 41cb071
- commit date: 2022-08-05
- overall geometric mean: 1.01x faster \*
- HPT reliability: 98.32%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 5.05 ms: 1.01x faster                                                       |
| html5lib       | 37.5 ms                                                     | 38.4 ms: 1.02x slower                                                       |
| tornado_http   | 91.8 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.9 ms: 1.03x faster                                                       |
| nbody          | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 89.4 ms: 1.01x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list          | 2.68 us                                                     | 2.57 us: 1.04x faster                                                       |
| pickle               | 6.61 us                                                     | 6.44 us: 1.03x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 94.8 ms: 1.01x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 150 us: 1.01x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 36.7 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 52.6 ms: 1.01x slower                                                       |
| pickle_pure_python   | 200 us                                                      | 202 us: 1.01x slower                                                        |
| json_dumps           | 7.56 ms                                                     | 7.73 ms: 1.02x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.64 us: 1.04x slower                                                       |
| json_loads           | 12.9 us                                                     | 14.0 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): pickle_dict, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 23.7 ms: 1.02x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 16.7 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220805-pythonperf1-amd64-python-41cb07120b7792eac641-3.11.0rc1-41cb071 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                    | 3.25 ms                                                     | 2.94 ms: 1.11x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 41.9 ns: 1.10x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 659 ms: 1.06x faster                                                        |
| async_tree_io           | 779 ms                                                      | 739 ms: 1.05x faster                                                        |
| comprehensions          | 15.9 us                                                     | 15.2 us: 1.05x faster                                                       |
| aiohttp                 | 899 us                                                      | 861 us: 1.04x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.57 us: 1.04x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.6 ms: 1.04x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 665 us: 1.04x faster                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.40 ms: 1.04x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.37 us: 1.04x faster                                                       |
| raytrace                | 211 ms                                                      | 204 ms: 1.04x faster                                                        |
| async_tree_none         | 320 ms                                                      | 310 ms: 1.03x faster                                                        |
| float                   | 54.6 ms                                                     | 52.9 ms: 1.03x faster                                                       |
| 2to3                    | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| deepcopy                | 246 us                                                      | 238 us: 1.03x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 97.0 ms: 1.03x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 925 us: 1.03x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.13 ms: 1.03x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 43.3 ms: 1.03x faster                                                       |
| pickle                  | 6.61 us                                                     | 6.44 us: 1.03x faster                                                       |
| pylint                  | 326 ms                                                      | 318 ms: 1.03x faster                                                        |
| nbody                   | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.46 ms: 1.02x faster                                                       |
| fannkuch                | 252 ms                                                      | 247 ms: 1.02x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 73.3 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 491 ms: 1.02x faster                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 61.4 ms: 1.02x faster                                                       |
| thrift                  | 491 us                                                      | 482 us: 1.02x faster                                                        |
| python_startup          | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                       |
| sympy_expand            | 295 ms                                                      | 290 ms: 1.02x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.90 us: 1.02x faster                                                       |
| django_template         | 24.1 ms                                                     | 23.7 ms: 1.02x faster                                                       |
| pidigits                | 148 ms                                                      | 146 ms: 1.02x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 16.7 ms: 1.01x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 89.4 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 2.05 us: 1.01x faster                                                       |
| chameleon               | 5.11 ms                                                     | 5.05 ms: 1.01x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 94.8 ms: 1.01x faster                                                       |
| sympy_str               | 182 ms                                                      | 180 ms: 1.01x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 64.2 ms: 1.01x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 150 us: 1.01x faster                                                        |
| tornado_http            | 91.8 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 34.5 ms: 1.01x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 36.7 ms: 1.01x faster                                                       |
| async_generators        | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.87 ms: 1.01x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 189 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 44.4 ms: 1.01x faster                                                       |
| pyflate                 | 304 ms                                                      | 303 ms: 1.00x faster                                                        |
| bench_thread_pool       | 852 us                                                      | 856 us: 1.00x slower                                                        |
| deepcopy_memo           | 25.2 us                                                     | 25.3 us: 1.01x slower                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.04 sec: 1.01x slower                                                      |
| deltablue               | 2.61 ms                                                     | 2.63 ms: 1.01x slower                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 52.6 ms: 1.01x slower                                                       |
| coroutines              | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                                       |
| pickle_pure_python      | 200 us                                                      | 202 us: 1.01x slower                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.61 ms: 1.02x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 72.6 ms: 1.02x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.4 ms: 1.02x slower                                                       |
| scimark_sor             | 75.6 ms                                                     | 77.3 ms: 1.02x slower                                                       |
| scimark_fft             | 178 ms                                                      | 182 ms: 1.02x slower                                                        |
| html5lib                | 37.5 ms                                                     | 38.4 ms: 1.02x slower                                                       |
| json_dumps              | 7.56 ms                                                     | 7.73 ms: 1.02x slower                                                       |
| richards                | 30.6 ms                                                     | 31.3 ms: 1.02x slower                                                       |
| sqlalchemy_declarative  | 81.5 ms                                                     | 83.4 ms: 1.02x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 48.7 ms: 1.02x slower                                                       |
| logging_silent          | 69.8 ns                                                     | 71.9 ns: 1.03x slower                                                       |
| go                      | 97.3 ms                                                     | 101 ms: 1.03x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.64 us: 1.04x slower                                                       |
| chaos                   | 47.1 ms                                                     | 49.6 ms: 1.05x slower                                                       |
| spectral_norm           | 67.9 ms                                                     | 71.8 ms: 1.06x slower                                                       |
| regex_dna               | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| json_loads              | 12.9 us                                                     | 14.0 us: 1.09x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                                       |
| mypy2                   | 229 ms                                                      | 275 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (14): async_tree_memoization, docutils, pickle_dict, pycparser, sqlite_synth, mako, generators, flaskblogging, scimark_lu, unpickle, pprint_safe_repr, xml_etree_iterparse, dask, genshi_xml
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 98.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
