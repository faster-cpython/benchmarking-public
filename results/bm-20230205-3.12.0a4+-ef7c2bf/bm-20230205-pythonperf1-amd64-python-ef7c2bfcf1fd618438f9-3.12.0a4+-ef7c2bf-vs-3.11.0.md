
# Results vs. 3.11.0

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: windows-amd64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.59 ms: 1.11x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| html5lib       | 37.5 ms                                                     | 34.6 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 61.4 ms: 1.14x faster                                                       |
| float          | 54.6 ms                                                     | 50.4 ms: 1.08x faster                                                       |
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 77.6 ms: 1.17x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.14 ms: 1.47x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 122 us: 1.24x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 175 us: 1.14x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 87.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 34.5 ms: 1.08x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 49.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| pickle               | 6.61 us                                                     | 6.79 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.79 us: 1.10x slower                                                       |
| unpickle             | 8.09 us                                                     | 9.39 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (2): json_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 6.14 ms: 1.18x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 14.8 ms: 1.15x faster                                                       |
| django_template | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.8 ns: 1.72x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.14 ms: 1.47x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 481 ms: 1.45x faster                                                        |
| comprehensions          | 15.9 us                                                     | 12.3 us: 1.30x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.02 ms: 1.29x faster                                                       |
| richards                | 30.6 ms                                                     | 24.5 ms: 1.25x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 122 us: 1.24x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 57.2 ns: 1.22x faster                                                       |
| raytrace                | 211 ms                                                      | 174 ms: 1.21x faster                                                        |
| fannkuch                | 252 ms                                                      | 212 ms: 1.19x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.14 ms: 1.18x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.86 ms: 1.18x faster                                                       |
| json                    | 3.25 ms                                                     | 2.76 ms: 1.18x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.5 us: 1.17x faster                                                       |
| pyflate                 | 304 ms                                                      | 259 ms: 1.17x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 77.6 ms: 1.17x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 38.4 ms: 1.16x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 65.4 ms: 1.15x faster                                                       |
| chaos                   | 47.1 ms                                                     | 40.9 ms: 1.15x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.3 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                                       |
| deepcopy                | 246 us                                                      | 214 us: 1.15x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.8 ms: 1.15x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 175 us: 1.14x faster                                                        |
| nbody                   | 70.0 ms                                                     | 61.4 ms: 1.14x faster                                                       |
| go                      | 97.3 ms                                                     | 85.9 ms: 1.13x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 929 ms: 1.12x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 60.8 ms: 1.12x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.59 ms: 1.11x faster                                                       |
| sympy_str               | 182 ms                                                      | 164 ms: 1.11x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 462 ms: 1.11x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 57.5 ms: 1.10x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.51 sec: 1.10x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 12.5 ms: 1.10x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 40.6 ms: 1.10x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.89 us: 1.10x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 87.7 ms: 1.09x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 175 ms: 1.09x faster                                                        |
| html5lib                | 37.5 ms                                                     | 34.6 ms: 1.09x faster                                                       |
| float                   | 54.6 ms                                                     | 50.4 ms: 1.08x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 92.8 ms: 1.08x faster                                                       |
| scimark_fft             | 178 ms                                                      | 166 ms: 1.08x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 34.5 ms: 1.08x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.08 ms: 1.07x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.5 ms: 1.07x faster                                                       |
| thrift                  | 491 us                                                      | 457 us: 1.07x faster                                                        |
| sympy_expand            | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.19 us: 1.07x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 891 us: 1.07x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 44.5 ms: 1.07x faster                                                       |
| pycparser               | 691 ms                                                      | 648 ms: 1.07x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.58 us: 1.07x faster                                                       |
| mypy2                   | 229 ms                                                      | 217 ms: 1.06x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 71.1 ms: 1.05x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 49.9 ms: 1.05x faster                                                       |
| 2to3                    | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| regex_v8                | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.9 ms: 1.04x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.77 ms: 1.04x faster                                                       |
| async_tree_none         | 320 ms                                                      | 312 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 490 ms: 1.02x faster                                                        |
| async_generators        | 178 ms                                                      | 173 ms: 1.02x faster                                                        |
| bench_thread_pool       | 852 us                                                      | 836 us: 1.02x faster                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                                       |
| generators              | 33.8 ms                                                     | 34.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| pidigits                | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.79 us: 1.03x slower                                                       |
| regex_dna               | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| create_gc_cycles        | 693 us                                                      | 718 us: 1.04x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.1 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.79 us: 1.10x slower                                                       |
| unpickle                | 8.09 us                                                     | 9.39 us: 1.16x slower                                                       |
| dask                    | 264 ms                                                      | 353 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (8): python_startup_no_site, json_loads, async_tree_memoization, async_tree_io, python_startup, coroutines, tornado_http, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
