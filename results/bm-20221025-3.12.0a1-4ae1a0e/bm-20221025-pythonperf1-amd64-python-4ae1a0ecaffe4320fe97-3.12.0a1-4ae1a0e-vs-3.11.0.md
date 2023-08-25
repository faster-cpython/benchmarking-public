
# Results vs. 3.11.0

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: windows-amd64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.99 ms: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 67.2 ms: 1.04x faster                                                      |
| float          | 54.6 ms                                                     | 53.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.3 ms: 1.05x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.62 ms: 1.35x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 86.8 ms: 1.10x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 143 us: 1.06x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.5 ms: 1.03x faster                                                      |
| pickle_pure_python   | 200 us                                                      | 196 us: 1.02x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                      |
| pickle_list          | 2.68 us                                                     | 2.64 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.60 us: 1.02x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.87 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 6.93 ms: 1.05x faster                                                      |
| django_template | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                      |
| genshi_text     | 17.0 ms                                                     | 17.1 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 7.56 ms                                                     | 5.62 ms: 1.35x faster                                                      |
| json                    | 3.25 ms                                                     | 2.77 ms: 1.17x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 86.8 ms: 1.10x faster                                                      |
| unpack_sequence         | 46.1 ns                                                     | 42.3 ns: 1.09x faster                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.37 ms: 1.09x faster                                                      |
| coverage                | 55.9 ms                                                     | 52.1 ms: 1.07x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 143 us: 1.06x faster                                                       |
| fannkuch                | 252 ms                                                      | 238 ms: 1.06x faster                                                       |
| mypy2                   | 229 ms                                                      | 218 ms: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| regex_compile           | 90.6 ms                                                     | 86.3 ms: 1.05x faster                                                      |
| mako                    | 7.26 ms                                                     | 6.93 ms: 1.05x faster                                                      |
| deepcopy                | 246 us                                                      | 235 us: 1.05x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 663 us: 1.04x faster                                                       |
| nbody                   | 70.0 ms                                                     | 67.2 ms: 1.04x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 71.8 ms: 1.04x faster                                                      |
| deltablue               | 2.61 ms                                                     | 2.51 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.04 sec                                                    | 1.00 sec: 1.04x faster                                                     |
| go                      | 97.3 ms                                                     | 93.8 ms: 1.04x faster                                                      |
| 2to3                    | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| raytrace                | 211 ms                                                      | 204 ms: 1.04x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 495 ms: 1.03x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 50.5 ms: 1.03x faster                                                      |
| pylint                  | 326 ms                                                      | 317 ms: 1.03x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 60.9 ms: 1.03x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.42 ms: 1.03x faster                                                      |
| chameleon               | 5.11 ms                                                     | 4.99 ms: 1.03x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| pyflate                 | 304 ms                                                      | 297 ms: 1.02x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 73.8 ms: 1.02x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 43.5 ms: 1.02x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.14 ms: 1.02x faster                                                      |
| float                   | 54.6 ms                                                     | 53.5 ms: 1.02x faster                                                      |
| pickle_pure_python      | 200 us                                                      | 196 us: 1.02x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 43.8 ms: 1.02x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 24.7 us: 1.02x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.64 us: 1.02x faster                                                      |
| comprehensions          | 15.9 us                                                     | 15.6 us: 1.02x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.85 ms: 1.02x faster                                                      |
| logging_silent          | 69.8 ns                                                     | 68.8 ns: 1.01x faster                                                      |
| async_tree_none         | 320 ms                                                      | 316 ms: 1.01x faster                                                       |
| chaos                   | 47.1 ms                                                     | 46.5 ms: 1.01x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 34.4 ms: 1.01x faster                                                      |
| django_template         | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 190 ms                                                      | 188 ms: 1.01x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 844 us: 1.01x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 98.9 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 2.05 us: 1.01x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 4.51 ms: 1.01x faster                                                      |
| thrift                  | 491 us                                                      | 486 us: 1.01x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 47.2 ms: 1.01x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 17.1 ms: 1.01x slower                                                      |
| nqueens                 | 64.9 ms                                                     | 65.4 ms: 1.01x slower                                                      |
| richards                | 30.6 ms                                                     | 31.0 ms: 1.01x slower                                                      |
| html5lib                | 37.5 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                                      |
| generators              | 33.8 ms                                                     | 34.5 ms: 1.02x slower                                                      |
| async_generators        | 178 ms                                                      | 181 ms: 1.02x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.60 us: 1.02x slower                                                      |
| coroutines              | 14.6 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| async_tree_memoization  | 371 ms                                                      | 381 ms: 1.03x slower                                                       |
| logging_simple          | 6.61 us                                                     | 6.80 us: 1.03x slower                                                      |
| regex_dna               | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.0 ms: 1.04x slower                                                      |
| logging_format          | 7.01 us                                                     | 7.28 us: 1.04x slower                                                      |
| scimark_lu              | 63.5 ms                                                     | 66.6 ms: 1.05x slower                                                      |
| json_loads              | 12.9 us                                                     | 13.5 us: 1.05x slower                                                      |
| scimark_fft             | 178 ms                                                      | 188 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 73.8 ms: 1.09x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                                      |
| unpickle                | 8.09 us                                                     | 8.87 us: 1.10x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (14): pickle_dict, pickle, asyncio_tcp, docutils, async_tree_io, tornado_http, sqlglot_parse, pidigits, dask, sympy_expand, sympy_str, async_tree_cpu_io_mixed, genshi_xml, pycparser
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
