# Results vs. 3.13.0b2

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.01x faster
- HPT reliability: 88.12%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 231 ms: 1.12x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.76 sec: 1.08x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 86.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 518 ms: 1.17x faster                                                       |
| async_tree_io             | 588 ms                                                          | 522 ms: 1.13x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 249 ms: 1.06x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 52.7 ms: 1.28x faster                                                      |
| float          | 49.7 ms                                                         | 45.0 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 89.0 ms: 1.14x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 18.2 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.0 ms: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 132 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.4 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 43.7 ms: 1.38x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 523 us: 15.49x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.6 us: 1.42x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.2 ms: 1.41x faster                                                      |
| nbody                     | 67.6 ms                                                         | 52.7 ms: 1.28x faster                                                      |
| deepcopy                  | 220 us                                                          | 175 us: 1.25x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 518 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| scimark_fft               | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 522 ms: 1.13x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.78 us: 1.12x faster                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| float                     | 49.7 ms                                                         | 45.0 ms: 1.10x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| fannkuch                  | 243 ms                                                          | 226 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.39 sec: 1.07x faster                                                     |
| pyflate                   | 279 ms                                                          | 262 ms: 1.06x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 249 ms: 1.06x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.42 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.6 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                                      |
| pathlib                   | 75.9 ms                                                         | 74.3 ms: 1.02x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 465 ms: 1.02x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 957 ms: 1.01x faster                                                       |
| regex_dna                 | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| create_gc_cycles          | 888 us                                                          | 900 us: 1.01x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 37.0 ms: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| chaos                     | 38.4 ms                                                         | 39.3 ms: 1.03x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 798 us: 1.04x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 86.3 ms: 1.05x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.0 ms: 1.06x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 60.1 ms: 1.06x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 800 us: 1.07x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 69.4 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.02 ms: 1.07x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.4 ms: 1.07x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 56.9 ns: 1.07x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 35.4 ms: 1.08x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 132 us: 1.08x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.76 sec: 1.08x slower                                                     |
| sqlglot_normalize         | 173 ms                                                          | 188 ms: 1.08x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 92.2 ms: 1.09x slower                                                      |
| raytrace                  | 162 ms                                                          | 178 ms: 1.10x slower                                                       |
| coverage                  | 42.1 ms                                                         | 46.2 ms: 1.10x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.45 sec: 1.11x slower                                                     |
| html5lib                  | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                       |
| 2to3                      | 207 ms                                                          | 231 ms: 1.12x slower                                                       |
| pylint                    | 205 ms                                                          | 229 ms: 1.12x slower                                                       |
| sympy_str                 | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 13.8 ms: 1.13x slower                                                      |
| sympy_expand              | 271 ms                                                          | 308 ms: 1.14x slower                                                       |
| go                        | 82.1 ms                                                         | 93.4 ms: 1.14x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 89.0 ms: 1.14x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 18.2 ms: 1.15x slower                                                      |
| richards                  | 26.7 ms                                                         | 31.0 ms: 1.16x slower                                                      |
| async_generators          | 223 ms                                                          | 260 ms: 1.16x slower                                                       |
| richards_super            | 30.2 ms                                                         | 35.1 ms: 1.16x slower                                                      |
| django_template           | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 89.5 ms: 1.19x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.24 ms: 1.19x slower                                                      |
| generators                | 19.6 ms                                                         | 23.4 ms: 1.20x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.65 ms: 1.25x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 73.0 ms: 1.29x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 43.7 ms: 1.38x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (10): json, async_tree_cpu_io_mixed, regex_effbot, logging_format, logging_simple, pickle_pure_python, asyncio_tcp, gc_traversal, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown