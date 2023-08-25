
# Results vs. 3.11.0

- fork: python
- ref: 3dd6ee2c0022cb49e5cb
- machine: windows-amd64
- commit hash: 3dd6ee2
- commit date: 2022-11-11
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 36.8 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 64.7 ms: 1.08x faster                                                       |
| float          | 54.6 ms                                                     | 50.8 ms: 1.08x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.4 ms: 1.07x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.19 ms: 1.46x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 131 us: 1.16x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 88.9 ms: 1.08x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 189 us: 1.06x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| unpickle             | 8.09 us                                                     | 8.01 us: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.65 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 6.90 us: 1.04x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.4 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.8 ms: 1.15x faster                                                       |
| mako            | 7.26 ms                                                     | 6.37 ms: 1.14x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 33.2 ms: 1.12x faster                                                       |
| django_template | 24.1 ms                                                     | 22.4 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1+-3dd6ee2 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 30.6 ns: 1.51x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.19 ms: 1.46x faster                                                       |
| json                    | 3.25 ms                                                     | 2.70 ms: 1.21x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 131 us: 1.16x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 60.7 ns: 1.15x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.8 ms: 1.15x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.37 ms: 1.14x faster                                                       |
| richards                | 30.6 ms                                                     | 26.8 ms: 1.14x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.29 ms: 1.14x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.6 ms: 1.13x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 33.2 ms: 1.12x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 22.6 us: 1.11x faster                                                       |
| raytrace                | 211 ms                                                      | 190 ms: 1.11x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 57.6 ms: 1.10x faster                                                       |
| deepcopy                | 246 us                                                      | 223 us: 1.10x faster                                                        |
| go                      | 97.3 ms                                                     | 88.3 ms: 1.10x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.15 ms: 1.10x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| pyflate                 | 304 ms                                                      | 280 ms: 1.09x faster                                                        |
| nbody                   | 70.0 ms                                                     | 64.7 ms: 1.08x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 69.9 ms: 1.08x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 88.9 ms: 1.08x faster                                                       |
| float                   | 54.6 ms                                                     | 50.8 ms: 1.08x faster                                                       |
| fannkuch                | 252 ms                                                      | 235 ms: 1.07x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 84.4 ms: 1.07x faster                                                       |
| django_template         | 24.1 ms                                                     | 22.4 ms: 1.07x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.93 us: 1.07x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 478 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.40 ms: 1.07x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 178 ms: 1.07x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 63.6 ms: 1.07x faster                                                       |
| pycparser               | 691 ms                                                      | 653 ms: 1.06x faster                                                        |
| pickle_pure_python      | 200 us                                                      | 189 us: 1.06x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| scimark_fft             | 178 ms                                                      | 169 ms: 1.06x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 33.0 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 985 ms: 1.06x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.10 ms: 1.05x faster                                                       |
| sympy_str               | 182 ms                                                      | 174 ms: 1.05x faster                                                        |
| sqlglot_parse           | 952 us                                                      | 908 us: 1.05x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.4 ms: 1.05x faster                                                       |
| chaos                   | 47.1 ms                                                     | 45.1 ms: 1.05x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 71.5 ms: 1.05x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| mypy2                   | 229 ms                                                      | 221 ms: 1.04x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.40 us: 1.03x faster                                                       |
| sympy_expand            | 295 ms                                                      | 286 ms: 1.03x faster                                                        |
| 2to3                    | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.85 us: 1.02x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.83 ms: 1.02x faster                                                       |
| html5lib                | 37.5 ms                                                     | 36.8 ms: 1.02x faster                                                       |
| dask                    | 264 ms                                                      | 261 ms: 1.01x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 98.8 ms: 1.01x faster                                                       |
| thrift                  | 491 us                                                      | 486 us: 1.01x faster                                                        |
| unpickle                | 8.09 us                                                     | 8.01 us: 1.01x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.8 us: 1.01x faster                                                       |
| coverage                | 55.9 ms                                                     | 55.5 ms: 1.01x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.0 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.48 ms: 1.01x slower                                                       |
| coroutines              | 14.6 ms                                                     | 14.9 ms: 1.02x slower                                                       |
| async_generators        | 178 ms                                                      | 183 ms: 1.03x slower                                                        |
| async_tree_memoization  | 371 ms                                                      | 382 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 517 ms: 1.03x slower                                                        |
| async_tree_io           | 779 ms                                                      | 804 ms: 1.03x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 73.8 ms: 1.03x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.65 us: 1.04x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| async_tree_none         | 320 ms                                                      | 334 ms: 1.04x slower                                                        |
| pickle                  | 6.61 us                                                     | 6.90 us: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.05x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.4 us: 1.05x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 765 ms: 1.09x slower                                                        |
| generators              | 33.8 ms                                                     | 37.3 ms: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (6): python_startup_no_site, create_gc_cycles, bench_thread_pool, regex_v8, json_loads, tornado_http
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
