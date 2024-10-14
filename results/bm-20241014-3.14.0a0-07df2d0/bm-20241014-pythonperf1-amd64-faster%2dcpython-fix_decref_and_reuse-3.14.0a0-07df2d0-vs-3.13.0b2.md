# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 229 ms: 1.11x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                               |
| html5lib       | 35.0 ms                                                         | 44.1 ms: 1.26x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 94.2 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 53.3 ms: 1.07x slower                                                                |
| nbody          | 67.6 ms                                                         | 74.9 ms: 1.11x slower                                                                |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 123 ms: 1.03x slower                                                                 |
| regex_effbot   | 1.58 ms                                                         | 1.64 ms: 1.04x slower                                                                |
| regex_compile  | 78.0 ms                                                         | 92.0 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                                |
| pickle_dict          | 18.1 us                                                         | 19.1 us: 1.05x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.5 ms: 1.05x slower                                                                |
| json_loads           | 14.2 us                                                         | 15.0 us: 1.06x slower                                                                |
| xml_etree_parse      | 90.9 ms                                                         | 97.0 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                                |
| unpickle_list        | 2.62 us                                                         | 2.85 us: 1.09x slower                                                                |
| unpickle             | 8.40 us                                                         | 9.30 us: 1.11x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 40.8 ms: 1.12x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                               |
| json_dumps           | 5.61 ms                                                         | 6.78 ms: 1.21x slower                                                                |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.23x slower                                                                 |
| pickle_pure_python   | 175 us                                                          | 216 us: 1.23x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.01 ms: 1.10x slower                                                                |
| django_template | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 38.1 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 521 us: 15.57x faster                                                                |
| deepcopy                 | 220 us                                                          | 189 us: 1.16x faster                                                                 |
| deepcopy_memo            | 22.1 us                                                         | 20.0 us: 1.10x faster                                                                |
| deepcopy_reduce          | 1.99 us                                                         | 1.95 us: 1.02x faster                                                                |
| pickle                   | 7.11 us                                                         | 7.19 us: 1.01x slower                                                                |
| telco                    | 4.67 ms                                                         | 4.79 ms: 1.03x slower                                                                |
| sqlite_synth             | 1.60 us                                                         | 1.64 us: 1.03x slower                                                                |
| regex_dna                | 119 ms                                                          | 123 ms: 1.03x slower                                                                 |
| regex_effbot             | 1.58 ms                                                         | 1.64 ms: 1.04x slower                                                                |
| pickle_dict              | 18.1 us                                                         | 19.1 us: 1.05x slower                                                                |
| xml_etree_iterparse      | 62.3 ms                                                         | 65.5 ms: 1.05x slower                                                                |
| bench_thread_pool        | 768 us                                                          | 809 us: 1.05x slower                                                                 |
| json_loads               | 14.2 us                                                         | 15.0 us: 1.06x slower                                                                |
| sympy_sum                | 84.4 ms                                                         | 89.3 ms: 1.06x slower                                                                |
| create_gc_cycles         | 888 us                                                          | 940 us: 1.06x slower                                                                 |
| docutils                 | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                               |
| pathlib                  | 75.9 ms                                                         | 80.6 ms: 1.06x slower                                                                |
| crypto_pyaes             | 45.5 ms                                                         | 48.4 ms: 1.06x slower                                                                |
| xml_etree_parse          | 90.9 ms                                                         | 97.0 ms: 1.07x slower                                                                |
| spectral_norm            | 63.7 ms                                                         | 68.2 ms: 1.07x slower                                                                |
| float                    | 49.7 ms                                                         | 53.3 ms: 1.07x slower                                                                |
| go                       | 82.1 ms                                                         | 87.9 ms: 1.07x slower                                                                |
| coroutines               | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                                |
| bench_mp_pool            | 64.8 ms                                                         | 69.6 ms: 1.08x slower                                                                |
| xml_etree_generate       | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                                |
| unpickle_list            | 2.62 us                                                         | 2.85 us: 1.09x slower                                                                |
| logging_format           | 6.22 us                                                         | 6.79 us: 1.09x slower                                                                |
| sympy_integrate          | 12.2 ms                                                         | 13.4 ms: 1.09x slower                                                                |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.73 ms: 1.09x slower                                                                |
| meteor_contest           | 69.9 ms                                                         | 76.5 ms: 1.09x slower                                                                |
| python_startup           | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                                |
| mako                     | 6.36 ms                                                         | 7.01 ms: 1.10x slower                                                                |
| async_generators         | 223 ms                                                          | 247 ms: 1.11x slower                                                                 |
| 2to3                     | 207 ms                                                          | 229 ms: 1.11x slower                                                                 |
| nbody                    | 67.6 ms                                                         | 74.9 ms: 1.11x slower                                                                |
| unpickle                 | 8.40 us                                                         | 9.30 us: 1.11x slower                                                                |
| nqueens                  | 56.7 ms                                                         | 62.8 ms: 1.11x slower                                                                |
| typing_runtime_protocols | 101 us                                                          | 112 us: 1.11x slower                                                                 |
| scimark_lu               | 56.6 ms                                                         | 62.9 ms: 1.11x slower                                                                |
| pylint                   | 205 ms                                                          | 228 ms: 1.11x slower                                                                 |
| mdp                      | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                               |
| logging_simple           | 5.78 us                                                         | 6.44 us: 1.11x slower                                                                |
| python_startup_no_site   | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                                |
| sympy_str                | 159 ms                                                          | 178 ms: 1.12x slower                                                                 |
| sqlglot_optimize         | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                                                |
| xml_etree_process        | 36.4 ms                                                         | 40.8 ms: 1.12x slower                                                                |
| chaos                    | 38.4 ms                                                         | 43.1 ms: 1.12x slower                                                                |
| sqlglot_normalize        | 173 ms                                                          | 194 ms: 1.12x slower                                                                 |
| generators               | 19.6 ms                                                         | 22.1 ms: 1.13x slower                                                                |
| coverage                 | 42.1 ms                                                         | 47.5 ms: 1.13x slower                                                                |
| sympy_expand             | 271 ms                                                          | 306 ms: 1.13x slower                                                                 |
| comprehensions           | 10.4 us                                                         | 11.7 us: 1.13x slower                                                                |
| pprint_safe_repr         | 474 ms                                                          | 540 ms: 1.14x slower                                                                 |
| fannkuch                 | 243 ms                                                          | 279 ms: 1.15x slower                                                                 |
| tornado_http             | 81.8 ms                                                         | 94.2 ms: 1.15x slower                                                                |
| scimark_fft              | 171 ms                                                          | 197 ms: 1.15x slower                                                                 |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.71 sec: 1.16x slower                                                               |
| pprint_pformat           | 966 ms                                                          | 1.12 sec: 1.16x slower                                                               |
| pyflate                  | 279 ms                                                          | 323 ms: 1.16x slower                                                                 |
| dulwich_log              | 38.0 ms                                                         | 44.2 ms: 1.16x slower                                                                |
| logging_silent           | 52.9 ns                                                         | 61.7 ns: 1.17x slower                                                                |
| raytrace                 | 162 ms                                                          | 191 ms: 1.17x slower                                                                 |
| regex_compile            | 78.0 ms                                                         | 92.0 ms: 1.18x slower                                                                |
| django_template          | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                                |
| sqlglot_transpile        | 955 us                                                          | 1.13 ms: 1.19x slower                                                                |
| hexiom                   | 3.72 ms                                                         | 4.43 ms: 1.19x slower                                                                |
| scimark_sor              | 75.3 ms                                                         | 89.7 ms: 1.19x slower                                                                |
| genshi_text              | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                                |
| tomli_loads              | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                               |
| genshi_xml               | 31.6 ms                                                         | 38.1 ms: 1.20x slower                                                                |
| json_dumps               | 5.61 ms                                                         | 6.78 ms: 1.21x slower                                                                |
| scimark_monte_carlo      | 39.1 ms                                                         | 47.5 ms: 1.21x slower                                                                |
| richards                 | 26.7 ms                                                         | 32.7 ms: 1.23x slower                                                                |
| unpickle_pure_python     | 122 us                                                          | 149 us: 1.23x slower                                                                 |
| sqlglot_parse            | 748 us                                                          | 920 us: 1.23x slower                                                                 |
| pickle_pure_python       | 175 us                                                          | 216 us: 1.23x slower                                                                 |
| richards_super           | 30.2 ms                                                         | 37.3 ms: 1.24x slower                                                                |
| deltablue                | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                                |
| html5lib                 | 35.0 ms                                                         | 44.1 ms: 1.26x slower                                                                |
| asyncio_tcp              | 471 ms                                                          | 646 ms: 1.37x slower                                                                 |
| json                     | 3.19 ms                                                         | 4.52 ms: 1.42x slower                                                                |
| Geometric mean           | (ref)                                                           | 1.08x slower                                                                         |

Benchmark hidden because not significant (5): pycparser, regex_v8, gc_traversal, pidigits, pickle_list
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown