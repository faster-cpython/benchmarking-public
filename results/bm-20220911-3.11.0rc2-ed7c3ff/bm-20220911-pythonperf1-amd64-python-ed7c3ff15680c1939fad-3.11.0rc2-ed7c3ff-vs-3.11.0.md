
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: windows-amd64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| docutils       | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 68.6 ms: 1.02x faster                                                       |
| float          | 54.6 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                                       |
| regex_compile  | 90.6 ms                                                     | 89.5 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 115 ms: 1.01x faster                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 8.09 us                                                     | 7.70 us: 1.05x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.6 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 149 us: 1.02x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.02x faster                                                        |
| pickle_list          | 2.68 us                                                     | 2.65 us: 1.01x faster                                                       |
| json_dumps           | 7.56 ms                                                     | 7.66 ms: 1.01x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 16.7 ms: 1.02x faster                                                       |
| django_template | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 38.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 42.7 ns: 1.08x faster                                                       |
| async_tree_io           | 779 ms                                                      | 740 ms: 1.05x faster                                                        |
| unpickle                | 8.09 us                                                     | 7.70 us: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.2 us: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| aiohttp                 | 899 us                                                      | 857 us: 1.05x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 91.6 ms: 1.05x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.12 ms: 1.04x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 667 us: 1.04x faster                                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.41 ms: 1.04x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 920 us: 1.04x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 2.00 us: 1.03x faster                                                       |
| 2to3                    | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| async_tree_none         | 320 ms                                                      | 310 ms: 1.03x faster                                                        |
| pylint                  | 326 ms                                                      | 316 ms: 1.03x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                                       |
| deepcopy                | 246 us                                                      | 239 us: 1.03x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 488 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 34.0 ms: 1.02x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 186 ms: 1.02x faster                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 61.2 ms: 1.02x faster                                                       |
| nbody                   | 70.0 ms                                                     | 68.6 ms: 1.02x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| pickle_dict             | 18.5 us                                                     | 18.2 us: 1.02x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 149 us: 1.02x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 98.2 ms: 1.02x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 16.7 ms: 1.02x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.48 ms: 1.02x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 197 us: 1.02x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 89.5 ms: 1.01x faster                                                       |
| float                   | 54.6 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| async_generators        | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| django_template         | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                       |
| pickle_list             | 2.68 us                                                     | 2.65 us: 1.01x faster                                                       |
| generators              | 33.8 ms                                                     | 33.5 ms: 1.01x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.57 us: 1.01x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 74.3 ms: 1.01x faster                                                       |
| regex_dna               | 115 ms                                                      | 115 ms: 1.01x faster                                                        |
| sympy_expand            | 295 ms                                                      | 294 ms: 1.01x faster                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.67 us: 1.00x faster                                                       |
| pyflate                 | 304 ms                                                      | 303 ms: 1.00x faster                                                        |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.3 ms: 1.01x slower                                                       |
| deepcopy_memo           | 25.2 us                                                     | 25.4 us: 1.01x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 72.1 ms: 1.01x slower                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.05 sec: 1.01x slower                                                      |
| json_dumps              | 7.56 ms                                                     | 7.66 ms: 1.01x slower                                                       |
| logging_silent          | 69.8 ns                                                     | 70.9 ns: 1.02x slower                                                       |
| coroutines              | 14.6 ms                                                     | 14.9 ms: 1.02x slower                                                       |
| fannkuch                | 252 ms                                                      | 256 ms: 1.02x slower                                                        |
| chaos                   | 47.1 ms                                                     | 48.0 ms: 1.02x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 48.5 ms: 1.02x slower                                                       |
| scimark_sor             | 75.6 ms                                                     | 77.3 ms: 1.02x slower                                                       |
| genshi_xml              | 37.3 ms                                                     | 38.3 ms: 1.03x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| scimark_fft             | 178 ms                                                      | 189 ms: 1.06x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| spectral_norm           | 67.9 ms                                                     | 73.2 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.81 ms: 1.09x slower                                                       |
| mypy2                   | 229 ms                                                      | 276 ms: 1.21x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (27): json, asyncio_tcp, pycparser, xml_etree_iterparse, html5lib, async_tree_memoization, mako, logging_format, chameleon, nqueens, bench_thread_pool, scimark_lu, scimark_monte_carlo, pickle, raytrace, flaskblogging, richards, telco, sympy_str, deltablue, unpickle_list, go, pprint_safe_repr, thrift, tornado_http, sqlalchemy_declarative, dask
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
