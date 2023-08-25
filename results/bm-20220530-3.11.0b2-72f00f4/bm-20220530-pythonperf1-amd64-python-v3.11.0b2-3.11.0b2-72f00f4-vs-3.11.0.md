
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: windows-amd64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 211 ms: 1.01x slower                                            |
| chameleon      | 5.11 ms                                                     | 5.59 ms: 1.09x slower                                           |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                          |
| html5lib       | 37.5 ms                                                     | 41.4 ms: 1.10x slower                                           |
| tornado_http   | 91.8 ms                                                     | 95.3 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.50 ms                                                     | 1.39 ms: 1.08x faster                                           |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                            |
| regex_v8       | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                           |
| regex_compile  | 90.6 ms                                                     | 97.0 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 17.4 us: 1.06x faster                                           |
| pickle_list          | 2.68 us                                                     | 2.64 us: 1.01x faster                                           |
| pickle               | 6.61 us                                                     | 6.74 us: 1.02x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 54.1 ms: 1.04x slower                                           |
| xml_etree_process    | 37.1 ms                                                     | 39.1 ms: 1.05x slower                                           |
| pickle_pure_python   | 200 us                                                      | 216 us: 1.08x slower                                            |
| unpickle_pure_python | 152 us                                                      | 164 us: 1.08x slower                                            |
| unpickle_list        | 2.55 us                                                     | 2.76 us: 1.08x slower                                           |
| json_dumps           | 7.56 ms                                                     | 8.21 ms: 1.09x slower                                           |
| json_loads           | 12.9 us                                                     | 14.1 us: 1.09x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 25.1 ms: 1.04x slower                                           |
| mako            | 7.26 ms                                                     | 7.62 ms: 1.05x slower                                           |
| genshi_text     | 17.0 ms                                                     | 17.9 ms: 1.06x slower                                           |
| genshi_xml      | 37.3 ms                                                     | 40.2 ms: 1.08x slower                                           |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| logging_simple          | 6.61 us                                                     | 5.94 us: 1.11x faster                                           |
| logging_format          | 7.01 us                                                     | 6.39 us: 1.10x faster                                           |
| regex_effbot            | 1.50 ms                                                     | 1.39 ms: 1.08x faster                                           |
| pickle_dict             | 18.5 us                                                     | 17.4 us: 1.06x faster                                           |
| unpack_sequence         | 46.1 ns                                                     | 44.3 ns: 1.04x faster                                           |
| create_gc_cycles        | 693 us                                                      | 675 us: 1.03x faster                                            |
| pickle_list             | 2.68 us                                                     | 2.64 us: 1.01x faster                                           |
| 2to3                    | 209 ms                                                      | 211 ms: 1.01x slower                                            |
| bench_mp_pool           | 62.5 ms                                                     | 63.3 ms: 1.01x slower                                           |
| raytrace                | 211 ms                                                      | 213 ms: 1.01x slower                                            |
| scimark_lu              | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                           |
| sqlite_synth            | 1.68 us                                                     | 1.71 us: 1.02x slower                                           |
| python_startup          | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                           |
| pickle                  | 6.61 us                                                     | 6.74 us: 1.02x slower                                           |
| async_tree_io           | 779 ms                                                      | 794 ms: 1.02x slower                                            |
| sqlalchemy_declarative  | 81.5 ms                                                     | 83.2 ms: 1.02x slower                                           |
| aiohttp                 | 899 us                                                      | 921 us: 1.02x slower                                            |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.5 ms: 1.03x slower                                           |
| sympy_sum               | 99.9 ms                                                     | 103 ms: 1.03x slower                                            |
| go                      | 97.3 ms                                                     | 100 ms: 1.03x slower                                            |
| sympy_integrate         | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                           |
| scimark_monte_carlo     | 44.6 ms                                                     | 46.0 ms: 1.03x slower                                           |
| pidigits                | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| pyflate                 | 304 ms                                                      | 314 ms: 1.03x slower                                            |
| richards                | 30.6 ms                                                     | 31.6 ms: 1.03x slower                                           |
| logging_silent          | 69.8 ns                                                     | 72.2 ns: 1.03x slower                                           |
| docutils                | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                          |
| dulwich_log             | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                           |
| telco                   | 3.90 ms                                                     | 4.05 ms: 1.04x slower                                           |
| deepcopy_memo           | 25.2 us                                                     | 26.1 us: 1.04x slower                                           |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                            |
| xml_etree_generate      | 52.2 ms                                                     | 54.1 ms: 1.04x slower                                           |
| tornado_http            | 91.8 ms                                                     | 95.3 ms: 1.04x slower                                           |
| async_tree_cpu_io_mixed | 501 ms                                                      | 520 ms: 1.04x slower                                            |
| spectral_norm           | 67.9 ms                                                     | 70.6 ms: 1.04x slower                                           |
| django_template         | 24.1 ms                                                     | 25.1 ms: 1.04x slower                                           |
| deltablue               | 2.61 ms                                                     | 2.72 ms: 1.04x slower                                           |
| sympy_str               | 182 ms                                                      | 190 ms: 1.04x slower                                            |
| regex_v8                | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                           |
| bench_thread_pool       | 852 us                                                      | 889 us: 1.04x slower                                            |
| pathlib                 | 71.4 ms                                                     | 74.8 ms: 1.05x slower                                           |
| mako                    | 7.26 ms                                                     | 7.62 ms: 1.05x slower                                           |
| async_tree_none         | 320 ms                                                      | 336 ms: 1.05x slower                                            |
| mdp                     | 1.67 sec                                                    | 1.75 sec: 1.05x slower                                          |
| thrift                  | 491 us                                                      | 516 us: 1.05x slower                                            |
| meteor_contest          | 74.7 ms                                                     | 78.7 ms: 1.05x slower                                           |
| xml_etree_process       | 37.1 ms                                                     | 39.1 ms: 1.05x slower                                           |
| fannkuch                | 252 ms                                                      | 266 ms: 1.05x slower                                            |
| async_generators        | 178 ms                                                      | 187 ms: 1.05x slower                                            |
| genshi_text             | 17.0 ms                                                     | 17.9 ms: 1.06x slower                                           |
| generators              | 33.8 ms                                                     | 35.7 ms: 1.06x slower                                           |
| sympy_expand            | 295 ms                                                      | 312 ms: 1.06x slower                                            |
| scimark_sor             | 75.6 ms                                                     | 80.0 ms: 1.06x slower                                           |
| deepcopy_reduce         | 2.07 us                                                     | 2.19 us: 1.06x slower                                           |
| dask                    | 264 ms                                                      | 280 ms: 1.06x slower                                            |
| nqueens                 | 64.9 ms                                                     | 68.9 ms: 1.06x slower                                           |
| deepcopy                | 246 us                                                      | 261 us: 1.06x slower                                            |
| asyncio_tcp             | 699 ms                                                      | 742 ms: 1.06x slower                                            |
| hexiom                  | 4.55 ms                                                     | 4.84 ms: 1.06x slower                                           |
| sqlglot_normalize       | 190 ms                                                      | 203 ms: 1.06x slower                                            |
| coroutines              | 14.6 ms                                                     | 15.6 ms: 1.07x slower                                           |
| scimark_fft             | 178 ms                                                      | 191 ms: 1.07x slower                                            |
| pprint_safe_repr        | 512 ms                                                      | 548 ms: 1.07x slower                                            |
| pprint_pformat          | 1.04 sec                                                    | 1.11 sec: 1.07x slower                                          |
| regex_compile           | 90.6 ms                                                     | 97.0 ms: 1.07x slower                                           |
| sqlglot_optimize        | 34.9 ms                                                     | 37.5 ms: 1.07x slower                                           |
| async_tree_memoization  | 371 ms                                                      | 400 ms: 1.08x slower                                            |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.77 ms: 1.08x slower                                           |
| genshi_xml              | 37.3 ms                                                     | 40.2 ms: 1.08x slower                                           |
| pickle_pure_python      | 200 us                                                      | 216 us: 1.08x slower                                            |
| unpickle_pure_python    | 152 us                                                      | 164 us: 1.08x slower                                            |
| unpickle_list           | 2.55 us                                                     | 2.76 us: 1.08x slower                                           |
| pycparser               | 691 ms                                                      | 750 ms: 1.08x slower                                            |
| json_dumps              | 7.56 ms                                                     | 8.21 ms: 1.09x slower                                           |
| crypto_pyaes            | 47.6 ms                                                     | 51.8 ms: 1.09x slower                                           |
| json_loads              | 12.9 us                                                     | 14.1 us: 1.09x slower                                           |
| chameleon               | 5.11 ms                                                     | 5.59 ms: 1.09x slower                                           |
| chaos                   | 47.1 ms                                                     | 51.8 ms: 1.10x slower                                           |
| html5lib                | 37.5 ms                                                     | 41.4 ms: 1.10x slower                                           |
| comprehensions          | 15.9 us                                                     | 18.2 us: 1.14x slower                                           |
| sqlglot_transpile       | 1.16 ms                                                     | 1.42 ms: 1.22x slower                                           |
| sqlglot_parse           | 952 us                                                      | 1.21 ms: 1.27x slower                                           |
| mypy2                   | 229 ms                                                      | 295 ms: 1.29x slower                                            |
| coverage                | 55.9 ms                                                     | 106 ms: 1.89x slower                                            |
| Geometric mean          | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (9): xml_etree_iterparse, json, python_startup_no_site, unpickle, gc_traversal, float, nbody, xml_etree_parse, pylint
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x
