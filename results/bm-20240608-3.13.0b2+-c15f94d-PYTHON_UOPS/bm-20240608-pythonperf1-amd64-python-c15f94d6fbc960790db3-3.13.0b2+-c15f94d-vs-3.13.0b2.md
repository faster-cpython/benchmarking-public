# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 232 ms: 1.12x slower                                                        |
| chameleon      | 4.80 ms                                                         | 5.12 ms: 1.06x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.84 sec: 1.13x slower                                                      |
| html5lib       | 35.0 ms                                                         | 41.6 ms: 1.19x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 87.8 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 275 ms: 1.06x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 282 ms: 1.07x slower                                                        |
| async_tree_none           | 218 ms                                                          | 233 ms: 1.07x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                        |
| float          | 49.7 ms                                                         | 52.6 ms: 1.06x slower                                                       |
| nbody          | 67.6 ms                                                         | 73.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                        |
| regex_compile  | 78.0 ms                                                         | 106 ms: 1.36x slower                                                        |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.51 us: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.81 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.4 ms: 1.08x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.84 us: 1.08x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                        |
| unpickle_pure_python | 122 us                                                          | 156 us: 1.28x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.34 ms: 1.15x slower                                                       |
| django_template | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 17.6 ms: 1.22x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                      | 3.19 ms                                                         | 2.92 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.39 sec: 1.07x faster                                                      |
| coroutines                | 12.8 ms                                                         | 12.6 ms: 1.01x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| pidigits                  | 150 ms                                                          | 151 ms: 1.00x slower                                                        |
| generators                | 19.6 ms                                                         | 19.7 ms: 1.01x slower                                                       |
| sqlite_synth              | 1.60 us                                                         | 1.61 us: 1.01x slower                                                       |
| telco                     | 4.67 ms                                                         | 4.70 ms: 1.01x slower                                                       |
| pickle                    | 7.11 us                                                         | 7.17 us: 1.01x slower                                                       |
| python_startup            | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.51 us: 1.01x slower                                                       |
| pickle_dict               | 18.1 us                                                         | 18.4 us: 1.01x slower                                                       |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                        |
| create_gc_cycles          | 888 us                                                          | 917 us: 1.03x slower                                                        |
| bench_mp_pool             | 64.8 ms                                                         | 67.0 ms: 1.03x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.81 ms: 1.04x slower                                                       |
| coverage                  | 42.1 ms                                                         | 43.7 ms: 1.04x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                       |
| aiohttp                   | 889 us                                                          | 933 us: 1.05x slower                                                        |
| logging_format            | 6.22 us                                                         | 6.56 us: 1.05x slower                                                       |
| float                     | 49.7 ms                                                         | 52.6 ms: 1.06x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 275 ms: 1.06x slower                                                        |
| logging_simple            | 5.78 us                                                         | 6.16 us: 1.06x slower                                                       |
| chameleon                 | 4.80 ms                                                         | 5.12 ms: 1.06x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 282 ms: 1.07x slower                                                        |
| async_tree_none           | 218 ms                                                          | 233 ms: 1.07x slower                                                        |
| tornado_http              | 81.8 ms                                                         | 87.8 ms: 1.07x slower                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                        |
| xml_etree_process         | 36.4 ms                                                         | 39.4 ms: 1.08x slower                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 2.16 us: 1.08x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.84 us: 1.08x slower                                                       |
| fannkuch                  | 243 ms                                                          | 265 ms: 1.09x slower                                                        |
| async_generators          | 223 ms                                                          | 243 ms: 1.09x slower                                                        |
| crypto_pyaes              | 45.5 ms                                                         | 49.6 ms: 1.09x slower                                                       |
| nbody                     | 67.6 ms                                                         | 73.8 ms: 1.09x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 76.4 ms: 1.09x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.3 ms: 1.10x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 843 us: 1.10x slower                                                        |
| richards_super            | 30.2 ms                                                         | 33.2 ms: 1.10x slower                                                       |
| scimark_fft               | 171 ms                                                          | 189 ms: 1.10x slower                                                        |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                        |
| pylint                    | 205 ms                                                          | 229 ms: 1.12x slower                                                        |
| 2to3                      | 207 ms                                                          | 232 ms: 1.12x slower                                                        |
| raytrace                  | 162 ms                                                          | 182 ms: 1.12x slower                                                        |
| chaos                     | 38.4 ms                                                         | 43.1 ms: 1.12x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.09 sec: 1.13x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.84 sec: 1.13x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 536 ms: 1.13x slower                                                        |
| scimark_sor               | 75.3 ms                                                         | 85.7 ms: 1.14x slower                                                       |
| mypy2                     | 418 ms                                                          | 480 ms: 1.15x slower                                                        |
| pyflate                   | 279 ms                                                          | 321 ms: 1.15x slower                                                        |
| mako                      | 6.36 ms                                                         | 7.34 ms: 1.15x slower                                                       |
| dulwich_log               | 38.0 ms                                                         | 44.1 ms: 1.16x slower                                                       |
| deepcopy                  | 220 us                                                          | 255 us: 1.16x slower                                                        |
| spectral_norm             | 63.7 ms                                                         | 74.1 ms: 1.16x slower                                                       |
| pycparser                 | 754 ms                                                          | 876 ms: 1.16x slower                                                        |
| sympy_sum                 | 84.4 ms                                                         | 98.4 ms: 1.17x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 38.3 ms: 1.17x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.12 ms: 1.17x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 66.6 ms: 1.17x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.94 ms: 1.18x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 881 us: 1.18x slower                                                        |
| django_template           | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.56 ms: 1.18x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 41.6 ms: 1.19x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.6 ms: 1.19x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 47.0 ms: 1.20x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 212 us: 1.21x slower                                                        |
| sympy_str                 | 159 ms                                                          | 194 ms: 1.22x slower                                                        |
| genshi_xml                | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 17.6 ms: 1.22x slower                                                       |
| sympy_expand              | 271 ms                                                          | 335 ms: 1.24x slower                                                        |
| go                        | 82.1 ms                                                         | 102 ms: 1.24x slower                                                        |
| comprehensions            | 10.4 us                                                         | 13.3 us: 1.28x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 156 us: 1.28x slower                                                        |
| deepcopy_memo             | 22.1 us                                                         | 28.5 us: 1.29x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 68.3 ns: 1.29x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 73.6 ms: 1.30x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.55 ms: 1.36x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 106 ms: 1.36x slower                                                        |
| hexiom                    | 3.72 ms                                                         | 5.18 ms: 1.39x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.10x slower                                                                |

Benchmark hidden because not significant (10): regex_v8, pickle_list, regex_effbot, pathlib, flaskblogging, xml_etree_parse, asyncio_tcp, python_startup_no_site, async_tree_io, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown