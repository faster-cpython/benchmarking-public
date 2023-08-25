
# Results vs. 3.10.4

- fork: python
- ref: 2cd268a3a9340346dd86
- machine: windows-amd64
- commit hash: 2cd268a
- commit date: 2021-12-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 232 ms: 1.02x faster                                                     |
| docutils       | 1.89 sec                                                    | 1.88 sec: 1.01x faster                                                   |
| html5lib       | 46.5 ms                                                     | 48.7 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                                     |
| float          | 60.2 ms                                                     | 61.8 ms: 1.03x slower                                                    |
| nbody          | 69.3 ms                                                     | 77.2 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                       | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 129 ms: 1.02x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.74 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 9.17 us                                                     | 8.17 us: 1.12x faster                                                    |
| unpickle_list        | 2.81 us                                                     | 2.64 us: 1.07x faster                                                    |
| xml_etree_parse      | 102 ms                                                      | 98.0 ms: 1.04x faster                                                    |
| pickle               | 6.80 us                                                     | 6.84 us: 1.01x slower                                                    |
| xml_etree_generate   | 54.5 ms                                                     | 55.0 ms: 1.01x slower                                                    |
| xml_etree_process    | 43.4 ms                                                     | 44.0 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                                    |
| unpickle_pure_python | 171 us                                                      | 177 us: 1.03x slower                                                     |
| pickle_pure_python   | 257 us                                                      | 267 us: 1.04x slower                                                     |
| pickle_list          | 2.59 us                                                     | 2.70 us: 1.04x slower                                                    |
| json_loads           | 14.2 us                                                     | 15.0 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (2): json_dumps, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 15.1 ms: 1.03x faster                                                    |
| python_startup         | 20.0 ms                                                     | 19.7 ms: 1.02x faster                                                    |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 8.56 ms: 1.03x faster                                                    |
| genshi_xml      | 40.5 ms                                                     | 40.9 ms: 1.01x slower                                                    |
| genshi_text     | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                    |
| django_template | 28.2 ms                                                     | 29.2 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle                | 9.17 us                                                     | 8.17 us: 1.12x faster                                                    |
| unpickle_list           | 2.81 us                                                     | 2.64 us: 1.07x faster                                                    |
| xml_etree_parse         | 102 ms                                                      | 98.0 ms: 1.04x faster                                                    |
| async_tree_io           | 1.07 sec                                                    | 1.03 sec: 1.04x faster                                                   |
| coverage                | 40.0 ms                                                     | 38.8 ms: 1.03x faster                                                    |
| generators              | 31.6 ms                                                     | 30.7 ms: 1.03x faster                                                    |
| async_tree_memoization  | 497 ms                                                      | 484 ms: 1.03x faster                                                     |
| mako                    | 8.80 ms                                                     | 8.56 ms: 1.03x faster                                                    |
| python_startup_no_site  | 15.5 ms                                                     | 15.1 ms: 1.03x faster                                                    |
| scimark_lu              | 85.4 ms                                                     | 83.4 ms: 1.02x faster                                                    |
| nqueens                 | 67.0 ms                                                     | 65.5 ms: 1.02x faster                                                    |
| 2to3                    | 237 ms                                                      | 232 ms: 1.02x faster                                                     |
| pathlib                 | 77.4 ms                                                     | 75.9 ms: 1.02x faster                                                    |
| regex_dna               | 132 ms                                                      | 129 ms: 1.02x faster                                                     |
| hexiom                  | 5.52 ms                                                     | 5.42 ms: 1.02x faster                                                    |
| aiohttp                 | 1.01 ms                                                     | 990 us: 1.02x faster                                                     |
| python_startup          | 20.0 ms                                                     | 19.7 ms: 1.02x faster                                                    |
| create_gc_cycles        | 782 us                                                      | 770 us: 1.02x faster                                                     |
| pylint                  | 347 ms                                                      | 343 ms: 1.01x faster                                                     |
| sqlglot_parse           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                    |
| deltablue               | 4.17 ms                                                     | 4.13 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                                    |
| docutils                | 1.89 sec                                                    | 1.88 sec: 1.01x faster                                                   |
| comprehensions          | 16.0 us                                                     | 15.8 us: 1.01x faster                                                    |
| richards                | 41.2 ms                                                     | 40.9 ms: 1.01x faster                                                    |
| bench_mp_pool           | 60.7 ms                                                     | 60.4 ms: 1.00x faster                                                    |
| sqlglot_normalize       | 202 ms                                                      | 203 ms: 1.00x slower                                                     |
| mdp                     | 1.71 sec                                                    | 1.72 sec: 1.00x slower                                                   |
| pickle                  | 6.80 us                                                     | 6.84 us: 1.01x slower                                                    |
| sqlglot_optimize        | 39.0 ms                                                     | 39.2 ms: 1.01x slower                                                    |
| raytrace                | 271 ms                                                      | 273 ms: 1.01x slower                                                     |
| sqlite_synth            | 1.84 us                                                     | 1.85 us: 1.01x slower                                                    |
| deepcopy_memo           | 28.5 us                                                     | 28.7 us: 1.01x slower                                                    |
| chaos                   | 58.9 ms                                                     | 59.4 ms: 1.01x slower                                                    |
| genshi_xml              | 40.5 ms                                                     | 40.9 ms: 1.01x slower                                                    |
| scimark_fft             | 193 ms                                                      | 195 ms: 1.01x slower                                                     |
| xml_etree_generate      | 54.5 ms                                                     | 55.0 ms: 1.01x slower                                                    |
| logging_format          | 6.66 us                                                     | 6.72 us: 1.01x slower                                                    |
| meteor_contest          | 72.5 ms                                                     | 73.2 ms: 1.01x slower                                                    |
| go                      | 136 ms                                                      | 137 ms: 1.01x slower                                                     |
| scimark_sor             | 105 ms                                                      | 106 ms: 1.01x slower                                                     |
| xml_etree_process       | 43.4 ms                                                     | 44.0 ms: 1.01x slower                                                    |
| sympy_str               | 188 ms                                                      | 191 ms: 1.02x slower                                                     |
| thrift                  | 615 us                                                      | 625 us: 1.02x slower                                                     |
| xml_etree_iterparse     | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                                    |
| spectral_norm           | 78.0 ms                                                     | 79.4 ms: 1.02x slower                                                    |
| scimark_monte_carlo     | 55.9 ms                                                     | 56.9 ms: 1.02x slower                                                    |
| pyflate                 | 387 ms                                                      | 394 ms: 1.02x slower                                                     |
| bench_thread_pool       | 946 us                                                      | 965 us: 1.02x slower                                                     |
| telco                   | 3.78 ms                                                     | 3.86 ms: 1.02x slower                                                    |
| pprint_safe_repr        | 589 ms                                                      | 601 ms: 1.02x slower                                                     |
| gc_traversal            | 1.34 ms                                                     | 1.37 ms: 1.02x slower                                                    |
| dulwich_log             | 47.6 ms                                                     | 48.7 ms: 1.02x slower                                                    |
| pidigits                | 145 ms                                                      | 149 ms: 1.03x slower                                                     |
| genshi_text             | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                    |
| json                    | 3.05 ms                                                     | 3.13 ms: 1.03x slower                                                    |
| float                   | 60.2 ms                                                     | 61.8 ms: 1.03x slower                                                    |
| fannkuch                | 258 ms                                                      | 266 ms: 1.03x slower                                                     |
| pprint_pformat          | 1.21 sec                                                    | 1.24 sec: 1.03x slower                                                   |
| sqlalchemy_declarative  | 95.4 ms                                                     | 98.4 ms: 1.03x slower                                                    |
| django_template         | 28.2 ms                                                     | 29.2 ms: 1.03x slower                                                    |
| unpickle_pure_python    | 171 us                                                      | 177 us: 1.03x slower                                                     |
| sqlalchemy_imperative   | 11.0 ms                                                     | 11.4 ms: 1.04x slower                                                    |
| pickle_pure_python      | 257 us                                                      | 267 us: 1.04x slower                                                     |
| pickle_list             | 2.59 us                                                     | 2.70 us: 1.04x slower                                                    |
| regex_effbot            | 1.66 ms                                                     | 1.74 ms: 1.04x slower                                                    |
| dask                    | 305 ms                                                      | 319 ms: 1.05x slower                                                     |
| html5lib                | 46.5 ms                                                     | 48.7 ms: 1.05x slower                                                    |
| crypto_pyaes            | 62.3 ms                                                     | 65.5 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.80 ms: 1.05x slower                                                    |
| json_loads              | 14.2 us                                                     | 15.0 us: 1.06x slower                                                    |
| unpack_sequence         | 37.8 ns                                                     | 40.5 ns: 1.07x slower                                                    |
| nbody                   | 69.3 ms                                                     | 77.2 ms: 1.11x slower                                                    |
| Geometric mean          | (ref)                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (21): mypy2, pycparser, async_tree_none, chameleon, json_dumps, regex_compile, regex_v8, deepcopy, coroutines, deepcopy_reduce, async_generators, flaskblogging, asyncio_tcp, sympy_expand, tornado_http, sympy_sum, pickle_dict, sympy_integrate, logging_simple, async_tree_cpu_io_mixed, logging_silent
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 98.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
