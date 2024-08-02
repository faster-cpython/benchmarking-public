# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x slower
- HPT reliability: 96.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 530 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 543 ms: 1.08x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 190 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                       |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 256 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                      |
| float          | 49.7 ms                                                         | 45.1 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.2 ms: 1.16x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 23.9 ms: 1.52x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.28 sec: 1.06x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 52.8 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 179 us: 1.02x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 93.4 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 134 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.18 ms: 1.23x faster                                                      |
| django_template | 21.7 ms                                                         | 26.3 ms: 1.22x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 528 us: 15.37x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.6 us: 1.41x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.8 ms: 1.39x faster                                                      |
| nbody                     | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.18 ms: 1.23x faster                                                      |
| deepcopy                  | 220 us                                                          | 180 us: 1.22x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.17 ms: 1.15x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 530 ms: 1.14x faster                                                       |
| scimark_fft               | 171 ms                                                          | 151 ms: 1.13x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 40.8 ms: 1.11x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.80 us: 1.11x faster                                                      |
| float                     | 49.7 ms                                                         | 45.1 ms: 1.10x faster                                                      |
| fannkuch                  | 243 ms                                                          | 225 ms: 1.08x faster                                                       |
| async_tree_io             | 588 ms                                                          | 543 ms: 1.08x faster                                                       |
| pyflate                   | 279 ms                                                          | 260 ms: 1.07x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 190 ms: 1.06x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.28 sec: 1.06x faster                                                     |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                       |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 256 ms: 1.03x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.1 ms: 1.03x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 462 ms: 1.02x faster                                                       |
| pprint_pformat            | 966 ms                                                          | 947 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| pathlib                   | 75.9 ms                                                         | 74.9 ms: 1.01x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 52.8 ms: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.27 us: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 900 us: 1.01x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 179 us: 1.02x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 93.4 ms: 1.03x slower                                                      |
| python_startup            | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                                      |
| chaos                     | 38.4 ms                                                         | 40.0 ms: 1.04x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 808 us: 1.05x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.95 ms: 1.06x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.1 ms: 1.06x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 57.3 ns: 1.08x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 815 us: 1.09x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 61.9 ms: 1.09x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| unpickle_pure_python      | 122 us                                                          | 134 us: 1.10x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 36.4 ms: 1.11x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                     |
| sympy_sum                 | 84.4 ms                                                         | 94.0 ms: 1.11x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 193 ms: 1.12x slower                                                       |
| coroutines                | 12.8 ms                                                         | 14.3 ms: 1.12x slower                                                      |
| 2to3                      | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| pylint                    | 205 ms                                                          | 232 ms: 1.13x slower                                                       |
| raytrace                  | 162 ms                                                          | 185 ms: 1.14x slower                                                       |
| richards                  | 26.7 ms                                                         | 30.6 ms: 1.15x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.15x slower                                                      |
| coverage                  | 42.1 ms                                                         | 48.5 ms: 1.15x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.8 ms: 1.15x slower                                                      |
| sympy_str                 | 159 ms                                                          | 184 ms: 1.16x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 90.2 ms: 1.16x slower                                                      |
| async_generators          | 223 ms                                                          | 259 ms: 1.16x slower                                                       |
| sympy_expand              | 271 ms                                                          | 319 ms: 1.18x slower                                                       |
| go                        | 82.1 ms                                                         | 97.7 ms: 1.19x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 91.6 ms: 1.22x slower                                                      |
| django_template           | 21.7 ms                                                         | 26.3 ms: 1.22x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.61 ms: 1.24x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| generators                | 19.6 ms                                                         | 25.0 ms: 1.28x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 77.0 ms: 1.36x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 23.9 ms: 1.52x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, json, xml_etree_iterparse, logging_simple, gc_traversal, async_tree_cpu_io_mixed_tg, asyncio_tcp, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 96.47% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown