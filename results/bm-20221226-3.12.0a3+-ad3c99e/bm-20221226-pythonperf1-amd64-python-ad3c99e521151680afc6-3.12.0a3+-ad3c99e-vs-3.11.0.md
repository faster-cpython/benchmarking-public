
# Results vs. 3.11.0

- fork: python
- ref: ad3c99e521151680afc6
- machine: windows-amd64
- commit hash: ad3c99e
- commit date: 2022-12-26
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.02x faster                                                      |
| html5lib       | 37.5 ms                                                     | 34.7 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 51.1 ms: 1.07x faster                                                       |
| nbody          | 70.0 ms                                                     | 66.0 ms: 1.06x faster                                                       |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 83.8 ms: 1.08x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 125 ms: 1.09x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.43 ms: 1.39x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 127 us: 1.19x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 186 us: 1.08x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.62 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 7.29 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.6 ms: 1.16x faster                                                       |
| mako            | 7.26 ms                                                     | 6.35 ms: 1.14x faster                                                       |
| django_template | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 33.9 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 29.9 ns: 1.54x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 482 ms: 1.45x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.43 ms: 1.39x faster                                                       |
| json                    | 3.25 ms                                                     | 2.69 ms: 1.21x faster                                                       |
| richards                | 30.6 ms                                                     | 25.6 ms: 1.20x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 127 us: 1.19x faster                                                        |
| deltablue               | 2.61 ms                                                     | 2.25 ms: 1.16x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.6 ms: 1.16x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 60.9 ns: 1.15x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.35 ms: 1.14x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.9 ms: 1.14x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 22.6 us: 1.11x faster                                                       |
| raytrace                | 211 ms                                                      | 190 ms: 1.11x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 4.12 ms: 1.11x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| deepcopy                | 246 us                                                      | 223 us: 1.10x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 33.9 ms: 1.10x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 40.7 ms: 1.10x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.0 ms: 1.09x faster                                                       |
| pyflate                 | 304 ms                                                      | 279 ms: 1.09x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 62.4 ms: 1.09x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.7 ms: 1.08x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 83.8 ms: 1.08x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 59.0 ms: 1.08x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 186 us: 1.08x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 70.3 ms: 1.07x faster                                                       |
| float                   | 54.6 ms                                                     | 51.1 ms: 1.07x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                       |
| go                      | 97.3 ms                                                     | 91.7 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                                       |
| nbody                   | 70.0 ms                                                     | 66.0 ms: 1.06x faster                                                       |
| fannkuch                | 252 ms                                                      | 238 ms: 1.06x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 484 ms: 1.06x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 987 ms: 1.05x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.97 us: 1.05x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 181 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.4 ms: 1.05x faster                                                       |
| pycparser               | 691 ms                                                      | 661 ms: 1.05x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 42.6 ms: 1.05x faster                                                       |
| thrift                  | 491 us                                                      | 470 us: 1.04x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 71.8 ms: 1.04x faster                                                       |
| sympy_expand            | 295 ms                                                      | 284 ms: 1.04x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| chaos                   | 47.1 ms                                                     | 45.6 ms: 1.03x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| 2to3                    | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.80 ms: 1.03x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.84 us: 1.03x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.02x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 97.7 ms: 1.02x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 932 us: 1.02x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.7 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 492 ms: 1.02x faster                                                        |
| create_gc_cycles        | 693 us                                                      | 681 us: 1.02x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.51 us: 1.02x faster                                                       |
| sympy_str               | 182 ms                                                      | 180 ms: 1.01x faster                                                        |
| scimark_fft             | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| comprehensions          | 15.9 us                                                     | 16.0 us: 1.01x slower                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| async_tree_io           | 779 ms                                                      | 788 ms: 1.01x slower                                                        |
| async_generators        | 178 ms                                                      | 180 ms: 1.01x slower                                                        |
| coroutines              | 14.6 ms                                                     | 14.9 ms: 1.02x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 381 ms: 1.03x slower                                                        |
| pidigits                | 148 ms                                                      | 153 ms: 1.03x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.62 us: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.83 us: 1.06x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 76.4 ms: 1.07x slower                                                       |
| regex_dna               | 115 ms                                                      | 125 ms: 1.09x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.29 us: 1.10x slower                                                       |
| generators              | 33.8 ms                                                     | 37.8 ms: 1.12x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (8): dask, bench_thread_pool, mypy2, json_loads, bench_mp_pool, async_tree_none, xml_etree_iterparse, unpickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
