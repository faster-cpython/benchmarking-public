# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.00x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.11 ms: 1.06x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.76 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 37.2 ms: 1.06x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization    | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 269 ms: 1.04x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 211 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.5 ms: 1.34x faster                                                      |
| float          | 49.7 ms                                                         | 44.2 ms: 1.12x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 87.2 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.1 ms: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.5 us: 1.03x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 173 us: 1.01x faster                                                       |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 91.5 ms: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.69 us: 1.04x slower                                                      |
| pickle               | 7.11 us                                                         | 7.37 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.87 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.17 ms: 1.23x faster                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.7 ms: 1.41x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 516 us: 15.71x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.1 ms: 1.41x faster                                                      |
| nbody                     | 67.6 ms                                                         | 50.5 ms: 1.34x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.17 ms: 1.23x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.17 ms: 1.15x faster                                                      |
| scimark_fft               | 171 ms                                                          | 151 ms: 1.13x faster                                                       |
| float                     | 49.7 ms                                                         | 44.2 ms: 1.12x faster                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 41.0 ms: 1.11x faster                                                      |
| regex_v8                  | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| fannkuch                  | 243 ms                                                          | 222 ms: 1.10x faster                                                       |
| json                      | 3.19 ms                                                         | 2.92 ms: 1.09x faster                                                      |
| pyflate                   | 279 ms                                                          | 257 ms: 1.08x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.6 us: 1.07x faster                                                      |
| telco                     | 4.67 ms                                                         | 4.48 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.1 ms: 1.04x faster                                                      |
| pickle_dict               | 18.1 us                                                         | 17.5 us: 1.03x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 459 ms: 1.03x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.56 us: 1.02x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 945 ms: 1.02x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.5 ms: 1.02x faster                                                      |
| pickle_pure_python        | 175 us                                                          | 173 us: 1.01x faster                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| logging_simple            | 5.78 us                                                         | 5.75 us: 1.01x faster                                                      |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| regex_dna                 | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 91.5 ms: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 907 us: 1.02x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 125 us: 1.03x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.69 us: 1.04x slower                                                      |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                       |
| pickle                    | 7.11 us                                                         | 7.37 us: 1.04x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 84.9 ms: 1.04x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.07 us: 1.04x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 78.8 ms: 1.04x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 269 ms: 1.04x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 211 ms: 1.04x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 56.0 ns: 1.06x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 37.2 ms: 1.06x slower                                                      |
| chameleon                 | 4.80 ms                                                         | 5.11 ms: 1.06x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.5 ms: 1.07x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 799 us: 1.07x slower                                                       |
| python_startup            | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 61.0 ms: 1.08x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.76 sec: 1.09x slower                                                     |
| deepcopy                  | 220 us                                                          | 238 us: 1.09x slower                                                       |
| raytrace                  | 162 ms                                                          | 176 ms: 1.09x slower                                                       |
| coverage                  | 42.1 ms                                                         | 45.8 ms: 1.09x slower                                                      |
| unpickle_list             | 2.62 us                                                         | 2.87 us: 1.09x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 92.5 ms: 1.10x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 842 us: 1.10x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 111 us: 1.10x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 82.8 ms: 1.10x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 71.3 ms: 1.10x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.5 ms: 1.10x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.3 ms: 1.10x slower                                                      |
| generators                | 19.6 ms                                                         | 21.6 ms: 1.10x slower                                                      |
| sympy_str                 | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 87.2 ms: 1.12x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 36.7 ms: 1.12x slower                                                      |
| 2to3                      | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.48 sec: 1.13x slower                                                     |
| sympy_expand              | 271 ms                                                          | 309 ms: 1.14x slower                                                       |
| go                        | 82.1 ms                                                         | 93.8 ms: 1.14x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.14x slower                                                      |
| async_generators          | 223 ms                                                          | 257 ms: 1.15x slower                                                       |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                       |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 69.9 ms: 1.23x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.33 ms: 1.24x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.65 ms: 1.25x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.7 ms: 1.41x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (13): asyncio_tcp_ssl, comprehensions, pycparser, logging_format, xml_etree_process, flaskblogging, gc_traversal, pickle_list, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_tcp
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown